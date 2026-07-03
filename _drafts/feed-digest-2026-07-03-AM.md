# Digest — 2026-07-03 AM

- Window: last 14h
- Raw items considered: 12
- Relevant: 5
- Skippable: 7

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** Google, FBI Disrupt NetNut Residential Proxy Network Powered by Millions of Devices — `2026-07-03-netnut-residential-proxy-takedown.md`
- [x] **[MEDIUM]** PamStealer Uses Fake Maccy Sites and PAM Checks to Steal Mac Login Passwords — `2026-07-03-pamstealer-macos-info-stealer.md`
- [x] **[HIGH]** Critical Cursor AI Code Editor Flaws Could Lead to OS-Level Remote Code Execution — `2026-07-03-cursor-ai-duneslide-rce-flaws.md`
- [x] **[HIGH]** Spyware Found on Phone of European Parliament Member Probing It — `2026-07-03-pegasus-spyware-european-parliament-member.md`
- [x] **[INFORMATIONAL]** How We Added WebAuthn to a Browser-Based RDP Client — `2026-07-02-webauthn-browser-rdp-client.md`

## Relevant (details)

### 1. Google, FBI Disrupt NetNut Residential Proxy Network Powered by Millions of Devices
- **Source:** SecurityWeek — https://www.securityweek.com/google-fbi-disrupt-netnut-residential-proxy-network-powered-by-millions-of-devices/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `google`
- **Slug:** `netnut-residential-proxy-takedown`
- **Must-know:** no
- **Summary:** Google and the FBI disrupted NetNut, a residential proxy network built from millions of compromised devices. Cybercriminals and nation-state actors used it to mask their identities during attacks.

### 2. PamStealer Uses Fake Maccy Sites and PAM Checks to Steal Mac Login Passwords
- **Source:** The Hacker News — https://thehackernews.com/2026/07/pamstealer-uses-fake-maccy-sites-and.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `phishing`
- **Slug:** `pamstealer-macos-info-stealer`
- **Must-know:** no
- **Summary:** Jamf Threat Labs identified a new macOS info stealer, PamStealer, distributed as a compiled AppleScript file impersonating the Maccy clipboard manager. It uses PAM checks as part of its infection tricks to harvest login credentials.

### 3. Critical Cursor AI Code Editor Flaws Could Lead to OS-Level Remote Code Execution
- **Source:** SecurityWeek — https://www.securityweek.com/critical-cursor-ai-ide-flaws-could-lead-to-os-level-remote-code-execution/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `rce`, `vulnerability`, `ai-safety`
- **Slug:** `cursor-ai-duneslide-rce-flaws`
- **Must-know:** no
- **Summary:** Vulnerabilities codenamed DuneSlide in the Cursor AI code editor enable zero-click prompt injection that escapes the sandbox and executes arbitrary code on the host OS. Active exploitation isn't confirmed, so severity is kept at high rather than critical.

### 4. Spyware Found on Phone of European Parliament Member Probing It
- **Source:** The Record (Recorded Future) — https://therecord.media/pegasus-spyware-european-parliament-pega-committee-member
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`
- **Slug:** `pegasus-spyware-european-parliament-member`
- **Must-know:** no
- **Summary:** Researchers found Pegasus spyware on the phone of Stelios Kouloglou, a former member of the European Parliament's PEGA committee investigating spyware abuse. He was reportedly infected twice while serving on the committee.

### 5. How We Added WebAuthn to a Browser-Based RDP Client
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/webauthn-added-to-browser-based-rdp/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** informational
- **Tags:** `appsec`
- **Slug:** `webauthn-browser-rdp-client`
- **Must-know:** no
- **Summary:** Unit 42 documents the reverse-engineering process behind adding WebAuthn redirection to a browser-based RDP client, reportedly the first such client outside Windows to support it. This is a defensive tooling write-up, not a new vulnerability.

## Skippable

- **Alleged Scattered Spider Hacker Extradited to US** — SecurityWeek. Arrest/legal news about a past case, no new technical detail or IOCs.
- **Claude Fable 5 isn't permanently leaving subscriptions, Anthropic says** — BleepingComputer. Product/subscription policy news, no security angle.
- **Claude Fable relaunch disappoints users with nerfed performance** — BleepingComputer. Opinion/performance impressions, no security substance; duplicate topic of the item above.
- **Mark Zuckerberg tells staff that AI agents haven't progressed as quickly as he'd hoped** — TechCrunch AI. Internal-meeting commentary/opinion, no launch or security substance.
- **Aussies Face Reduced Cybercrime Risk, as Pressure Shifts to SMBs** — Dark Reading. General trend/opinion piece without technical detail.
- **Launch of UK's National Cyber Action Plan delayed amid Labour leadership crisis** — The Record. Political delay news, no concrete policy substance yet.
- **Jersey Mike's IPO illustrates how bad the AI hype has become** — TechCrunch AI. Opinion/satire piece, no news value.
