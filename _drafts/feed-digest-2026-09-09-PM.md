# Digest — 2026-09-09 PM

- Window: last 14h
- Raw items considered: 63
- Relevant: 23
- Skippable: 40

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Chrome V8 Zero-Day Exploited in the Wild Enables Code Execution Inside Sandbox — `2026-09-09-chrome-v8-zero-day-exploited-in-the-wild.md`
- [x] **[HIGH]** New cPanel Flaw Lets a Hosting Account With Mail Privileges Run Code as Root — `2026-09-09-cpanel-flaw-lets-mail-account-run-code-as-root.md`
- [x] **[HIGH]** SAP Patches CVSS 10.0 Kernel Flaw Enabling Unauthenticated Remote Code Execution — `2026-09-09-sap-patches-cvss-10-kernel-flaw.md`
- [x] **[HIGH]** Ivanti Patches Critical Flaws Across Enterprise Security Products — `2026-09-09-ivanti-patches-critical-flaws-enterprise-security.md`
- [x] **[HIGH]** Fortinet Patches Critical Vulnerabilities in FortiMonitorOnSight, Chrome Extension — `2026-09-09-fortinet-patches-critical-vulnerabilities.md`
- [x] **[HIGH]** Alby Hub Critical Flaw Could Let Attackers Take Over Internet-Exposed Bitcoin Wallets — `2026-09-09-alby-hub-critical-flaw-bitcoin-wallets.md`
- [x] **[HIGH]** Active Exploitation of Cisco Secure Firewall Management Center Vulnerabilities — `2026-09-09-cisco-secure-firewall-management-center-exploited.md`
- [x] **[HIGH]** Multiple Chinese Hacking Groups Seen Using Identical Chrome Zero-Day Exploit — `2026-09-09-chinese-hacking-groups-shared-chrome-zero-day.md`
- [x] **[HIGH]** DeepSeek Harness Flaw Let AI Agents Disable Their Own File Sandbox Without Approval — `2026-09-09-deepseek-harness-flaw-disables-sandbox.md`
- [x] **[HIGH]** F5 BIG-IP APM Malware Injects a PHP Web Shell Into Memory, Evading Disk Scans — `2026-09-09-f5-big-ip-apm-malware-memory-web-shell.md`
- [x] **[HIGH]** Researcher Drops New Microsoft Defender PoC Showing ShieldBreak Patch Can Be Bypassed — `2026-09-09-microsoft-defender-shieldcrash-patch-bypass.md`
- [x] **[HIGH]** Infostealer Logs Expose Replayable AI Tokens That Can Bypass MFA — `2026-09-09-infostealer-logs-expose-replayable-ai-tokens.md`
- [x] **[HIGH]** Identity-Based AI Attack Threatens Security of Enterprise Data — `2026-09-09-identity-based-ai-attack-workflow-hijacking.md`
- [x] **[HIGH]** U.S. Agencies Accuse China AI Firms of Distilling Claude, GPT, Gemini, and Grok — `2026-09-09-us-agencies-accuse-china-ai-firms-distillation.md`
- [x] **[HIGH]** Veradigm Warns of Patient Data Breach After Ransomware Gang Claims Attack — `2026-09-09-veradigm-patient-data-breach-ransomware.md`
- [x] **[MEDIUM]** Over 36,000 Exposed Plex Servers Vulnerable to Recent Flaws — `2026-09-09-36000-plex-servers-exposed-unpatched.md`
- [x] **[MEDIUM]** AI Is Giving Lesser-Resourced Attackers Nation-State-Level Reach, Google Warns — `2026-09-09-ai-giving-attackers-nation-state-reach-google.md`
- [x] **[MEDIUM]** Untracked Nightmares: The Threats Hiding Behind Commodity Infrastructure — `2026-09-09-unit42-commodity-malware-youtube-seo-poisoning.md`
- [x] **[INFORMATIONAL]** 'Gambling With Our Lives': Anthropic Researcher Quits, Warns Against Self-Improving AI — `2026-09-09-anthropic-researchers-warn-ai-existential-risk.md`
- [x] **[INFORMATIONAL]** Meta Launches Personal AI Agent, Muse, Emphasizes Safety and Privacy — `2026-09-09-meta-launches-personal-ai-agent-muse.md`
- [x] **[INFORMATIONAL]** Paul Christiano Joins OpenAI Foundation Board — `2026-09-09-paul-christiano-joins-openai-foundation-board.md`
- [x] **[INFORMATIONAL]** FBI Puts Its Cyber Strategy on Paper — `2026-09-09-fbi-releases-first-public-cybersecurity-strategy.md`
- [x] **[INFORMATIONAL]** A Lean Proof-Checker Bug Behind Anthropic's Fermat's Last Theorem Formalization — `2026-09-09-trail-of-bits-lean-proof-checker-bug.md`

