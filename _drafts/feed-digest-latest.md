# Digest — 2026-11-10 PM

- Window: last 14h
- Raw items considered: 51
- Relevant: 15
- Skippable: 36

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** SAP Patches Four CVSS 10.0 Flaws Enabling Unauthenticated RCE — `2026-11-10-sap-netweaver-webdispatcher-cvss-10-rce.md`
- [x] **[CRITICAL]** Chrome Patches Eighth Actively Exploited Zero-Day of 2026 — `2026-11-10-chrome-eighth-zero-day-xml-uaf.md`
- [x] **[HIGH]** iOS Sandbox Escape Exposes Crypto Wallet Keys, No Apple Fix Yet — `2026-11-10-ios-sandbox-escape-crypto-wallet-keys.md`
- [x] **[HIGH]** Barracuda ESG Flaws Now Exploited for Root Access — `2026-11-10-barracuda-esg-root-access-exploited.md`
- [x] **[HIGH]** Qubole Supply Chain Attack Hits Over a Dozen Organizations — `2026-11-10-qubole-supply-chain-attack.md`
- [x] **[HIGH]** Turla's New Cereal Malware Targets Government Exchange Servers — `2026-11-10-turla-cereal-malware-exchange-espionage.md`
- [x] **[HIGH]** N-able Takes N-central Offline After 33 Zero-Days Disclosed — `2026-11-10-n-able-n-central-33-zero-days-offline.md`
- [x] **[HIGH]** CISA Adds OpenSSH, GPUStack, FreeSwitch, IBM Flaws to KEV — `2026-11-10-cisa-kev-openssh-gpustack-freeswitch-ibm.md`
- [x] **[HIGH]** France Blames Iran for Sabotage of Retail Refrigeration Controllers — `2026-11-10-iran-refrigeration-sabotage-france.md`
- [x] **[HIGH]** Fireworks AI Discloses Breach After Third-Party Cloud Provider Hack — `2026-11-10-fireworks-ai-breach-cloud-provider.md`
- [x] **[MEDIUM]** Apple Patches iMessage Group Chat and Bluetooth Pairing Flaws — `2026-11-10-apple-imessage-bluetooth-patches.md`
- [x] **[MEDIUM]** AI Lowers the Barrier for Reverse Engineering Software and Malware — `2026-11-10-ai-reverse-engineering-malware-barrier.md`
- [x] **[INFORMATIONAL]** Anthropic Ships Claude Fable 5.2 and Mythos 5.2 With Security-Focused Gains — `2026-11-10-anthropic-fable-mythos-5-2-security.md`
- [x] **[INFORMATIONAL]** Flashpoint Launches Agentic AI for Threat Intelligence — `2026-11-10-flashpoint-agentic-ai-threat-intel.md`
- [x] **[INFORMATIONAL]** DeepMind's AlphaProof Code Verifies Signal's Core Encryption — `2026-11-10-deepmind-alphaproof-code-signal-encryption.md`

## Relevant (details)

### 1. SAP Patches Four CVSS 10.0 Flaws Enabling Unauthenticated RCE
- **Source:** The Hacker News — https://thehackernews.com/2026/11/sap-patches-four-cvss-100-flaws.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `rce`, `cve`
- **Slug:** `sap-netweaver-webdispatcher-cvss-10-rce`
- **Must-know:** no
- **Summary:** SAP's November Patch Day fixed four flaws rated CVSS 10.0 — three in NetWeaver and one in the internet-facing Web Dispatcher. All four require no authentication, and two enable remote code execution.

### 2. Chrome Patches Eighth Actively Exploited Zero-Day of 2026
- **Source:** The Hacker News — https://thehackernews.com/2026/11/google-issues-chrome-security-update.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `cve`, `google`
- **Slug:** `chrome-eighth-zero-day-xml-uaf`
- **Must-know:** yes
- **Summary:** Google patched CVE-2026-125350, a use-after-free in Chrome's XML component that is already under active exploitation. It's the eighth Chrome zero-day fixed so far this year.

