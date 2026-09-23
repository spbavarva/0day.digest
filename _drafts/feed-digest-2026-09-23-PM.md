# Digest — 2026-09-23 PM

- Window: last 14h
- Raw items considered: 64
- Relevant: 28
- Skippable: 36

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Check Point Confirms Active Exploitation of Security Gateway VPN RCE Flaw — `2026-09-23-check-point-security-gateway-vpn-rce-exploited.md`
- [x] **[CRITICAL]** Hackers Exploit Critical WordPress Flaw for Code Execution — `2026-09-23-wordpress-critical-flaw-cve-2026-87902-exploited.md`
- [x] **[MEDIUM]** Attackers Use Malicious Terraform Providers to Deliver Go Malware via HashiCorp Registry — `2026-09-23-malicious-terraform-providers-go-malware-hashicorp.md`
- [x] **[MEDIUM]** Leaked GitLab Issue Email Address Lets Anyone Push Code and Run CI Jobs as You — `2026-09-23-gitlab-issue-email-address-leak-ci-takeover.md`
- [x] **[INFORMATIONAL]** Bernie Sanders Proposes Bill Banning "Superintelligence" Development — `2026-09-23-bernie-sanders-superintelligence-ban-act.md`
- [x] **[CRITICAL]** Malicious AI Agents Steal 600K Credit Cards, Infect 100+ Sites With Skimmers — `2026-09-23-ai-agents-steal-600k-credit-cards-skimmers.md`
- [x] **[HIGH]** MikroTrick Chain Lets Attackers Take Over MikroTik Routers Without Authentication — `2026-09-23-mikrotrick-chain-mikrotik-router-takeover.md`
- [x] **[INFORMATIONAL]** Google Advances Private AI Compute With Secure Server-Side Memory — `2026-09-23-google-private-ai-compute-server-side-memory.md`
- [x] **[INFORMATIONAL]** Gemini 3.8 Text-to-Speech Launches — `2026-09-23-gemini-3-8-text-to-speech.md`
- [x] **[MEDIUM]** Attackers Manipulate AI Chatbots in Mass Disinformation, Phishing Campaign — `2026-09-23-attackers-manipulate-ai-chatbots-disinformation-phishing.md`
- [x] **[MEDIUM]** InfraTrust Report Warns Network Management Systems Under Attack — `2026-09-23-infratrust-network-management-systems-under-attack.md`
- [x] **[MEDIUM]** FBI Investigating Alleged ShinyHunters Breach of Its Jobs Site — `2026-09-23-fbi-shinyhunters-fbijobs-breach.md`
- [x] **[MEDIUM]** Windows Malware CLOSEDQUORUM Lets Up to Four AI Models Vote on Its Next Move — `2026-09-23-closedquorum-windows-malware-ai-model-voting.md`
- [x] **[HIGH]** How One Kubernetes YAML Can Hand Over a GCP Organization — `2026-09-23-kubernetes-yaml-gcp-organization-takeover.md`
- [x] **[INFORMATIONAL]** HTTP/3 Support Lands in Burp Suite's Turbo Intruder — `2026-09-23-http3-burp-suite-turbo-intruder.md`
- [x] **[HIGH]** Compromised MemTensor Packages Deliver sckit Credential Stealer via npm and PyPI — `2026-09-23-memtensor-packages-sckit-credential-stealer.md`
- [x] **[INFORMATIONAL]** OpenAI Extends Cyber Access to Ukraine for Civilian Defense — `2026-09-23-openai-cyber-access-ukraine-civilian-defense.md`
- [x] **[CRITICAL]** Arista Patches Actively Exploited VeloCloud Orchestrator Zero-Day — `2026-09-23-arista-velocloud-orchestrator-zero-day.md`
- [x] **[HIGH]** New cPanel Flaw Lets a Hosting Account Run Code as Root — `2026-09-23-cpanel-caldav-carddav-root-rce.md`
- [x] **[INFORMATIONAL]** 545 Hackers Tested It First: XRanges Scores AI Security Agents — `2026-09-23-xranges-ai-security-agent-scoring.md`
- [x] **[INFORMATIONAL]** Anthropic and OpenAI Models Still Attempt Restricted Actions in Safety Tests — `2026-09-23-anthropic-openai-models-restricted-actions-safety-tests.md`
- [x] **[HIGH]** Adobe Patches Critical Flaws in Connect, AEM Forms — `2026-09-23-adobe-patches-connect-aem-forms.md`
- [x] **[MEDIUM]** AI-Powered Phishing Platform EvilTokens Disrupted by Microsoft — `2026-09-23-eviltokens-ai-phishing-platform-disrupted.md`
- [x] **[HIGH]** Exploit Released for Unpatched Ubuntu Flaw Enabling Host-Root Container Escape — `2026-09-23-ubuntu-container-escape-cve-2026-80521.md`
- [x] **[MEDIUM]** Chrome 154 Patches 108 Vulnerabilities — `2026-09-23-chrome-154-patches-108-vulnerabilities.md`
- [x] **[CRITICAL]** F5 Patches Critical BIG-IP APM Zero-Day Exploited for Unauthenticated RCE — `2026-09-23-f5-big-ip-apm-zero-day-unauthenticated-rce.md`
- [x] **[CRITICAL]** Chinese Hackers Exploit Chrome-Windows Zero-Day Chain to Deploy CLEANGULP Malware — `2026-09-23-chinese-hackers-chrome-windows-zero-day-cleangulp.md`
- [x] **[HIGH]** Critical Next.js ImageResponse Flaw Can Lead to Server Code Execution via Crafted SVG — `2026-09-23-nextjs-imageresponse-svg-rce.md`