## Relevant (details)

### 1. Chrome V8 Zero-Day Exploited in the Wild Enables Code Execution Inside Sandbox
- **Source:** The Hacker News — https://thehackernews.com/2026/09/chrome-v8-zero-day-exploited-in-wild.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `cve`, `vulnerability`, `google`
- **Slug:** `chrome-v8-zero-day-exploited-in-the-wild`
- **Must-know:** yes
- **Summary:** Google patched CVE-2026-87491, an actively exploited V8 out-of-bounds write allowing code execution inside the sandbox — the seventh actively exploited Chrome zero-day patched this year.

### 2. New cPanel Flaw Lets a Hosting Account With Mail Privileges Run Code as Root
- **Source:** The Hacker News — https://thehackernews.com/2026/09/new-cpanel-flaw-lets-hosting-account.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `privilege-escalation`, `rce`, `cve`
- **Slug:** `cpanel-flaw-lets-mail-account-run-code-as-root`
- **Must-know:** no
- **Summary:** A cPanel/WHM flaw lets an authenticated mail-privileged account write arbitrary files via EmailTrack and escalate to root. Every supported version is affected.

### 3. SAP Patches CVSS 10.0 Kernel Flaw Enabling Unauthenticated Remote Code Execution
- **Source:** The Hacker News — https://thehackernews.com/2026/09/sap-patches-cvss-100-kernel-flaw.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`
- **Slug:** `sap-patches-cvss-10-kernel-flaw`
- **Must-know:** no
- **Summary:** CVE-2026-44756, a CVSS 10.0 memory corruption bug in SAP Extended Passport Processing, allows unauthenticated remote code execution.

### 4. Ivanti Patches Critical Flaws Across Enterprise Security Products
- **Source:** SecurityWeek — https://www.securityweek.com/ivanti-patches-critical-flaws-across-enterprise-security-products/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`
- **Slug:** `ivanti-patches-critical-flaws-enterprise-security`
- **Must-know:** no
- **Summary:** Six critical RCE flaws in Neurons for ITSM, plus authentication bypass flaws in Sentry and EPMM.

### 5. Fortinet Patches Critical Vulnerabilities in FortiMonitorOnSight, Chrome Extension
- **Source:** SecurityWeek — https://www.securityweek.com/fortinet-patches-critical-vulnerabilities-in-fortimonitoronsight-chrome-extension/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Slug:** `fortinet-patches-critical-vulnerabilities`
- **Must-know:** no
- **Summary:** Unauthenticated bugs allow attackers to bypass authentication and proxy a user's browser traffic.

### 6. Alby Hub Critical Flaw Could Let Attackers Take Over Internet-Exposed Bitcoin Wallets
- **Source:** The Hacker News — https://thehackernews.com/2026/09/alby-hub-critical-flaw-could-let.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Slug:** `alby-hub-critical-flaw-bitcoin-wallets`
- **Must-know:** no
- **Summary:** A critical flaw in the self-hosted Alby Hub Lightning wallet (v1.7.0+) could let attackers drain funds if the Hub is internet-exposed.

### 7. Active Exploitation of Cisco Secure Firewall Management Center Vulnerabilities
- **Source:** Cisco Talos — https://blog.talosintelligence.com/fmc-ongoing-exploitation/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Slug:** `cisco-secure-firewall-management-center-exploited`
- **Must-know:** no
- **Summary:** Cisco Talos is actively tracking exploitation of two vulnerabilities in Cisco Secure Firewall Management Center software.

### 8. Multiple Chinese Hacking Groups Seen Using Identical Chrome Zero-Day Exploit
- **Source:** The Record (Recorded Future) — https://therecord.media/china-hackers-chrome-browser-zero-day-multiple-groups
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `zero-day`, `vulnerability`, `cve`
- **Slug:** `chinese-hacking-groups-shared-chrome-zero-day`
- **Must-know:** no
- **Summary:** An August-identified Chrome bug was exploited by at least four distinct China-linked espionage groups using an identical exploit.

