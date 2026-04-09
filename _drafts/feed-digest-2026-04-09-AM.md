# Digest — 2026-04-09 AM

- Window: last 14h
- Raw items considered: 26
- Relevant: 20
- Skippable: 6

## Relevant

### 1. CISA Orders Feds to Patch Actively Exploited Ivanti EPMM Flaw by Sunday
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-exploited-ivanti-epmm-flaw-by-sunday/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `zero-day`
- **Slug:** `cisa-ivanti-epmm-actively-exploited`
- **Must-know:** yes
- **Summary:** CISA issued an emergency directive giving federal agencies until Sunday to patch a critical Ivanti EPMM vulnerability that has been actively exploited since January. The flaw targets mobile device management infrastructure across U.S. government networks.

### 2. Russia's APT28 (Forest Blizzard) Conducts Malwareless Espionage via SOHO Router DNS Hijack
- **Source:** Dark Reading — https://www.darkreading.com/threat-intelligence/russia-forest-blizzard-logins-soho-routers
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `malware`, `cloud-security`, `apt`
- **Slug:** `forest-blizzard-soho-router-dns-espionage`
- **Must-know:** no
- **Summary:** Russia's APT28 is harvesting credentials from global organizations without deploying malware — by modifying a single DNS setting on vulnerable SOHO routers. The FBI subsequently disrupted the campaign via a court-authorized operation.

### 3. FBI Operation Disrupts Russia's SOHO Router Campaign Targeting Critical Infrastructure
- **Source:** Cybersecurity Dive — https://www.cybersecuritydive.com/news/russia-routers-hacking-dns-fbi-disruption/816960/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cloud-security`, `apt`
- **Slug:** `fbi-operation-evicts-russia-soho-routers`
- **Must-know:** no
- **Summary:** The U.S. government disclosed a court-authorized operation to evict Forest Blizzard from compromised SOHO routers used against critical infrastructure. The action removes persistent access but does not fix the underlying end-of-life device problem.

### 4. SVG Pixel Trick Hides Credit Card Skimmer Across Nearly 100 Magento Stores
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-use-pixel-large-svg-trick-to-hide-credit-card-stealer/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `appsec`, `data-breach`
- **Slug:** `svg-pixel-skimmer-magento-stores`
- **Must-know:** no
- **Summary:** Attackers are concealing credit card skimming code inside a 1×1 pixel SVG image on Magento store pages, bypassing file-content detectors that don't parse SVG internals. The campaign has hit nearly 100 stores.

### 5. AWS Bedrock AgentCore "Agent God Mode" Enables IAM Privilege Escalation and Data Exfiltration
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/exploit-of-aws-agentcore-iam-god-mode/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `privilege-escalation`, `cloud-security`, `aws`, `llm`
- **Slug:** `aws-bedrock-agentcore-iam-god-mode`
- **Must-know:** no
- **Summary:** Unit 42 found that overly broad IAM permissions in Amazon Bedrock AgentCore allow privilege escalation to near-full AWS account control, enabling unrestricted data exfiltration. Organizations using AgentCore should audit IAM roles and apply least-privilege configurations.

### 6. New Threat Actor UNC6783 Steals Enterprise Zendesk Tickets via BPO Supply Chain
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/google-new-unc6783-hackers-steal-corporate-zendesk-support-tickets/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `phishing`, `supply-chain`
- **Slug:** `unc6783-zendesk-ticket-theft-bpo`
- **Must-know:** no
- **Summary:** Google is tracking UNC6783, a new threat actor that compromises BPO providers as a supply-chain pivot into high-value enterprise targets, specifically stealing Zendesk support tickets containing sensitive internal data.

### 7. Atomic Stealer Delivered to macOS Users via ClickFix Script Editor Attack
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-macos-stealer-campaign-uses-script-editor-in-clickfix-attack/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `phishing`
- **Slug:** `macos-atomic-stealer-clickfix-script-editor`
- **Must-know:** no
- **Summary:** A campaign distributes Atomic Stealer by abusing macOS Script Editor in a ClickFix-style social engineering attack, tricking users into pasting malicious Terminal commands. This adapts a Windows-common technique to macOS, bypassing Gatekeeper via a trusted system app.