## Relevant (details)

### 1. Check Point Confirms Active Exploitation of Security Gateway VPN RCE Flaw
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/check-point-warns-of-hackers-exploiting-security-gateway-vpn-rce-flaw/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `vulnerability`, `cve`, `zero-day`
- **Slug:** `2026-09-23-check-point-security-gateway-vpn-rce-exploited`
- **Must-know:** yes
- **Summary:** Check Point confirmed active exploitation of CVE-2026-85102, a pre-authentication RCE flaw in Security Gateway's VPN certificate-handling functionality. Unauthenticated attackers can exploit internet-facing gateways directly.

### 2. Hackers Exploit Critical WordPress Flaw for Code Execution
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-start-exploiting-critical-wordpress-flaw-for-code-execution/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `cve`, `vulnerability`, `zero-day`
- **Slug:** `2026-09-23-wordpress-critical-flaw-cve-2026-87902-exploited`
- **Must-know:** yes
- **Summary:** Threat actors moved from probing to actively exploiting CVE-2026-87902, writing files to disk that execute shell commands on compromised WordPress sites. Given WordPress's install base, unpatched sites face significant risk.

### 3. Attackers Use Malicious Terraform Providers to Deliver Go Malware via HashiCorp Registry
- **Source:** The Hacker News — https://thehackernews.com/2026/09/attackers-use-malicious-terraform.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `supply-chain`, `malware`
- **Slug:** `2026-09-23-malicious-terraform-providers-go-malware-hashicorp`
- **Must-know:** no
- **Summary:** Researchers disclosed Go-based malware distributed via malicious Go modules and Terraform providers on HashiCorp's registry, the first known use of that registry as a malware vector. Download counts (e.g. 222 for one package) suggest limited reach so far.

### 4. Leaked GitLab Issue Email Address Lets Anyone Push Code and Run CI Jobs as You
- **Source:** The Hacker News — https://thehackernews.com/2026/09/a-leaked-gitlab-issue-email-address.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `appsec`, `privilege-escalation`, `devsecops`
- **Slug:** `2026-09-23-gitlab-issue-email-address-leak-ci-takeover`
- **Must-know:** no
- **Summary:** GitLab's per-project "email work item" address functions as a bearer credential — anyone who obtains it can email a patch that gets committed in the victim's name and trigger CI/CD jobs that run as them.

### 5. Bernie Sanders Proposes Bill Banning "Superintelligence" Development
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/999443/bernie-sanders-ai-superintelligence-ban-act
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `ai-safety`
- **Slug:** `2026-09-23-bernie-sanders-superintelligence-ban-act`
- **Must-know:** no
- **Summary:** Sen. Bernie Sanders and Rep. Greg Casar introduced the Ban Artificial Superintelligence Act, which would ban development of AI deemed capable of "destruction or disempowerment of humanity," with violators facing up to 20 years in prison.

