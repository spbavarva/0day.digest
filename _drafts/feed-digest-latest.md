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
- **Severity:** medium
- **Tags:** `phishing`, `microsoft`, `dns-hijacking`
- **Summary:** Attackers are altering DNS settings on Wi-Fi devices at hotels and conference centers to redirect guests to fake Microsoft 365 login pages, harvesting credentials at the network level.

### 2. Anthropic Launches Opus 5
- **Source:** TechCrunch AI — https://techcrunch.com/2026/07/24/anthropic-launches-opus-5/
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `anthropic`
- **Summary:** Anthropic released Opus 5, positioned as cheaper and less restrictive than Fable 5 while coming "close" to Fable 5's capabilities in many domains.

### 3. BlueNoroff Zoom Phishing Kit Profiles Crypto Wallets Before Malware Delivery
- **Source:** The Hacker News — https://thehackernews.com/2026/07/bluenoroff-zoom-phishing-kit-profiles.html
- **Severity:** high
- **Tags:** `phishing`, `malware`, `cryptocurrency`
- **Summary:** North Korean threat actor BlueNoroff operates an active phishing kit impersonating Zoom/Teams to profile victims' crypto wallets before delivering malware.

### 4. Certighost Exploit Lets Low-Privileged AD Users Impersonate a Domain Controller
- **Source:** The Hacker News — https://thehackernews.com/2026/07/certighost-exploit-lets-low-privileged.html
- **Severity:** high
- **Tags:** `privilege-escalation`, `vulnerability`
- **Summary:** A published exploit lets a low-privileged AD user obtain a Domain Controller certificate and authenticate as that machine, enabling DCSync retrieval of the krbtgt secret.

### 5. Slopsquatting, Phantom Domains, and HalluSquatting Are the Same AI Attack
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/slopsquatting-phantom-domains-and-hallusquatting-are-the-same-ai-attack/
- **Severity:** medium
- **Tags:** `supply-chain`, `ai-safety`, `llm`, `npm`, `pypi`
- **Summary:** Slopsquatting, phantom-domain squatting, and HalluSquatting all exploit the same pattern of AI coding agents trusting hallucinated package/repo/domain names.

### 6. Vatican's Official Prayer App Leaks 700K+ Global Users' PII
- **Source:** Dark Reading — https://www.darkreading.com/vulnerabilities-threats/vatican-official-prayer-app-leaks-700k-pii
- **Severity:** high
- **Tags:** `data-breach`, `appsec`
- **Summary:** A porous, unauthenticated API endpoint exposed names, emails, country, and account status for 700,000+ users of the Vatican's official prayer app.

### 7. Default Azure Automation Setting Enables Cross-Tenant Identity Takeover
- **Source:** Dark Reading — https://www.darkreading.com/cloud-security/default-azure-automation-setting-cross-tenant-identity-takeover
- **Severity:** high
- **Tags:** `azure`, `cloud-security`, `iam`, `privilege-escalation`
- **Summary:** A public-by-default Azure Automation setting plus a chain of code flaws could have let attackers seize another tenant's identity and workloads. Microsoft has fixed it.

### 8. ChatGPT AgentForger Flaw Could Deploy Rogue Workspace Agents via a Phishing Link
- **Source:** The Hacker News — https://thehackernews.com/2026/07/chatgpt-agentforger-flaw-could-deploy.html
- **Severity:** high
- **Tags:** `openai`, `llm`, `vulnerability`, `phishing`
- **Summary:** A single phishing link could have stealthily built, authorized, and deployed a rogue AI agent inside a victim's ChatGPT Workspace. OpenAI patched it in June.

### 9. Bing Images Flaws Let Crafted SVGs Run Commands as SYSTEM on Microsoft's Servers
- **Source:** The Hacker News — https://thehackernews.com/2026/07/bing-images-flaws-let-crafted-svgs-run.html
- **Severity:** high
- **Tags:** `microsoft`, `rce`, `cve`, `vulnerability`
- **Summary:** A crafted SVG uploaded to Bing image search ran commands as SYSTEM/root on Microsoft's production image-processing fleet. Microsoft assigned critical CVEs and fixed it.

### 10. Hacker Runs Hermes AI Agent Unattended for Post-Exploitation at Thai Finance Ministry
- **Source:** The Hacker News — https://thehackernews.com/2026/07/hacker-runs-hermes-ai-agent-unattended.html
- **Severity:** high
- **Tags:** `llm`, `ai-safety`, `privilege-escalation`
- **Summary:** An attacker ran the Hermes AI agent unattended against Thailand's Ministry of Finance network, autonomously hunting for privilege escalation paths and post-exploitation opportunities.

### 11. Golden Chickens Resurfaces With Four New Malware Families
- **Source:** The Hacker News — https://thehackernews.com/2026/07/golden-chickens-resurfaces-with-four.html
- **Severity:** medium
- **Tags:** `malware`
- **Summary:** The Golden Chickens malware-as-a-service group has resurfaced with four new malware families, including TinyEgg and modularized ChonkyChicken variants.

### 12. NodeBB Patches Eight AI-Found Flaws Exposing Admin Access and Private Chats
- **Source:** The Hacker News — https://thehackernews.com/2026/07/nodebb-patches-eight-ai-found-flaws.html
- **Severity:** high
- **Tags:** `vulnerability`, `llm`, `privilege-escalation`
- **Summary:** AI pentest agents found eight flaws in NodeBB forum software during a six-hour source review, exposing admin access and private chats. All versions before 4.14.0 are affected.

### 13. Clop Ransomware Targets Windchill, FlexPLM in Data Theft Attacks
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/clop-ransomware-targets-windchill-flexplm-in-data-theft-attacks/
- **Severity:** high
- **Tags:** `ransomware`, `data-breach`
- **Summary:** The Clop ransomware gang is targeting internet-exposed PTC Windchill and FlexPLM instances in a data theft extortion campaign.

### 14. Kimi K3 Agents Found Redis Zero-Days and Built RCE Exploit
- **Source:** The Hacker News — https://thehackernews.com/2026/07/kimi-k3-agents-found-redis-zero-days.html
- **Severity:** critical
- **Tags:** `zero-day`, `rce`, `llm`, `vulnerability`
- **Summary:** AI agents built on Kimi K3 reportedly produced authenticated RCE PoCs against stock Redis versions, prompting Redis to ship seven security releases.

### 15. Fake Notepad++ Plugin Delivers MATCHBOIL.V2 in UAC-0099 Attacks
- **Source:** The Hacker News — https://thehackernews.com/2026/07/fake-notepad-plugin-delivers.html
- **Severity:** medium
- **Tags:** `malware`
- **Summary:** CERT-UA warns of a campaign disguising malware as a Notepad++ plugin, attributed to the Russia-aligned UAC-0099 cluster.

### 16. Data Breach Confirmed After Australian Energy Giant Origin Is Hacked
- **Source:** SecurityWeek — https://www.securityweek.com/data-breach-confirmed-after-australian-energy-giant-origin-is-hacked/
- **Severity:** critical
- **Tags:** `data-breach`
- **Summary:** A hacker claims to have stolen the personal information of 2 million Origin Energy customers and is threatening to leak it; Origin has confirmed the breach.

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
