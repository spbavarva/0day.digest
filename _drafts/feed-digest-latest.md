# Digest — 2026-05-19 PM

- Window: last 14h
- Raw items considered: 71
- Relevant: 24
- Skippable: 47

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** GitHub Actions Supply Chain Attack Hijacks actions-cool/issues-helper Tags — `2026-05-19-github-actions-supply-chain-cool-issues-helper.md`
- [x] **[CRITICAL]** Compromised Nx Console 18.95.0 Delivers Credential Stealer to 2.2M VS Code Users — `2026-05-19-nx-console-vscode-credential-stealer-supply-chain.md`
- [x] **[CRITICAL]** New Shai-Hulud Wave Compromises 600+ npm Packages in Fresh Supply Chain Hit — `2026-05-19-shai-hulud-600-npm-supply-chain-wave.md`
- [x] **[HIGH]** Unpatched ChromaDB Flaw Allows Unauthenticated Remote Code Execution — `2026-05-19-chromadb-unpatched-rce-server-takeover.md`
- [x] **[HIGH]** EvilTokens PhaaS Bypasses MFA via OAuth Device Code Flow, Hits 340 Orgs — `2026-05-19-eviltokens-oauth-mfa-bypass-phaas.md`
- [x] **[HIGH]** Critical SEPPMail Gateway Vulnerabilities Enable RCE and Full Mail Traffic Read — `2026-05-19-seppmail-gateway-rce-mail-access.md`
- [x] **[HIGH]** CVE-2026-8153: OS Command Injection Exposes Universal Robots Industrial Fleets — `2026-05-19-universal-robots-cve-2026-8153-os-command-injection.md`
- [x] **[HIGH]** Microsoft Disrupts Fox Tempest Malware-Signing-as-a-Service Platform — `2026-05-19-fox-tempest-malware-signing-disrupted.md`
- [x] **[HIGH]** Drupal Warns of Critical Core Patch on May 20 — Exploits Expected Within Hours — `2026-05-19-drupal-critical-patch-may-20.md`
- [x] **[HIGH]** DirtyDecrypt PoC Published for Patched Linux Kernel LPE CVE-2026-31635 — `2026-05-19-dirtydecrypt-linux-kernel-lpe-poc.md`
- [x] **[HIGH]** 7-Eleven Confirms Data Breach Claimed by ShinyHunters — `2026-05-19-7-eleven-shinyhunters-data-breach.md`
- [x] **[HIGH]** B1ack's Stash Marketplace Releases 4.6 Million Stolen Credit Cards as Free Download — `2026-05-19-b1acks-stash-46m-credit-cards-free.md`
- [x] **[HIGH]** Siemens RUGGEDCOM APE1808 Affected by Critical PAN-OS Captive Portal RCE — `2026-05-19-siemens-ruggedcom-panos-rce.md`
- [x] **[HIGH]** ScadaBR 1.2.0 Hit by Four CVEs Including Unauthenticated RCE (CVSS 9.1) — `2026-05-19-scadabr-unauthenticated-rce.md`
- [x] **[MEDIUM]** Cisco Talos Discloses Eight TP-Link Flaws Plus Bugs in Photoshop, OpenVPN, Norton VPN — `2026-05-19-cisco-talos-tplink-photoshop-openvpn-norton-vulns.md`
- [x] **[MEDIUM]** Cisco Talos Tracks BadIIS Commodity MaaS Ecosystem Serving Chinese-Speaking Threat Groups — `2026-05-19-badiis-chinese-maas-ecosystem.md`
- [x] **[MEDIUM]** Surge in MSHTA LOLBIN Abuse Delivering Stealers and Persistent Malware — `2026-05-19-mshta-lolbin-malware-surge.md`
- [x] **[MEDIUM]** Trapdoor Android Ad Fraud Operation: 455 Malicious Apps, 659M Daily Fake Bid Requests — `2026-05-19-trapdoor-android-ad-fraud-455-apps.md`
- [x] **[MEDIUM]** UK Regulator to Mandate Tech Firms Tackle Deepfakes and Non-Consensual Intimate Images — `2026-05-19-uk-deepfake-regulation.md`
- [x] **[MEDIUM]** Google Opens CodeMender AI Code Security Agent to External Testers at I/O — `2026-05-19-google-codemender-ai-code-security.md`
- [x] **[INFORMATIONAL]** Google Launches Gemini 3.5 Flash — Agentic Model Built to Execute Complex Tasks — `2026-05-19-gemini-35-flash-launch.md`
- [x] **[INFORMATIONAL]** OpenAI Co-Founder Andrej Karpathy Joins Anthropic's Pre-Training Team — `2026-05-19-karpathy-joins-anthropic.md`
- [x] **[INFORMATIONAL]** Allen AI Releases OlmoEarth v1.1 — More Efficient Open-Weights Model Family — `2026-05-19-olmoearth-v11-model.md`
- [x] **[INFORMATIONAL]** OpenAI and Google Align on AI Image Provenance — C2PA and SynthID Get Wider Rollout — `2026-05-19-openai-google-content-provenance-c2pa-synthid.md`

