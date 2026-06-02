# Digest — 2026-06-02 AM

- Window: last 14h
- Raw items considered: 17
- Relevant: 8
- Skippable: 9

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Google Patches Actively Exploited Android Zero-Day in June 2026 Security Update — `2026-06-02-android-june-2026-zero-day-124-patches.md`
- [x] **[CRITICAL]** Supply Chain Attack Compromises 32 Red Hat npm Packages with Miasma Credential Stealer — `2026-06-02-redhat-npm-supply-chain-miasma-credential-stealer.md`
- [x] **[HIGH]** Meta AI Confused Deputy Flaw Lets Attackers Take Over Instagram Accounts — `2026-06-02-meta-ai-instagram-account-takeover-confused-deputy.md`
- [x] **[HIGH]** Operation FlutterBridge: macOS Malvertising Campaign Deploys Flutter-Based Backdoor — `2026-06-02-operation-flutterbridge-fluttershell-macos-backdoor.md`
- [x] **[HIGH]** DriveSurge Campaign Hijacks Thousands of Websites for ClickFix and FakeUpdate Attacks — `2026-06-02-drivesurge-clickfix-fakeupdate-site-hijacking.md`
- [x] **[MEDIUM]** Pakistan-Linked SideCopy Deploys Xeno RAT Against Afghanistan Finance Ministry — `2026-06-02-sidecopy-xeno-rat-afghanistan-finance.md`
- [x] **[MEDIUM]** Dashlane Discloses Brute-Force Attack; Fewer Than 20 Encrypted Vaults Downloaded — `2026-06-02-dashlane-brute-force-encrypted-vaults.md`
- [x] **[INFORMATIONAL]** OpenAI GPT-5.5, GPT-5.4, and Codex Now Available on Amazon Bedrock — `2026-06-02-openai-gpt55-gpt54-codex-amazon-bedrock.md`

## Relevant (details)

### 1. Google Patches Actively Exploited Android Zero-Day in June 2026 Security Update
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/google-fixes-one-actively-exploited-android-zero-day-124-flaws/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `google`, `android`
- **Slug:** `2026-06-02-android-june-2026-zero-day-124-patches`
- **Must-know:** yes
- **Summary:** Google's June 2026 Android security update patches 124 vulnerabilities, including one zero-day confirmed as actively exploited in targeted attacks. All Android device owners should apply the update immediately.

### 2. Supply Chain Attack Compromises 32 Red Hat npm Packages with Miasma Credential Stealer
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/red-hat-npm-packages-compromised-to-steal-developer-credentials/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `malware`, `appsec`
- **Slug:** `2026-06-02-redhat-npm-supply-chain-miasma-credential-stealer`
- **Must-know:** yes
- **Summary:** Attackers compromised over 30 npm packages in Red Hat's @redhat-cloud-services namespace, publishing 96 malicious versions containing "Miasma," a new variant of the Shai-Hulud credential-stealing worm. Any CI/CD pipeline that installed the affected packages during the compromise window should be treated as potentially exfiltrated.

### 3. Meta AI Confused Deputy Flaw Lets Attackers Take Over Instagram Accounts
- **Source:** SecurityWeek — https://www.securityweek.com/meta-ai-hands-over-high-profile-instagram-accounts-to-hackers/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `ai-safety`, `meta`, `phishing`
- **Slug:** `2026-06-02-meta-ai-instagram-account-takeover-confused-deputy`
- **Must-know:** no
- **Summary:** Hackers exploited a confused deputy vulnerability in Meta's AI support chatbot to take over high-profile Instagram accounts by simply asking the bot to link a target account to an attacker-controlled email. Meta wired account management capabilities into its AI support bot without sufficient identity verification, enabling social engineering at scale.

### 4. Operation FlutterBridge: macOS Malvertising Campaign Deploys Flutter-Based Backdoor
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/flutterbridge-new-fluttershell-backdoor/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `malware`, `macos`, `malvertising`
- **Slug:** `2026-06-02-operation-flutterbridge-fluttershell-macos-backdoor`
- **Must-know:** no
- **Summary:** Unit 42 documented Operation FlutterBridge, a macOS-targeted malvertising campaign delivering FlutterShell, a new backdoor built on Google's Flutter framework. Building the payload in Flutter complicates signature-based detection because the Dart runtime is bundled within the application binary.

