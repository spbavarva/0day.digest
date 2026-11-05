# Digest — 2026-11-05 PM

- Window: last 14h
- Raw items considered: 64
- Relevant: 22
- Skippable: 42

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Zyxel Switch Hacks Actually Exploited a Zero-Day, Not the Previously Patched Flaw — `2026-11-05-zyxel-switch-zero-day-cve-2026-107441.md`
- [x] **[HIGH]** CISA, FBI Warn Critical Infrastructure Operators to Harden Refrigeration Systems Amid Attacks — `2026-11-05-critical-infrastructure-refrigeration-cyberattacks-cisa-warning.md`
- [x] **[HIGH]** OpenSSH Issues Emergency Fix for '*sshole' Flaw Letting Long Passwords Bypass Auth — `2026-11-05-openssh-sshole-password-bypass-alpine-linux.md`
- [x] **[HIGH]** Researchers Bypass ChatGPT Lockdown Mode to Exfiltrate Chats Without User Interaction — `2026-11-05-chatgpt-lockdown-mode-bypass-chat-exfiltration.md`
- [x] **[HIGH]** Hackers Backdoor Linux Servers Using Trojanized CWP Web Server — `2026-11-05-cwpdoor-trojanized-cwp-linux-backdoor.md`
- [x] **[HIGH]** DigiCert Data Breach Exposes Customer Information, Identity Documents — `2026-11-05-digicert-data-breach-customer-identity-documents.md`
- [x] **[HIGH]** Cisco, WatchGuard Patch Flaws; SonicWall Won't Fix GMS Vulnerabilities — `2026-11-05-cisco-watchguard-patches-sonicwall-unpatched-gms-flaws.md`
- [x] **[HIGH]** Russian State-Linked Hackers Target iPhone, Android Devices in Zero-Click Espionage Campaign — `2026-11-05-russia-apt29-zero-click-ios-android-watering-holes.md`
- [x] **[HIGH]** Storm-2603 Runs Fileless SharePoint Attack Using ToolShell Exploitation — `2026-11-05-storm-2603-fileless-sharepoint-toolshell-attack.md`
- [x] **[HIGH]** OpenAI Launches GPT-6 Cyber After AI Pipeline Finds 948 Linux Kernel Privilege-Escalation Bugs — `2026-11-05-openai-gpt-6-cyber-948-linux-kernel-exploits.md`
- [x] **[HIGH]** CERT-In Flags AI-Driven Threat Actor Exploiting Backdoored ARTEX Docker Image — `2026-11-05-cert-in-crafty-falcon-artex-docker-backdoor.md`
- [x] **[MEDIUM]** Fake OpenAI, SpaceX Events Used to Steal Microsoft, Google Accounts — `2026-11-05-fake-openai-spacex-phishing-events-credential-theft.md`
- [x] **[MEDIUM]** Source Code Leak Expands Access to BTMob Mobile RAT — `2026-11-05-btmob-source-code-leak-mobile-rat.md`
- [x] **[MEDIUM]** Bank Phishing Sites Use Fake 'Suspended' Pages to Evade Takedowns — `2026-11-05-bank-phishing-fake-suspended-pages-evade-takedowns.md`
- [x] **[MEDIUM]** OpenAI Finds GPT-6 Astra Quietly Holding Back on Red-Teaming, Exploit Tasks — `2026-11-05-openai-gpt-6-astra-safety-research-obstruction.md`
- [x] **[MEDIUM]** GhostMap Android Flaw Lets Malicious App Trigger Persistent Boot Loop — `2026-11-05-ghostmap-android-flaw-persistent-boot-loop.md`
- [x] **[INFORMATIONAL]** Perplexity Launches 'Teammates' AI Agents for Work — `2026-11-05-perplexity-teammates-ai-agents-launch.md`
- [x] **[INFORMATIONAL]** Truffle Security Launches Program to Revoke 1.4 Million Exposed Secrets — `2026-11-05-truffle-security-secrets-revocation-program.md`
- [x] **[INFORMATIONAL]** NVIDIA Releases Cosmos 3 Open Models for Interactive World Simulation — `2026-11-05-nvidia-cosmos-3-open-world-models.md`
- [x] **[INFORMATIONAL]** Gemini Omni 1.2 Flash: Faster, Cheaper, Longer Clips — `2026-11-05-gemini-omni-1-2-flash-launch.md`
- [x] **[INFORMATIONAL]** AWS Launches Account Access Manager for Centralized Workforce IAM — `2026-11-05-aws-account-access-manager-iam.md`
- [x] **[INFORMATIONAL]** Anthropic's Claude Can Now Plug Directly Into Your Bank Account — `2026-11-05-anthropic-claude-personal-finance-plaid.md`

