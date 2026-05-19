# Digest — 2026-05-19 AM

- Window: last 14h
- Raw items considered: 16
- Relevant: 12
- Skippable: 4

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Microsoft Exchange Zero-Day Under Active Attack, No Patch Available — `2026-05-18-microsoft-exchange-zero-day-xss-owa-no-patch.md`
- [x] **[CRITICAL]** CISA Contractor Exposed AWS GovCloud Keys and Internal System Details on Public GitHub — `2026-05-18-cisa-contractor-aws-govcloud-keys-github-leak.md`
- [x] **[CRITICAL]** GitHub Actions Supply Chain Attack Redirects All Tags to Credential-Stealing Commit — `2026-05-19-github-actions-supply-chain-ci-cd-credentials.md`
- [x] **[CRITICAL]** Mini Shai-Hulud Campaign Poisons AntV npm Packages via Compromised Maintainer Account — `2026-05-19-antv-npm-supply-chain-mini-shai-hulud.md`
- [x] **[CRITICAL]** Compromised Nx Console VS Code Extension Installed Credential Stealer on 2.2M Developer Machines — `2026-05-19-nx-console-vscode-supply-chain-credential-stealer.md`
- [x] **[CRITICAL]** Critical SEPPMail Secure E-Mail Gateway Flaws Enable RCE and Full Mail Traffic Interception — `2026-05-19-seppmail-email-gateway-rce.md`
- [x] **[HIGH]** CVE-2026-8153: OS Command Injection in Universal Robots PolyScope 5 Exposes Industrial Robot Fleets — `2026-05-19-universal-robots-polyscope-rce-cve-2026-8153.md`
- [x] **[HIGH]** PoC Released for DirtyDecrypt Linux Kernel Privilege Escalation to Root — `2026-05-19-dirtydecrypt-linux-kernel-poc.md`
- [x] **[HIGH]** SHub macOS Infostealer Variant Spoofs Apple Security Updates to Install Backdoor — `2026-05-18-shub-macos-infostealer-fake-security-updates.md`
- [x] **[HIGH]** Cisco Talos Uncovers BadIIS Malware-as-a-Service Ecosystem Shared Among Chinese-Speaking Threat Actors — `2026-05-19-badiis-maas-chinese-threat-actors.md`
- [x] **[HIGH]** 'Claw Chain' Vulnerabilities in OpenClaw AI Agent Framework Allow Credential Theft and Persistence — `2026-05-18-openclaw-ai-agent-framework-claw-chain-vulns.md`
- [x] **[MEDIUM]** INTERPOL Operation Ramz Seizes 53 Malware and Phishing Servers, Arrests 200+ in MENA — `2026-05-18-interpol-operation-ramz-middle-east.md`

## Relevant (details)

### 1. Microsoft Exchange Zero-Day Under Active Attack, No Patch Available
- **Source:** Dark Reading — https://www.darkreading.com/vulnerabilities-threats/microsoft-exchange-zero-day-no-patch
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `microsoft`, `xss`, `vulnerability`, `cve`
- **Slug:** `2026-05-18-microsoft-exchange-zero-day-xss-owa-no-patch`
- **Must-know:** yes
- **Summary:** CVE-2026-42897 is an XSS vulnerability in Microsoft Exchange OWA actively being exploited with no patch available. Exploitation allows full OWA mailbox compromise; Exchange administrators should restrict external OWA exposure immediately.

### 2. CISA Contractor Exposed AWS GovCloud Keys and Internal System Details on Public GitHub
- **Source:** Krebs on Security — https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `data-breach`, `aws`, `iam`, `github`, `cloud-security`
- **Slug:** `2026-05-18-cisa-contractor-aws-govcloud-keys-github-leak`
- **Must-know:** yes
- **Summary:** A public GitHub repo maintained by a CISA contractor exposed credentials to highly privileged AWS GovCloud accounts and internal CISA deployment details, described by security experts as one of the worst government data leaks in recent memory. The repo has been taken down as of last weekend.

### 3. GitHub Actions Supply Chain Attack Redirects All Tags to Credential-Stealing Commit
- **Source:** The Hacker News — https://thehackernews.com/2026/05/github-actions-supply-chain-attack.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `github`, `ci-cd`, `malware`, `credential-stealer`
- **Slug:** `2026-05-19-github-actions-supply-chain-ci-cd-credentials`
- **Must-know:** yes
- **Summary:** The `actions-cool/issues-helper` GitHub Actions workflow was compromised with all tags redirected to a malicious commit that exfiltrates CI/CD credentials. Any pipeline referencing this action by tag should be considered compromised and secrets rotated.

### 4. Mini Shai-Hulud Campaign Poisons AntV npm Packages via Compromised Maintainer Account
- **Source:** The Hacker News — https://thehackernews.com/2026/05/mini-shai-hulud-pushes-malicious-antv.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `malware`, `credential-stealer`
- **Slug:** `2026-05-19-antv-npm-supply-chain-mini-shai-hulud`
- **Must-know:** yes
- **Summary:** The Mini Shai-Hulud campaign has compromised the `atool` npm maintainer account, poisoning `@antv` packages including `echarts-for-react` (~1.1M weekly downloads). Developers using these packages should audit their installed versions and rotate build environment secrets.

