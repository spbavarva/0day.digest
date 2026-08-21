# Digest — 2026-08-21 AM

- Window: last 14h
- Raw items considered: 21
- Relevant: 8
- Skippable: 13

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Microsoft Entra ID Flaw (CVSS 10.0) Exploited in the Wild — `2026-08-21-microsoft-entra-id-cvss-10-rce-exploited.md`
- [x] **[CRITICAL]** Rust Supply Chain Attack Plants Build-Time Malware in Crates with 245M Downloads — `2026-08-20-rust-crates-supply-chain-attack-arrayref.md`
- [x] **[HIGH]** CISA Urges Immediate Patching of Exploited TrueConf Vulnerabilities — `2026-08-21-trueconf-vulnerabilities-exploited-phantomcore.md`
- [x] **[HIGH]** Suspected Russian Hackers Abuse Google OAuth and WhatsApp Linking to Hijack Accounts — `2026-08-20-russian-hackers-google-oauth-whatsapp-hijack.md`
- [x] **[HIGH]** China's 'SilkParasite' Espionage Operation Targets Central Asia with AI-Assisted Malware — `2026-08-20-silkparasite-china-espionage-ai-malware.md`
- [x] **[MEDIUM]** N-able Bug Exposes Password Vault Master Keys — `2026-08-20-n-able-password-vault-master-keys.md`
- [x] **[INFORMATIONAL]** New CUSTODY Framework Aims to Constrain AI Agents Inside the Network — `2026-08-20-custody-framework-ai-agent-security.md`
- [x] **[INFORMATIONAL]** AWS Network Firewall Adds Rule Hit Count Visibility — `2026-08-20-aws-network-firewall-rule-hit-count.md`

## Relevant (details)

### 1. Microsoft Entra ID Flaw (CVSS 10.0) Exploited in the Wild
- **Source:** The Hacker News — https://thehackernews.com/2026/08/microsoft-entra-id-flaw-cvss-100.html
- **Severity:** critical
- **Tags:** `rce`, `cve`, `vulnerability`, `microsoft`, `iam`
- **Summary:** A maximum-severity (CVSS 10.0) remote code execution flaw in Microsoft Entra ID, tracked as CVE-2026-69836, is being exploited in the wild. Microsoft says no customer action is required, but exploitation details were not disclosed.

### 2. Rust Supply Chain Attack Plants Build-Time Malware in Crates with 245M Downloads
- **Source:** The Hacker News — https://thehackernews.com/2026/08/rust-supply-chain-attack-puts-build.html
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`, `rust`, `github`
- **Summary:** A compromised maintainer account published malicious versions of three widely used Rust crates (arrayref, internment, append-only-vec, ~245M combined downloads) whose build scripts executed a remote payload during compilation. The malicious versions have been removed from crates.io.

### 3. CISA Urges Immediate Patching of Exploited TrueConf Vulnerabilities
- **Source:** SecurityWeek — https://www.securityweek.com/cisa-urges-immediate-patching-of-exploited-trueconf-vulnerabilities/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `malware`
- **Summary:** CISA is urging immediate patching of TrueConf vulnerabilities being actively exploited by the Head Mare hacktivist group to deploy PhantomCore malware. No CVE IDs or technical exploitation details were provided.

### 4. Suspected Russian Hackers Abuse Google OAuth and WhatsApp Linking to Hijack Accounts
- **Source:** The Hacker News — https://thehackernews.com/2026/08/suspected-russian-hackers-abuse-google.html
- **Severity:** high
- **Tags:** `google`, `iam`, `espionage`
- **Summary:** Three suspected Russian espionage clusters (UNC6293, UNC7005, UNC5976) are abusing legitimate Google OAuth and WhatsApp device-linking flows to hijack accounts of academics, defense/aerospace workers, and government/think-tank staff across Europe and the US.

### 5. China's 'SilkParasite' Espionage Operation Targets Central Asia with AI-Assisted Malware
- **Source:** The Record (Recorded Future) — https://therecord.media/china-cyber-espionage-central-asia
- **Severity:** high
- **Tags:** `malware`, `espionage`, `llm`
- **Summary:** Suspected China-linked military hackers used AI to help develop malware in a campaign targeting Central Asian government networks. Technical details on the malware and AI tooling were not disclosed.

### 6. N-able Bug Exposes Password Vault Master Keys
- **Source:** Dark Reading — https://www.darkreading.com/vulnerabilities-threats/n-able-bug-password-vault-master-keys
- **Severity:** medium
- **Tags:** `vulnerability`, `iam`, `cloud-security`
- **Summary:** A bug in N-able's Passportal password manager exposed vault master keys; the product reportedly remains risky even post-patch due to its cloud-based design. Passportal is used widely by MSPs, so exposure could cascade to client environments.

### 7. New CUSTODY Framework Aims to Constrain AI Agents Inside the Network
- **Source:** Dark Reading — https://www.darkreading.com/perimeter/new-custody-framework-constrains-ai-agents-inside-network
- **Severity:** informational
- **Tags:** `ai-safety`, `appsec`, `devsecops`
- **Summary:** Researcher Jake Williams released CUSTODY, a new framework for constraining agentic AI systems' actions inside a network, discussed on the Dark Reading News Desk. Few technical details were given.

### 8. AWS Network Firewall Adds Rule Hit Count Visibility
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/aws-network-firewall-now-supports-rule-hit-count/
- **Severity:** informational
- **Tags:** `aws`, `cloud-security`, `devsecops`
- **Summary:** AWS Network Firewall now reports rule hit counts, letting teams see which rules are actively matching traffic versus dormant — useful for compliance policies requiring removal of unused rules.

## Skippable

- **Calling on Cyber Pros to Help Defend City Hall** — Dark Reading. Recruitment/volunteer call, no technical substance.
- **AI data startup Micro1 reaches $500M gross run rate amid AI training boom** — TechCrunch AI. Business/funding news, no security or technical AI angle.
- **ChatGPT search now uses the site:operator at scale** — Simon Willison. SEO/GEO industry commentary, not a model launch or safety item.
- **OpenAI is gaining on Anthropic with business users, new data indicates** — TechCrunch AI. Market-share commentary, no technical substance.
- **ChatGPT can now send texts for you with new Apple Messages plug-in** — TechCrunch AI. Minor consumer feature integration, no security angle.
- **Google Discover is getting an AI chatbot-tuned feed** — The Verge AI. Consumer feature launch, no security implications.
- **OK, can we actually cool data centers with our pee?** — TechCrunch AI. Off-topic, no security/AI substance.
- **Google gives publishers a new way to fight AI-driven traffic losses** — TechCrunch AI. Publisher/business tooling, no security angle.
- **Runlayer, Rippling drop lawsuits — but the brouhaha is still a cautionary tale for founders** — TechCrunch AI. Legal/business news, no security or AI substance.
- **What We Missed: Delta Flight Disrupted With Wi-Fi Hack** — Dark Reading. Video roundup segment, too thin on technical detail to draft a factual post.
- **Linkdaze's smart calendar is built to run a household, not just track a schedule** — TechCrunch AI. Consumer product launch, no security angle.
- **Is Cyber missing the Marque?** — Cisco Talos. Newsletter/opinion piece introducing a new author, thin on hard facts.
- **Hackers poison arrayref Rust crate to push infostealer malware** — BleepingComputer. Duplicate coverage of the Rust supply chain attack (see Hacker News item above).
