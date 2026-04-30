# Digest — 2026-04-29 PM

- Window: last 14h
- Raw items considered: 43
- Relevant: 19
- Skippable: 24

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** SAP npm Packages Compromised in Credential-Stealing Supply Chain Attack — `2026-04-29-sap-npm-supply-chain-credential-theft.md`
- [x] **[CRITICAL]** CISA Adds Actively Exploited ConnectWise ScreenConnect and Windows Flaws to KEV — `2026-04-29-cisa-kev-connectwise-windows-zero-day.md`
- [x] **[CRITICAL]** cPanel and WHM Emergency Patch Fixes Critical Authentication Bypass — `2026-04-29-cpanel-whm-critical-auth-bypass.md`
- [x] **[CRITICAL]** LiteLLM CVE-2026-42208 SQL Injection Exploited Within 36 Hours of Disclosure — `2026-04-29-litellm-sqli-cve-2026-42208-exploited.md`
- [x] **[CRITICAL]** GitHub RCE Flaw CVE-2026-3854 Exposed Millions of Private Repositories — `2026-04-29-github-rce-cve-2026-3854-private-repos.md`
- [x] **[HIGH]** DPRK Threat Actors Use Claude Opus to Plant Malicious npm Packages — `2026-04-29-dprk-ai-npm-malware-fake-firms.md`
- [x] **[HIGH]** Checkmarx Confirms Data Exfiltrated from GitHub Environment in Supply Chain Attack — `2026-04-29-checkmarx-data-stolen-supply-chain.md`
- [x] **[HIGH]** Vect 2.0 Ransomware Behaves as Wiper Due to Encryption Design Flaw — `2026-04-29-vect-ransomware-wiper-teampcp.md`
- [x] **[HIGH]** Lotus Wiper Targets Venezuelan Energy Firms with Living-Off-the-Land Techniques — `2026-04-29-lotus-wiper-venezuela-energy.md`
- [x] **[HIGH]** Forescout Finds Tens of Thousands of Exposed RDP and VNC Servers Tied to ICS/OT — `2026-04-29-exposed-vnc-ics-ot-critical-infrastructure.md`
- [x] **[HIGH]** 38 Vulnerabilities in OpenEMR Allow Access to and Modification of Patient Data — `2026-04-29-openemr-38-vulnerabilities-patient-data.md`
- [x] **[HIGH]** Iranian Group Handala Targets US Military Personnel in Bahrain via WhatsApp — `2026-04-29-handala-iran-us-troops-bahrain.md`
- [x] **[HIGH]** Tumbler Ridge Shooting Victims' Families Sue OpenAI Over ChatGPT Safety Failures — `2026-04-29-openai-lawsuit-tumbler-ridge-chatgpt-shooting.md`
- [x] **[MEDIUM]** Ubuntu's Bundled AI Features Prompt Users to Demand an Opt-Out Kill Switch — `2026-04-29-ubuntu-ai-features-user-backlash.md`
- [x] **[MEDIUM]** AI-Generated Celebrity Deepfakes Drive Scam Campaigns on TikTok — `2026-04-29-deepfake-celebrity-scams-tiktok.md`
- [x] **[INFORMATIONAL]** Cisco Talos Demonstrates Generative AI Honeypots to Counter Malicious AI Agents — `2026-04-29-ai-honeypots-malicious-agents-talos.md`
- [x] **[INFORMATIONAL]** CISA and Partners Release Zero Trust Guidance for Operational Technology Environments — `2026-04-29-cisa-zero-trust-ot-guidance.md`
- [x] **[INFORMATIONAL]** IBM Releases Granite 4.1 LLM Family on Hugging Face — `2026-04-29-ibm-granite-4-1-llm-release.md`
- [x] **[INFORMATIONAL]** Trail of Bits Extends Ruzzy Ruby Fuzzer with LibAFL Engine — `2026-04-29-ruzzy-libafl-ruby-fuzzing.md`

## Relevant (details)

### 1. SAP npm Packages Compromised in Credential-Stealing Supply Chain Attack
- **Source:** The Hacker News — https://thehackernews.com/2026/04/sap-npm-packages-compromised-by-mini.html
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `malware`
- **Summary:** A coordinated campaign dubbed "mini Shai-Hulud," confirmed by five independent security firms, compromised multiple SAP-related npm packages with credential-stealing malware targeting SAP JavaScript ecosystem developers. Organizations should audit npm dependency trees and rotate exposed credentials immediately.

