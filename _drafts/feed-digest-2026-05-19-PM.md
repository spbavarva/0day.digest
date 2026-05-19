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
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `github`, `credential-theft`, `devsecops`
- **Slug:** `2026-05-19-github-actions-supply-chain-cool-issues-helper`
- **Must-know:** yes
- **Summary:** Threat actors redirected every existing tag in the `actions-cool/issues-helper` GitHub Actions repository to a malicious imposter commit that harvests CI/CD credentials. Any pipeline using this action by tag reference — rather than a pinned commit SHA — executed the attacker's payload.

### 2. Compromised Nx Console 18.95.0 Delivers Credential Stealer to 2.2M VS Code Users
- **Source:** The Hacker News — https://thehackernews.com/2026/05/compromised-nx-console-18950-targeted.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `credential-theft`, `appsec`, `devsecops`
- **Slug:** `2026-05-19-nx-console-vscode-credential-stealer-supply-chain`
- **Must-know:** yes
- **Summary:** A malicious version of the Nx Console VS Code extension (`rwl.angular-console` v18.95.0) was published to the VS Code Marketplace, targeting the extension's 2.2 million users with a credential stealer. Developers who installed v18.95.0 should remove it and rotate any secrets accessible from their environment.

### 3. New Shai-Hulud Wave Compromises 600+ npm Packages
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-shai-hulud-malware-wave-compromises-600-npm-packages/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `malware`
- **Slug:** `2026-05-19-shai-hulud-600-npm-supply-chain-wave`
- **Must-know:** yes
- **Summary:** Threat actors published more than 600 malicious packages to npm today in a new wave of the Shai-Hulud supply-chain campaign. Developers who installed npm packages in the affected window should audit dependencies and rotate any accessible secrets.

### 4. Unpatched ChromaDB Flaw Allows Unauthenticated Remote Code Execution
- **Source:** SecurityWeek — https://www.securityweek.com/unpatched-chromadb-vulnerability-can-lead-to-server-takeover/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `rce`, `llm`, `appsec`
- **Slug:** `2026-05-19-chromadb-unpatched-rce-server-takeover`
- **Must-know:** no
- **Summary:** An unpatched vulnerability in ChromaDB allows remote unauthenticated attackers to execute arbitrary code and exfiltrate sensitive data. No patch is available; operators should restrict network access to ChromaDB instances immediately.

### 5. EvilTokens PhaaS Bypasses MFA via OAuth Device Code Flow, Hits 340 Orgs
- **Source:** The Hacker News — https://thehackernews.com/2026/05/the-new-phishing-click-how-oauth.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `phishing`, `iam`, `microsoft`, `vulnerability`
- **Slug:** `2026-05-19-eviltokens-oauth-mfa-bypass-phaas`
- **Must-know:** no
- **Summary:** EvilTokens, a PhaaS platform launched in February 2026, compromised 340+ Microsoft 365 organizations in five weeks by abusing the OAuth device code flow to capture valid access tokens while victims complete their normal MFA challenge. Organizations should restrict the device code flow via Conditional Access policies.

### 6. Critical SEPPMail Gateway Vulnerabilities Enable RCE and Full Mail Traffic Read
- **Source:** The Hacker News — https://thehackernews.com/2026/05/seppmail-secure-e-mail-gateway.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `rce`, `appsec`
- **Slug:** `2026-05-19-seppmail-gateway-rce-mail-access`
- **Must-know:** no
- **Summary:** Critical vulnerabilities in the SEPPMail Secure E-Mail Gateway allow remote code execution and reading of all mail traffic, potentially exposing an entire organization's email to attackers or providing an internal network entry point. Administrators should patch immediately.

### 7. CVE-2026-8153: OS Command Injection Exposes Universal Robots Industrial Fleets
- **Source:** SecurityWeek — https://www.securityweek.com/critical-vulnerability-exposes-industrial-robot-fleets-to-hacking/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`, `ics`
- **Slug:** `2026-05-19-universal-robots-cve-2026-8153-os-command-injection`
- **Must-know:** no
- **Summary:** CVE-2026-8153 in Universal Robots PolyScope 5 allows OS command injection, enabling attackers to compromise industrial robot controllers and disrupt or manipulate robotic operations. Organizations should patch and review network segmentation for robot controller access.

