# Digest — 2026-04-10 PM

- Window: last 14h
- Raw items considered: 33
- Relevant: 14
- Skippable: 19

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** CPUID Supply Chain Attack Poisons CPU-Z and HWMonitor Downloads — `2026-04-10-cpuid-supply-chain-cpu-z-hwmonitor.md`
- [x] **[CRITICAL]** GlassWorm Campaign Uses Zig Dropper to Infect All IDEs on Developer Machines — `2026-04-10-glassworm-zig-dropper-developer-ide.md`
- [x] **[HIGH]** North Korea Stole $280M From Crypto Protocol Drift via Fake Company Social Engineering — `2026-04-10-north-korea-drift-280m-crypto-theft.md`
- [x] **[HIGH]** Iranian Hackers Target ~4,000 Exposed US Industrial PLCs — `2026-04-10-iranian-plc-attacks-us-critical-infrastructure.md`
- [x] **[HIGH]** Windows Zero-Day, Stryker Cyberattack, Jones Day Breach in Security Week Roundup — `2026-04-10-windows-zero-day-stryker-jones-day.md`
- [x] **[HIGH]** Juniper Networks Patches Critical Unauthenticated RCE in Junos OS — `2026-04-10-juniper-junos-critical-rce.md`
- [x] **[HIGH]** Storm-2755 Hijacks Accounts to Redirect Canadian Employee Payroll — `2026-04-10-storm-2755-canadian-payroll-attacks.md`
- [x] **[HIGH]** Orthanc DICOM Server Vulnerabilities Enable RCE in Medical Imaging Systems — `2026-04-10-orthanc-dicom-rce-vulnerabilities.md`
- [x] **[MEDIUM]** Hims Telehealth Breach Exposes Highly Sensitive PHI — `2026-04-10-hims-phi-breach-telehealth.md`
- [x] **[MEDIUM]** Flashpoint Maps the Maturing Phishing-as-a-Service Pipeline Driving Global Fraud — `2026-04-10-phishing-as-a-service-pipeline-flashpoint.md`
- [x] **[MEDIUM]** Florida Investigates OpenAI Over ChatGPT's Role in Fatal Shooting — `2026-04-10-florida-chatgpt-shooting-investigation.md`
- [x] **[MEDIUM]** Lawsuit: OpenAI Ignored Three Safety Flags Before ChatGPT User Stalked Ex-Girlfriend — `2026-04-10-chatgpt-stalking-lawsuit-openai.md`
- [x] **[MEDIUM]** Analysis of 1 Billion CISA KEV Records Shows Defenders Are Losing the Patching Race — `2026-04-10-cisa-kev-remediation-analysis.md`
- [x] **[MEDIUM]** UK Regulator Threatens Tech Executives With Jail Over AI Nudification Tools — `2026-04-10-uk-nudification-crackdown-ofcom.md`

## Relevant (details)

### 1. CPUID Supply Chain Attack Poisons CPU-Z and HWMonitor Downloads
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/supply-chain-attack-at-cpuid-pushes-malware-with-cpu-z-hwmonitor/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`
- **Slug:** `2026-04-10-cpuid-supply-chain-cpu-z-hwmonitor`
- **Must-know:** yes
- **Summary:** Hackers compromised a CPUID API and replaced official download links for CPU-Z and HWMonitor with malicious executables. CPU-Z and HWMonitor are among the most widely used Windows hardware diagnostics utilities, making this a high-exposure supply chain incident.

### 2. GlassWorm Campaign Uses Zig Dropper to Infect All IDEs on Developer Machines
- **Source:** The Hacker News — https://thehackernews.com/2026/04/glassworm-campaign-uses-zig-dropper-to.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`, `appsec`
- **Slug:** `2026-04-10-glassworm-zig-dropper-developer-ide`
- **Must-know:** yes
- **Summary:** GlassWorm now distributes a Zig-language dropper via a malicious Open VSX extension impersonating WakaTime; once installed, it infects all IDEs on the developer's machine. The use of Zig and the targeting of developer toolchains makes detection and blast radius particularly severe.

### 3. North Korea Stole $280M From Crypto Protocol Drift via Fake Company Social Engineering
- **Source:** The Record (Recorded Future) — https://therecord.media/drift-crypto-theft-post-mortem-north-korea
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `data-breach`, `north-korea`
- **Slug:** `2026-04-10-north-korea-drift-280m-crypto-theft`
- **Must-know:** no
- **Summary:** North Korean actors posed as a fake quantitative trading firm and cultivated trust with Drift staff over six months before executing a $280M theft. The operation used fake companies and financial cutouts to launder proceeds — a multi-stage, long-dwell DPRK playbook.