### 3. iOS Sandbox Escape Exposes Crypto Wallet Keys, No Apple Fix Yet
- **Source:** The Hacker News — https://thehackernews.com/2026/11/binance-warns-of-ios-sandbox-escape.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `zero-day`, `privilege-escalation`
- **Slug:** `ios-sandbox-escape-crypto-wallet-keys`
- **Must-know:** no
- **Summary:** A publicly released iOS sandbox escape called worse_query lets one app read another app's files on iOS 26/27, putting crypto wallet seed phrases and credentials at risk. Apple's latest updates don't list a fix.

### 4. Barracuda ESG Flaws Now Exploited for Root Access
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-exploit-barracuda-email-security-gateway-flaws-to-get-root-access/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `privilege-escalation`, `rce`
- **Slug:** `barracuda-esg-root-access-exploited`
- **Must-know:** no
- **Summary:** Barracuda confirmed active exploitation of two previously patched Email Security Gateway flaws that let attackers run commands with root privileges on unpatched appliances.

### 5. Qubole Supply Chain Attack Hits Over a Dozen Organizations
- **Source:** SecurityWeek — https://www.securityweek.com/over-a-dozen-organizations-hit-in-qubole-supply-chain-attack/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `data-breach`, `iam`
- **Slug:** `qubole-supply-chain-attack`
- **Must-know:** no
- **Summary:** Attackers used compromised IAM credentials belonging to Qubole to access customer environments, stealing files, secrets, API keys, and other credentials across more than a dozen organizations.

### 6. Turla's New Cereal Malware Targets Government Exchange Servers
- **Source:** The Hacker News — https://thehackernews.com/2026/11/russian-turla-hackers-use-new-cereal.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `data-breach`
- **Slug:** `turla-cereal-malware-exchange-espionage`
- **Must-know:** no
- **Summary:** Russia-aligned Turla (Snake) is using a previously undocumented modular toolset called Cereal to intercept email on government Microsoft Exchange servers, including mail systems in Romania and Kazakhstan carrying NATO/EU correspondence.

### 7. N-able Takes N-central Offline After 33 Zero-Days Disclosed
- **Source:** The Hacker News — https://thehackernews.com/2026/11/n-able-takes-hosted-n-central-offline.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `zero-day`, `rce`, `privilege-escalation`
- **Slug:** `n-able-n-central-33-zero-days-offline`
- **Must-know:** no
- **Summary:** A researcher publicly disclosed over 30 vulnerabilities (tracked as Able2Shell) with working PoC exploits against N-able's N-central RMM platform. N-able took its hosted environment offline and told on-prem customers to shut down pending fixes.

### 8. CISA Adds OpenSSH, GPUStack, FreeSwitch, IBM Flaws to KEV
- **Source:** The Hacker News — https://thehackernews.com/2026/11/cisa-warns-of-active-exploitation-of.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Slug:** `cisa-kev-openssh-gpustack-freeswitch-ibm`
- **Must-know:** no
- **Summary:** CISA added four actively exploited flaws to its KEV catalog — in GPUStack (CVE-2026-123218, CVSS 9.8), OpenBSD OpenSSH, SignalWire FreeSwitch, and IBM Aspera Faspex — giving federal agencies three days to patch.

### 9. France Blames Iran for Sabotage of Retail Refrigeration Controllers
- **Source:** The Hacker News — https://thehackernews.com/2026/11/france-blames-iran-for-sabotage-attack.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ics`
- **Slug:** `iran-refrigeration-sabotage-france`
- **Must-know:** no
- **Summary:** France attributed an October 11 cyberattack that altered defrost settings on refrigeration controllers at roughly 700 retail sites to an IRGC cyber unit, causing food losses and at least 15 fires.

### 10. Fireworks AI Discloses Breach After Third-Party Cloud Provider Hack
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/fireworks-ai-discloses-new-breach-after-cloud-provider-hack/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `cloud-security`
- **Slug:** `fireworks-ai-breach-cloud-provider`
- **Must-know:** no
- **Summary:** AI infrastructure startup Fireworks AI disclosed that attackers accessed its development machines after first breaching a third-party cloud provider it relies on.