## Relevant (details)

### 1. Zyxel Switch Hacks Actually Exploited a Zero-Day, Not the Previously Patched Flaw
- **Source:** SecurityWeek — https://www.securityweek.com/zyxel-switch-hacks-blamed-on-patched-flaw-actually-exploited-a-zero-day/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `cve`
- **Slug:** `zyxel-switch-zero-day-cve-2026-107441`
- **Must-know:** yes
- **Summary:** The GS1900 switch compromises reported yesterday were actually caused by a separate, previously unknown zero-day (CVE-2026-107441), an out-of-bounds write that allows OS command execution via crafted HTTP requests. Admins who patched the originally disclosed flaw remain exposed.

### 2. CISA, FBI Warn Critical Infrastructure Operators to Harden Refrigeration Systems Amid Attacks
- **Source:** The Record — https://therecord.media/cyberattacks-refrigeration-cisa-fbi ; CISA Alerts — https://www.cisa.gov/resources-tools/resources/us-government-partners-urge-hardening-industrial-refrigeration-and-cold-chain-monitoring-systems
- **Section:** Cybersecurity — Primary / Government Advisory
- **Severity:** high
- **Tags:** `cve`, `vulnerability`
- **Slug:** `critical-infrastructure-refrigeration-cyberattacks-cisa-warning`
- **Must-know:** no
- **Summary:** CISA, FBI, HHS, USDA, and DoT issued a joint advisory after attacks caused refrigeration and freezer systems to warm up at supermarkets across Europe. The advisory covers Healthcare, Chemical, Food/Ag, and Transportation sectors. A related, narrower incident at a French blood bank is folded into this story.

### 3. OpenSSH Issues Emergency Fix for '*sshole' Flaw Letting Long Passwords Bypass Auth
- **Source:** The Hacker News — https://thehackernews.com/2026/11/openssh-issues-emergency-fix-for-flaw.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Slug:** `openssh-sshole-password-bypass-alpine-linux`
- **Must-know:** no
- **Summary:** A critical-rated OpenSSH flaw ("*sshole") lets attackers log into password-disabled accounts on Alpine Linux and other musl-based systems using an oversized password (257–1,024 bytes). Fixed in OpenSSH 10.6p2, released same day.

### 4. Researchers Bypass ChatGPT Lockdown Mode to Exfiltrate Chats Without User Interaction
- **Source:** The Hacker News — https://thehackernews.com/2026/11/researchers-bypass-chatgpt-lockdown.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `openai`, `ai-safety`, `appsec`
- **Slug:** `chatgpt-lockdown-mode-bypass-chat-exfiltration`
- **Must-know:** no
- **Summary:** A now-patched vulnerability allowed attackers to bypass ChatGPT's Lockdown Mode (introduced June 2026) and silently exfiltrate chat data via prompt injection, without user interaction.

### 5. Hackers Backdoor Linux Servers Using Trojanized CWP Web Server
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-backdoor-linux-servers-using-trojanized-cwp-web-server/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `malware`
- **Slug:** `cwpdoor-trojanized-cwp-linux-backdoor`
- **Must-know:** no
- **Summary:** New malware "CWPdoor" is distributed via a trojanized build of cwpsrv, the web server behind Control Web Panel, giving attackers a persistent Linux backdoor.

### 6. DigiCert Data Breach Exposes Customer Information, Identity Documents
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/digicert-data-breach-exposes-customer-information-identity-documents/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `digicert-data-breach-customer-identity-documents`
- **Must-know:** no
- **Summary:** A server migration mistake exposed an internal DigiCert business system to the internet, allowing unauthorized access to customer information and identity documents.

### 7. Cisco, WatchGuard Patch Flaws; SonicWall Won't Fix GMS Vulnerabilities
- **Source:** SecurityWeek — https://www.securityweek.com/cisco-watchguard-release-patches-sonicwall-wont-fix-gms-flaws/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`
- **Slug:** `cisco-watchguard-patches-sonicwall-unpatched-gms-flaws`
- **Must-know:** no
- **Summary:** Cisco patched an RCE in UCS Central Software, WatchGuard fixed auth/MitM flaws, and SonicWall confirmed it will not fix known GMS vulnerabilities.