### 4. Iranian Hackers Target ~4,000 Exposed US Industrial PLCs
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/nearly-4-000-us-industrial-devices-exposed-to-iranian-cyberattacks/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `ics-ot`
- **Slug:** `2026-04-10-iranian-plc-attacks-us-critical-infrastructure`
- **Must-know:** no
- **Summary:** Iranian-linked actors are targeting ~4,000 internet-exposed Rockwell Automation PLCs in attacks against U.S. critical infrastructure. The U.S. government is warning asset owners to immediately isolate OT devices from internet exposure.

### 5. Windows Zero-Day, Stryker Cyberattack, Jones Day Breach in Security Week Roundup
- **Source:** SecurityWeek — https://www.securityweek.com/in-other-news-cyberattack-stings-stryker-windows-zero-day-china-supercomputer-hack/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `zero-day`, `microsoft`, `malware`, `data-breach`
- **Slug:** `2026-04-10-windows-zero-day-stryker-jones-day`
- **Must-know:** no
- **Summary:** SecurityWeek's roundup covers a Windows zero-day under investigation, cyberattacks on Stryker and Jones Day, a compromised Chinese supercomputer, a paused Internet Bug Bounty program, and a new Mac stealer. The Windows zero-day is the highest-priority item pending further disclosure from Microsoft.

### 6. Juniper Networks Patches Critical Unauthenticated RCE in Junos OS
- **Source:** SecurityWeek — https://www.securityweek.com/juniper-networks-patches-dozens-of-junos-os-vulnerabilities/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`
- **Slug:** `2026-04-10-juniper-junos-critical-rce`
- **Must-know:** no
- **Summary:** Juniper patched dozens of Junos OS flaws including a critical unauthenticated RCE enabling full device takeover. No active exploitation was noted; Juniper devices are widely deployed in enterprise and service provider networks.

### 7. Storm-2755 Hijacks Accounts to Redirect Canadian Employee Payroll
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/microsoft-canadian-employees-targeted-in-payroll-pirate-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `phishing`, `microsoft`
- **Slug:** `2026-04-10-storm-2755-canadian-payroll-attacks`
- **Must-know:** no
- **Summary:** Microsoft tracked Storm-2755 conducting "payroll pirate" attacks that compromise employee accounts and redirect direct deposit payments. Targeting Canadian employees; organizations should enforce MFA on HR platforms and add controls around banking info changes.

### 8. Orthanc DICOM Server Vulnerabilities Enable RCE in Medical Imaging Systems
- **Source:** SecurityWeek — https://www.securityweek.com/orthanc-dicom-vulnerabilities-lead-to-crashes-rce/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`
- **Slug:** `2026-04-10-orthanc-dicom-rce-vulnerabilities`
- **Must-know:** no
- **Summary:** Multiple Orthanc DICOM server vulnerabilities allow DoS, information disclosure, and arbitrary code execution. Orthanc is widely deployed in healthcare imaging; RCE in medical environments can expose patient data and disrupt clinical operations.

### 9. Hims Telehealth Breach Exposes Highly Sensitive PHI
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/hims-breach-exposes-sensitive-phi
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`
- **Slug:** `2026-04-10-hims-phi-breach-telehealth`
- **Must-know:** no
- **Summary:** Threat actors breached Hims, a telehealth brand serving customers with stigmatized health conditions (hair loss, obesity, sexual health), exposing PHI. Breach scale undisclosed; affected users face elevated phishing and extortion risk given the sensitivity of their health data.

### 10. Flashpoint Maps the Maturing Phishing-as-a-Service Pipeline Driving Global Fraud
- **Source:** Flashpoint — https://flashpoint.io/blog/the-phishing-as-a-service-pipeline-how-a-scalable-fraud-ecosystem-is-driving-global-attacks/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `phishing`
- **Slug:** `2026-04-10-phishing-as-a-service-pipeline-flashpoint`
- **Must-know:** no
- **Summary:** Flashpoint documented a mature PhaaS ecosystem with specialized roles across kit developers, infrastructure providers, spam services, and fraud actors. Detection requires tracking shared infrastructure fingerprints across the ecosystem rather than individual actors.

### 11. Florida Investigates OpenAI Over ChatGPT's Role in Fatal Shooting
- **Source:** The Record (Recorded Future) — https://therecord.media/florida-investigates-openai-chatgpt-deadly-shooting
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ai-safety`, `openai`, `llm`
- **Slug:** `2026-04-10-florida-chatgpt-shooting-investigation`
- **Must-know:** no
- **Summary:** Florida has opened an investigation into OpenAI after a gunman who maintained constant communication with ChatGPT committed a fatal shooting. A separate wrongful death lawsuit is being filed by the victim's family, adding to growing legal and regulatory scrutiny of AI platform liability.

