# Digest — 2026-06-12 PM

- Window: last 14h
- Raw items considered: 38
- Relevant: 11
- Skippable: 25

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** 400+ Arch Linux AUR Packages Compromised With Rootkit and Infostealer — `2026-06-12-arch-linux-aur-packages-rootkit-infostealer.md`
- [x] **[CRITICAL]** Critical LangGraph Vulnerability Chain Enables Remote Code Execution in Self-Hosted AI Agents — `2026-06-12-langgraph-vulnerability-chain-rce.md`
- [x] **[CRITICAL]** CISA Orders Federal Agencies to Patch Actively Exploited Ivanti Sentry RCE Within 3 Days — `2026-06-12-ivanti-sentry-rce-cisa-bod-26-04.md`
- [x] **[CRITICAL]** Oracle PeopleSoft Zero-Day (CVE-2026-35273) Exploited by ShinyHunters, Added to CISA KEV — `2026-06-12-oracle-peoplesoft-zero-day-cve-2026-35273-shinyhunters.md`
- [x] **[HIGH]** phpBB Patches Decade-Old Authentication Bypass Allowing Admin Takeover — `2026-06-12-phpbb-auth-bypass-decade-old-flaw.md`
- [x] **[HIGH]** 'Agentjacking' Attack Tricks AI Coding Agents Into Running Malicious Code via Fake Sentry Error Reports — `2026-06-12-agentjacking-ai-coding-agents-sentry.md`
- [x] **[HIGH]** Trail of Bits Finds 'Short-Sleeve' RSA Keys Factorable via Polynomial Attack — `2026-06-12-short-sleeve-rsa-keys-polynomial-factoring.md`
- [x] **[MEDIUM]** Google Sues Chinese 'Outsider Enterprise' Group Over AI-Generated Scam Text Campaign — `2026-06-12-google-sues-outsider-enterprise-ai-scam-texts.md`
- [x] **[MEDIUM]** Anthropic Disputes Claimed Prompt-Based Jailbreak of Claude Fable 5 — `2026-06-12-anthropic-disputes-fable-5-jailbreak-claim.md`
- [x] **[INFORMATIONAL]** INTERPOL-Led Operation Dismantles Decade-Old Sniper Dz Phishing-as-a-Service Platform — `2026-06-12-interpol-sniper-dz-phishing-takedown.md`
- [x] **[INFORMATIONAL]** Europol Disrupts AudiA6 Crypto-Laundering Service Tied to Ransomware Gangs — `2026-06-12-europol-audia6-crypto-laundering-takedown.md`

## Relevant (details)

