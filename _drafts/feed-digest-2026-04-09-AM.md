# Digest — 2026-04-09 AM

- Window: last 14h
- Raw items considered: 29
- Relevant: 19
- Skippable: 10

## Relevant

### 1. CISA Orders Feds to Patch Exploited Ivanti EPMM Flaw by Sunday
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-exploited-ivanti-epmm-flaw-by-sunday/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `zero-day`
- **Slug:** `ivanti-epmm-cve-exploited-cisa-patch-deadline`
- **Must-know:** yes
- **Summary:** CISA has given U.S. federal agencies four days to patch a critical Ivanti EPMM vulnerability that has been actively exploited since January 2026. The extended exploitation window and agency-wide mandate make this an immediate priority for any organization running Ivanti mobile device management infrastructure.

### 2. 13-Year-Old RCE Vulnerability Found in Apache ActiveMQ Classic
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/13-year-old-bug-in-activemq-lets-hackers-remotely-execute-commands/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`
- **Slug:** `apache-activemq-13-year-rce-vulnerability`
- **Must-know:** no
- **Summary:** Researchers discovered an RCE vulnerability in Apache ActiveMQ Classic that went undetected for 13 years. While the RCE itself requires authentication, a separate flaw exposes the Jolokia API without authentication, potentially providing an unauthenticated exploitation path.

### 3. FBI-Led Operation Disrupts Russia's Forest Blizzard SOHO Router Campaign
- **Source:** Cybersecurity Dive — https://www.cybersecuritydive.com/news/russia-routers-hacking-dns-fbi-disruption/816960/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `malware`
- **Slug:** `russia-forest-blizzard-soho-router-hijacking`
- **Must-know:** no
- **Summary:** A court-authorized U.S. operation disrupted Russia's APT28 (Forest Blizzard) campaign that hijacked SOHO routers via a single DNS setting change to conduct malwareless espionage against global organizations. The campaign is the latest evidence that end-of-life routers are a persistent nation-state attack surface.

### 4. Iran-Linked Hackers Targeting US Water and Energy Sectors, FBI and CISA Warn
- **Source:** Cybersecurity Dive — https://www.cybersecuritydive.com/news/iran-linked-hackers-targeting-water-energy-in-us-fbi-and-cisa-warn/816949/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `ics`
- **Slug:** `iran-hackers-target-water-energy-fbi-cisa-warning`
- **Must-know:** no
- **Summary:** FBI and CISA issued a joint advisory warning that Iran-linked threat actors are actively exploiting vulnerabilities in industrial programmable logic controllers to target U.S. water and energy sectors, causing operational disruption and financial losses. Critical infrastructure operators should audit exposed OT/ICS systems immediately.

### 5. AWS Bedrock AgentCore "Agent God Mode" — IAM Privilege Escalation Risk
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/exploit-of-aws-agentcore-iam-god-mode/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `privilege-escalation`, `cloud-security`, `llm`, `aws`
- **Slug:** `aws-bedrock-agentcore-iam-privilege-escalation`
- **Must-know:** no
- **Summary:** Unit 42 disclosed an "Agent God Mode" attack against Amazon Bedrock AgentCore where overly broad IAM permissions allow privilege escalation and data exfiltration from the underlying AWS account. This research highlights a systemic AI infrastructure risk where IAM misconfigurations can lead to full account compromise.

### 6. UNC6783 Compromises BPO Providers to Steal Corporate Zendesk Support Tickets
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/google-new-unc6783-hackers-steal-corporate-zendesk-support-tickets/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `phishing`, `supply-chain`
- **Slug:** `unc6783-bpo-zendesk-ticket-theft`
- **Must-know:** no
- **Summary:** Google researchers documented UNC6783, a new threat group compromising business process outsourcing providers to pivot into high-value companies across multiple sectors. Targeting Zendesk support tickets suggests an intent to harvest credentials, PII, and internal communications from victim organizations.

### 7. Atomic Stealer Delivered via ClickFix Script Editor Abuse on macOS
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-macos-stealer-campaign-uses-script-editor-in-clickfix-attack/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `phishing`
- **Slug:** `macos-atomic-stealer-clickfix-script-editor`
- **Must-know:** no
- **Summary:** A new macOS campaign delivers Atomic Stealer by abusing Script Editor in a ClickFix variant that tricks users into executing malicious Terminal commands, bypassing browser-based defenses. Any unsolicited instruction to open Script Editor or paste commands into Terminal should be treated as a social engineering attempt.

### 8. Breach Exposes 7.7 TB of Sensitive LAPD Files From City Attorney Systems
- **Source:** The Record (Recorded Future) — https://therecord.media/breach-exposes-lapd-files-city-attorney-systems
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `lapd-city-attorney-breach-7-7tb-sensitive-files`
- **Must-know:** no
- **Summary:** A breach of Los Angeles city attorney systems exposed sensitive LAPD files, with social media posts advertising 7.7 terabytes of data available for download before some posts were removed. The full scope and specific record types compromised have not been officially confirmed.

### 9. Eurail Confirms Over 300,000 Passport Numbers Leaked in December Breach
- **Source:** The Record (Recorded Future) — https://therecord.media/eurail-reports-data-breach-impacting-over-300000
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `eurail-data-breach-300k-passports-leaked`
- **Must-know:** no
- **Summary:** Eurail confirmed that passport numbers for more than 300,000 individuals were exposed in the December 2025 breach. The attacker who claimed the attack says they stole 1.3 TB of data including source code, database backups, and Zendesk support tickets.

### 10. Minnesota Deploys National Guard to Winona County After Cyberattack on Critical Systems
- **Source:** The Record (Recorded Future) — https://therecord.media/minnesota-sends-national-guard-after-local-cyberattack
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`
- **Slug:** `minnesota-national-guard-winona-county-cyberattack`
- **Must-know:** no
- **Summary:** Minnesota Governor Tim Walz deployed the National Guard to Winona County via executive order after a cyberattack disrupted critical county systems beginning Monday. The nature of the attack has not been publicly confirmed.

