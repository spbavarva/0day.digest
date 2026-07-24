# Digest — 2026-07-24 PM

- Window: last 14h
- Raw items considered: 39
- Relevant: 16
- Skippable: 23

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[MEDIUM]** Hackers Hijack Hotel Wi-Fi DNS to Steal Microsoft 365 Accounts — `2026-07-24-hotel-wifi-dns-hijack-microsoft-365-phishing.md`
- [x] **[INFORMATIONAL]** Anthropic Launches Opus 5 — `2026-07-24-anthropic-launches-opus-5.md`
- [x] **[HIGH]** BlueNoroff Zoom Phishing Kit Profiles Crypto Wallets Before Malware Delivery — `2026-07-24-bluenoroff-zoom-phishing-kit-crypto-wallets.md`
- [x] **[HIGH]** Certighost Exploit Lets Low-Privileged AD Users Impersonate a Domain Controller — `2026-07-24-certighost-active-directory-domain-controller-impersonation.md`
- [x] **[MEDIUM]** Slopsquatting, Phantom Domains, and HalluSquatting Are the Same AI Attack — `2026-07-24-slopsquatting-hallusquatting-ai-hallucination-attacks.md`
- [x] **[HIGH]** Vatican's Official Prayer App Leaks 700K+ Global Users' PII — `2026-07-24-vatican-prayer-app-leaks-pii.md`
- [x] **[HIGH]** Default Azure Automation Setting Enables Cross-Tenant Identity Takeover — `2026-07-24-azure-automation-cross-tenant-identity-takeover.md`
- [x] **[HIGH]** ChatGPT AgentForger Flaw Could Deploy Rogue Workspace Agents via a Phishing Link — `2026-07-24-chatgpt-agentforger-rogue-workspace-agents.md`
- [x] **[HIGH]** Bing Images Flaws Let Crafted SVGs Run Commands as SYSTEM on Microsoft's Servers — `2026-07-24-bing-images-svg-rce-system-root.md`
- [x] **[HIGH]** Hacker Runs Hermes AI Agent Unattended for Post-Exploitation at Thai Finance Ministry — `2026-07-24-hermes-ai-agent-thai-finance-ministry-post-exploitation.md`
- [x] **[MEDIUM]** Golden Chickens Resurfaces With Four New Malware Families — `2026-07-24-golden-chickens-new-malware-families-modular-implants.md`
- [x] **[HIGH]** NodeBB Patches Eight AI-Found Flaws Exposing Admin Access and Private Chats — `2026-07-24-nodebb-eight-ai-found-flaws-admin-access.md`
- [x] **[HIGH]** Clop Ransomware Targets Windchill, FlexPLM in Data Theft Attacks — `2026-07-24-clop-ransomware-windchill-flexplm-data-theft.md`
- [x] **[CRITICAL]** Kimi K3 Agents Found Redis Zero-Days and Built RCE Exploit — `2026-07-24-kimi-k3-redis-zero-days-rce-exploit.md`
- [x] **[MEDIUM]** Fake Notepad++ Plugin Delivers MATCHBOIL.V2 in UAC-0099 Attacks — `2026-07-24-fake-notepad-plugin-matchboil-uac-0099.md`
- [x] **[CRITICAL]** Data Breach Confirmed After Australian Energy Giant Origin Is Hacked — `2026-07-24-origin-energy-data-breach-2-million-customers.md`

## Relevant (details)

