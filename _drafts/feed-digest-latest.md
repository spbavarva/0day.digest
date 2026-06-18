# Digest — 2026-06-18 AM

- Window: last 14h
- Raw items considered: 14
- Relevant: 5
- Skippable: 9

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** Atlassian, Splunk Patch Critical Vulnerabilities — `2026-06-18-atlassian-splunk-critical-vulnerabilities-patched.md`
- [x] **[HIGH]** Rokarolla Banking Trojan Targets 200 Applications — `2026-06-18-rokarolla-banking-trojan-targets-200-apps.md`
- [x] **[HIGH]** Critical Command Execution Vulnerability Patched in Cisco ISE — `2026-06-18-cisco-ise-critical-rce-patched.md`
- [x] **[INFORMATIONAL]** Scripting the Disassembler: Agentic Reverse Engineering via vbdec — `2026-06-18-talos-agentic-reverse-engineering-vbdec.md`
- [x] **[HIGH]** F5 Patches Critical, High-Severity NGINX Vulnerabilities — `2026-06-18-f5-nginx-critical-vulnerabilities-patched.md`

## Relevant (details)

### 1. Atlassian, Splunk Patch Critical Vulnerabilities
- **Source:** SecurityWeek — https://www.securityweek.com/atlassian-splunk-patch-critical-vulnerabilities/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `llm`, `appsec`
- **Summary:** Splunk patched an OS command injection vulnerability in its AI Toolkit, while Atlassian fixed dozens of flaws across its products' third-party dependencies. Both vendors have shipped patches; no active exploitation has been reported.

### 2. Rokarolla Banking Trojan Targets 200 Applications
- **Source:** SecurityWeek — https://www.securityweek.com/rokarolla-banking-trojan-targets-200-applications/
- **Severity:** high
- **Tags:** `malware`
- **Summary:** A new Android banking trojan dubbed Rokarolla targets roughly 200 financial and banking applications, letting operators take remote control of infected devices and harvest sensitive data. The scope of targeted apps gives it a wide potential victim pool among mobile banking users.

### 3. Critical Command Execution Vulnerability Patched in Cisco ISE
- **Source:** SecurityWeek — https://www.securityweek.com/critical-command-execution-vulnerability-patched-in-cisco-ise/
- **Severity:** high
- **Tags:** `rce`, `privilege-escalation`, `vulnerability`, `cve`
- **Summary:** Cisco patched a critical vulnerability in Identity Services Engine (ISE) caused by insufficient input validation, letting an authenticated attacker reach the underlying OS and escalate privileges to root. The flaw is fixed; no in-the-wild exploitation has been reported.

### 4. Scripting the Disassembler: Agentic Reverse Engineering via vbdec
- **Source:** Cisco Talos — https://blog.talosintelligence.com/scripting-the-disassembler/
- **Severity:** informational
- **Tags:** `llm`, `appsec`
- **Summary:** Cisco Talos described a workflow pairing local AI agents with the VB6 disassembler vbdec, which exposes its parsed data through a live COM interface rather than bolting AI on top of static output. It's a research/tooling write-up on agentic AI applied to reverse engineering, not a vulnerability disclosure.

### 5. F5 Patches Critical, High-Severity NGINX Vulnerabilities
- **Source:** SecurityWeek — https://www.securityweek.com/f5-patches-critical-high-severity-nginx-vulnerabilities/
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`
- **Summary:** F5 patched critical and high-severity flaws in NGINX that could let a remote, unauthenticated attacker trigger a restart and potentially execute arbitrary code. Patches are available; no active exploitation has been reported.

## Skippable

- **Microsoft fixes Windows Server 2016 security update failures** — BleepingComputer. Fix for a failed update installation process, not a vulnerability or security incident.
- **SailPoint to Acquire Entro in Reported $200 Million Deal** — SecurityWeek. M&A/business news, no technical security content.
- **Kodak Admits Data Breach After ShinyHunters Hack Claims** — SecurityWeek. Generic breach disclosure with no scope details or technical substance; Kodak says no operational impact.
- **EU Gets a Head Start in Developing 6G Network Security** — Dark Reading. Forward-looking policy/R&D initiative ("Shield-6G"), no concrete technical detail yet.
- **Choice, compliance, and collaboration: Europe's path to open digital sovereignty** — Google Cloud Security. Policy opinion piece on EU digital sovereignty, no actionable security content.
- **Midjourney goes from generating cat images to full-body ultrasound scans** — The Verge AI. Consumer hardware launch (medical imaging device), not a security or core model-capability story.
- **Leak confirms OpenAI is testing a ChatGPT for Science subscription** — BleepingComputer. Unconfirmed product leak, no security angle.
- **How to turn off AI in your Google Docs** — TechCrunch AI. Consumer how-to tip, not news.
- **GLM-5.2 is probably the most powerful text-only open weights LLM** — Simon Willison. Commentary on the same GLM-5.2 release already covered in yesterday's digest (2026-06-17-glm-5-2-long-horizon-release.md); duplicate coverage.