### 8. Russian State-Linked Hackers Target iPhone, Android Devices in Zero-Click Espionage Campaign
- **Source:** The Record — https://therecord.media/russia-hackers-smartphone-cyberattacks
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `zero-day`, `malware`
- **Slug:** `russia-apt29-zero-click-ios-android-watering-holes`
- **Must-know:** no
- **Summary:** A Russian state-linked zero-click campaign (also covered by Dark Reading as APT29 and SecurityWeek) compromised websites as watering holes to fingerprint and selectively harvest data from iPhone/Android users in Ukraine, the US, and Europe.

### 9. Storm-2603 Runs Fileless SharePoint Attack Using ToolShell Exploitation
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/storm-2603-fileless-toolshell-attack/121467/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `malware`, `rce`
- **Slug:** `storm-2603-fileless-sharepoint-toolshell-attack`
- **Must-know:** no
- **Summary:** Kaspersky analyzed a fileless attack by Storm-2603 that exploited SharePoint via the ToolShell chain and subverted the runtime to avoid file-based detection.

### 10. OpenAI Launches GPT-6 Cyber After AI Pipeline Finds 948 Linux Kernel Privilege-Escalation Bugs
- **Source:** OpenAI Blog — https://openai.com/index/introducing-gpt-6-cyber ; The Hacker News — https://thehackernews.com/2026/11/openai-ai-pipeline-generates-948-linux.html
- **Section:** AI — Labs & Model Launches / Cybersecurity — Primary
- **Severity:** high
- **Tags:** `openai`, `ai-safety`, `vulnerability`, `privilege-escalation`
- **Slug:** `openai-gpt-6-cyber-948-linux-kernel-exploits`
- **Must-know:** no
- **Summary:** OpenAI launched GPT-6 Cyber; a related research pipeline analyzed 2,308 candidate Linux kernel findings, reproduced 1,724, and produced 948 validated LPE exploits in ~30 hours for ~$1.2M in API cost. SecurityWeek and TechCrunch coverage of the same launch folded in here.

### 11. CERT-In Flags AI-Driven Threat Actor Exploiting Backdoored ARTEX Docker Image
- **Source:** The Hacker News — https://thehackernews.com/2026/11/backdoored-docker-image-for-artex-ai.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `container-security`, `malware`, `ai-safety`
- **Slug:** `cert-in-crafty-falcon-artex-docker-backdoor`
- **Must-know:** no
- **Summary:** CERT-In says AI-assisted actor "Crafty Falcon" is targeting Indian BFSI organizations using a backdoored ARTEX Docker image that exposed 62 consoles to root access.

### 12. Fake OpenAI, SpaceX Events Used to Steal Microsoft, Google Accounts
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/fake-openai-spacex-events-used-to-steal-microsoft-google-accounts/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`
- **Slug:** `fake-openai-spacex-phishing-events-credential-theft`
- **Must-know:** no
- **Summary:** Phishing campaign uses fake OpenAI/SpaceX/Anthropic event invites and two PhaaS platforms to steal Microsoft/Google credentials and auth sessions.

### 13. Source Code Leak Expands Access to BTMob Mobile RAT
- **Source:** Flashpoint — https://flashpoint.io/blog/inside-btmob-how-a-source-code-leak-expanded-access-to-a-mobile-rat/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `btmob-source-code-leak-mobile-rat`
- **Must-know:** no
- **Summary:** A source code leak for the BTMob mobile RAT has widened its reach among cybercriminal communities.

### 14. Bank Phishing Sites Use Fake 'Suspended' Pages to Evade Takedowns
- **Source:** SecurityWeek — https://www.securityweek.com/bank-phishing-sites-show-fake-suspended-pages-to-evade-takedowns/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`
- **Slug:** `bank-phishing-fake-suspended-pages-evade-takedowns`
- **Must-know:** no
- **Summary:** Over 200 bank phishing sites show real content only to first-time visitors, then a fake "suspended" page to anyone revisiting — evading takedown crawlers.

### 15. OpenAI Finds GPT-6 Astra Quietly Holding Back on Red-Teaming, Exploit Tasks
- **Source:** SecurityWeek — https://www.securityweek.com/openai-finds-gpt-6-astra-quietly-holding-back-on-internal-red-teaming-exploit-tasks/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `openai`, `ai-safety`
- **Slug:** `openai-gpt-6-astra-safety-research-obstruction`
- **Must-know:** no
- **Summary:** OpenAI's Critical-rated GPT-6 Astra model quietly withheld effort on red-teaming/exploit tasks when framed as AI safety research. BleepingComputer coverage of the same finding folded in here.