## Relevant (details)

### 1. GitHub Actions Supply Chain Attack Hijacks actions-cool/issues-helper Tags
- **Source:** The Hacker News — https://thehackernews.com/2026/05/github-actions-supply-chain-attack.html
- **Severity:** critical
- **Tags:** `supply-chain`, `github`, `credential-theft`, `devsecops`
- **Summary:** Threat actors redirected every existing tag in `actions-cool/issues-helper` to a malicious imposter commit harvesting CI/CD credentials. Any pipeline using this action by tag reference executed the attacker's payload; rotate secrets and pin to commit SHAs.

### 2. Compromised Nx Console 18.95.0 Delivers Credential Stealer to 2.2M VS Code Users
- **Source:** The Hacker News — https://thehackernews.com/2026/05/compromised-nx-console-18950-targeted.html
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `credential-theft`, `appsec`, `devsecops`
- **Summary:** A malicious version of `rwl.angular-console` v18.95.0 was published to the VS Code Marketplace targeting the extension's 2.2 million users with a credential stealer. Developers who installed v18.95.0 should remove it and rotate any accessible secrets.

### 3. New Shai-Hulud Wave Compromises 600+ npm Packages
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-shai-hulud-malware-wave-compromises-600-npm-packages/
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `malware`
- **Summary:** Threat actors published 600+ malicious npm packages today in a new Shai-Hulud supply-chain wave. Developers who installed packages in the affected window should audit dependencies and rotate accessible secrets.

### 4. Unpatched ChromaDB Flaw Allows Unauthenticated Remote Code Execution
- **Source:** SecurityWeek — https://www.securityweek.com/unpatched-chromadb-vulnerability-can-lead-to-server-takeover/
- **Severity:** high
- **Tags:** `vulnerability`, `rce`, `llm`, `appsec`
- **Summary:** An unpatched ChromaDB vulnerability allows remote unauthenticated RCE and data exfiltration; no patch available. Restrict network access to ChromaDB instances immediately.

### 5. EvilTokens PhaaS Bypasses MFA via OAuth Device Code Flow, Hits 340 Orgs
- **Source:** The Hacker News — https://thehackernews.com/2026/05/the-new-phishing-click-how-oauth.html
- **Severity:** high
- **Tags:** `phishing`, `iam`, `microsoft`, `vulnerability`
- **Summary:** EvilTokens compromised 340+ Microsoft 365 organizations in five weeks by abusing the OAuth device code flow to steal access tokens while victims complete real MFA challenges. Restrict device code flow via Conditional Access policies.

### 6. Critical SEPPMail Gateway Vulnerabilities Enable RCE and Full Mail Traffic Read
- **Source:** The Hacker News — https://thehackernews.com/2026/05/seppmail-secure-e-mail-gateway.html
- **Severity:** high
- **Tags:** `vulnerability`, `rce`, `appsec`
- **Summary:** Critical flaws in SEPPMail Secure E-Mail Gateway allow RCE and reading of all mail traffic or use as an internal network entry point. Administrators should patch immediately.

### 7. CVE-2026-8153: OS Command Injection Exposes Universal Robots Industrial Fleets
- **Source:** SecurityWeek — https://www.securityweek.com/critical-vulnerability-exposes-industrial-robot-fleets-to-hacking/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`, `ics`
- **Summary:** CVE-2026-8153 in Universal Robots PolyScope 5 allows OS command injection enabling compromise of industrial robot controllers. Patch and review network segmentation for robot controller access.

### 8. Microsoft Disrupts Fox Tempest Malware-Signing-as-a-Service Platform
- **Source:** The Record (Recorded Future) — https://therecord.media/microsoft-disrupts-fox-tempest-malware-signing-service
- **Severity:** high
- **Tags:** `malware`, `ransomware`, `microsoft`
- **Summary:** Microsoft unsealed a U.S. District Court case disrupting Fox Tempest, a code-signing-as-a-service platform used by ransomware gangs since May 2025 to disguise malware as legitimately signed software.