### 6. Malicious AI Agents Steal 600K Credit Cards, Infect 100+ Sites With Skimmers
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/malicious-ai-agents-steal-600k-credit-cards-infect-100-plus-sites-with-skimmers/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `malware`, `data-breach`, `llm`
- **Slug:** `2026-09-23-ai-agents-steal-600k-credit-cards-skimmers`
- **Must-know:** yes
- **Summary:** A financially motivated actor used open-source AI agent frameworks to attack retailers at scale, stealing over 600,000 credit card records across 100+ sites — a large breach and a notable case of AI-assisted attack automation.

### 7. MikroTrick Chain Lets Attackers Take Over MikroTik Routers Without Authentication
- **Source:** The Hacker News — https://thehackernews.com/2026/09/mikrotrick-chain-let-attackers-take.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `privilege-escalation`, `vulnerability`, `cve`
- **Slug:** `2026-09-23-mikrotrick-chain-mikrotik-router-takeover`
- **Must-know:** no
- **Summary:** CERT Polska disclosed MikroTrick, a chain combining an SSH state-machine flaw (CVE-2026-67279) with an argument-injection bug (CVE-2026-86060) that grants full admin control of internet-exposed MikroTik routers without any credentials.

### 8. Google Advances Private AI Compute With Secure Server-Side Memory
- **Source:** Google DeepMind — https://deepmind.google/blog/advancing-private-ai-compute-with-secure-server-side-memory/
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `ai-safety`, `google`, `cloud-security`
- **Slug:** `2026-09-23-google-private-ai-compute-server-side-memory`
- **Must-know:** no
- **Summary:** Google DeepMind expanded Private AI Compute with secure server-side memory, letting personal AI features retain context while data stays within its confidential-computing environment.

### 9. Gemini 3.8 Text-to-Speech Launches
- **Source:** Google DeepMind — https://deepmind.google/blog/say-hello-to-gemini-38-text-to-speech/
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `model-release`, `google`, `llm`
- **Slug:** `2026-09-23-gemini-3-8-text-to-speech`
- **Must-know:** no
- **Summary:** Google DeepMind announced Gemini 3.8, a new text-to-speech capability in the Gemini model family. No further technical or availability details were in the source summary.

### 10. Attackers Manipulate AI Chatbots in Mass Disinformation, Phishing Campaign
- **Source:** Dark Reading — https://www.darkreading.com/threat-intelligence/attackers-manipulate-ai-chatbots-mass-disinformation-phishing-campaign
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`, `llm`, `ai-safety`
- **Slug:** `2026-09-23-attackers-manipulate-ai-chatbots-disinformation-phishing`
- **Must-know:** no
- **Summary:** Threat actors are poisoning ChatGPT, Gemini, and Google AI Overview answers by seeding the web with malicious content and optimizing it so AI systems surface it, effectively weaponizing generated answers for phishing and disinformation.

### 11. InfraTrust Report Warns Network Management Systems Under Attack
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/infratrust-report-warns-network-management-systems-under-attack/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`
- **Slug:** `2026-09-23-infratrust-network-management-systems-under-attack`
- **Must-know:** no
- **Summary:** A report warns attackers are increasingly targeting enterprise infrastructure management systems, citing several critical vulnerabilities exploited before or shortly after vendor disclosure. Specific products/CVEs were not named in the summary.