### 11. New Chaos Botnet Variant Expands to Target Misconfigured Cloud Deployments
- **Source:** The Hacker News — https://thehackernews.com/2026/04/new-chaos-variant-targets-misconfigured.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `cloud-security`
- **Slug:** `chaos-botnet-variant-targets-cloud-deployments`
- **Must-know:** no
- **Summary:** A new Chaos malware variant targets misconfigured cloud deployments in addition to its traditional router and edge device focus, adding a SOCKS proxy capability. Darktrace researchers say the operator is actively expanding the botnet's targeting infrastructure.

### 12. Magecart Campaign Hides Credit Card Stealer in Pixel-Sized SVG on Magento Stores
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-use-pixel-large-svg-trick-to-hide-credit-card-stealer/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `appsec`, `data-breach`
- **Slug:** `magento-svg-credit-card-stealer-campaign`
- **Must-know:** no
- **Summary:** A Magecart campaign affecting nearly 100 Magento-powered online stores hides card-stealing code inside a pixel-sized SVG image element to evade file-based scanners. Magento store operators should audit all third-party scripts and image assets for injected content.

### 13. OpenSSL Patches Seven Vulnerabilities Including Data Leakage Flaw
- **Source:** SecurityWeek — https://www.securityweek.com/data-leakage-vulnerability-patched-in-openssl/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`, `cve`
- **Slug:** `openssl-data-leakage-vulnerability-patched`
- **Must-know:** no
- **Summary:** OpenSSL released patches for seven vulnerabilities, most enabling denial-of-service attacks, plus one data leakage flaw. Operators of OpenSSL-dependent services should schedule patching at the next available maintenance window.