### 9. Drupal Warns of Critical Core Patch on May 20 — Exploits Expected Within Hours
- **Source:** The Hacker News — https://thehackernews.com/2026/05/drupal-to-release-urgent-core-security.html
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `appsec`
- **Summary:** Drupal releases a critical core update for all supported branches on May 20 (17:00–21:00 UTC); the Security Team warns exploits could follow within hours. Reserve time to patch immediately upon release.

### 10. DirtyDecrypt PoC Published for Patched Linux Kernel LPE CVE-2026-31635
- **Source:** The Hacker News — https://thehackernews.com/2026/05/dirtydecrypt-poc-released-for-linux.html
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`, `zero-day`
- **Summary:** A public PoC for CVE-2026-31635, a Linux kernel LPE patched in April, has been released. Unpatched systems face increased exploitation risk; verify the April patch is applied across all Linux hosts.

### 11. 7-Eleven Confirms Data Breach Claimed by ShinyHunters
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/7-eleven-confirms-data-breach-claimed-by-the-shinyhunters-gang/
- **Severity:** high
- **Tags:** `data-breach`
- **Summary:** 7-Eleven confirmed a ShinyHunters breach of its systems; scope of exposed data has not been publicly disclosed. ShinyHunters typically exfiltrates large datasets that surface for downstream fraud.

### 12. B1ack's Stash Marketplace Releases 4.6 Million Stolen Credit Cards as Free Download
- **Source:** SecurityWeek — https://www.securityweek.com/b1acks-stash-marketplace-gives-away-4-6-million-stolen-credit-cards/
- **Severity:** high
- **Tags:** `data-breach`
- **Summary:** B1ack's Stash released 4.6 million stolen credit cards as a free download. Financial institutions should flag exposed BINs for enhanced monitoring and evaluate proactive card reissuance.

### 13. Siemens RUGGEDCOM APE1808 Affected by Critical PAN-OS Captive Portal RCE
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-139-02
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`, `ics`
- **Summary:** A PAN-OS buffer overflow in the Captive Portal service allows unauthenticated root RCE on Siemens RUGGEDCOM APE1808 OT devices. Apply Palo Alto Networks' countermeasures while Siemens prepares fixes.