### 2. CISA Adds Actively Exploited ConnectWise ScreenConnect and Windows Flaws to KEV
- **Source:** The Hacker News — https://thehackernews.com/2026/04/cisa-adds-actively-exploited.html
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `cve`, `microsoft`
- **Summary:** CISA added CVE-2024-1708 (ConnectWise ScreenConnect path traversal) and an actively exploited Windows zero-day to the KEV catalog. Both are confirmed under active exploitation; federal agencies must remediate on mandatory timelines.

### 3. cPanel and WHM Emergency Patch Fixes Critical Authentication Bypass
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cpanel-whm-emergency-update-fixes-critical-auth-bypass-bug/
- **Severity:** critical
- **Tags:** `vulnerability`, `privilege-escalation`, `appsec`, `cve`
- **Summary:** An unauthenticated auth bypass in all supported cPanel/WHM versions allows control panel access without credentials. Emergency update released; hosting providers should patch immediately to fixed versions 11.110.0.97, 11.118.0.63, 11.126.0.54, or 11.132.0.29.

### 4. LiteLLM CVE-2026-42208 SQL Injection Exploited Within 36 Hours of Disclosure
- **Source:** The Hacker News — https://thehackernews.com/2026/04/litellm-cve-2026-42208-sql-injection.html
- **Severity:** critical
- **Tags:** `sqli`, `llm`, `vulnerability`, `cve`
- **Summary:** CVE-2026-42208 (CVSS 9.3) in LiteLLM is a SQL injection that exposes and allows modification of the proxy database, including API keys and model configs. Exploitation began 36 hours after disclosure; organizations must patch and rotate secrets immediately.

### 5. GitHub RCE Flaw CVE-2026-3854 Exposed Millions of Private Repositories
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/github-fixes-rce-flaw-that-gave-access-to-millions-of-private-repos/
- **Severity:** critical
- **Tags:** `rce`, `vulnerability`, `cve`, `github`
- **Summary:** Wiz Research discovered CVE-2026-3854, an RCE in GitHub's git infrastructure affecting GitHub.com and GitHub Enterprise Server. GitHub patched it in under six hours in early March with no known exploitation. Enterprise Server operators should verify patched versions.

### 6. DPRK Threat Actors Use Claude Opus to Plant Malicious npm Packages
- **Source:** The Hacker News — https://thehackernews.com/2026/04/new-wave-of-dprk-attacks-uses-ai.html
- **Severity:** high
- **Tags:** `supply-chain`, `npm`, `malware`, `anthropic`, `llm`
- **Summary:** DPRK actors planted malicious npm package "@validate-sdk/v2" as a project dependency; Claude Opus incidentally detected it during a developer's AI-assisted code review. The campaign combines fake companies, RATs, and AI-generated malicious packages consistent with Lazarus Group supply chain TTPs.

### 7. Checkmarx Confirms Data Exfiltrated from GitHub Environment in Supply Chain Attack
- **Source:** SecurityWeek — https://www.securityweek.com/checkmarx-confirms-data-stolen-in-supply-chain-attack/
- **Severity:** high
- **Tags:** `supply-chain`, `data-breach`, `github`
- **Summary:** Checkmarx confirmed data was exfiltrated from its GitHub environment on March 30, one week after malicious code was published. The breach is notable because Checkmarx is a code security platform; organizations using its GitHub integrations should audit permissions and monitor for anomalous access.

### 8. Vect 2.0 Ransomware Behaves as Wiper Due to Encryption Design Flaw
- **Source:** Dark Reading — https://www.darkreading.com/threat-intelligence/vect-ransomware-wiper-design-error
- **Severity:** high
- **Tags:** `ransomware`, `malware`, `supply-chain`
- **Summary:** Vect 2.0, deployed against TeamPCP supply chain attack victims, permanently destroys data due to a broken encryption implementation — no decryptor exists. Victims should not pay ransom; recovery requires intact backups.

### 9. Lotus Wiper Targets Venezuelan Energy Firms with Living-Off-the-Land Techniques
- **Source:** Dark Reading — https://www.darkreading.com/cyber-risk/lotus-wiper-attack-targeted-venezuelan-energy-firms-utilities
- **Severity:** high
- **Tags:** `malware`, `ics`
- **Summary:** Lotus Wiper hit Venezuelan energy firms using sophisticated LotL techniques for widespread data deletion, leveraging native OS tools to evade detection. Energy sector operators should assess behavioral detection capabilities and maintain tested offline backup strategies.