### 11. Apple Patches iMessage Group Chat and Bluetooth Pairing Flaws
- **Source:** The Hacker News — https://thehackernews.com/2026/11/apple-patches-imessage-group-chat.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`
- **Slug:** `apple-imessage-bluetooth-patches`
- **Must-know:** no
- **Summary:** Apple fixed an iMessage flaw letting a remote attacker join a group chat and receive its messages (plus a related bug exposing pre-join history), along with separate Bluetooth pairing vulnerabilities.

### 12. AI Lowers the Barrier for Reverse Engineering Software and Malware
- **Source:** Dark Reading — https://www.darkreading.com/application-security/ai-reverse-engineering-apps
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `llm`, `malware`
- **Slug:** `ai-reverse-engineering-malware-barrier`
- **Must-know:** no
- **Summary:** Researchers used AI tools to unpack, map, and recreate complex software, including the Turla malware family, far faster than manual reverse engineering, cutting both ways for defenders and attackers.

### 13. Anthropic Ships Claude Fable 5.2 and Mythos 5.2 With Security-Focused Gains
- **Source:** The Hacker News — https://thehackernews.com/2026/11/anthropics-claude-fable-52-beats-gpt-6.html
- **Source:** SecurityWeek — https://www.securityweek.com/anthropic-rolls-out-mythos-5-2-with-improved-bug-hunting-fewer-sandbox-escapes/
- **Section:** AI — News & Analysis / Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `anthropic`, `ai-safety`
- **Slug:** `anthropic-fable-mythos-5-2-security`
- **Must-know:** no
- **Summary:** Anthropic released Claude Fable 5.2 and Mythos 5.2. Fable 5.2 reportedly outperformed GPT-6 Cyber on a multi-stage cyberattack benchmark, while Mythos 5.2 shows improved vulnerability-hunting ability and fewer sandbox escapes in controlled testing.

### 14. Flashpoint Launches Agentic AI for Threat Intelligence
- **Source:** Flashpoint — https://flashpoint.io/blog/introducing-flashpoint-agentic-ai/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** informational
- **Tags:** `ai-launch`, `llm`
- **Slug:** `flashpoint-agentic-ai-threat-intel`
- **Must-know:** no
- **Summary:** Flashpoint launched purpose-built AI agents for threat intelligence, aimed at supporting investigations and automating recurring intelligence workflows using its primary-source data.

### 15. DeepMind's AlphaProof Code Verifies Signal's Core Encryption
- **Source:** Google DeepMind — https://deepmind.google/blog/introducing-alphaproof-code/
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `google`
- **Slug:** `deepmind-alphaproof-code-signal-encryption`
- **Must-know:** no
- **Summary:** Google DeepMind introduced AlphaProof Code, an AI system that writes formal Lean proofs to verify software correctness, producing roughly three million lines of proofs to verify Signal's core encryption.

## Skippable