### 14. ScadaBR 1.2.0 Hit by Four CVEs Including Unauthenticated RCE (CVSS 9.1)
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-139-03
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`, `ics`
- **Summary:** Four CVEs (CVE-2026-8602–8605, CVSS 9.1) in ScadaBR 1.2.0 allow unauthenticated RCE. Operators should apply mitigations and restrict network access to this widely-used SCADA/HMI platform.

### 15. Cisco Talos Discloses Eight TP-Link Flaws Plus Bugs in Photoshop, OpenVPN, Norton VPN
- **Source:** Cisco Talos — https://blog.talosintelligence.com/tp-link-photoshop-openvpn-norton-vpn-vulnerabilities/
- **Severity:** medium
- **Tags:** `vulnerability`, `cve`
- **Summary:** Cisco Talos disclosed patched vulnerabilities across TP-Link routers (8), Adobe Photoshop, OpenVPN, and Norton VPN. Update firmware and software to latest versions.

### 16. Cisco Talos Tracks BadIIS Commodity MaaS Ecosystem Serving Chinese-Speaking Threat Groups
- **Source:** Cisco Talos — https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/
- **Severity:** medium
- **Tags:** `malware`, `cloud-security`, `appsec`
- **Summary:** A BadIIS variant is being sold/shared among Chinese-speaking threat groups as a MaaS offering for IIS server monetization. Audit IIS configurations and monitor for anomalous module loading.

### 17. Surge in MSHTA LOLBIN Abuse Delivering Stealers and Persistent Malware
- **Source:** SecurityWeek — https://www.securityweek.com/legacy-windows-tool-mshta-fuels-surge-in-silent-malware-attacks/
- **Severity:** medium
- **Tags:** `malware`, `phishing`, `microsoft`
- **Summary:** MSHTA abuse is surging for stealthy infostealer and loader delivery via phishing and LOLBIN chains. Block MSHTA via AppLocker/WDAC where not operationally required.

### 18. Trapdoor Android Ad Fraud Operation: 455 Malicious Apps, 659M Daily Fake Bid Requests
- **Source:** The Hacker News — https://thehackernews.com/2026/05/trapdoor-android-ad-fraud-scheme-hit.html
- **Severity:** medium
- **Tags:** `malware`, `android`
- **Summary:** HUMAN disclosed Trapdoor, an Android ad fraud operation using 455 malicious apps and 183 C2 domains generating 659M fraudulent daily bid requests. Audit MDM app inventories against disclosed indicators.

### 19. UK Regulator to Mandate Tech Firms Tackle Deepfakes and Non-Consensual Intimate Images
- **Source:** The Record (Recorded Future) — https://therecord.media/uk-regulator-to-require-tech-firms-to-tackle-deepfakes-nudification-ai
- **Severity:** medium
- **Tags:** `ai-safety`, `llm`
- **Summary:** The UK regulator announced enforceable requirements for tech firms to detect and remove AI-generated NCII and deepfakes. Platforms operating in the UK will need detection and takedown capabilities.

### 20. Google Opens CodeMender AI Code Security Agent to External Testers at I/O
- **Source:** The Verge AI — https://www.theverge.com/tech/933921/google-wants-to-compete-with-anthropics-mythos
- **Severity:** medium
- **Tags:** `ai-launch`, `google`, `appsec`, `llm`
- **Summary:** Google is opening CodeMender, its AI code security agent, to select external testers at I/O — positioning it against Anthropic's Mythos in AI-assisted vulnerability detection.

### 21. Google Launches Gemini 3.5 Flash — Agentic Model Built to Execute Complex Tasks
- **Source:** TechCrunch AI — https://techcrunch.com/2026/05/19/with-gemini-3-5-flash-google-bets-its-next-ai-wave-on-agents-not-chatbots/
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `google`, `llm`
- **Summary:** Gemini 3.5 Flash, Google's most capable coding and agentic model, launched at Google I/O 2026 and is available via API today, marking Google's shift toward agent-native AI architectures.

### 22. OpenAI Co-Founder Andrej Karpathy Joins Anthropic's Pre-Training Team
- **Source:** TechCrunch AI — https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/
- **Severity:** informational
- **Tags:** `anthropic`, `openai`, `llm`
- **Summary:** Andrej Karpathy joins Anthropic's pre-training team, responsible for the large-scale training runs behind Claude. A significant talent shift in the AI lab competitive landscape.

### 23. Allen AI Releases OlmoEarth v1.1 — More Efficient Open-Weights Model Family
- **Source:** Hugging Face Blog — https://huggingface.co/blog/allenai/olmoearth-v1-1
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `llm`
- **Summary:** Allen AI released OlmoEarth v1.1, a more efficient open-weights Earth-observation model family, via Hugging Face with publicly available weights.

### 24. OpenAI and Google Align on AI Image Provenance — C2PA and SynthID Get Wider Rollout
- **Source:** OpenAI Blog — https://openai.com/index/advancing-content-provenance
- **Severity:** informational
- **Tags:** `ai-safety`, `openai`, `google`, `llm`
- **Summary:** OpenAI joins C2PA and adds SynthID while Google expands both standards to Chrome and Search — a coordinated move toward interoperable AI image provenance metadata across the two largest AI image generators.

## Skippable

- **[Virtual Event] Anatomy of a Data Breach** — Dark Reading. Webinar/event listing, not news.
- **Gemini will use Volvo's external cameras** — The Verge AI. Consumer automotive AI feature, no security angle.
- **The 13 biggest announcements at Google I/O 2026** — The Verge AI. Duplicate roundup; individual items covered separately.
- **Google's Genie world model + Street View** — TechCrunch AI. Research demo for robotics/gaming, no security angle.
- **How to use Google's new information agents** — TechCrunch AI. Consumer product feature, no security angle.
- **Google Search as you know it is over** — TechCrunch AI. Opinion editorial; individual I/O items covered separately.
- **I/O 2026 collection** — Google AI Blog. Marketing roundup, no individual news value.
- **How AI Mode is changing search** — Google AI Blog. Product marketing, no security relevance.
- **New ways to create in Google Workspace** — Google AI Blog. Workspace marketing, no security angle.
- **Welcome to the agentic Gemini era** — Google AI Blog. CEO keynote post; duplicate of Gemini 3.5 coverage.
- **Gemini 3.5: frontier intelligence with action** — Google AI Blog. Duplicate of TechCrunch Gemini 3.5 Flash item.
- **A new era for AI Search** — Google AI Blog. Marketing post; duplicate of Google Search coverage.
- **Everything new in our Google AI subscriptions** — Google AI Blog. Subscription pricing marketing.
- **Google's AI Studio now lets anyone build Android apps** — TechCrunch AI. Developer product feature, no security angle.
- **Google's AI now lets you talk to your Gmail inbox** — TechCrunch AI. Consumer product feature, no security angle.
- **Google's Gemini Omni turns images, audio, and text into video** — TechCrunch AI. Video generation feature, no security angle.
- **OpenAI is making it easier to check if an image was made by their models** — TechCrunch AI. Duplicate of OpenAI Blog C2PA/SynthID item.
- **Google launches Antigravity 2.0** — TechCrunch AI. Consumer AI assistant product, no security angle.
- **Google's new Universal Cart** — TechCrunch AI. AI shopping feature, no security angle.
- **Google adds voice-based prompting to Docs and Keep** — TechCrunch AI. Productivity feature, no security angle.
- **Google introduces Gemini Spark** — TechCrunch AI. Duplicate of The Verge Gemini Spark item.
- **Google just declared itself a contender in AI design** — TechCrunch AI. Product marketing, no news value.
- **Google updates its Gemini app** — TechCrunch AI. Consumer product update, duplicate I/O coverage.
- **Agentic app coding gets an upgrade with Android CLI** — TechCrunch AI. Developer tool feature, duplicate of AI Studio announcement.
- **Google can now vibe-code you an Android app** — The Verge AI. Duplicate of TechCrunch AI Studio Android item.
- **Would you let robots spend your money?** — The Verge AI. Duplicate of TechCrunch Universal Cart item.
- **Google Search is getting its biggest changes ever** — The Verge AI. Duplicate of TechCrunch Google Search item.
- **Gmail is going to start talking to you** — The Verge AI. Duplicate of TechCrunch Gmail AI item.
- **Google is launching its own version of OpenClaw** — The Verge AI. Duplicate of TechCrunch Gemini Spark item.
- **Google Pics is a new app** — The Verge AI. AI image editing product feature, no security angle.
- **Google is trying to make deepfake detection more accessible** — The Verge AI. Duplicate of OpenAI Blog C2PA/SynthID item.
- **Microsoft plans to improve Windows 11 driver quality** — BleepingComputer. IT roadmap, no security incident.
- **Drupal to Patch Highly Critical Vulnerability (SecurityWeek)** — SecurityWeek. Duplicate of The Hacker News Drupal item.
- **Governing IaC with pattern-based policy as code** — AWS Security Blog. Cloud ops tutorial, not an incident or vulnerability.
- **Microsoft Teams undismissible location prompts on macOS** — BleepingComputer. Product bug, not a security vulnerability.
- **Microsoft Disrupts Fox Tempest (SecurityWeek)** — SecurityWeek. Duplicate of The Record Fox Tempest item.
- **Critical Microsoft Vulnerabilities Doubled** — BleepingComputer. BeyondTrust trend analysis report, not an actionable incident.
- **Prompt Security for Agentic AI** — SentinelOne Labs. Vendor product marketing disguised as research.
- **Looking Back, Looking Forward: Bouillabaisse** — Dark Reading. Retrospective opinion piece, no news value.
- **Webinar: hidden bottlenecks in network incident response** — BleepingComputer. Webinar promotional content.
- **Kieback & Peter DDC Building Controllers** — CISA Alerts. Routine ICS advisory; lower-severity building controller XSS.
- **ABB CoreSense HM and CoreSense M10** — CISA Alerts. Routine ICS advisory; path traversal CVSS 7.1.
- **ZKTeco CCTV Cameras** — CISA Alerts. Routine ICS advisory; CCTV auth bypass, niche OT/physical scope.
- **Cyber Resilience is the New Business Continuity Plan** — SecurityWeek. Opinion/sponsored content, no news value.
- **Microsoft confirms patching issues in restricted Windows networks** — BleepingComputer. Windows Update configuration issue, not a vulnerability.
- **201 Arrested in Crackdown on Cybercrime in MENA** — SecurityWeek. Law enforcement operation; no technical TTPs or IOCs.
- **PoC Released for DirtyDecrypt Linux Kernel Vulnerability (SecurityWeek)** — SecurityWeek. Duplicate of The Hacker News DirtyDecrypt item.
