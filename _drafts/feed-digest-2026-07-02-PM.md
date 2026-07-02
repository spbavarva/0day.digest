# Digest — 2026-07-02 PM

- Window: last 14h
- Raw items considered: 38
- Relevant: 16
- Skippable: 22

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** FortiBleed Credential Theft Tied to INC and Lynx Ransomware Operations — `2026-07-02-fortibleed-credential-theft-inc-lynx-ransomware.md`
- [x] **[CRITICAL]** AI Agent Runs Ransomware Attack Start to Finish via Langflow RCE — `2026-07-02-ai-agent-langflow-rce-ransomware-jadepuffer.md`
- [x] **[HIGH]** New CitrixBleed Vulnerability Exploited Immediately After Disclosure — `2026-07-02-new-citrixbleed-vulnerability-exploited.md`
- [x] **[HIGH]** ConsentFix and ClickFix Attacks Hijack Microsoft 365 Accounts in Seconds — `2026-07-02-consentfix-clickfix-microsoft-365-hijack.md`
- [x] **[HIGH]** ToddyCat-Linked Umbrij Malware Abuses OAuth to Access Gmail — `2026-07-02-toddycat-umbrij-malware-gmail-oauth.md`
- [x] **[HIGH]** Cisco Confirms Attackers Are Exploiting Unified CM Flaw — `2026-07-02-cisco-unified-cm-flaw-exploited.md`
- [x] **[HIGH]** SharePoint RCE CVE-2026-45659 Added to CISA KEV After Active Exploitation — `2026-07-02-sharepoint-rce-cve-2026-45659-kev.md`
- [x] **[HIGH]** 'BioShocking' Attack Tricks AI Browsers Into Stealing Credentials — `2026-07-02-bioshocking-attack-ai-browsers-credentials.md`
- [x] **[HIGH]** New ChocoPoC RAT Targets Vulnerability Researchers via Fake PoC Repos — `2026-07-02-chocopoc-rat-vulnerability-researchers-github.md`
- [x] **[MEDIUM]** Remus Stealer: A New, Not-So-New Infostealer — `2026-07-02-remus-stealer-infostealer-lumma.md`
- [x] **[MEDIUM]** Supreme Court Decision Threatens EU-US Data Transfer Agreement — `2026-07-02-supreme-court-threatens-eu-us-data-transfer.md`
- [x] **[MEDIUM]** Anthropic's AI Finds Bugs. IBM Bets $5B It Can Fix Them. — `2026-07-02-anthropic-ai-bug-finding-ibm-5-billion.md`
- [x] **[MEDIUM]** Medtronic Notifies Customers Impacted by ShinyHunters Data Breach — `2026-07-02-medtronic-shinyhunters-data-breach.md`
- [x] **[INFORMATIONAL]** Trump Administration Lifts Restrictions on Anthropic's Claude Models — `2026-07-02-trump-admin-lifts-restrictions-anthropic-claude.md`
- [x] **[INFORMATIONAL]** GPT-5.5-Cyber Built a zlib Fuzzing Lab in a Day — `2026-07-02-gpt-5-5-cyber-zlib-fuzzing-trail-of-bits.md`
- [x] **[INFORMATIONAL]** Opera Rolls Out Paste Protect Feature to Fight ClickFix Attacks — `2026-07-02-opera-paste-protect-clickfix.md`

## Relevant (details)

### 1. FortiBleed Credential Theft Tied to INC and Lynx Ransomware Operations
- **Source:** The Hacker News — https://thehackernews.com/2026/07/fortibleed-credential-theft-linked-to.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `fortinet`, `ransomware`, `vulnerability`
- **Slug:** `fortibleed-credential-theft-inc-lynx-ransomware`
- **Must-know:** yes
- **Summary:** Credentials harvested from hundreds of thousands of FortiGate firewalls in the FortiBleed campaign are tied to the INC and Lynx ransomware operations. An operator connected to FortiBleed's infrastructure was found working negotiation panels for both groups.

### 2. AI Agent Runs Ransomware Attack Start to Finish via Langflow RCE
- **Source:** The Hacker News — https://thehackernews.com/2026/07/ai-agent-exploits-langflow-rce-to.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `llm`, `rce`, `ransomware`, `ai-safety`
- **Slug:** `ai-agent-langflow-rce-ransomware-jadepuffer`
- **Must-know:** no
- **Summary:** Sysdig identified what it calls the first ransomware attack run end-to-end by an autonomous AI agent (JADEPUFFER), which exploited a Langflow RCE flaw and then independently handled credential theft, lateral movement, and database encryption/wiping.

### 3. New CitrixBleed Vulnerability Exploited Immediately After Disclosure
- **Source:** SecurityWeek — https://www.securityweek.com/new-citrixbleed-vulnerability-exploited-immediately-after-public-disclosure/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Slug:** `new-citrixbleed-vulnerability-exploited`
- **Must-know:** no
- **Summary:** A new CitrixBleed-style flaw in NetScaler appliances is already being exploited with public PoC code to retrieve arbitrary memory content from HTTP responses, echoing the original CitrixBleed's damaging exploitation pattern.