### 5. DriveSurge Campaign Hijacks Thousands of Websites for ClickFix and FakeUpdate Attacks
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-hijack-thousands-of-sites-for-clickfix-and-fakeupdate-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `phishing`, `appsec`
- **Slug:** `2026-06-02-drivesurge-clickfix-fakeupdate-site-hijacking`
- **Must-know:** no
- **Summary:** A threat actor tracked as DriveSurge is operating large-scale malware distribution campaigns by compromising thousands of websites and deploying ClickFix and FakeUpdate lures. The operation combines social engineering (fake browser update prompts) with hijacked site infrastructure to achieve wide victim reach.

### 6. Pakistan-Linked SideCopy Deploys Xeno RAT Against Afghanistan Finance Ministry
- **Source:** The Hacker News — https://thehackernews.com/2026/06/pakistan-linked-sidecopy-targets.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `phishing`, `apt`
- **Slug:** `2026-06-02-sidecopy-xeno-rat-afghanistan-finance`
- **Must-know:** no
- **Summary:** The Pakistan-aligned SideCopy APT group targeted Afghanistan's Ministry of Finance with a spear-phishing campaign delivering the open-source Xeno RAT via a ZIP containing a malicious Pashto-language LNK file. The campaign illustrates continued geopolitical targeting of South Asian government financial institutions by state-affiliated actors.

### 7. Dashlane Discloses Brute-Force Attack; Fewer Than 20 Encrypted Vaults Downloaded
- **Source:** The Hacker News — https://thehackernews.com/2026/06/dashlane-discloses-brute-force-attack.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`, `appsec`
- **Slug:** `2026-06-02-dashlane-brute-force-encrypted-vaults`
- **Must-know:** no
- **Summary:** Dashlane disclosed that an external threat actor launched a brute-force attack on May 31, 2026 targeting 2FA on personal accounts, resulting in encrypted vault downloads for fewer than 20 users. Accounts were automatically locked; downloaded vaults remain encrypted and require the master password to decrypt.

### 8. OpenAI GPT-5.5, GPT-5.4, and Codex Now Available on Amazon Bedrock
- **Source:** AWS News Blog — https://aws.amazon.com/blogs/aws/get-started-with-openai-gpt-5-5-gpt-5-4-models-and-codex-on-amazon-bedrock/
- **Section:** Cloud Security & Infrastructure
- **Severity:** informational
- **Tags:** `ai-launch`, `openai`, `aws`, `model-release`
- **Slug:** `2026-06-02-openai-gpt55-gpt54-codex-amazon-bedrock`
- **Must-know:** no
- **Summary:** OpenAI's GPT-5.5, GPT-5.4, and Codex coding agent are now generally available on Amazon Bedrock with built-in security, governance, and pay-per-token pricing. AWS customers can now access OpenAI frontier models through Bedrock's managed inference infrastructure without a direct OpenAI API integration.

## Skippable

- **Oracle's First Monthly Patches Resolve 77 Vulnerabilities** — SecurityWeek. Routine patch release; no single CVE confirmed actively exploited and no critical technical detail provided.
- **Pasted File Editor** — Simon Willison. Personal developer tool project built with Codex; no security or AI-launch news value.
- **Codex is becoming a productivity tool for everyone** — OpenAI Blog. Marketing report on Codex productivity use cases; no new model launch or security angle.
- **Alphabet plans to raise $80B to pay for AI buildout** — TechCrunch AI. Financial/business news without technical or security substance.
- **Supply Chain Attack Hits 32 Red Hat NPM Packages** — SecurityWeek. Duplicate of the Red Hat npm supply chain story; BleepingComputer item has more technical detail (Miasma variant name, @redhat-cloud-services namespace specifics).
- **Dashlane Brute-Force Attack Leads to Limited Encrypted Vault Downloads** — SecurityWeek. Duplicate of the Dashlane brute-force incident; The Hacker News item carries more detail.
- **Nvidia chases $200B CPU market with AI agent PCs from Microsoft, Dell, and HP** — TechCrunch AI. Hardware/business announcement without a security angle.
- **Spain arrests doxer leaking sensitive data of govt employees** — BleepingComputer. Regional arrest of a single actor; limited technical substance.
- **Hackers Simply Asked Meta AI to Give Them Access to High-Profile Instagram Accounts. It Worked** — Simon Willison. Commentary and secondary verification of the Meta AI Instagram takeover; SecurityWeek is the primary source.