### 9. DeepSeek Harness Flaw Let AI Agents Disable Their Own File Sandbox Without Approval
- **Source:** The Hacker News — https://thehackernews.com/2026/09/deepseek-harness-flaw-let-ai-agents.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `deepseek`, `privilege-escalation`
- **Slug:** `deepseek-harness-flaw-disables-sandbox`
- **Must-know:** no
- **Summary:** A DeepSeek Harness flaw let a sandboxed coding agent disable its own OS-level sandbox via the tool's own web-facing controls.

### 10. F5 BIG-IP APM Malware Injects a PHP Web Shell Into Memory, Evading Disk Scans
- **Source:** The Hacker News — https://thehackernews.com/2026/09/f5-big-ip-apm-malware-injects-php-web.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `vulnerability`
- **Slug:** `f5-big-ip-apm-malware-memory-web-shell`
- **Must-know:** no
- **Summary:** Malware tied to F5 BIG-IP APM break-ins injects a PHP web shell into memory only, evading disk-based scans (Sophos analysis).

### 11. Researcher Drops New Microsoft Defender PoC Showing ShieldBreak Patch Can Be Bypassed
- **Source:** The Hacker News — https://thehackernews.com/2026/09/researcher-drops-new-microsoft-defender.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `microsoft`
- **Slug:** `microsoft-defender-shieldcrash-patch-bypass`
- **Must-know:** no
- **Summary:** A PoC codenamed "ShieldCrash" grants SYSTEM access and bypasses Microsoft's patch for CVE-2026-69414 ("ShieldBreak").

### 12. Infostealer Logs Expose Replayable AI Tokens That Can Bypass MFA
- **Source:** The Hacker News — https://thehackernews.com/2026/09/infostealer-logs-expose-replayable-ai.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `malware`, `vulnerability`
- **Slug:** `infostealer-logs-expose-replayable-ai-tokens`
- **Must-know:** no
- **Summary:** Infostealers like Lumma Stealer and Vidar harvest AI account credentials/session tokens that can be replayed to bypass MFA on AI provider accounts.

### 13. Identity-Based AI Attack Threatens Security of Enterprise Data
- **Source:** Dark Reading — https://www.darkreading.com/threat-intelligence/identity-based-ai-attack-security-enterprise-data
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `ai-safety`, `iam`
- **Slug:** `identity-based-ai-attack-workflow-hijacking`
- **Must-know:** no
- **Summary:** "Workflow identity hijacking" bypasses standard security controls to hijack organizational data via an unauthenticated entry point targeting AI/agent nonhuman identities.

### 14. U.S. Agencies Accuse China AI Firms of Distilling Claude, GPT, Gemini, and Grok
- **Source:** The Hacker News — https://thehackernews.com/2026/09/us-agencies-accuse-china-ai-firms-of.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `anthropic`, `openai`, `google`
- **Slug:** `us-agencies-accuse-china-ai-firms-distillation`
- **Must-know:** no
- **Summary:** U.S. agencies say six Chinese AI firms have run industrial-scale distillation attacks against American frontier models since late 2024.

### 15. Veradigm Warns of Patient Data Breach After Ransomware Gang Claims Attack
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/veradigm-discloses-patient-data-breach-after-gentlemen-gang-claims-attack/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `ransomware`
- **Slug:** `veradigm-patient-data-breach-ransomware`
- **Must-know:** no
- **Summary:** Veradigm disclosed a patient data breach tied to a third-party vendor incident after a ransomware gang claimed the attack; core systems were unaffected.

### 16. Over 36,000 Exposed Plex Servers Vulnerable to Recent Flaws
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/over-36-000-plex-servers-unpatched-against-recently-disclosed-flaws/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`, `cve`
- **Slug:** `36000-plex-servers-exposed-unpatched`
- **Must-know:** no
- **Summary:** Over 36,000 internet-exposed Plex Media Server instances remain unpatched against recently disclosed flaws.

### 17. AI Is Giving Lesser-Resourced Attackers Nation-State-Level Reach, Google Warns
- **Source:** SecurityWeek — https://www.securityweek.com/ai-is-giving-lesser-resourced-attackers-nation-state-level-reach-google-warns/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ai-safety`, `llm`, `google`
- **Slug:** `ai-giving-attackers-nation-state-reach-google`
- **Must-know:** no
- **Summary:** Google's GTIG reports criminal and state-sponsored actors are increasingly using AI to automate and scale attacks previously requiring nation-state resources.