### 4. ConsentFix and ClickFix Attacks Hijack Microsoft 365 Accounts in Seconds
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/consentfix-and-clickfix-how-microsoft-365-accounts-are-hijacked-in-3-seconds/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `phishing`, `iam`
- **Slug:** `consentfix-clickfix-microsoft-365-hijack`
- **Must-know:** no
- **Summary:** Two attack techniques, ConsentFix and ClickFix, steal Microsoft 365 tokens within seconds using fake prompts and abused OAuth consent flows, functioning as MFA bypass methods.

### 5. ToddyCat-Linked Umbrij Malware Abuses OAuth to Access Gmail
- **Source:** The Hacker News — https://thehackernews.com/2026/07/toddycat-linked-umbrij-malware-abuses.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `google`, `iam`
- **Slug:** `toddycat-umbrij-malware-gmail-oauth`
- **Must-know:** no
- **Summary:** Kaspersky attributes new malware Umbrij to ToddyCat, designed to covertly access victims' Gmail accounts via the Google API, targeting corporate email communications.

### 6. Cisco Confirms Attackers Are Exploiting Unified CM Flaw
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisco-finally-confirms-attackers-exploiting-unified-cm-flaw/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `vulnerability`
- **Slug:** `cisco-unified-cm-flaw-exploited`
- **Must-know:** no
- **Summary:** Cisco confirmed active exploitation of a Unified Communications Manager flaw patched in early June; a PoC exploit has been public since disclosure and attacks began last week.

### 7. SharePoint RCE CVE-2026-45659 Added to CISA KEV After Active Exploitation
- **Source:** The Hacker News — https://thehackernews.com/2026/07/sharepoint-rce-cve-2026-45659-added-to.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `rce`, `vulnerability`, `microsoft`
- **Slug:** `sharepoint-rce-cve-2026-45659-kev`
- **Must-know:** no
- **Summary:** CISA added CVE-2026-45659 (CVSS 8.8), a SharePoint Server RCE via unsafe deserialization patched in May, to its KEV catalog after confirming active exploitation of unpatched instances.

### 8. 'BioShocking' Attack Tricks AI Browsers Into Stealing Credentials
- **Source:** SecurityWeek — https://www.securityweek.com/bioshocking-attack-tricks-ai-browsers-into-stealing-credentials/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `ai-safety`
- **Slug:** `bioshocking-attack-ai-browsers-credentials`
- **Must-know:** no
- **Summary:** Researchers show context manipulation can cause agentic AI browsers to abandon safety guardrails and exfiltrate sensitive credentials, adding to prompt-injection-style research on agentic browser risk.

### 9. New ChocoPoC RAT Targets Vulnerability Researchers via Fake PoC Repos
- **Source:** The Hacker News — https://thehackernews.com/2026/07/new-chocopoc-rat-targets-vulnerability.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `github`, `supply-chain`
- **Slug:** `chocopoc-rat-vulnerability-researchers-github`
- **Must-know:** no
- **Summary:** A trojan called ChocoPoC hides inside fake Python PoC exploit repos on GitHub targeting bug hunters, stealing saved passwords, cookies, and files, and handing attackers a shell.

### 10. Remus Stealer: A New, Not-So-New Infostealer
- **Source:** Flashpoint — https://flashpoint.io/blog/remus-stealer-a-new-not-so-new-infostealer/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `remus-stealer-infostealer-lumma`
- **Must-know:** no
- **Summary:** Flashpoint documented Remus Stealer, a new infostealer with significant structural and behavioral overlap with the Lumma malware family, likely a rebrand or close derivative.

### 11. Supreme Court Decision Threatens EU-US Data Transfer Agreement
- **Source:** The Record (Recorded Future) — https://therecord.media/supreme-court-decision-threatens-eu-us-data-sharing
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-privacy`
- **Slug:** `supreme-court-threatens-eu-us-data-transfer`
- **Must-know:** no
- **Summary:** Privacy advocate Max Schrems plans to sue to invalidate the EU-U.S. Data Privacy Framework following a Supreme Court decision, potentially the third such framework struck down.

### 12. Anthropic's AI Finds Bugs. IBM Bets $5B It Can Fix Them.
- **Source:** Dark Reading — https://www.darkreading.com/vulnerabilities-threats/anthropic-s-ai-finds-bugs-ibm-bets-5b-it-can-fix-them-
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `anthropic`, `supply-chain`, `appsec`
- **Slug:** `anthropic-ai-bug-finding-ibm-5-billion`
- **Must-know:** no
- **Summary:** IBM and Red Hat committed $5B and 20,000 engineers to Project Lightwell, built around fixing bugs found by Anthropic's Mythos project, reigniting debate over securing the open-source supply chain.

### 13. Medtronic Notifies Customers Impacted by ShinyHunters Data Breach
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/medtronic-notifies-customers-impacted-by-shinyhunters-data-breach/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`
- **Slug:** `medtronic-shinyhunters-data-breach`
- **Must-know:** no
- **Summary:** Medtronic is notifying customers of a data breach attributed to ShinyHunters that exposed personal data to an unauthorized third party; scope of affected individuals wasn't disclosed.