### 1. Hackers Hijack Hotel Wi-Fi DNS to Steal Microsoft 365 Accounts
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-hijack-hotel-wi-fi-dns-to-steal-microsoft-365-accounts/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`, `microsoft`, `dns-hijacking`
- **Slug:** `hotel-wifi-dns-hijack-microsoft-365-phishing`
- **Must-know:** no
- **Summary:** Attackers are altering DNS settings on Wi-Fi devices at hotels and conference centers to redirect guests to fake Microsoft 365 login pages. The technique targets travelers and conference attendees rather than a specific organization, harvesting M365 credentials at the network level.

### 2. Anthropic Launches Opus 5
- **Source:** TechCrunch AI — https://techcrunch.com/2026/07/24/anthropic-launches-opus-5/
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `anthropic`
- **Slug:** `anthropic-launches-opus-5`
- **Must-know:** no
- **Summary:** Anthropic released Opus 5, positioned as cheaper and less restrictive than Fable 5 while coming "close" to Fable 5's capabilities in many domains. The release lands shortly after Anthropic's back-and-forth with the US government and an OpenAI security incident that dominated industry discussion.

### 3. BlueNoroff Zoom Phishing Kit Profiles Crypto Wallets Before Malware Delivery
- **Source:** The Hacker News — https://thehackernews.com/2026/07/bluenoroff-zoom-phishing-kit-profiles.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `phishing`, `malware`, `cryptocurrency`
- **Slug:** `bluenoroff-zoom-phishing-kit-crypto-wallets`
- **Must-know:** no
- **Summary:** North Korean threat actor BlueNoroff, behind ClickFix-style campaigns using typosquatted Zoom and Teams domains, operates an active phishing kit that impersonates videoconferencing platforms to profile victims' crypto wallets before delivering malware. The group combines compromised industry contacts with social engineering to build trust before the attack.

### 4. Certighost Exploit Lets Low-Privileged AD Users Impersonate a Domain Controller
- **Source:** The Hacker News — https://thehackernews.com/2026/07/certighost-exploit-lets-low-privileged.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `privilege-escalation`, `vulnerability`
- **Slug:** `certighost-active-directory-domain-controller-impersonation`
- **Must-know:** no
- **Summary:** Researchers H0j3n and Aniq Fakhrul published a working exploit, codenamed Certighost, that lets a low-privileged Active Directory user obtain a certificate for a Domain Controller and authenticate as that machine. Because DC accounts carry directory replication rights, the resulting Kerberos credential can be used to retrieve the krbtgt secret via DCSync.

### 5. Slopsquatting, Phantom Domains, and HalluSquatting Are the Same AI Attack
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/slopsquatting-phantom-domains-and-hallusquatting-are-the-same-ai-attack/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `supply-chain`, `ai-safety`, `llm`, `npm`, `pypi`
- **Slug:** `slopsquatting-hallusquatting-ai-hallucination-attacks`
- **Must-know:** no
- **Summary:** Slopsquatting, phantom-domain squatting, and HalluSquatting all exploit the same late-binding attack pattern, where AI coding agents trust hallucinated package, repo, or domain names. ActiveState says pre-fetch verification and governed dependency management can stop the attacks before malicious code enters a pipeline.

### 6. Vatican's Official Prayer App Leaks 700K+ Global Users' PII
- **Source:** Dark Reading — https://www.darkreading.com/vulnerabilities-threats/vatican-official-prayer-app-leaks-700k-pii
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `appsec`
- **Slug:** `vatican-prayer-app-leaks-pii`
- **Must-know:** no
- **Summary:** A porous API endpoint in the Vatican's official prayer app exposed names, email addresses, country, and account status for over 700,000 global users. The data was retrievable by anyone with a browser, with no authentication required.

### 7. Default Azure Automation Setting Enables Cross-Tenant Identity Takeover
- **Source:** Dark Reading — https://www.darkreading.com/cloud-security/default-azure-automation-setting-cross-tenant-identity-takeover
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `azure`, `cloud-security`, `iam`, `privilege-escalation`
- **Slug:** `azure-automation-cross-tenant-identity-takeover`
- **Must-know:** no
- **Summary:** Microsoft fixed a public-by-default configuration in Azure Automation, combined with a chain of code flaws, that could have let attackers seize another tenant's identity and access that tenant's data, credentials, and cloud workloads across tenant boundaries.

### 8. ChatGPT AgentForger Flaw Could Deploy Rogue Workspace Agents via a Phishing Link
- **Source:** The Hacker News — https://thehackernews.com/2026/07/chatgpt-agentforger-flaw-could-deploy.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `openai`, `llm`, `vulnerability`, `phishing`
- **Slug:** `chatgpt-agentforger-rogue-workspace-agents`
- **Must-know:** no
- **Summary:** Zenity Labs disclosed a critical vulnerability, codenamed AgentForger, in OpenAI's ChatGPT Workspace Agents that could have let a single phishing link stealthily build, authorize, and deploy an autonomous AI agent inside a victim organization. OpenAI patched the issue as of June 8.

### 9. Bing Images Flaws Let Crafted SVGs Run Commands as SYSTEM on Microsoft's Servers
- **Source:** The Hacker News — https://thehackernews.com/2026/07/bing-images-flaws-let-crafted-svgs-run.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `microsoft`, `rce`, `cve`, `vulnerability`
- **Slug:** `bing-images-svg-rce-system-root`
- **Must-know:** no
- **Summary:** A crafted SVG submitted to Bing's image search executed commands as NT AUTHORITY\SYSTEM on Microsoft's production image-processing workers, and as root on Linux machines in the same fleet, per researchers at XBOW. Microsoft assigned critical CVEs, including CVE-2026-32194, and fixed the flaw.

### 10. Hacker Runs Hermes AI Agent Unattended for Post-Exploitation at Thai Finance Ministry
- **Source:** The Hacker News — https://thehackernews.com/2026/07/hacker-runs-hermes-ai-agent-unattended.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `ai-safety`, `privilege-escalation`
- **Slug:** `hermes-ai-agent-thai-finance-ministry-post-exploitation`
- **Must-know:** no
- **Summary:** An attacker installed the Hermes AI agent on a rented server, disabled the setting requiring approval before running risky commands, and pointed it at Thailand's Ministry of Finance. The unattended agent then worked through the ministry's network on its own, checking hosts for privilege escalation paths and searching file systems.

### 11. Golden Chickens Resurfaces With Four New Malware Families
- **Source:** The Hacker News — https://thehackernews.com/2026/07/golden-chickens-resurfaces-with-four.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `golden-chickens-new-malware-families-modular-implants`
- **Must-know:** no
- **Summary:** The threat actors behind the Golden Chickens malware-as-a-service ecosystem have resurfaced with four new malware families, including TinyEgg and modularized ChonkyChicken variants. The group continues operating despite extensive public disclosure of its tooling.

### 12. NodeBB Patches Eight AI-Found Flaws Exposing Admin Access and Private Chats
- **Source:** The Hacker News — https://thehackernews.com/2026/07/nodebb-patches-eight-ai-found-flaws.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `llm`, `privilege-escalation`
- **Slug:** `nodebb-eight-ai-found-flaws-admin-access`
- **Must-know:** no
- **Summary:** Eight security flaws in NodeBB forum software, found by Aikido Security's AI pentest agents during a six-hour source review, went public with exploit code. Every version before 4.14.0 is affected; NodeBB has patched all eight in 4.14.2.

### 13. Clop Ransomware Targets Windchill, FlexPLM in Data Theft Attacks
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/clop-ransomware-targets-windchill-flexplm-in-data-theft-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ransomware`, `data-breach`
- **Slug:** `clop-ransomware-windchill-flexplm-data-theft`
- **Must-know:** no
- **Summary:** The Clop ransomware gang is targeting internet-exposed PTC Windchill and FlexPLM instances in a new data theft extortion campaign. Organizations running these product lifecycle management platforms should check for internet exposure.