### 8. Microsoft Disrupts Fox Tempest Malware-Signing-as-a-Service Platform
- **Source:** The Record (Recorded Future) — https://therecord.media/microsoft-disrupts-fox-tempest-malware-signing-service
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `ransomware`, `microsoft`
- **Slug:** `2026-05-19-fox-tempest-malware-signing-disrupted`
- **Must-know:** no
- **Summary:** Microsoft unsealed a U.S. District Court case detailing the disruption of Fox Tempest, a malware-signing-as-a-service platform operating since May 2025 that helped ransomware gangs disguise malware as legitimately signed software.

### 9. Drupal Warns of Critical Core Patch on May 20 — Exploits Expected Within Hours
- **Source:** The Hacker News — https://thehackernews.com/2026/05/drupal-to-release-urgent-core-security.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `appsec`
- **Slug:** `2026-05-19-drupal-critical-patch-may-20`
- **Must-know:** no
- **Summary:** Drupal will release a critical core security update for all supported branches on May 20, 2026 (17:00–21:00 UTC); the Security Team warns exploits could follow within hours or days. Administrators should clear their schedules to patch immediately upon release.

### 10. DirtyDecrypt PoC Published for Patched Linux Kernel LPE CVE-2026-31635
- **Source:** The Hacker News — https://thehackernews.com/2026/05/dirtydecrypt-poc-released-for-linux.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`, `zero-day`
- **Slug:** `2026-05-19-dirtydecrypt-linux-kernel-lpe-poc`
- **Must-know:** no
- **Summary:** A public PoC has been released for CVE-2026-31635, a Linux kernel local privilege escalation flaw patched in April. With working exploit code now public, unpatched systems face increased risk; admins should verify the April patch is applied across all Linux hosts.

### 11. 7-Eleven Confirms Data Breach Claimed by ShinyHunters
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/7-eleven-confirms-data-breach-claimed-by-the-shinyhunters-gang/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `2026-05-19-7-eleven-shinyhunters-data-breach`
- **Must-know:** no
- **Summary:** 7-Eleven confirmed a breach of its systems following ShinyHunters' claim last month. The scope of exposed data has not been publicly disclosed. The extortion group has a history of large-scale exfiltration targeting consumer platforms.

### 12. B1ack's Stash Marketplace Releases 4.6 Million Stolen Credit Cards as Free Download
- **Source:** SecurityWeek — https://www.securityweek.com/b1acks-stash-marketplace-gives-away-4-6-million-stolen-credit-cards/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `2026-05-19-b1acks-stash-46m-credit-cards-free`
- **Must-know:** no
- **Summary:** B1ack's Stash released 4.6 million stolen credit cards as a free download to build marketplace reputation, directly fueling downstream card fraud. Financial institutions should flag potentially exposed BINs for enhanced monitoring and evaluate proactive reissuance.

### 13. Siemens RUGGEDCOM APE1808 Affected by Critical PAN-OS Captive Portal RCE
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-139-02
- **Section:** Government / Advisory
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`, `ics`
- **Slug:** `2026-05-19-siemens-ruggedcom-panos-rce`
- **Must-know:** no
- **Summary:** A PAN-OS buffer overflow in the Captive Portal service allows unauthenticated root-level RCE on firewalls embedded in Siemens RUGGEDCOM APE1808 OT devices. Siemens is preparing fixes; operators should apply Palo Alto Networks' published countermeasures in the interim.

### 14. ScadaBR 1.2.0 Hit by Four CVEs Including Unauthenticated RCE (CVSS 9.1)
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-139-03
- **Section:** Government / Advisory
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`, `ics`
- **Slug:** `2026-05-19-scadabr-unauthenticated-rce`
- **Must-know:** no
- **Summary:** Four CVEs (CVE-2026-8602–8605, CVSS 9.1) in ScadaBR 1.2.0 allow unauthenticated RCE via OS command injection, missing authentication, CSRF, and hardcoded credentials. Operators of this widely-used open-source SCADA/HMI platform should apply mitigations and restrict network access.