### 10. Forescout Finds Tens of Thousands of Exposed RDP and VNC Servers Tied to ICS/OT
- **Source:** SecurityWeek — https://www.securityweek.com/hundreds-of-internet-facing-vnc-servers-expose-ics-ot/
- **Severity:** high
- **Tags:** `vulnerability`, `ics`, `appsec`
- **Summary:** Forescout mapped tens of thousands of internet-exposed RDP/VNC servers to specific industries, with hundreds tied directly to ICS/OT environments. Internet-accessible remote desktop on OT networks enables direct ICS access on compromise; organizations should audit and segment immediately.

### 11. 38 Vulnerabilities in OpenEMR Allow Access to and Modification of Patient Data
- **Source:** SecurityWeek — https://www.securityweek.com/38-vulnerabilities-found-in-openemr-medical-software/
- **Severity:** high
- **Tags:** `vulnerability`, `data-breach`, `appsec`, `cve`
- **Summary:** Researchers found 38 vulnerabilities in open-source OpenEMR, some exploitable to access and modify sensitive patient data. Healthcare organizations should patch immediately and restrict network access; OpenEMR's small-provider deployment base has historically slow patching cycles.

### 12. Iranian Group Handala Targets US Military Personnel in Bahrain via WhatsApp
- **Source:** SecurityWeek — https://www.securityweek.com/iranian-cyber-group-handala-targets-us-troops-in-bahrain/
- **Severity:** high
- **Tags:** `phishing`, `malware`
- **Summary:** Handala sent WhatsApp messages to US troops in Bahrain threatening drone/missile strikes in a psychological operations campaign. Handala has previously deployed destructive wipers and social engineering often precedes technical intrusions from this group.

### 13. Tumbler Ridge Shooting Victims' Families Sue OpenAI Over ChatGPT Safety Failures
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/920479/tumbler-ridge-chagpt-openai-lawsuit
- **Severity:** high
- **Tags:** `openai`, `ai-safety`, `llm`
- **Summary:** Seven families of Tumbler Ridge shooting victims sued OpenAI for failing to alert authorities after ChatGPT flagged threatening activity from the suspect. The litigation is a landmark test of AI provider duty-of-care and may influence mandatory reporting obligations for AI platforms.

### 14. Ubuntu's Bundled AI Features Prompt Users to Demand an Opt-Out Kill Switch
- **Source:** The Verge AI — https://www.theverge.com/tech/920723/linux-ubuntu-ai-features-ai-kill-switch
- **Severity:** medium
- **Tags:** `ai-safety`, `llm`
- **Summary:** Canonical's embedded AI features for Ubuntu generated backlash over privacy and telemetry concerns, with users demanding an AI-free variant. Signals growing resistance to AI in foundational infrastructure software without explicit opt-in controls.

### 15. AI-Generated Celebrity Deepfakes Drive Scam Campaigns on TikTok
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/920351/ai-celebrity-deepfake-ads-tiktok-copyleaks
- **Severity:** medium
- **Tags:** `ai-safety`, `phishing`, `llm`
- **Summary:** Copyleaks documented scammers using AI deepfake videos of Taylor Swift and Rihanna on TikTok to promote fraudulent reward programs. Video quality is increasing to the point where user-level detection is unreliable; platform-scale detection is the primary countermeasure.

### 16. Cisco Talos Demonstrates Generative AI Honeypots to Counter Malicious AI Agents
- **Source:** Cisco Talos — https://blog.talosintelligence.com/ai-powered-honeypots-turning-the-tables-on-malicious-ai-agents/
- **Severity:** informational
- **Tags:** `ai-safety`, `llm`, `malware`, `appsec`
- **Summary:** Talos published a practical blueprint for using generative AI to deploy adaptive honeypots that detect and study AI-powered attack agents. Actionable defensive technique for threat intelligence teams wanting to apply AI offensively in defensive operations.

### 17. CISA and Partners Release Zero Trust Guidance for Operational Technology Environments
- **Source:** CISA Alerts — https://www.cisa.gov/resources-tools/resources/adapting-zero-trust-principles-operational-technology
- **Severity:** informational
- **Tags:** `iam`, `devsecops`, `ics`
- **Summary:** Joint guidance from CISA, DoD, DOE, FBI, and State on applying zero trust to OT environments, covering identity-based access controls adapted for industrial device constraints and legacy protocols. Relevant for any ICS or critical infrastructure operator.