### 1. 400+ Arch Linux AUR Packages Compromised With Rootkit and Infostealer
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/over-400-arch-linux-packages-compromised-to-push-rootkit-infostealer/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`, `privilege-escalation`
- **Slug:** `arch-linux-aur-packages-rootkit-infostealer`
- **Must-know:** yes
- **Summary:** More than 400 packages in the Arch User Repository (AUR) were found distributing a Linux rootkit and infostealer that targets credentials and access tokens. A large-scale supply-chain compromise of a widely-used community package repository.

### 2. Critical LangGraph Vulnerability Chain Enables Remote Code Execution in Self-Hosted AI Agents
- **Source:** The Hacker News — https://thehackernews.com/2026/06/langgraph-flaw-chain-exposes-self.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `llm`, `rce`, `sqli`, `vulnerability`
- **Slug:** `langgraph-vulnerability-chain-rce`
- **Must-know:** no
- **Summary:** Researchers disclosed three now-patched LangGraph flaws, including a SQL injection, that chain into a critical remote code execution vulnerability for self-hosted multi-agent AI deployments. All three issues are already patched upstream.

### 3. CISA Orders Federal Agencies to Patch Actively Exploited Ivanti Sentry RCE Within 3 Days
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-gives-feds-3-days-to-patch-ivanti-flaw-exploited-in-attacks/
- **Source:** SecurityWeek — https://www.securityweek.com/ivanti-sentry-exploitation-attempts-hitting-honeypots/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `rce`, `vulnerability`, `privilege-escalation`
- **Slug:** `ivanti-sentry-rce-cisa-bod-26-04`
- **Must-know:** yes
- **Summary:** CISA's newly issued BOD 26-04 orders federal agencies to patch an actively exploited critical OS command injection vulnerability in Ivanti Sentry within three days; the flaw grants root-level remote code execution and SecurityWeek reports exploitation attempts already hitting honeypots.

### 4. Oracle PeopleSoft Zero-Day (CVE-2026-35273) Exploited by ShinyHunters, Added to CISA KEV
- **Source:** SecurityWeek — https://www.securityweek.com/google-confirms-exploitation-of-oracle-peoplesoft-zero-day-by-shinyhunters/
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/alerts/2026/06/12/cisa-adds-one-known-exploited-vulnerability-catalog
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `cve`, `vulnerability`, `privilege-escalation`
- **Slug:** `oracle-peoplesoft-zero-day-cve-2026-35273-shinyhunters`
- **Must-know:** yes
- **Summary:** CVE-2026-35273, a missing-authentication-for-critical-function flaw in Oracle PeopleSoft Enterprise PeopleTools, is being actively exploited by ShinyHunters according to Google, and CISA has added it to the Known Exploited Vulnerabilities catalog under BOD 26-04. Oracle has shipped a mitigation but has not publicly confirmed in-the-wild exploitation.

### 5. phpBB Patches Decade-Old Authentication Bypass Allowing Admin Takeover
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/phpbb-forum-fixes-auth-bypass-bug-lurking-for-a-decade/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `privilege-escalation`, `appsec`
- **Slug:** `phpbb-auth-bypass-decade-old-flaw`
- **Must-know:** no
- **Summary:** A 10-year-old authentication bypass vulnerability in phpBB forum software allowed an attacker to log in as any user, including administrators, without valid credentials. The issue has now been patched.

### 6. 'Agentjacking' Attack Tricks AI Coding Agents Into Running Malicious Code via Fake Sentry Error Reports
- **Source:** The Hacker News — https://thehackernews.com/2026/06/agentjacking-attack-tricks-ai-coding.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `rce`, `vulnerability`, `appsec`
- **Slug:** `agentjacking-ai-coding-agents-sentry`
- **Must-know:** no
- **Summary:** Tenet Security disclosed "Agentjacking," a new attack class that tricks AI coding agents into executing arbitrary code on developer machines via a fake error report crafted using Sentry, the open-source error-tracking platform.

### 7. Trail of Bits Finds 'Short-Sleeve' RSA Keys Factorable via Polynomial Attack
- **Source:** Trail of Bits — https://blog.trailofbits.com/2026/06/12/factoring-short-sleeve-rsa-keys-with-polynomials/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `vulnerability`, `appsec`
- **Slug:** `short-sleeve-rsa-keys-polynomial-factoring`
- **Must-know:** no
- **Summary:** Trail of Bits, working with Hanno Böck of the badkeys project, found hundreds of RSA keys in the wild with structurally biased private-key bits and developed a polynomial-based technique to factor them, also tracing the root-cause bug.

### 8. Google Sues Chinese 'Outsider Enterprise' Group Over AI-Generated Scam Text Campaign
- **Source:** TechCrunch AI — https://techcrunch.com/2026/06/12/google-sues-alleged-chinese-cybercrime-operation-that-used-ai-to-send-scam-texts/
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `phishing`, `llm`
- **Slug:** `google-sues-outsider-enterprise-ai-scam-texts`
- **Must-know:** no
- **Summary:** Google sued an alleged Chinese cybercrime operation, "Outsider Enterprise," accusing it of using AI to send roughly 2.5 million scam text messages over two weeks and scamming hundreds of thousands of victims.

### 9. Anthropic Disputes Claimed Prompt-Based Jailbreak of Claude Fable 5
- **Source:** SecurityWeek — https://www.securityweek.com/anthropic-disputes-fable-5-ai-jailbreak/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ai-safety`, `anthropic`, `llm`
- **Slug:** `anthropic-disputes-fable-5-jailbreak-claim`
- **Must-know:** no
- **Summary:** An independent researcher claims to have achieved a prompt-based jailbreak of Claude Fable 5 shortly after launch; Anthropic disputes that the bypass is a genuine jailbreak, and no technical details have been independently verified.

### 10. INTERPOL-Led Operation Dismantles Decade-Old Sniper Dz Phishing-as-a-Service Platform
- **Source:** The Hacker News — https://thehackernews.com/2026/06/interpol-takes-down-sniper-dz-phishing.html
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `phishing`
- **Slug:** `interpol-sniper-dz-phishing-takedown`
- **Must-know:** no
- **Summary:** "Operation Ramz," an INTERPOL-led effort across 13 MENA countries running October 2025–February 2026, dismantled the long-running Sniper Dz phishing-as-a-service platform and resulted in 201 arrests, including its primary operator.