### 15. Cisco Talos Discloses Eight TP-Link Flaws Plus Bugs in Photoshop, OpenVPN, Norton VPN
- **Source:** Cisco Talos — https://blog.talosintelligence.com/tp-link-photoshop-openvpn-norton-vpn-vulnerabilities/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `vulnerability`, `cve`
- **Slug:** `2026-05-19-cisco-talos-tplink-photoshop-openvpn-norton-vulns`
- **Must-know:** no
- **Summary:** Cisco Talos disclosed eight TP-Link router vulnerabilities and individual flaws in Adobe Photoshop, OpenVPN, and Norton VPN. All have been patched; users should update to the latest versions of affected software and firmware.

### 16. Cisco Talos Tracks BadIIS Commodity MaaS Ecosystem Serving Chinese-Speaking Threat Groups
- **Source:** Cisco Talos — https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `malware`, `cloud-security`, `appsec`
- **Slug:** `2026-05-19-badiis-chinese-maas-ecosystem`
- **Must-know:** no
- **Summary:** Cisco Talos identified a BadIIS variant sold or shared among Chinese-speaking cybercrime groups as a commodity MaaS offering for continuous IIS server monetization. Defenders should audit IIS module configurations and monitor for anomalous loading or outbound traffic.

### 17. Surge in MSHTA LOLBIN Abuse Delivering Stealers and Persistent Malware
- **Source:** SecurityWeek — https://www.securityweek.com/legacy-windows-tool-mshta-fuels-surge-in-silent-malware-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `phishing`, `microsoft`
- **Slug:** `2026-05-19-mshta-lolbin-malware-surge`
- **Must-know:** no
- **Summary:** MSHTA (`mshta.exe`), a legitimate but legacy Windows binary, is seeing a surge in abuse for stealthy infostealer and loader delivery via phishing and LOLBIN chains. Organizations should block MSHTA via AppLocker/WDAC where it has no operational use.

### 18. Trapdoor Android Ad Fraud Operation: 455 Malicious Apps, 659M Daily Fake Bid Requests
- **Source:** The Hacker News — https://thehackernews.com/2026/05/trapdoor-android-ad-fraud-scheme-hit.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `android`
- **Slug:** `2026-05-19-trapdoor-android-ad-fraud-455-apps`
- **Must-know:** no
- **Summary:** HUMAN's Satori team disclosed Trapdoor, an Android-targeting ad fraud operation using 455 malicious apps and 183 C2 domains generating 659M fraudulent daily bid requests. Enterprises should audit mobile device inventories against disclosed indicators.