### 8. Chaos Botnet Variant Expands to Misconfigured Cloud Deployments, Adds SOCKS Proxy
- **Source:** The Hacker News — https://thehackernews.com/2026/04/new-chaos-variant-targets-misconfigured.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `cloud-security`
- **Slug:** `chaos-malware-cloud-deployments-socks-proxy`
- **Must-know:** no
- **Summary:** A new Chaos variant has shifted from routers and edge devices to misconfigured cloud deployments, adding SOCKS proxy capability for persistent access. Cloud operators should audit exposed services and monitor for unexpected outbound proxy traffic.

### 9. Eurail December Breach Leaked Passport Numbers for Over 300,000 Users
- **Source:** The Record (Recorded Future) — https://therecord.media/eurail-reports-data-breach-impacting-over-300000
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `eurail-passport-breach-300k`
- **Must-know:** no
- **Summary:** A December 2025 Eurail breach exposed passport numbers for 300,000+ users; a threat actor claims 1.3 TB stolen including source code, database backups, and Zendesk tickets. Affected users face elevated identity fraud risk from passport data exposure.

### 10. Breach of LA City Attorney System Exposes Sensitive LAPD Files — 7.7TB Available
- **Source:** The Record (Recorded Future) — https://therecord.media/breach-exposes-lapd-files-city-attorney-systems
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `lapd-breach-sensitive-files-7tb`
- **Must-know:** no
- **Summary:** A breach of the Los Angeles city attorney's systems exposed sensitive LAPD files, with social media posts advertising 7.7 terabytes for download. The scale and sensitivity of the dataset pose significant risks for active investigations and officer safety.

### 11. Apache ActiveMQ Classic Carries 13-Year-Old RCE Risk via Unauthenticated Jolokia API
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/13-year-old-bug-in-activemq-lets-hackers-remotely-execute-commands/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`
- **Slug:** `activemq-13-year-rce-vulnerability`
- **Must-know:** no
- **Summary:** A 13-year-old RCE vulnerability in Apache ActiveMQ Classic requires authentication to exploit, but a second flaw exposes the Jolokia API without authentication — creating a practical exploitation chain. Patch immediately; ActiveMQ is widely deployed in enterprise Java environments.

### 12. Minnesota Governor Deploys National Guard After Cyberattack on Winona County Systems
- **Source:** The Record (Recorded Future) — https://therecord.media/minnesota-sends-national-guard-after-local-cyberattack
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ransomware`
- **Slug:** `minnesota-national-guard-cyberattack`
- **Must-know:** no
- **Summary:** Governor Tim Walz issued an executive order deploying National Guard cyber assets to Winona County after a Monday cyberattack disrupted critical county systems. The state-level response signals significant operational impact, consistent with ransomware patterns against local government.