### 5. Compromised Nx Console VS Code Extension Installed Credential Stealer on 2.2M Developer Machines
- **Source:** The Hacker News — https://thehackernews.com/2026/05/compromised-nx-console-18950-targeted.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `credential-stealer`, `malware`, `github`
- **Slug:** `2026-05-19-nx-console-vscode-supply-chain-credential-stealer`
- **Must-know:** yes
- **Summary:** Version 18.95.0 of the Nx Console VS Code extension (`rwl.angular-console`) was published with a credential stealer, reaching 2.2 million installs across VS Code, Cursor, and JetBrains. Developers should remove the affected version and rotate any secrets accessible in their IDE environment.

### 6. Critical SEPPMail Secure E-Mail Gateway Flaws Enable RCE and Full Mail Traffic Interception
- **Source:** The Hacker News — https://thehackernews.com/2026/05/seppmail-secure-e-mail-gateway.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `vulnerability`, `cve`, `appsec`
- **Slug:** `2026-05-19-seppmail-email-gateway-rce`
- **Must-know:** no
- **Summary:** Multiple critical vulnerabilities in SEPPMail's Secure E-Mail Gateway allow remote code execution and interception of all mail traffic flowing through the appliance. Enterprises using SEPPMail should patch immediately given the gateway's privileged position in email flows.

### 7. CVE-2026-8153: OS Command Injection in Universal Robots PolyScope 5 Exposes Industrial Robot Fleets
- **Source:** SecurityWeek — https://www.securityweek.com/critical-vulnerability-exposes-industrial-robot-fleets-to-hacking/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `cve`, `vulnerability`
- **Slug:** `2026-05-19-universal-robots-polyscope-rce-cve-2026-8153`
- **Must-know:** no
- **Summary:** CVE-2026-8153 is a critical OS command injection flaw in Universal Robots PolyScope 5 exposing industrial robot fleets to remote exploitation. Beyond IT impact, compromised robot controllers carry physical safety implications for manufacturing and logistics environments.

### 8. PoC Released for DirtyDecrypt Linux Kernel Privilege Escalation to Root
- **Source:** SecurityWeek — https://www.securityweek.com/poc-released-for-dirtydecrypt-linux-kernel-vulnerability/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `privilege-escalation`, `vulnerability`, `cve`
- **Slug:** `2026-05-19-dirtydecrypt-linux-kernel-poc`
- **Must-know:** no
- **Summary:** A public PoC now exists for the DirtyDecrypt Linux kernel vulnerability (patched April 2026) that allows local privilege escalation to root. Linux hosts without April kernel patches are at immediate heightened risk, especially container hosts and multi-tenant systems.

### 9. SHub macOS Infostealer Variant Spoofs Apple Security Updates to Install Backdoor
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/shub-macos-infostealer-variant-spoofs-apple-security-updates/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `phishing`
- **Slug:** `2026-05-18-shub-macos-infostealer-fake-security-updates`
- **Must-know:** no
- **Summary:** A new SHub variant uses AppleScript to present convincing fake Apple security update dialogs, tricking macOS users into authorizing a persistent backdoor installation. Security teams should hunt for unusual AppleScript execution and unexpected LaunchAgent entries.

### 10. Cisco Talos Uncovers BadIIS Malware-as-a-Service Ecosystem Shared Among Chinese-Speaking Threat Actors
- **Source:** Cisco Talos — https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `malware`, `vulnerability`, `appsec`
- **Slug:** `2026-05-19-badiis-maas-chinese-threat-actors`
- **Must-know:** no
- **Summary:** Cisco Talos tracked a BadIIS variant identifiable by "demo.pdb" strings operating as a shared MaaS tool among multiple Chinese-speaking cybercrime groups. IIS administrators should audit server modules and logs for signs of compromise.

### 11. 'Claw Chain' Vulnerabilities in OpenClaw AI Agent Framework Allow Credential Theft and Persistence
- **Source:** Dark Reading — https://www.darkreading.com/application-security/claw-chain-vulnerabilities-threaten-openclaw
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `llm`, `appsec`, `privilege-escalation`, `ai-safety`
- **Slug:** `2026-05-18-openclaw-ai-agent-framework-claw-chain-vulns`
- **Must-know:** no
- **Summary:** A now-patched chain of vulnerabilities in the OpenClaw AI agent framework enabled credential theft, privilege escalation, and persistence within agent deployments. Teams using OpenClaw in production should apply patches and audit agent permission scopes.

### 12. INTERPOL Operation Ramz Seizes 53 Malware and Phishing Servers, Arrests 200+ in MENA
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/interpol-operation-ramz-seizes-53-malware-phishing-servers/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `phishing`
- **Slug:** `2026-05-18-interpol-operation-ramz-middle-east`
- **Must-know:** no
- **Summary:** INTERPOL's Operation Ramz seized 53 malware and phishing servers across the Middle East and North Africa and arrested more than 200 individuals for cybercrime. Specific IOCs and TTPs have not yet been published; watch for follow-on reporting.

## Skippable

- **Gemini is in danger of going full Copilot** — The Verge AI. Editorial opinion piece on Gemini's expansion into Google Workspace apps; no technical news value.
- **The last six months in LLMs in five minutes** — Simon Willison. Annotated lightning talk slides from PyCon US 2026; retrospective summary with no new information.
- **SandboxAQ brings its drug discovery models to Claude** — TechCrunch AI. Product partnership announcement (drug discovery, not security-relevant); marketing framing with no security angle.
- **More than 200 arrested in cyber raids aimed at Middle East scam networks** — The Record (Recorded Future). Duplicate coverage of INTERPOL Operation Ramz; BleepingComputer item selected as primary source.