### 19. UK Regulator to Mandate Tech Firms Tackle Deepfakes and Non-Consensual Intimate Images
- **Source:** The Record (Recorded Future) — https://therecord.media/uk-regulator-to-require-tech-firms-to-tackle-deepfakes-nudification-ai
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ai-safety`, `llm`
- **Slug:** `2026-05-19-uk-deepfake-regulation`
- **Must-know:** no
- **Summary:** The UK regulator announced formal requirements for technology firms to detect and remove deepfakes and AI-generated non-consensual intimate imagery, moving beyond guidance to enforceable obligations. Platforms operating in the UK will need detection and takedown capabilities.

### 20. Google Opens CodeMender AI Code Security Agent to External Testers at I/O
- **Source:** The Verge AI — https://www.theverge.com/tech/933921/google-wants-to-compete-with-anthropics-mythos
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `ai-launch`, `google`, `appsec`, `llm`
- **Slug:** `2026-05-19-google-codemender-ai-code-security`
- **Must-know:** no
- **Summary:** Google announced wider external access to CodeMender, its AI agent for code security, at Google I/O — positioning it as a direct competitor to Anthropic's Mythos. Select security experts are being invited to test the API as Google expands its AI-powered AppSec tooling.

### 21. Google Launches Gemini 3.5 Flash — Agentic Model Built to Execute Complex Tasks
- **Source:** TechCrunch AI — https://techcrunch.com/2026/05/19/with-gemini-3-5-flash-google-bets-its-next-ai-wave-on-agents-not-chatbots/
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `google`, `llm`
- **Slug:** `2026-05-19-gemini-35-flash-launch`
- **Must-know:** no
- **Summary:** Google launched Gemini 3.5 Flash at Google I/O 2026, its most capable coding and agentic model, available today via the API. The launch signals Google's pivot from chatbot interfaces toward agent-native AI architectures.

### 22. OpenAI Co-Founder Andrej Karpathy Joins Anthropic's Pre-Training Team
- **Source:** TechCrunch AI — https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `anthropic`, `openai`, `llm`
- **Slug:** `2026-05-19-karpathy-joins-anthropic`
- **Must-know:** no
- **Summary:** Andrej Karpathy has joined Anthropic's pre-training team — the group responsible for large-scale training runs that give Claude its foundational capabilities. The move is a significant talent shift in the AI lab competitive landscape.

### 23. Allen AI Releases OlmoEarth v1.1 — More Efficient Open-Weights Model Family
- **Source:** Hugging Face Blog — https://huggingface.co/blog/allenai/olmoearth-v1-1
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `llm`
- **Slug:** `2026-05-19-olmoearth-v11-model`
- **Must-know:** no
- **Summary:** Allen AI released OlmoEarth v1.1, a more efficient iteration of its open-weights Earth-observation model family, via Hugging Face. Full model weights and technical details are publicly available.

### 24. OpenAI and Google Align on AI Image Provenance — C2PA and SynthID Get Wider Rollout
- **Source:** OpenAI Blog — https://openai.com/index/advancing-content-provenance
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `ai-safety`, `openai`, `google`, `llm`
- **Slug:** `2026-05-19-openai-google-content-provenance-c2pa-synthid`
- **Must-know:** no
- **Summary:** OpenAI is joining C2PA and adding SynthID to its products; Google is expanding SynthID and C2PA detection to Chrome and Search. The coordinated move by the two largest AI image generators toward interoperable provenance metadata is a meaningful step for AI content trust infrastructure.

## Skippable

- **[Virtual Event] Anatomy of a Data Breach** — Dark Reading. Webinar/event listing, not news.
- **Gemini will use Volvo's external cameras to interpret parking signs** — The Verge AI. Consumer automotive AI feature, no security angle.
- **The 13 biggest announcements at Google I/O 2026** — The Verge AI. Duplicate roundup; individual I/O items covered separately where relevant.
- **Google's Genie world model can now simulate real streets** — TechCrunch AI. Research demo for robotics and gaming, no security angle.
- **How to use Google's new information agents** — TechCrunch AI. Consumer product feature, no security angle.
- **Google Search as you know it is over** — TechCrunch AI. Opinion/editorial piece; individual Google I/O announcements covered separately.
- **I/O 2026 (collection)** — Google AI Blog. Marketing roundup with no individual news value.
- **How AI Mode is changing the way people search** — Google AI Blog. Product marketing, no security relevance.
- **New ways to create in Google Workspace** — Google AI Blog. Workspace feature marketing, no security angle.
- **I/O 2026: Welcome to the agentic Gemini era** — Google AI Blog. CEO keynote blog post; duplicate of Gemini 3.5 coverage.
- **Gemini 3.5: frontier intelligence with action** — Google AI Blog. Duplicate of TechCrunch Gemini 3.5 Flash item.
- **A new era for AI Search** — Google AI Blog. Marketing post; duplicate of broader Google Search coverage.
- **Everything new in our Google AI subscriptions** — Google AI Blog. Subscription pricing marketing, no news value.
- **Google's AI Studio now lets anyone build Android apps in minutes** — TechCrunch AI. Developer product feature, no security angle.
- **Google's AI now lets you talk to your Gmail inbox** — TechCrunch AI. Consumer product feature, no security angle.
- **Google's Gemini Omni turns images, audio, and text into video** — TechCrunch AI. Video generation product feature, no security angle.
- **OpenAI is making it easier to check if an image was made by their models** — TechCrunch AI. Duplicate of OpenAI Blog C2PA/SynthID item.
- **Google launches Antigravity 2.0** — TechCrunch AI. Consumer AI assistant product launch, no security angle.
- **Google's new Universal Cart** — TechCrunch AI. AI-powered shopping feature, no security angle.
- **Google adds voice-based prompting to Docs and Keep** — TechCrunch AI. Productivity feature, no security angle.
- **Google introduces Gemini Spark** — TechCrunch AI. Duplicate of The Verge item 32 coverage.
- **Google just declared itself a contender in AI design** — TechCrunch AI. Product marketing, no news value.
- **Google updates its Gemini app** — TechCrunch AI. Consumer product update, duplicate of I/O coverage.
- **Agentic app coding gets an upgrade with Google's release of Android CLI** — TechCrunch AI. Developer tool feature, duplicate of AI Studio announcement.
- **Google can now vibe-code you an Android app** — The Verge AI. Duplicate of TechCrunch AI Studio Android item.
- **Would you let robots spend your money?** — The Verge AI. Duplicate of TechCrunch Universal Cart item.
- **Google Search is getting its biggest changes ever** — The Verge AI. Duplicate of TechCrunch Google Search item.
- **Gmail is going to start talking to you** — The Verge AI. Duplicate of TechCrunch Gmail AI item.
- **Google is launching its own version of OpenClaw** — The Verge AI. Duplicate of TechCrunch Gemini Spark item.
- **Google Pics is a new app that tries to fix AI image editing** — The Verge AI. AI image editing product feature, no security angle.
- **Google is trying to make deepfake detection more accessible** — The Verge AI. Duplicate of OpenAI Blog C2PA/SynthID item.
- **Microsoft plans to improve Windows 11 driver quality in 2026** — BleepingComputer. IT roadmap announcement, no security incident.
- **Drupal to Patch Highly Critical Vulnerability** — SecurityWeek. Duplicate of The Hacker News Drupal item.
- **Governing infrastructure as code using pattern-based policy as code** — AWS Security Blog. Cloud ops tutorial, not an incident or vulnerability.
- **Microsoft blames macOS update for undismissible Teams location prompts** — BleepingComputer. Product bug, not a security vulnerability.
- **Microsoft Disrupts Fox Tempest (SecurityWeek)** — SecurityWeek. Duplicate of The Record Fox Tempest item.
- **Critical Microsoft Vulnerabilities Doubled** — BleepingComputer. BeyondTrust trend analysis report, not an actionable security incident.
- **Turn Blind Trust into Verified Control with Prompt Security for Agentic AI** — SentinelOne Labs. Vendor product marketing disguised as research.
- **Looking Back, Looking Forward: Bouillabaisse of Cyber Evolution** — Dark Reading. Retrospective opinion piece, no news value.
- **Webinar: The hidden bottlenecks in network incident response** — BleepingComputer. Webinar promotional content.
- **Kieback & Peter DDC Building Controllers** — CISA Alerts. Routine ICS advisory; browser XSS in building controllers, lower severity.
- **ABB CoreSense HM and CoreSense M10** — CISA Alerts. Routine ICS advisory; path traversal, CVSS 7.1, limited scope.
- **ZKTeco CCTV Cameras** — CISA Alerts. Routine ICS advisory; CCTV auth bypass — niche OT/physical security scope.
- **Cyber Resilience is the New Business Continuity Plan** — SecurityWeek. Opinion/sponsored content, no news value.
- **Microsoft confirms patching issues in restricted Windows networks** — BleepingComputer. Windows Update configuration issue, not a vulnerability.
- **201 Arrested in Crackdown on Cybercrime in Middle East, North Africa** — SecurityWeek. Law enforcement operation; no technical TTPs or IOCs disclosed.
- **PoC Released for DirtyDecrypt Linux Kernel Vulnerability** — SecurityWeek. Duplicate of The Hacker News DirtyDecrypt item.