### 11. Europol Disrupts AudiA6 Crypto-Laundering Service Tied to Ransomware Gangs
- **Source:** The Hacker News — https://thehackernews.com/2026/06/europol-disrupts-audia6-crypto.html
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `ransomware`
- **Slug:** `europol-audia6-crypto-laundering-takedown`
- **Must-know:** no
- **Summary:** Europol disrupted AudiA6, a cryptocurrency laundering service used by ransomware gangs and other cybercriminal networks, estimated to have laundered over €336 million (~$389 million) in illicit proceeds.

## Skippable

- **SpaceX IPO: Live updates on everything you need to know** — TechCrunch AI. Generic business/IPO coverage, no security or AI substance.
- **Quoting Andrew Singleton** — Simon Willison. Allegorical/opinion post on AI investment bubbles, no news value.
- **Ukrainian national pleads guilty to role in Conti ransomware operation** — BleepingComputer. Legal follow-up on a years-old case, no new TTPs or IOCs.
- **Mistral is rumored to be raising €3B at €20B valuation** — TechCrunch AI. Funding rumor, no security or launch substance.
- **Bankruptcy admin approves settlement fund of $47 million for 23andMe data breach victims** — The Record. Legal settlement follow-up to a 2023 breach, no new technical detail.
- **Major US surveillance program poised to lapse after legislative deadlock** — The Record. US policy/legislative news unrelated to AI, no actionable technical content.
- **Elon Musk is the world's first trillionaire** — The Verge AI. Business/markets news tied to SpaceX IPO, no security angle.
- **SpaceX, Anthropic, and OpenAI's hot IPO summer** — TechCrunch AI. IPO market commentary, no security or model-launch substance.
- **In Other News: Google Security Layoffs, AudiA6 Takedown, $400 Million Coupang Fine** — SecurityWeek. Roundup post; underlying stories covered separately or via better sources.
- **South Korea hits Coupang with record $409 million fine over data breach** — The Record. Regulatory fine follow-up to a prior breach, no new technical detail.
- **It's hot IPO summer, and the MANGOS are ripe** — TechCrunch AI. Duplicate IPO market commentary.
- **SpaceX's massive IPO: all the latest news** — The Verge AI. Duplicate IPO coverage.
- **Jeff Bezos' AI startup aims to build an 'artificial general engineer'** — The Verge AI. Speculative reporting on a new AI startup's ambitions, no concrete launch.
- **Early Warning Signs of Supply-Chain Attacks Live in the Dark Web** — BleepingComputer. Vendor-sponsored general discussion, no specific new incident.
- **Claude Fable 5 Doesn't Change the Mythos Security Story** — Dark Reading. Analysis/opinion piece on the already-covered Fable 5 launch.
- **The Good, the Bad and the Ugly in Cybersecurity – Week 24** — SentinelOne Labs. Weekly roundup; stories covered individually or already reported.
- **Industry Reactions to Claude Fable 5: Feedback Friday** — SecurityWeek. Industry-reaction roundup on the already-covered Fable 5 launch, opinion without news value.
- **Microsoft fixes Windows update failures linked to WUSA installer** — BleepingComputer. Generic IT bug fix, no security implication.
- **Iranian Cyber Group Handala Claims Cal Water Hack** — SecurityWeek. Single-org breach claim, no TTPs or IOCs.
- **Rethinking MDR as Attackers and Defenders Embrace AI** — The Hacker News. Opinion/vendor piece on MDR strategy, no news value.
- **Pharma giant Novo Nordisk discloses breach of clinical trials data** — BleepingComputer. Breach disclosure without technical substance or confirmed scale.
- **New OpenAI Academy courses for the next era of work** — OpenAI Blog. Educational/marketing content, no model launch or security substance.
- **Chrome 149 Update Patches 28 Vulnerabilities** — SecurityWeek. Routine patch coverage; no actively-exploited critical CVE highlighted, and Chrome 149's zero-day was already covered.
- **Over 73,000 French govt employees affected in Tchap messenger breach** — BleepingComputer. Breach affects under 100k users with no technical detail on the attack vector.
- **Siri won't be your AI girlfriend** — The Verge AI. Feature/opinion piece on Siri's conversational design, no security or major-launch substance.