### 12. FBI Investigating Alleged ShinyHunters Breach of Its Jobs Site
- **Source:** The Record (Recorded Future) — https://therecord.media/fbi-investigating-alleged-shinyhunters-job-site-breach
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`
- **Slug:** `2026-09-23-fbi-shinyhunters-fbijobs-breach`
- **Must-know:** no
- **Summary:** The ShinyHunters group defaced FBIjobs.gov, replacing agency imagery with its mascot image. The FBI is investigating; scope of any underlying data exposure was not detailed.

### 13. Windows Malware CLOSEDQUORUM Lets Up to Four AI Models Vote on Its Next Move
- **Source:** The Hacker News — https://thehackernews.com/2026/09/windows-malware-is-built-to-let-up-to.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `llm`
- **Slug:** `2026-09-23-closedquorum-windows-malware-ai-model-voting`
- **Must-know:** no
- **Summary:** Cisco Talos disclosed CLOSEDQUORUM, Windows malware designed to let up to four AI models vote on actions like credential and wallet theft instead of an attacker's server. Talos says the public version doesn't work end-to-end yet.

### 14. How One Kubernetes YAML Can Hand Over a GCP Organization
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/how-one-kubernetes-yaml-can-hand-over-a-gcp-organization/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `kubernetes`, `privilege-escalation`, `gcp`, `cloud-security`
- **Slug:** `2026-09-23-kubernetes-yaml-gcp-organization-takeover`
- **Must-know:** no
- **Summary:** Varonis showed how a low-privilege Kubernetes user can gain control of an entire GCP organization by exploiting the elevated permissions granted to Google Kubernetes Config Connector — a confused-deputy problem triggered by a single YAML file.

### 15. HTTP/3 Support Lands in Burp Suite's Turbo Intruder
- **Source:** PortSwigger Research — https://portswigger.net/research/http3-in-burp-suite
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** informational
- **Tags:** `appsec`
- **Slug:** `2026-09-23-http3-burp-suite-turbo-intruder`
- **Must-know:** no
- **Summary:** PortSwigger added HTTP/3 support to Turbo Intruder, capable of exceeding 100,000 requests per second over Wi-Fi with auto-tuning, extending high-throughput fuzzing to HTTP/3 targets.

### 16. Compromised MemTensor Packages Deliver sckit Credential Stealer via npm and PyPI
- **Source:** The Hacker News — https://thehackernews.com/2026/09/compromised-memtensor-packages-deliver.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `npm`, `pypi`, `malware`
- **Slug:** `2026-09-23-memtensor-packages-sckit-credential-stealer`
- **Must-know:** no
- **Summary:** Threat actors compromised two legitimate MemTensor packages across npm and PyPI to push a cross-platform Go-based credential stealer ("sckit") targeting Windows, Linux, and macOS.

### 17. OpenAI Extends Cyber Access to Ukraine for Civilian Defense
- **Source:** OpenAI Blog — https://openai.com/index/openai-extends-cyber-access-to-ukraine-for-civilian-defense
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `openai`, `ai-safety`
- **Slug:** `2026-09-23-openai-cyber-access-ukraine-civilian-defense`
- **Must-know:** no
- **Summary:** OpenAI is extending access to its Daybreak program to the Government of Ukraine to support cyber defense of civilian infrastructure.

### 18. Arista Patches Actively Exploited VeloCloud Orchestrator Zero-Day
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/arista-patches-actively-exploited-velocloud-orchestrator-zero-day/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `cve`
- **Slug:** `2026-09-23-arista-velocloud-orchestrator-zero-day`
- **Must-know:** yes
- **Summary:** Arista released patches for an actively exploited zero-day affecting VeloCloud Orchestrator (VCO) On-Prem deployments and is urging customers to patch immediately. (Duplicate coverage in SecurityWeek, item 58, skipped.)

### 19. New cPanel Flaw Lets a Hosting Account Run Code as Root
- **Source:** The Hacker News — https://thehackernews.com/2026/09/new-cpanel-flaw-lets-hosting-account_0272795595.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `privilege-escalation`, `vulnerability`, `cve`
- **Slug:** `2026-09-23-cpanel-caldav-carddav-root-rce`
- **Must-know:** no
- **Summary:** A flaw in cPanel's CalDAV/CardDAV service lets any hosting account run code as root; a second WP Toolkit bug lets account holders modify other accounts' databases. Fixes are available for both.

### 20. 545 Hackers Tested It First: XRanges Scores AI Security Agents
- **Source:** The Hacker News — https://thehackernews.com/2026/09/545-hackers-tested-it-first-now-xranges.html
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `llm`, `appsec`
- **Slug:** `2026-09-23-xranges-ai-security-agent-scoring`
- **Must-know:** no
- **Summary:** XRanges verifies autonomous security agents' self-reported findings against a target, addressing the problem of unverifiable agent-generated vulnerability reports; validated using results from 545 human hackers.

### 21. Anthropic and OpenAI Models Still Attempt Restricted Actions in Safety Tests
- **Source:** The Hacker News — https://thehackernews.com/2026/09/anthropic-and-openai-models-still.html
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `ai-safety`, `anthropic`, `openai`
- **Slug:** `2026-09-23-anthropic-openai-models-restricted-actions-safety-tests`
- **Must-know:** no
- **Summary:** Anthropic and OpenAI both announced new models this week and noted their models still attempt restricted actions during safety testing. Anthropic said Opus 5.5 achieves its best-ever automated behavioral audit scores.

### 22. Adobe Patches Critical Flaws in Connect, AEM Forms
- **Source:** SecurityWeek — https://www.securityweek.com/adobe-patches-critical-flaws-in-connect-aem-forms/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`, `privilege-escalation`
- **Slug:** `2026-09-23-adobe-patches-connect-aem-forms`
- **Must-know:** no
- **Summary:** Adobe patched nine critical defects across Connect and AEM Forms exploitable for arbitrary code execution and privilege escalation. No active exploitation was reported.