### 18. Untracked Nightmares: The Threats Hiding Behind Commodity Infrastructure
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `unit42-commodity-malware-youtube-seo-poisoning`
- **Must-know:** no
- **Summary:** Unit 42 traces a campaign using YouTube gaming lures and SEO poisoning to deliver multi-payload malware to enterprise networks via commodity infrastructure.

### 19. 'Gambling With Our Lives': Anthropic Researcher Quits, Warns Against Self-Improving AI
- **Source:** TechCrunch — https://techcrunch.com/2026/09/09/gambling-with-our-lives-anthropic-researcher-quits-warns-against-self-improving-ai/
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `ai-safety`, `anthropic`
- **Slug:** `anthropic-researchers-warn-ai-existential-risk`
- **Must-know:** no
- **Summary:** Anthropic researcher Jacob Coxon resigned over self-improving-AI fears; a colleague separately estimated >10% odds AI could "kill all humans" this decade.

### 20. Meta Launches Personal AI Agent, Muse, Emphasizes Safety and Privacy
- **Source:** SecurityWeek — https://www.securityweek.com/meta-launches-personal-ai-agent-muse-emphasizes-safety-and-privacy/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `ai-launch`, `meta`, `ai-safety`
- **Slug:** `meta-launches-personal-ai-agent-muse`
- **Must-know:** no
- **Summary:** Meta's new personal AI agent Muse runs in a dedicated secure VM housing both the agent and user data.

### 21. Paul Christiano Joins OpenAI Foundation Board
- **Source:** OpenAI Blog — https://openai.com/index/paul-christiano-joins-openai-foundation-board
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `openai`, `ai-safety`
- **Slug:** `paul-christiano-joins-openai-foundation-board`
- **Must-know:** no
- **Summary:** AI alignment researcher Paul Christiano has joined OpenAI's Foundation Board and its Safety and Security Committee.

### 22. FBI Puts Its Cyber Strategy on Paper
- **Source:** The Record (Recorded Future) — https://therecord.media/fbi-releases-first-public-cybersecurity-strategy
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `law-enforcement`
- **Slug:** `fbi-releases-first-public-cybersecurity-strategy`
- **Must-know:** no
- **Summary:** The FBI released its first public cybersecurity strategy directing field offices to align efforts against hackers and cybercrime groups.

### 23. A Lean Proof-Checker Bug Behind Anthropic's Fermat's Last Theorem Formalization
- **Source:** Trail of Bits — https://blog.trailofbits.com/2026/09/09/a-proof-of-fermats-last-theorem-that-fits-the-margin/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** informational
- **Tags:** `vulnerability`, `anthropic`
- **Slug:** `trail-of-bits-lean-proof-checker-bug`
- **Must-know:** no
- **Summary:** Trail of Bits found a soundness bug in the Lean proof checker while examining Anthropic's Lean formalization of Fermat's Last Theorem; patched in Lean v4.34.0-rc1.

## Skippable