### 14. HackerOne Pauses Open Source Bug Bounties as AI Shifts Bottleneck to Remediation
- **Source:** Dark Reading — https://www.darkreading.com/application-security/ai-led-remediation-crisis-prompts-hackerone-pause-bug-bounties
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ai-safety`, `appsec`, `llm`
- **Slug:** `hackerone-pauses-bug-bounties-ai-remediation-crisis`
- **Must-know:** no
- **Summary:** HackerOne paused bug bounty payouts for open source projects after AI-driven discovery tooling shifted the bottleneck from finding bugs to fixing them—a cost bounties don't fund. This marks a structural inflection point for the vulnerability disclosure ecosystem driven by AI tooling.

### 15. Masjesu Botnet Surfaces as Telegram-Advertised DDoS-for-Hire Targeting Global IoT
- **Source:** The Hacker News — https://thehackernews.com/2026/04/masjesu-botnet-emerges-as-ddos-for-hire.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `masjesu-ddos-for-hire-botnet-iot-devices`
- **Must-know:** no
- **Summary:** Researchers documented the Masjesu botnet, a DDoS-for-hire service advertised on Telegram since 2023 targeting IoT devices including routers and gateways across multiple CPU architectures. The commercial botnet model reflects continued commoditization of DDoS infrastructure.

### 16. Egyptian Journalists Targeted With Elaborate Spearphishing Campaign Tied to Spyware
- **Source:** The Record (Recorded Future) — https://therecord.media/two-egyptian-journalists-targeted-spearphishing-campaign
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`
- **Slug:** `egyptian-journalists-targeted-spearphishing-spyware`
- **Must-know:** no
- **Summary:** Access Now and Lookout documented an elaborate spearphishing campaign targeting two prominent Egyptian journalists, with evidence the infrastructure may have been used to deliver spyware and exfiltrate data. The operation fits a recurring pattern of commercial or state-linked spyware use against civil society targets.

### 17. Threat Actors Use Emoji Encoding to Bypass Security Detection Filters
- **Source:** Dark Reading — https://www.darkreading.com/cyber-risk/emojis-power-covert-threat-actor-communications
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `emoji-covert-communications-threat-actors`
- **Must-know:** no
- **Summary:** Researchers documented threat actors using emoji-based encoding in covert communications—🤖 for "bot available," 🧰 for "toolkit," 💰💰💰 for "big ransom"—to bypass keyword-based detection filters. Security teams should review SIEM alerting rules to account for non-ASCII encoding in monitored threat actor channels.

### 18. TikTok Removes Covert Influence Networks Targeting Hungarian Election
- **Source:** The Record (Recorded Future) — https://therecord.media/tiktok-removes-covert-networks-hungary-vote
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `influence-ops`
- **Slug:** `tiktok-removes-covert-networks-hungary-vote`
- **Must-know:** no
- **Summary:** TikTok removed covert networks of fake accounts amplifying political content targeting Hungarian users ahead of a national election, aimed at both opposition and ruling party figures. The action reflects continued platform enforcement against coordinated inauthentic behavior around major elections.

### 19. Meta Launches Muse Spark, First Model From Its Reorganized AI Division
- **Source:** The Verge AI — https://www.theverge.com/tech/908769/meta-muse-spark-ai-model-launch-rollout
- **Section:** Mixed / General Tech Security
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `llm`
- **Slug:** `meta-muse-spark-ai-model-launch`
- **Must-know:** no
- **Summary:** Meta Superintelligence Labs launched Muse Spark, the first model release since Zuckerberg overhauled the company's AI efforts, now powering the Meta AI app and website in the US. Rollout to WhatsApp, Instagram, Facebook, and Messenger is planned for coming weeks.

## Skippable

- **Black Hat USA** — Dark Reading. Events listing for the August 2026 conference; no security news or incident angle.
- **Shaky Ceasefire Unlikely to Stop Cyberattacks From Iran-Linked Hackers** — SecurityWeek. Opinion/analysis piece; substantive Iran threat news captured in item 4 above (FBI/CISA joint advisory).
- **Russia's Forest Blizzard Nabs Rafts of Logins Via SOHO Routers** — Dark Reading. Duplicate coverage of the Forest Blizzard SOHO router story; primary source selected from Cybersecurity Dive (item 3 above).
- **Gemini Gets Notebooks to Help You Organize Projects** — The Verge AI. Non-security AI product feature update with no security angle.
- **OpenAI Made Economic Proposals — Here's What DC Thinks** — The Verge AI. Policy opinion newsletter with no breaking news value.
- **Fraud Rockets Higher in Mobile-First Latin America** — Dark Reading. Trend/analysis piece without a specific incident or actionable news hook.
- **Full Sail University to Open IBM Cyber Defense Range** — Dark Reading. Marketing/partnership announcement with no security news value.
- **RCE Bug Lurked in Apache ActiveMQ Classic for 13 Years** — SecurityWeek. Duplicate coverage of the ActiveMQ RCE story; primary source selected from BleepingComputer (item 2 above).
- **ALTK‑Evolve: On‑the‑Job Learning for AI Agents** — Hugging Face Blog. AI research paper with no security angle or incident.
- **Niobium Introduces The Fog** — Dark Reading. Product launch announcement with no summary or security incident context.