- **Ransomware recovery is now a client retention metric** — BleepingComputer. Vendor (Kaseya) marketing content, no technical substance.
- **Today: CISO Forum Virtual Summit 2026** — SecurityWeek. Event promotion, not news.
- **WhiteMatter Raises $20 Million in Series A Funding** — SecurityWeek. Funding announcement, no technical substance.
- **SAP Patches Critical ICM2SHELL, ProxyGate Vulnerabilities** — SecurityWeek. Duplicate SAP Patch Day coverage; best source (The Hacker News) pulled instead.
- **Palantir exec nominated to lead CISA; lame-duck Senate vote is uncertain** — The Record. Personnel/political nomination, no technical substance.
- **Anthropic targets $1.4 trillion IPO** — The Verge AI. Business/financial news, not a model or security story.
- **Adobe brings AI agents and new creative tools to Photoshop, Premiere, and Firefly** — TechCrunch AI. Consumer product marketing, no security angle.
- **Anthropic sets IPO price range of $70 to $78 per share...** — TechCrunch AI. Duplicate IPO financial news.
- **We're bringing Adobe's creative and productivity tools closer to your everyday Google apps** — Google AI Blog. Partnership marketing, no security angle.
- **Spotify's AI DJ gets new voices, personalities, and an option for less chatter** — TechCrunch AI. Consumer feature, no security angle.
- **After challenging Google's Android with Cyanogen, its co-founder takes aim at Windows for AI era** — TechCrunch AI. Consumer product launch, not a major lab or security story.
- **Adobe is going all in on agentic AI** — The Verge AI. Duplicate Adobe Max marketing coverage.
- **Photoshop, Lightroom, and Premiere are making it easier to remove things** — The Verge AI. Duplicate Adobe Max marketing coverage.
- **Hands-on with Ring's new AI drone camera for your home** — The Verge AI. Consumer hardware hands-on, no security angle.
- **Russian hackers compromised government email servers to steal NATO, EU correspondence** — The Record. Duplicate of the Turla Cereal malware story; best source (The Hacker News) pulled instead.
- **Google Cloud launches Gemini for healthcare** — Google AI Blog. Enterprise feature launch, no security angle.
- **Cyberattacks threaten to make open-source AI a little less open, Hugging Face exec warns** — TechCrunch AI. General warning/opinion, no specific incident.
- **Anthropic Rolls Out Mythos 5.2 With Improved Bug Hunting, Fewer Sandbox Escapes** — SecurityWeek. Folded into the combined Fable/Mythos 5.2 post as a second source.
- **SAP patches ICM2SHELL and PROXYGATE maximum severity flaws** — BleepingComputer. Duplicate SAP Patch Day coverage.
- **Helping caregivers use AI in everyday life** — OpenAI Blog. Consumer/education content, no security angle.
- **Beyond the Alert: The Case for Rich Network Data** — The Hacker News. Vendor thought-leadership essay, no new incident or technique.
- **Turla hackers use new Cereal malware to spy on govt Exchange servers** — BleepingComputer. Duplicate of the Turla Cereal story; best source (The Hacker News) pulled instead.
- **N-able Takes N-central Offline as Researcher Drops Over 30 Zero-Days** — SecurityWeek. Duplicate; best source (The Hacker News, more detail) pulled instead.
- **IBM Aspera Faspex, SignalWire FreeSwitch Vulnerabilities Exploited in Attacks** — SecurityWeek. Duplicate of the CISA KEV story; best source (The Hacker News, broader coverage) pulled instead.
- **Closing the AI guidance gap in education** — OpenAI Blog. Education content, no security angle.
- **Google patches eighth Chrome zero-day exploited in attacks this year** — BleepingComputer. Duplicate; best source (The Hacker News, has CVE detail) pulled instead.
- **IT threat evolution in Q3 2026. Non-mobile statistics** — Securelist. Recurring quarterly stats roundup, no single standout finding.
- **IT threat evolution in Q3 2026. Mobile statistics** — Securelist. Recurring quarterly stats roundup, no single standout finding.
- **France Blames Iran for a Cyberattack That Heated Supermarket Refrigerators** — SecurityWeek. Duplicate; best source (The Hacker News, more technical detail) pulled instead.
- **Introducing Our Smallest, Most Efficient Model: Muse Ember** — Simon Willison. Pricing/positioning commentary on a Meta model, no security angle.
- **Work at the Frontier: AI's effect on freelance work** — OpenAI Blog. Labor-market research, no security angle.
- **Otter AI can now follow conversations across 30+ languages** — TechCrunch AI. Consumer feature, no security angle.
- **Chrome Update Patches Exploited XML Zero-Day, Eighth This Year** — SecurityWeek. Duplicate; best source (The Hacker News, has CVE detail) pulled instead.
- **Quoting Prompting Claude Fable 5.2** — Simon Willison. Prompting-technique commentary, no news value.
- **Yonkers Rises** — Simon Willison. Personal demo project, no news value.
- **Anthropic reportedly plans to move forward with IPO plans** — TechCrunch AI. Duplicate IPO financial news.