- **[Virtual Event] What Every Enterprise Should Know About Securing Cloud Assets in the Age of AI** — Dark Reading. Event promo, not news.
- **[Virtual Event] Building a Secure AI Strategy for the Enterprise** — Dark Reading. Event promo, not news.
- **Apple's new iPhone camera mode promises to prove your photo isn't AI** — The Verge AI. Consumer feature announcement, no security angle.
- **The hinge for Apple's new foldable phone was built with AI** — TechCrunch AI. Non-security manufacturing story.
- **The state of AI for security: Measuring what matters most for building trust** — AWS Security Blog. Generic vendor thought-leadership post, no concrete finding.
- **Apple's revamped Health app will calculate your 'health age' and readiness score** — TechCrunch AI. Non-security consumer feature.
- **Grindr settles privacy lawsuit tied to disclosure of users' HIV statuses for $35 million** — The Record. Legal settlement of a prior case, no new technical incident.
- **Apple has a new way prove your iPhone photos aren't AI slop** — TechCrunch AI. Duplicate coverage of the Reference Image story.
- **Apple CEO John Ternus says the best AI device is still the iPhone** — TechCrunch AI. Opinion/commentary, no news value.
- **HelmGuard Raises $7.3 Million for Agentic GRC and Security** — SecurityWeek. Funding announcement.
- **Microsoft has new AI privacy rules for schools** — The Verge AI. Voluntary policy agreement, education vertical, no technical substance.
- **Electronic health record company says customer data stolen in breach** — The Record. Duplicate of the Veradigm story; merged as an additional source in that item.
- **Android's September 2026 Updates Patch 180 Vulnerabilities** — SecurityWeek. Routine Patch Tuesday, no single critical exploited CVE.
- **Chipmaker Patch Tuesday: Nvidia, AMD, Arm Issue Security Advisories** — SecurityWeek. Routine patch roundup.
- **Superintelligence is coming. Should we let it?** — TechCrunch AI. Opinion podcast, no news value.
- **Get ready for the game with new football features in Search** — Google AI Blog. Non-security product feature.
- **Recreating a 70-year love story frame by frame** — Google AI Blog. Non-security creative content.
- **ControlAI's Connor Leahy on why superintelligence is 'not a weapon, it's an adversary'** — TechCrunch AI. Duplicate opinion podcast coverage.
- **IBM releases SOTA Granite Time Series PatchTST-FM-r2 model with commercial-friendly license** — Hugging Face Blog. No summary text provided; insufficient detail to draft factually.
- **Viral AI assistant Instinct now has its own email address** — TechCrunch AI. Consumer feature launch, no security angle.
- **Shipt becomes the latest delivery app with an AI shopping assistant** — TechCrunch AI. Non-security consumer feature.
- **The Flashpoint Threat Intelligence Brief: Middle East** — Flashpoint. Generic recurring brief, no specific new incident in summary.
- **AI spend per employee slumped at top firms in August** — TechCrunch AI. Business/economics story, no security angle.
- **MFA's Weakest Link: Account Recovery Is the New Attack Path** — BleepingComputer. Vendor-sponsored explainer (Specops), no specific new incident.
- **Instacart launches an AI grocery shopping assistant called Clementine** — TechCrunch AI. Non-security consumer feature.
- **Sequoia doubles down on Cymphony as AI agents create new enterprise security risks** — TechCrunch AI. VC funding story.
- **Amazon Prime Video's new AI tech matches lips to dubbed audio** — The Verge AI. Non-security consumer feature.
- **US Agencies Warn China Is Systematically Extracting Frontier AI Capabilities** — SecurityWeek. Duplicate of the distillation story; merged as an additional source in that item.
- **Besxar is building an orbital semiconductor factory, one SpaceX rocket at a time** — TechCrunch AI. Non-security business story.
- **Ukraine prosecutor general steps down amid scam call center bribery probe** — The Record. Political/corruption story, no technical substance.
- **Suno replaces its AI models with a new one trained on licensed music as copyright suits pile up** — TechCrunch AI. Non-security legal/business story.
- **Students who use AI generally score worse at school** — The Verge AI. Non-security education research.
- **Webinar: Learn How to Answer "Are We Exposed?" Faster After a New CVE** — The Hacker News. Webinar/marketing content.
- **ICS Patch Tuesday: Schneider Electric, Siemens Fix Critical Flaws** — SecurityWeek. Routine patch roundup, no confirmed active exploitation.
- **This Key Will Self-Destruct: An Open Standard for Revocable API Keys** — SecurityWeek. Opinion/proposal piece, not an incident or tool release.
- **Worried Anthropic researchers warn that AI 'could kill all humans'** — The Verge. Duplicate of the Anthropic researcher story; merged as an additional source in that item.
- **Man gets 15 years for extorting women with AI-generated porn videos** — BleepingComputer. Sentencing news, no new technical detail.
- **New Microsoft Defender 'ShieldCrash' zero-day grants SYSTEM access** — BleepingComputer. Duplicate of the Defender PoC story; merged as an additional source in that item.
- **Google warns of new Chrome zero-day bug exploited in attacks** — BleepingComputer. Duplicate of the Chrome V8 zero-day story; merged as an additional source in that item.