### 14. Kimi K3 Agents Found Redis Zero-Days and Built RCE Exploit
- **Source:** The Hacker News — https://thehackernews.com/2026/07/kimi-k3-agents-found-redis-zero-days.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `rce`, `llm`, `vulnerability`
- **Slug:** `kimi-k3-redis-zero-days-rce-exploit`
- **Must-know:** no
- **Summary:** Redis shipped seven security releases after researchers published authenticated RCE proof-of-concept exploits, reportedly built by AI agents on Moonshot's Kimi K3 model, against stock Redis 6.2.22, 7.4.9, 8.6.4, and 8.8.0. Redis says the underlying memory-safety flaws may lead to remote code execution and has released patched versions.

### 15. Fake Notepad++ Plugin Delivers MATCHBOIL.V2 in UAC-0099 Attacks
- **Source:** The Hacker News — https://thehackernews.com/2026/07/fake-notepad-plugin-delivers.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `fake-notepad-plugin-matchboil-uac-0099`
- **Must-know:** no
- **Summary:** CERT-UA has warned of a campaign using a malicious program disguised as a Notepad++ plugin to compromise Windows systems, delivering malware tracked as MATCHBOIL.V2. The activity is attributed to UAC-0099, a Russia-aligned cluster previously seen weaponizing WinRAR flaws.