### 12. Lawsuit: OpenAI Ignored Three Safety Flags Before ChatGPT User Stalked Ex-Girlfriend
- **Source:** TechCrunch AI — https://techcrunch.com/2026/04/10/stalking-victim-sues-openai-claims-chatgpt-fueled-her-abusers-delusions-and-ignored-her-warnings/
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `ai-safety`, `openai`, `llm`
- **Slug:** `2026-04-10-chatgpt-stalking-lawsuit-openai`
- **Must-know:** no
- **Summary:** A lawsuit alleges OpenAI's systems flagged a user's mass-casualty risk three times — including one flag from the platform's own systems — but no action was taken before the user stalked his ex-girlfriend. The case spotlights the liability gap when AI safety systems generate risk signals and platforms fail to act.

### 13. Analysis of 1 Billion CISA KEV Records Shows Defenders Are Losing the Patching Race
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/analysis-of-one-billion-cisa-kev-remediation-records-exposes-limits-of-human-scale-security/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`, `cve`
- **Slug:** `2026-04-10-cisa-kev-remediation-analysis`
- **Must-know:** no
- **Summary:** Qualys analyzed 1 billion CISA KEV remediation records and found that most critical flaws are exploited before organizations can patch them. The findings expose the structural failure of human-scale patch operations against today's attacker exploitation speeds.

### 14. UK Regulator Threatens Tech Executives With Jail Over AI Nudification Tools
- **Source:** The Record (Recorded Future) — https://therecord.media/uk-threatens-tech-bosses-with-jail-ai-nudification
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ai-safety`
- **Slug:** `2026-04-10-uk-nudification-crackdown-ofcom`
- **Must-know:** no
- **Summary:** Ofcom threatened platform executives with jail if they fail to suppress AI nudification tools, citing the Grok scandal that circulated millions of non-consensual AI-generated images. This sets a precedent for personal criminal liability for AI-enabled image abuse in the UK.

## Skippable

- **Anthropic temporarily banned OpenClaw's creator from accessing Claude** — TechCrunch AI. Informational note about a usage policy enforcement; summary too thin to post (one sentence with no technical detail).
- **20-year-old arrested for throwing Molotov cocktail at Sam Altman's house** — The Verge AI. Physical crime incident unrelated to cybersecurity or AI technology.
- **Your Next Breach Will Look Like Business as Usual** — Dark Reading. Opinion piece on detection model shifts; no news event.
- **Kākāpō parrots** — Simon Willison. Off-topic podcast clip about parrots.
- **Senator launches inquiry into 8 tech giants for failures to report CSAM** — The Record. Policy/regulatory inquiry with no technical security substance; no IOCs, TTPs, or new enforcement.
- **The Iranian Lego AI video creators credit their virality to 'heart'** — The Verge AI. Human interest story about AI-generated propaganda; no security or technical angle.
- **TechCrunch is heading to Tokyo — and bringing the Startup Battlefield with it** — TechCrunch AI. Event marketing.
- **Raising the security baseline: Essential AI and cloud security now on by default** — Google Cloud Security. Product marketing announcement for Google Security Command Center Standard tier.
- **ChatGPT voice mode is a weaker model** — Simon Willison. Commentary/observation about model capability; no news event.
- **FINRA Launches Financial Intelligence Fusion Center** — Dark Reading. Institutional announcement with no body text or technical detail.
- **[Video] The TTP Ep. 22: The Collapse of the Patch Window** — Cisco Talos. Video podcast; the underlying topic (patch window collapse) is covered by the Qualys/CISA KEV analysis above with primary data.
- **Orange Business Reimagines Enterprise Voice Communications** — Dark Reading. Marketing content; no security substance.
- **Last 24 hours: Save up to $500 on your TechCrunch Disrupt 2026 pass** — TechCrunch AI. Event ticket promotion.
- **Industrial Controllers Still Vulnerable As Conflicts Move to Cyber** — Dark Reading. Duplicate of the Iranian PLC item; covered by item #4 above.
- **UK says it exposed Russian submarine activity near undersea cables** — The Record. Geopolitical/military incident; no cyber attack TTPs or network security angle.
- **The Good, the Bad and the Ugly in Cybersecurity – Week 15** — SentinelOne Labs. Weekly roundup; individual stories (Iranian PLCs, ClickFix) are covered by primary-source items above.
- **Can Anthropic Keep Its Exploit-Writing AI Out of the Wrong Hands?** — Dark Reading. Follow-up commentary on Mythos Preview; already covered in published post `2026-04-08-anthropic-mythos-preview.md`.
- **Industry Reactions to Iran Hacking ICS in Critical Infrastructure: Feedback Friday** — SecurityWeek. Industry reaction roundup; duplicate coverage of the Iranian PLC story covered by item #4 above.
- **Fear and loathing at OpenAI** — The Verge AI. Podcast about Sam Altman organizational drama; no security or AI safety technical content.