### 18. IBM Releases Granite 4.1 LLM Family on Hugging Face
- **Source:** Hugging Face Blog — https://huggingface.co/blog/ibm-granite/granite-4-1
- **Severity:** informational
- **Tags:** `llm`, `model-release`
- **Summary:** IBM published Granite 4.1 on Hugging Face, expanding the enterprise open-weight LLM space. Model cards and benchmarks available for practitioners evaluating deployment in regulated industries.

### 19. Trail of Bits Extends Ruzzy Ruby Fuzzer with LibAFL Engine
- **Source:** Trail of Bits — https://blog.trailofbits.com/2026/04/29/extending-ruzzy-with-libafl/
- **Severity:** informational
- **Tags:** `appsec`, `devsecops`
- **Summary:** Trail of Bits integrated LibAFL (Rust-based, actively maintained) into Ruzzy, their Ruby coverage-guided fuzzer, replacing LLVM's libFuzzer which entered maintenance mode. Ruby developers gain state-of-the-art fuzzing without rewriting existing harness code.

## Skippable

- **All the evidence unveiled so far in Musk v. Altman** — The Verge AI. Legal/media trial coverage; no security or AI safety angle.
- **AI evals are becoming the new compute bottleneck** — Hugging Face Blog. ML engineering economics piece; no security relevance.
- **Google Photos uses AI to make the iconic closet from 'Clueless' a reality** — TechCrunch AI. Consumer feature announcement; no security or AI safety angle.
- **More Gemini features are coming to Google TV** — TechCrunch AI. Consumer feature rollout; no security angle.
- **Google Photos launches an AI try-on feature for clothes you already have** — The Verge AI. Consumer feature; no security angle.
- **European Commission accuses Meta of breaching child safety rules** — The Record. Regulatory/DSA enforcement action; no technical security substance.
- **ChatGPT downloads are slowing — and may cause problems for OpenAI's IPO** — The Verge AI. Market analysis piece; not security or AI safety.
- **European police dismantles €50 million crypto investment fraud ring** — BleepingComputer. Financial crime enforcement; no technical TTPs or IOCs.
- **Swiss police arrest 10 suspected members of Nigeria-linked crime group Black Axe** — The Record. Law enforcement action; no technical security content.
- **Larry's risky business** — The Verge AI. Opinion piece on Oracle's AI datacenter pivot; no security angle.
- **Firestorm Labs raises $82M to take drone factories into the field** — TechCrunch AI. Defense startup funding; no security research content.
- **Learning from the Vercel breach: Shadow AI & OAuth sprawl** — BleepingComputer. Vendor-sponsored analysis (Push) of a breach already covered in prior digests; duplicate coverage + marketing.
- **Fresh LiteLLM Vulnerability Exploited Shortly After Disclosure** — SecurityWeek. Duplicate of Item 43; The Hacker News has more detail including CVE and CVSS score.
- **Meet Shapes, the app bringing humans and AI into the same group chats** — TechCrunch AI. Consumer app launch; no security angle.
- **Webinar: How to Automate Exposure Validation to Match the Speed of AI Attacks** — The Hacker News. Vendor webinar marketing content.
- **What to Look for in an Exposure Management Platform** — The Hacker News. Vendor marketing disguised as guidance.
- **China freezes new robotaxi licenses after Baidu chaos** — The Verge AI. Regulatory/autonomous vehicle policy news; no security angle.
- **CISA orders feds to patch Windows flaw exploited as zero-day** — BleepingComputer. Duplicate of CISA KEV item; THN covers both CVEs more completely.
- **GitHub rushed to fix a critical vulnerability in less than six hours** — The Verge AI. Duplicate of GitHub RCE CVE-2026-3854; BleepingComputer has the CVE detail.
- **Colby Adcock's Scout AI raises $100M to train its models for war** — TechCrunch AI. Defense startup funding; no security research content.
- **Critical cPanel Authentication Vulnerability Identified** — The Hacker News. Duplicate of BleepingComputer cPanel item; same vulnerability and fix versions.
- **Chrome 147, Firefox 150 Security Updates Rolling Out** — SecurityWeek. Routine browser patch release; no CVE confirmed as actively exploited.
- **Microsoft says backend change broke Teams Free chat and calls** — BleepingComputer. Service disruption/outage; not a security incident.
- **Critical GitHub Vulnerability Exposed Millions of Repositories** — SecurityWeek. Duplicate of GitHub RCE CVE-2026-3854; BleepingComputer is the primary source used.