### 13. Two Egyptian Journalists Targeted with Spearphishing Campaign Potentially Delivering Spyware
- **Source:** The Record (Recorded Future) — https://therecord.media/two-egyptian-journalists-targeted-spearphishing-campaign
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`, `malware`
- **Slug:** `egyptian-journalists-spearphishing-spyware`
- **Must-know:** no
- **Summary:** Access Now and Lookout documented a targeted spearphishing campaign against two prominent Egyptian journalists using infrastructure associated with commercial spyware delivery. The operation is consistent with state-sponsored surveillance targeting civil society.

### 14. Threat Actors Use Emoji Encoding to Evade Detection in C2 and Criminal Channels
- **Source:** Dark Reading — https://www.darkreading.com/cyber-risk/emojis-power-covert-threat-actor-communications
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `appsec`
- **Slug:** `emoji-c2-evasion-threat-actors`
- **Must-know:** no
- **Summary:** Threat actors use emojis as semantic shorthand in C2 and marketplace channels — 🤖 for "bot available," 🧰 for "toolkit," 💰💰💰 for "big ransom" — bypassing text-pattern detection. Security teams should extend monitoring to emoji-rich messaging platforms like Telegram.

### 15. TikTok Removes Covert Influence Networks Targeting Hungarian Users Ahead of Elections
- **Source:** The Record (Recorded Future) — https://therecord.media/tiktok-removes-covert-networks-hungary-vote
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `influence-ops`
- **Slug:** `tiktok-covert-networks-hungary-vote`
- **Must-know:** no
- **Summary:** TikTok removed fake-account networks amplifying political content targeting Hungarian users before an upcoming vote, affecting both opposition and ruling-party narratives. The multi-directional targeting suggests destabilization as the goal rather than support for any single faction.

### 16. HackerOne Pauses Bug Bounties as AI Discovery Creates Remediation Backlog
- **Source:** Dark Reading — https://www.darkreading.com/application-security/ai-led-remediation-crisis-prompts-hackerone-pause-bug-bounties
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `appsec`, `llm`, `devsecops`
- **Slug:** `hackerone-bug-bounties-ai-remediation`
- **Must-know:** no
- **Summary:** HackerOne paused bounty programs for some open source projects after AI-assisted discovery flooded them with more valid bugs than maintainers can fix — shifting the bottleneck from finding to remediating. Bounties fund discovery, not remediation, creating a structural imbalance.

### 17. Masjesu DDoS-for-Hire Botnet Targets Global IoT Devices Across Architectures
- **Source:** The Hacker News — https://thehackernews.com/2026/04/masjesu-botnet-emerges-as-ddos-for-hire.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `vulnerability`
- **Slug:** `masjesu-ddos-hire-botnet-iot`
- **Must-know:** no
- **Summary:** Masjesu is a Telegram-advertised DDoS-for-hire service active since 2023 that recruits IoT routers and gateways across multiple CPU architectures. Public disclosure provides defenders with TTPs and infrastructure indicators for a previously low-profile threat service.

### 18. Meta Superintelligence Labs Launches Muse Spark, First Model of New AI Division
- **Source:** The Verge AI — https://www.theverge.com/tech/908769/meta-muse-spark-ai-model-launch-rollout
- **Section:** Mixed / General Tech Security
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `llm`
- **Slug:** `meta-muse-spark-ai-launch`
- **Must-know:** no
- **Summary:** Meta Superintelligence Labs launched Muse Spark, the first model from Zuckerberg's restructured AI division, now powering the Meta AI app and website in the US. WhatsApp, Instagram, Facebook, and Messenger integration is coming in the next few weeks.

### 19. OpenSSL Patches Data Leakage Vulnerability Alongside Six Additional Flaws
- **Source:** SecurityWeek — https://www.securityweek.com/data-leakage-vulnerability-patched-in-openssl/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`, `cve`, `appsec`
- **Slug:** `openssl-data-leakage-patch`
- **Must-know:** no
- **Summary:** OpenSSL patched seven vulnerabilities including a data leakage flaw; the remaining six are primarily DoS risks. No active exploitation reported — apply through the normal patching cycle.

### 20. Iran-Linked Hackers Signal Intent to Resume Attacks as Ceasefire Remains Fragile
- **Source:** SecurityWeek — https://www.securityweek.com/shaky-ceasefire-unlikely-to-stop-cyberattacks-from-iran-linked-hackers-for-long/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `phishing`, `apt`
- **Slug:** `iran-hackers-ceasefire-threat`
- **Must-know:** no
- **Summary:** Iran-linked threat actors vowed to resume attacks against American targets when geopolitical conditions shift, framing digital warfare as embedded in military conflict cycles. Critical infrastructure and government security teams should maintain elevated posture during the pause.

## Skippable

- **Black Hat USA** — Dark Reading. Future-dated event listing (published 2026-08-01); not a news article.
- **Gemini gets notebooks** — The Verge AI. Product feature update (chat notebooks) with no security angle.
- **OpenAI made economic proposals — here's what DC thinks** — The Verge AI. Political opinion newsletter; no actionable security news.
- **Fraud Rockets Higher in Mobile-First Latin America** — Dark Reading. Regional fraud trend analysis without specific CVE, breach, or tool disclosure.
- **Full Sail University to Open IBM Cyber Defense Range** — Dark Reading. Educational marketing press release; no news value.
- **RCE Bug Lurked in Apache ActiveMQ Classic for 13 Years** — SecurityWeek. Duplicate of item #11 (same CVE/story); BleepingComputer version retained as primary.