### 16. Data Breach Confirmed After Australian Energy Giant Origin Is Hacked
- **Source:** SecurityWeek — https://www.securityweek.com/data-breach-confirmed-after-australian-energy-giant-origin-is-hacked/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `data-breach`
- **Slug:** `origin-energy-data-breach-2-million-customers`
- **Must-know:** yes
- **Summary:** A hacker claims to have stolen the personal information of 2 million Origin Energy customers and is threatening to leak the data. Origin, an Australian energy giant, has confirmed the breach.

## Skippable

- **Why Cognition bought Poke: AI personality is becoming a competitive advantage** — TechCrunch AI. Business acquisition news, no security angle.
- **You can't ignore Google Zero anymore** — The Verge AI. Industry commentary/podcast, no security or model-launch substance.
- **Andy Burnham signals continuity on UK cyber policy, reappoints minister despite scrapping ministry** — The Record. Personnel/policy continuity story, no technical substance.
- **Anthropic releases Opus 5 with 'close' to Fable 5's capabilities** — The Verge AI. Duplicate coverage of the Opus 5 launch already pulled from TechCrunch.
- **Meta is making its AI chatbot more like an assistant** — The Verge AI. Generic product feature update, no security angle.
- **'Wrench' attacks against crypto holders appear to be on the rise** — The Record. Physical-crime trend piece, not a cyber or AI story.
- **As US weighs response to Chinese AI, industry urges against broad open-weight restrictions** — TechCrunch AI. Policy debate/lobbying, no concrete regulatory action yet.
- **Microsoft blames massive Microsoft 365 outage on maintenance bug** — BleepingComputer. Operational outage from an internal bug, not a security incident.
- **Bluesky's AI assistant Attie expands into an open social research tool** — TechCrunch AI. Generic product feature launch, no security relevance.
- **Midjourney acquired the astrology app Co-Star** — TechCrunch AI. Business acquisition, no security relevance.
- **The tech-broification of American science has officially begun** — The Verge AI. Government science-funding policy piece, no direct security implications.
- **In Other News: Dolphin X AI-Powered Malware, Car Anti-Theft Device Hack, 400 Linux Kernel Flaws** — SecurityWeek. Multi-topic roundup too thin on any single item to draft factually.
- **Chick-fil-A data breach affects more than 13,000 customers** — BleepingComputer. Below the >100k/technically-interesting bar; routine credential stuffing.
- **'AI communism', rogue models, and why Kimi K3 spooked Wall Street** — TechCrunch AI. Podcast commentary referencing other stories, no primary detail of its own.
- **OpenAI's new voice mode makes it to the ChatGPT desktop app** — TechCrunch AI. Generic product feature, no security angle.
- **The Good, the Bad and the Ugly in Cybersecurity – Week 30** — SentinelOne Labs. Multi-topic roundup; underlying stories referenced lack primary source detail in this batch.
- **Europol flags 4,340 URLs for removal in 'The Com' crackdown** — BleepingComputer. Law-enforcement takedown of extremist content, not a technical threat-intel story.
- **AegisAI Raises $36 Million for AI-Powered Email Security** — SecurityWeek. Funding announcement, no news substance beyond investment.
- **Your Best Analyst Shouldn't Be a Person. It Should Be a Capability Everyone Can Summon.** — SentinelOne Labs. Vendor opinion/marketing piece, no news value.
- **Seeing AI Agents Is Not Enough. Security Teams Must Enforce What They Can Do** — The Hacker News. Opinion piece on AI agent governance, no specific incident.
- **Industry Reactions to OpenAI Models Hacking Hugging Face: Feedback Friday** — SecurityWeek. Reaction roundup; no primary source with concrete facts on the underlying incident in this batch.
- **Man gets six years for hacking 750 women's Snapchat accounts** — BleepingComputer. Individual court case, no new technique.
- **Europe's Multilingual Reality Exposes AI Security Gaps** — Dark Reading. General commentary on guardrail gaps, no specific study or incident cited.