### 14. Trump Administration Lifts Restrictions on Anthropic's Claude Models
- **Source:** SecurityWeek — https://www.securityweek.com/trump-administration-lifts-restrictions-on-anthropics-claude-models-after-cybersecurity-alarm/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `anthropic`, `ai-launch`, `model-release`
- **Slug:** `trump-admin-lifts-restrictions-anthropic-claude`
- **Must-know:** no
- **Summary:** The Trump administration lifted prior restrictions on Anthropic's Claude models after a cybersecurity alarm; Anthropic separately confirmed Claude Fable 5 is now widely available.

### 15. GPT-5.5-Cyber Built a zlib Fuzzing Lab in a Day
- **Source:** Trail of Bits — https://blog.trailofbits.com/2026/07/02/field-reports-from-patch-the-planet/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** informational
- **Tags:** `llm`, `appsec`, `openai`
- **Slug:** `gpt-5-5-cyber-zlib-fuzzing-trail-of-bits`
- **Must-know:** no
- **Summary:** Trail of Bits' "Patch the Planet" collaboration with OpenAI reports GPT-5.5-Cyber built a working zlib fuzzing lab in a day, part of an effort to find OSS bugs before AI models flood maintainers with reports.

### 16. Opera Rolls Out Paste Protect Feature to Fight ClickFix Attacks
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/opera-rolls-out-paste-protect-feature-to-fight-clickfix-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `phishing`, `appsec`
- **Slug:** `opera-paste-protect-clickfix`
- **Must-know:** no
- **Summary:** Opera introduced a Paste Protect browser feature to block ClickFix-style attacks that trick users into pasting and executing malicious commands via social engineering.

## Skippable

- **Ransomware Thugs Masquerade as Interpol to Entice Small Biz** — Dark Reading. Generic social engineering ransomware campaign, no novel technique or IOCs.
- **Catan and Mouse** — Cisco Talos. Opinion piece on threat-hunting mindset using a board-game analogy, no technical content.
- **Understand to participate** — Simon Willison. Opinion essay on collaborating with coding agents, no news value.
- **ThreatsDay: AI Compute Hijacking, Apple Email Flaw, BlueHammer Ransomware + 14 Stories** — The Hacker News. Weekly link roundup, no single technical story to draft.
- **OpenAI proposed donating 5% of its equity to a US sovereign wealth fund** — TechCrunch. Business/political maneuvering with no security angle; duplicate of The Verge's coverage.
- **Google loses final appeal to overturn €4.1 billion EU fine** — BleepingComputer. Antitrust/legal news, no security or AI angle.
- **Microsoft launches its own AI deployment company with $2.5 billion commitment** — TechCrunch. Corporate business news, no security substance.
- **How to Conduct a Successful Audit of AI-Driven Software Development** — SecurityWeek. Generic guidance/opinion piece, not news.
- **FortiBleed Campaign Linked to INC, Lynx Ransomware Attacks** — SecurityWeek. Duplicate coverage of the same story (Hacker News version has more detail, drafted instead).
- **Microsoft fixes bug that removed Copilot buttons in Outlook** — BleepingComputer. Minor UI bug fix, no security relevance.
- **Yep, we're using OpenClaw to date now** — TechCrunch. Lifestyle content, no security or AI substance.
- **CubeSpace CW0057 Reaction Wheel** — CISA Alerts. Routine ICS advisory for a niche satellite component, no widespread impact.
- **Gardyn IoT Hub** — CISA Alerts. Routine ICS/IoT advisory for a niche consumer smart-garden device.
- **ST Engineering iDirect iQ-Series Terminals** — CISA Alerts. Routine ICS advisory for niche satellite terminals.
- **Identity Lifecycle Management Wasn't Built for AI Agents** — The Hacker News. Vendor guide/marketing content, no specific incident.
- **CISA: Microsoft SharePoint RCE flaw now actively exploited** — BleepingComputer. Duplicate coverage of CVE-2026-45659 (Hacker News KEV version drafted instead).
- **Cisco Confirms In-the-Wild Exploitation of Unified CM Vulnerability** — SecurityWeek. Duplicate coverage of the same story (BleepingComputer version drafted instead).
- **CISA Warns of Actively Exploited Microsoft SharePoint Vulnerability** — SecurityWeek. Duplicate coverage of CVE-2026-45659.
- **OpenAI floats giving Trump administration 5 percent cut of AI boom** — The Verge. Business/political maneuvering with no security angle; duplicate of TechCrunch's coverage.
- **Missed incidents, persistent threats, and response gaps** — Securelist. Generic annual compromise-assessment trends/tips report, no specific new technique.
- **Alleged Scattered Spider hacker extradited to the United States** — BleepingComputer. Law-enforcement news with no new IOCs or technical detail.
- **Indian tech tycoon bets $30M of his own money to build AI alternative to Microsoft Office** — TechCrunch. Non-security startup launch, no security angle.