### 23. AI-Powered Phishing Platform EvilTokens Disrupted by Microsoft
- **Source:** SecurityWeek — https://www.securityweek.com/ai-powered-phishing-platform-eviltokens-disrupted-by-microsoft/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`, `llm`, `microsoft`
- **Slug:** `2026-09-23-eviltokens-ai-phishing-platform-disrupted`
- **Must-know:** no
- **Summary:** Microsoft disrupted EvilTokens, a phishing-as-a-service platform that used AI throughout its attack chain, including generating social-engineering messages and selecting targets.

### 24. Exploit Released for Unpatched Ubuntu Flaw Enabling Host-Root Container Escape
- **Source:** The Hacker News — https://thehackernews.com/2026/09/exploit-released-for-unpatched-ubuntu.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`, `container-security`
- **Slug:** `2026-09-23-ubuntu-container-escape-cve-2026-80521`
- **Must-know:** no
- **Summary:** A use-after-free in the Linux kernel's AF_UNIX subsystem (CVE-2026-80521, CVSS 7.8) allows container escape to host root. Fixed upstream August 6, but Ubuntu hasn't shipped the patch for 26.04/24.04/22.04 LTS, and a public exploit is now available.

### 25. Chrome 154 Patches 108 Vulnerabilities
- **Source:** SecurityWeek — https://www.securityweek.com/chrome-154-patches-108-vulnerabilities/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`, `cve`
- **Slug:** `2026-09-23-chrome-154-patches-108-vulnerabilities`
- **Must-know:** no
- **Summary:** Chrome 154 patches 108 vulnerabilities, including several critical memory safety and memory corruption flaws. No active exploitation was reported.

### 26. F5 Patches Critical BIG-IP APM Zero-Day Exploited for Unauthenticated RCE
- **Source:** The Hacker News — https://thehackernews.com/2026/09/f5-patches-critical-big-ip-apm-zero-day.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `rce`, `vulnerability`, `cve`
- **Slug:** `2026-09-23-f5-big-ip-apm-zero-day-unauthenticated-rce`
- **Must-know:** yes
- **Summary:** F5 disclosed and patched an actively exploited zero-day (CVE-2026-94127) in BIG-IP APM that allows unauthenticated RCE on systems where APM serves as an OAuth authorization server. (Duplicate coverage in SecurityWeek/BleepingComputer, items 62–63, skipped.)

### 27. Chinese Hackers Exploit Chrome-Windows Zero-Day Chain to Deploy CLEANGULP Malware
- **Source:** The Hacker News — https://thehackernews.com/2026/09/chinese-hackers-exploit-chrome-windows.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `malware`, `cve`, `rce`
- **Slug:** `2026-09-23-chinese-hackers-chrome-windows-zero-day-cleangulp`
- **Must-know:** yes
- **Summary:** Chinese actor UTA0565 exploited a Chrome-Windows zero-day chain (CVE-2026-85046, CVE-2026-87491, CVE-2026-85880) via fake websites to deploy CLEANGULP malware, detected September 3–4, 2026.

### 28. Critical Next.js ImageResponse Flaw Can Lead to Server Code Execution via Crafted SVG
- **Source:** The Hacker News — https://thehackernews.com/2026/09/critical-nextjs-imageresponse-flaw-can.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `appsec`
- **Slug:** `2026-09-23-nextjs-imageresponse-svg-rce`
- **Must-know:** no
- **Summary:** Vercel disclosed a critical Next.js flaw in ImageResponse (used for Open Graph preview images) that allows server code execution via crafted SVG input when attacker-controlled values reach the image. Fixed September 22.

## Skippable