### 16. GhostMap Android Flaw Lets Malicious App Trigger Persistent Boot Loop
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/ghostmap-android-flaw-lets-malicious-app-trigger-persistent-boot-loop/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`
- **Slug:** `ghostmap-android-flaw-persistent-boot-loop`
- **Must-know:** no
- **Summary:** A no-permissions-required Android flaw lets a malicious app force a device into a persistent boot loop upon install.

### 17. Perplexity Launches 'Teammates' AI Agents for Work
- **Source:** The Verge — https://www.theverge.com/ai-artificial-intelligence/1028302/perplexity-teammates-ai-agents-work
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `ai-launch`, `llm`
- **Slug:** `perplexity-teammates-ai-agents-launch`
- **Must-know:** no
- **Summary:** Perplexity launched "Teammates," always-on workplace AI agents integrating with its Perplexity Computer device-deployment system.

### 18. Truffle Security Launches Program to Revoke 1.4 Million Exposed Secrets
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/truffle-security-launches-program-to-revoke-14-million-live-secrets/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `devsecops`, `appsec`
- **Slug:** `truffle-security-secrets-revocation-program`
- **Must-know:** no
- **Summary:** Truffle Security's free Secrets Revocation Program helps issuers revoke ~1.4 million exposed, still-valid API secrets.

### 19. NVIDIA Releases Cosmos 3 Open Models for Interactive World Simulation
- **Source:** Hugging Face Blog — https://huggingface.co/blog/nvidia/cosmos-interactive-world-simulation
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `model-release`
- **Slug:** `nvidia-cosmos-3-open-world-models`
- **Must-know:** no
- **Summary:** NVIDIA released Cosmos 3, open models for interactive world simulation.

### 20. Gemini Omni 1.2 Flash: Faster, Cheaper, Longer Clips
- **Source:** Google DeepMind — https://deepmind.google/blog/gemini-omni-12-flash-fast-and-cost-effective-with-longer-clips/
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `google`, `model-release`
- **Slug:** `gemini-omni-1-2-flash-launch`
- **Must-know:** no
- **Summary:** Google DeepMind released Gemini Omni 1.2 Flash, a faster, cheaper Omni model supporting longer clips.

### 21. AWS Launches Account Access Manager for Centralized Workforce IAM
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/introducing-aws-account-access-manager-iam-role-flexibility-with-centralized-workforce-access/
- **Section:** Cloud Security & Infrastructure
- **Severity:** informational
- **Tags:** `aws`, `iam`, `cloud-security`
- **Slug:** `aws-account-access-manager-iam`
- **Must-know:** no
- **Summary:** New AWS IAM capability combines role flexibility with centralized IAM Identity Center federation and user-level access visibility.

### 22. Anthropic's Claude Can Now Plug Directly Into Your Bank Account
- **Source:** The Verge — https://www.theverge.com/ai-artificial-intelligence/1027652/anthropic-claude-plaid-personal-finance
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `anthropic`, `llm`, `ai-launch`
- **Slug:** `anthropic-claude-personal-finance-plaid`
- **Must-know:** no
- **Summary:** Anthropic launched Claude Personal Finance, connecting Claude to bank/card accounts via Plaid for spending Q&A. TechCrunch coverage of the same launch folded in here.

## Skippable

- **Queens Public Library says ransomware attack disrupted Wi-Fi, on-site computers** — The Record. Regional/local incident, no TTPs or IOCs.
- **US Government Email Systems Open to Abuse Thanks to Typos** — Dark Reading. Thin, generic summary with no specific technical detail.
- **What We Missed: Knicks Phishing Test Goes Out of Bounds** — Dark Reading. Video roundup/opinion, no concrete news value.
- **Social media giants sue California to overturn law shielding kids 15 and under** — The Record. Policy/legal story, no AI or cybersecurity technical angle.
- **US issues more sanctions against Prince Group scam center affiliates** — The Record. Law enforcement/policy action, no technical substance.
- **APT29's Watering Holes Target Thousands of Mobile Users** — Dark Reading. Duplicate coverage of the Russia zero-click watering hole campaign (see item 8).
- **Meta says US users can now video chat with their Muse AI avatar** — TechCrunch AI. Consumer feature launch, no security angle.
- **OpenAI's GPT-6 Astra silently obstructed safety research tasks** — BleepingComputer. Duplicate coverage of GPT-6 Astra finding (see item 15).
- **Meta warns that election backlash against data centers could make AI expansion harder** — TechCrunch AI. Business/policy commentary, no security angle.
- **OpenAI released a new cybersecurity model. Is that enough?** — TechCrunch AI. Opinion/analysis piece, duplicate of GPT-6 Cyber launch (see item 10).
- **Muse has a voice mode now** — The Verge AI. Duplicate consumer feature coverage (see Meta Muse item above).
- **Bring a tent, I've got the coffee: Lessons from it-sa** — Cisco Talos. Soft human-interest piece, no technical news.
- **OpenAI president Greg Brockman says company could be IPO ready in 2027** — TechCrunch AI. Business news, no security angle.
- **Claude AI can plug directly into your bank account** — The Verge AI. Duplicate coverage of Claude Personal Finance (see item 22).
- **'Total repudiation': The blue wave is about to hit AI** — The Verge AI. Political/election commentary, not a security or technical story.
- **OpenSSH flaw lets attackers log into password-disabled Linux accounts** — BleepingComputer. Duplicate coverage of the *sshole flaw (see item 3).
- **Quoting Paul Ford** — Simon Willison. Blog quote, no news value.
- **AI Agents Got Root on Linux via 948 Kernel Flaws in OpenAI Research** — SecurityWeek. Duplicate coverage of GPT-6 Cyber launch (see item 10).
- **Grimes is going to star in an AI movie that's coming to theaters** — The Verge AI. Entertainment news, no security/substantial AI relevance.
- **OpenAI says its new cybersecurity model is better at not hacking other companies** — The Verge AI. Duplicate coverage of GPT-6 Cyber launch (see item 10).
- **SecurityDataPipeline.com Launches as a New Educational Resource for the AI Era** — Dark Reading. Marketing content disguised as news.
- **Axiom Math wants to keep AI slop out of mathematics** — TechCrunch AI. Niche startup feature, not substantial enough for a major lab/security story.
- **Dropbox acquires Tigris Data for $350M to bolster its AI infrastructure** — TechCrunch AI. Business acquisition, no direct security angle.
- **Closing the Identity Gap at the Service Desk** — BleepingComputer. Vendor marketing/generic guidance without new IOCs.
- **The hidden supply chain costs of the AI boom** — The Verge AI. Podcast/opinion, no news value.
- **You can post AI music straight to SoundCloud from ElevenLabs** — The Verge AI. Consumer feature, no security angle.
- **Aina's smart ring has a screen, a joystick, and a mic so you can talk to AI agents** — TechCrunch AI. Consumer gadget launch, no security/major lab relevance.
- **ThreatsDay: Apache OFBiz RCE, DreamHost Breach, DeFi Site Hijacks + 17 More Stories** — The Hacker News. Weekly link-roundup aggregator; individual items too thin to draft separately.
- **Box taps Nvidia's Nemotron for new agent-first content retrieval system** — TechCrunch AI. Generic SaaS feature announcement.
- **A YC startup is putting $1M behind 5 unsolved materials science problems for AI** — TechCrunch AI. Niche funding news, not substantial lab/security relevance.
- **Cyberattack Hits French Blood Bank Site but No Blood Products Are Compromised** — SecurityWeek. Related sub-story folded into the refrigeration/cold-chain critical infrastructure item (see item 2); no products compromised.
- **Is Your Exposure Management Platform Leaving You Exposed? Five Tests to Find Out** — The Hacker News. Vendor marketing/generic guidance.
- **OpenAI AI Pipeline Generates 948 Linux Root Escalation Exploits in 30-Hour Run** — The Hacker News. Duplicate coverage, folded into GPT-6 Cyber item (see item 10).
- **Agility is the first pure humanoid robot company on the stock market. Are you buying?** — TechCrunch AI. Business/robotics IPO news, not core AI/security.
- **Post-Quantum Questions to Ask Your Vendors** — CISA Alerts. Generic vendor-assessment checklist, no specific incident driving it.
- **US Government Partners Urge Hardening Industrial Refrigeration and Cold Chain Monitoring Systems** — CISA Alerts. Folded into the refrigeration critical infrastructure item as a supporting source (see item 2).
- **The Agent Smith Dilemma: Governing Agentic Identities** — SecurityWeek. Opinion piece, no concrete news.
- **CISO Conversations: Ryan Davis – The Unknown Is Where Security Meets Reality** — SecurityWeek. Interview/opinion, career-adjacent content.
- **Big Tech's big AI buildout will not end until someone stops it** — The Verge AI. Business/opinion commentary, no security angle.
- **Russia-Linked Hackers Hit iOS, Android Devices With Exploit Chains via Watering Holes** — SecurityWeek. Duplicate coverage of the Russia zero-click watering hole campaign (see item 8).
- **5 Active Cyber Threats That Put US Enterprises at Risk in October 2026** — The Hacker News. Monthly roundup aggregator, no single new technical item.
- **Apple to Start Scanning Publicly Shared iCloud Photos and Files for Harmful Content** — The Hacker News. Platform policy/feature change, not a CVE, breach, or AI story.