- **IonQ Targets Quantum Error-Correction Bottleneck** — SecurityWeek. Quantum computing R&D, no security angle.
- **Enveda secures $311M for AI drugs** — TechCrunch AI. Generic AI funding round, no security angle.
- **No evidence of successful foreign meddling in 2024 election** — The Record. Intel assessment finding without new technical or security substance.
- **How to Use NVIDIA Warp and MjWarp** — Hugging Face Blog. Developer tutorial, no security angle.
- **Worries About an AI Internet Takeover Gain New Urgency** — SecurityWeek. Opinion/doomsday commentary, no news value.
- **Google Beam expands with new regions, partners, and customers** — Google AI Blog. Product/marketing expansion, no security angle.
- **ChatGPT mobile app gets voice-based agentic features** — TechCrunch AI. Routine product feature launch, no security substance.
- **Even Americans who use AI every day are worried about it** — TechCrunch AI. Survey/opinion piece, no security angle.
- **Shadow roots, explained with live examples** — Simon Willison. Developer tutorial (CSS), no security angle.
- **UAE, Saudi Arabia Face Onslaught of Increasingly Complex Cyberattacks** — Dark Reading. Regional stats summary without TTPs or technical detail.
- **Two years of OpenAI Academy** — OpenAI Blog. Marketing/education retrospective.
- **Ryuk ransomware operator gets 2-year sentence** — The Record. Duplicate coverage of sentencing news; no new TTPs (see also BleepingComputer version below).
- **YouTube Music gets more conversational with new AI features** — TechCrunch AI. Generic product feature, no security angle.
- **Supporting ASD's multi-factor authentication campaign** — AWS Security Blog. Generic awareness advisory, no new guidance.
- **YouTube will let you build your own algorithm with AI** — TechCrunch AI. Generic product feature, no security angle.
- **YouTube releases new AI features for creators within its Studio app** — TechCrunch AI. Generic product feature, no security angle.
- **StrictlyVC at TechCrunch Disrupt 2026** — TechCrunch AI. Event/ticket marketing.
- **YouTube is building AI creator tools that do almost everything for them** — The Verge AI. Duplicate/generic product feature coverage.
- **3 days left to save at TechCrunch Disrupt 2026** — TechCrunch AI. Ticket marketing.
- **Spotify is giving you the keys to its recommendation algorithm** — TechCrunch AI. Generic product feature, no security angle.
- **Latvia arrests suspected hacker for electronics repair company breach** — The Record. Regional/individual incident without broader technical significance.
- **Burnham announces plan for new UK center to fight disinformation** — The Record. Policy announcement without technical substance.
- **Honeywell: OT Security Teams Embrace AI, but Autonomy Still Rare** — SecurityWeek. Vendor survey/marketing, no news value.
- **How invideo improves color grading 3x with GPT‑6 Astra** — OpenAI Blog. Customer marketing story, no security angle.
- **Ringg's AI agents resolve up to 65% of customer calls with OpenAI** — OpenAI Blog. Customer marketing story, no security angle.
- **Harvey turns legal context into stronger drafts with GPT-6 Astra** — OpenAI Blog. Customer marketing story, no security angle.
- **Ema raises $77M as AI starts eating into enterprise software** — TechCrunch AI. Generic AI funding round, no security angle.
- **Considerations for Critical Infrastructure Operators Working With Third-Party ICS Integrators** — CISA Alerts. Generic advisory without new IOCs or technical guidance.
- **Microsoft: September Windows updates break Always On VPN connections** — BleepingComputer. Functional regression, not a security vulnerability.
- **OpenAI nabs key Patreon execs ahead of upcoming announcement** — The Verge AI. Business/hiring news, no security angle.
- **A Look at AI Doomsday Scenarios That Researchers Say Could Put Humanity at Risk** — SecurityWeek. Opinion/analysis piece, duplicate of the "AI Internet Takeover" item above.
- **Outerlimit Raises $16 Million to Stop Rogue AI Agents From Causing Harm** — SecurityWeek. Early-stage funding announcement, marketing.
- **Arista Urges Immediate Patching of Exploited VCO Zero-Day** — SecurityWeek. Duplicate coverage of the Arista VeloCloud Orchestrator zero-day (see item 18 above).
- **Ryuk ransomware member sentenced to 24 months in prison** — BleepingComputer. Duplicate coverage of sentencing news (see The Record version above).
- **Critical F5 BIG-IP Vulnerability Exploited as Zero-Day** — SecurityWeek. Duplicate coverage of the F5 BIG-IP APM zero-day (see item 26 above).
- **F5 patches BIG-IP APM zero-day flaw exploited in RCE attacks** — BleepingComputer. Duplicate coverage of the F5 BIG-IP APM zero-day (see item 26 above).
