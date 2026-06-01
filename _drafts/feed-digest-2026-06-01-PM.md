# Digest — 2026-06-01 PM

- Window: last 14h
- Raw items considered: 46
- Relevant: 19
- Skippable: 27

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Miasma Supply Chain Attack Compromises Red Hat npm Packages — `2026-06-01-miasma-supply-chain-redhat-npm-worm.md`
- [x] **[CRITICAL]** OpenAI Codex Authentication Tokens Stolen via npm Supply Chain — `2026-06-01-openai-codex-tokens-stolen-npm-supply-chain.md`
- [x] **[CRITICAL]** Windows Netlogon RCE CVE-2026-41089 Now Actively Exploited — `2026-06-01-cve-2026-41089-windows-netlogon-rce-exploited.md`
- [x] **[CRITICAL]** Palo Alto PAN-OS Auth Bypass CVE-2026-0257 Exploited for Weeks — `2026-06-01-cve-2026-0257-panos-auth-bypass-exploited.md`
- [x] **[HIGH]** Meta AI Support Bot Exploited to Hijack Instagram Accounts — `2026-06-01-meta-ai-chatbot-instagram-account-takeover.md`
- [x] **[HIGH]** WP Maps Pro CVE-2026-8732 Exploited for Unauthorized Admin Account Creation — `2026-06-01-cve-2026-8732-wp-maps-pro-admin-takeover.md`
- [x] **[HIGH]** NIST NVD Backlog Swells to 27,000 Unprocessed Vulnerabilities — `2026-06-01-nist-nvd-backlog-27000-vulnerabilities.md`
- [x] **[HIGH]** Dutch Police Dismantle 17-Million-Device Botnet — `2026-06-01-dutch-police-dismantle-17m-device-botnet.md`
- [x] **[HIGH]** 19-Year-Old Linux Kernel CIFSwitch Flaw Gets Public PoC — `2026-06-01-linux-kernel-cifswitch-privesc-poc-released.md`
- [x] **[HIGH]** CISA KEV: Oracle WebLogic CVE-2024-21182 Added — `2026-06-01-cisa-kev-oracle-weblogic-cve-2024-21182.md`
- [x] **[HIGH]** Dragon Weave: China-Aligned Espionage Targets Czech and Taiwanese Sectors — `2026-06-01-dragon-weave-china-espionage-czech-taiwan.md`
- [x] **[HIGH]** WordPress Malware Hides C2 Commands Inside Steam Community Profiles — `2026-06-01-wordpress-malware-steam-profiles-c2.md`
- [x] **[MEDIUM]** Dashlane Users Locked Out Following Brute Force Campaign — `2026-06-01-dashlane-brute-force-lockouts.md`
- [x] **[MEDIUM]** Florida Sues OpenAI and Sam Altman Over AI's Alleged Role in Violent Incidents — `2026-06-01-florida-sues-openai-violent-incidents.md`
- [x] **[MEDIUM]** Container Attack Vectors Mapped: Secrets, Misconfigs, API Compromise, Supply Chain — `2026-06-01-container-attack-vectors-kaspersky.md`
- [x] **[INFORMATIONAL]** Anthropic Files Confidentially with SEC to Begin IPO Process — `2026-06-01-anthropic-ipo-filing.md`
- [x] **[INFORMATIONAL]** Google Gemini Spark: 24/7 Persistent AI Agent Launches — `2026-06-01-google-gemini-spark-ai-agent.md`
- [x] **[INFORMATIONAL]** JetBrains Releases Mellum2, a 12B Mixture-of-Experts Code Model — `2026-06-01-jetbrains-mellum2-12b-moe-model.md`
- [x] **[INFORMATIONAL]** Microsoft Pledges Not to Pursue Security Researchers After Zero-Day Backlash — `2026-06-01-microsoft-wont-pursue-security-researchers.md`

## Relevant (details)

### 1. Miasma Supply Chain Attack Compromises Red Hat npm Packages
- **Source:** The Hacker News — https://thehackernews.com/2026/06/miasma-supply-chain-attack-compromises.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `malware`, `github`
- **Slug:** `2026-06-01-miasma-supply-chain-redhat-npm-worm`
- **Must-know:** yes
- **Summary:** A campaign dubbed Miasma has backdoored @redhat-cloud-services npm packages with a credential-stealing worm using install-time execution, CI/CD credential harvesting, and encrypted exfiltration — same core tactics as the prior Shai-Hulud family. Any developer machine that ran an install of an affected package should be treated as compromised; rotate all secrets and CI/CD credentials immediately.

### 2. OpenAI Codex Authentication Tokens Stolen via npm Supply Chain
- **Source:** The Hacker News — https://thehackernews.com/2026/06/openai-codex-authentication-tokens.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `openai`
- **Slug:** `2026-06-01-openai-codex-tokens-stolen-npm-supply-chain`
- **Must-know:** yes
- **Summary:** The codexui-android npm package (29,000+ weekly downloads), marketed as a remote web UI for OpenAI Codex, steals authentication tokens from developer machines and remains live on npm. Any developer who installed it should immediately revoke all OpenAI API keys and Codex credentials.

### 3. Windows Netlogon RCE CVE-2026-41089 Now Actively Exploited
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/critical-windows-netlogon-remote-code-execution-flaw-now-exploited-in-attacks/ | SecurityWeek — https://www.securityweek.com/critical-windows-netlogon-vulnerability-in-attackers-crosshairs/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `vulnerability`, `cve`, `microsoft`
- **Slug:** `2026-06-01-cve-2026-41089-windows-netlogon-rce-exploited`
- **Must-know:** no
- **Summary:** Belgium's CCB and SecurityWeek both confirm active exploitation of CVE-2026-41089, a critical RCE in Windows Netlogon that affects domain controllers. Organizations running unpatched Active Directory infrastructure should treat this as a P0 remediation.

### 4. Palo Alto PAN-OS Auth Bypass CVE-2026-0257 Exploited for Weeks
- **Source:** Dark Reading — https://www.darkreading.com/threat-intelligence/patch-palo-alto-auth-bypass-bug-exploit | SecurityWeek — https://www.securityweek.com/recent-palo-alto-networks-vulnerability-exploited-for-weeks/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`
- **Slug:** `2026-06-01-cve-2026-0257-panos-auth-bypass-exploited`
- **Must-know:** no
- **Summary:** CVE-2026-0257, a PAN-OS GlobalProtect VPN authentication bypass, was exploited four days after public disclosure and has seen two attack waves through mid-May. Organizations should apply Palo Alto's patch immediately and review VPN access logs for anomalous authentication events.

### 5. Meta AI Support Bot Exploited to Hijack Instagram Accounts
- **Source:** Krebs on Security — https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/ | The Verge AI — https://www.theverge.com/tech/941179/meta-instagram-ai-support-chatbot-exploit-hacked
- **Section:** Cybersecurity — Primary / AI — News & Analysis
- **Severity:** high
- **Tags:** `llm`, `ai-safety`, `iam`, `meta`
- **Slug:** `2026-06-01-meta-ai-chatbot-instagram-account-takeover`
- **Must-know:** no
- **Summary:** Attackers tricked Meta's AI support chatbot into resetting Instagram passwords by requesting email address changes on arbitrary accounts; high-profile accounts including the Obama White House Instagram were briefly defaced with pro-Iranian imagery. Meta says the issue is patched; the incident illustrates authorization failures in AI-powered account management systems.

### 6. WP Maps Pro CVE-2026-8732 Exploited for Unauthorized Admin Account Creation
- **Source:** The Hacker News — https://thehackernews.com/2026/06/critical-wp-maps-pro-flaw-actively.html | SecurityWeek — https://www.securityweek.com/wp-maps-pro-vulnerability-exploited-to-take-over-wordpress-sites/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`
- **Slug:** `2026-06-01-cve-2026-8732-wp-maps-pro-admin-takeover`
- **Must-know:** no
- **Summary:** CVE-2026-8732 in WP Maps Pro (15,000+ Envato sales) allows unauthenticated attackers to create WordPress administrator accounts; active exploitation is ongoing. Update or deactivate the plugin immediately and audit your admin user list for unexpected accounts.

### 7. NIST NVD Backlog Swells to 27,000 Unprocessed Vulnerabilities
- **Source:** The Record — https://therecord.media/nist-mistakes-vulnerability-database-inspector-general
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Slug:** `2026-06-01-nist-nvd-backlog-27000-vulnerabilities`
- **Must-know:** no
- **Summary:** An inspector general report found NIST's NVD backlog nearly doubled from 13,000 to 27,000 unprocessed CVEs between early 2024 and end of 2025, degrading CVSS scores and product data for tools that rely on NVD enrichment. Organizations should supplement NVD with OSV, vendor advisories, or commercial intel sources to avoid blind spots.

### 8. Dutch Police Dismantle 17-Million-Device Botnet
- **Source:** SecurityWeek — https://www.securityweek.com/dutch-police-dismantle-massive-17-million-device-botnet/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`
- **Slug:** `2026-06-01-dutch-police-dismantle-17m-device-botnet`
- **Must-know:** no
- **Summary:** Dutch authorities seized C2 infrastructure for a 17-million-device botnet of infected computers, smartphones, and tablets allegedly operated as a residential proxy network for cybercrime. Residential proxy services route malicious traffic through consumer devices, defeating IP-based detection; this takedown is one of the largest of its kind.

### 9. 19-Year-Old Linux Kernel CIFSwitch Flaw Gets Public PoC
- **Source:** SecurityWeek — https://www.securityweek.com/19-year-old-linux-kernel-vulnerability-exposes-systems-to-root-access/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `privilege-escalation`
- **Slug:** `2026-06-01-linux-kernel-cifswitch-privesc-poc-released`
- **Must-know:** no
- **Summary:** A 19-year-old privilege escalation bug in the Linux kernel's CIFSwitch component now has a public PoC enabling low-privileged local users to gain root; its age means it spans a wide range of kernel versions. Shared hosting, multi-tenant container hosts, and systems with untrusted local users are at highest risk.

### 10. CISA KEV: Oracle WebLogic CVE-2024-21182 Added
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/alerts/2026/06/01/cisa-adds-one-known-exploited-vulnerability-catalog
- **Section:** Government / Advisory
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Slug:** `2026-06-01-cisa-kev-oracle-weblogic-cve-2024-21182`
- **Must-know:** no
- **Summary:** CISA added CVE-2024-21182, an unspecified Oracle WebLogic Server vulnerability, to the Known Exploited Vulnerabilities catalog based on confirmed active exploitation. Federal agencies must remediate per BOD 22-01; commercial operators running WebLogic should apply the Oracle patch immediately.

### 11. Dragon Weave: China-Aligned Espionage Targets Czech and Taiwanese Sectors
- **Source:** The Hacker News — https://thehackernews.com/2026/06/china-aligned-groups-ramp-up-attacks.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `phishing`, `malware`
- **Slug:** `2026-06-01-dragon-weave-china-espionage-czech-taiwan`
- **Must-know:** no
- **Summary:** Seqrite Labs documented Operation Dragon Weave, a China-aligned espionage campaign delivering AdaptixC2 agents to government, research, tech, and finance targets in Czech Republic and Taiwan via spear-phishing ZIP attachments. Organizations in targeted sectors should review email gateway logs and verify endpoint coverage for AdaptixC2 IoCs.

### 12. WordPress Malware Hides C2 Commands Inside Steam Community Profiles
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/wordpress-malware-campaign-hides-payloads-in-steam-profiles/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `appsec`
- **Slug:** `2026-06-01-wordpress-malware-steam-profiles-c2`
- **Must-know:** no
- **Summary:** Nearly 2,000 WordPress sites are infected with malware that reads C2 instructions embedded in Steam Community profile comments, using the legitimate gaming platform as an out-of-band C2 channel that defeats standard blocklists. Behavioral endpoint detection is more effective than network-based blocking for this technique.

### 13. Dashlane Users Locked Out Following Brute Force Campaign
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/dashlane-password-manager-users-locked-out-by-brute-force-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `iam`
- **Slug:** `2026-06-01-dashlane-brute-force-lockouts`
- **Must-know:** no
- **Summary:** Multiple Dashlane users were locked out after brute force login attempts from distant locations and unknown devices; successful account access has not been confirmed. Affected users should rotate their master password and ensure MFA is enabled, given that a vault compromise would expose all stored credentials.

### 14. Florida Sues OpenAI and Sam Altman Over AI's Alleged Role in Violent Incidents
- **Source:** TechCrunch AI — https://techcrunch.com/2026/06/01/florida-sues-openai-sam-altman-in-first-of-its-kind-lawsuit-over-violent-incidents/
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `openai`, `ai-safety`
- **Slug:** `2026-06-01-florida-sues-openai-violent-incidents`
- **Must-know:** no
- **Summary:** Florida filed what is described as a first-of-its-kind lawsuit against OpenAI and Sam Altman, partly citing ChatGPT's alleged role in a shooting at Florida State University. The outcome could set legal precedent for AI output liability applicable to all LLM providers and enterprise AI deployments.

### 15. Container Attack Vectors Mapped: Secrets, Misconfigs, API Compromise, Supply Chain
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/container-attack-vectors/120010/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `container-security`, `supply-chain`, `kubernetes`, `appsec`
- **Slug:** `2026-06-01-container-attack-vectors-kaspersky`
- **Must-know:** no
- **Summary:** Kaspersky GReAT published a practitioner-focused breakdown of container attack surfaces: exposed secrets, privilege misconfigurations, Docker/Kubernetes API compromise, and supply chain attacks on container images. Useful as a threat modeling reference; containers with the Docker socket mounted or privileged mode enabled represent the highest-risk configurations.

### 16. Anthropic Files Confidentially with SEC to Begin IPO Process
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/941016/anthropic-has-officially-filed-to-go-public | TechCrunch AI — https://techcrunch.com/2026/06/01/anthropic-files-to-go-public/
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `anthropic`
- **Slug:** `2026-06-01-anthropic-ipo-filing`
- **Must-know:** no
- **Summary:** Anthropic filed confidentially with the SEC to kick off the IPO process, beating competitor OpenAI to this milestone. The filing follows Anthropic's $40 billion valuation established in its most recent Google-led fundraise.

### 17. Google Gemini Spark: 24/7 Persistent AI Agent Launches
- **Source:** The Verge AI — https://www.theverge.com/tech/941138/google-gemini-spark-ai-agent-hands-on
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `google`, `llm`, `ai-launch`
- **Slug:** `2026-06-01-google-gemini-spark-ai-agent`
- **Must-know:** no
- **Summary:** Google launched Gemini Spark, a persistent AI agent that works autonomously on tasks for up to 24 hours; hands-on reviewers describe strong agentic capability but flag cost and privacy tradeoffs of an always-on agent with continuous account access. Security practitioners should note the expanded authorization scope persistent AI agents introduce.

### 18. JetBrains Releases Mellum2, a 12B Mixture-of-Experts Code Model
- **Source:** Hugging Face Blog — https://huggingface.co/blog/JetBrains/mellum2-launch
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `llm`
- **Slug:** `2026-06-01-jetbrains-mellum2-12b-moe-model`
- **Must-know:** no
- **Summary:** JetBrains released Mellum2, a 12B-parameter Mixture-of-Experts model for code completion, published as open weights on Hugging Face and designed for self-hosted deployment in JetBrains IDEs. MoE architecture enables larger effective capacity at lower inference cost compared to dense models of equivalent parameter count.

### 19. Microsoft Pledges Not to Pursue Security Researchers After Zero-Day Backlash
- **Source:** The Record — https://therecord.media/microsoft-says-it-will-not-pursue-security-researchers-disclosure
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `microsoft`, `vulnerability`
- **Slug:** `2026-06-01-microsoft-wont-pursue-security-researchers`
- **Must-know:** no
- **Summary:** Following backlash over its zero-day disclosure stance, Microsoft clarified it "has no intention to pursue action against individuals conducting or publishing their security research." The statement is informal rather than a formal policy document; researchers should still consult Microsoft's Security Researcher Safe Harbor policy.

## Skippable

- **This could be Windows' M1 moment** (The Verge AI) — Consumer laptop hardware announcement; no security angle.
- **NSA selects new leads for key cybersecurity posts** (The Record) — Organizational personnel change; no actionable security news.
- **Water access is now a risk factor in SpaceX's IPO** (TechCrunch AI) — Infrastructure business news; not security or AI launch.
- **Anthropic files to go public** (TechCrunch AI) — Duplicate of item 16; The Verge version used as primary.
- **Spring 2026 SOC 1, 2, and 3 reports now available** (AWS Security Blog) — Routine annual compliance certification; no new security signal.
- **How we used Gemini to build Google I/O 2026** (Google AI Blog) — Marketing content; no substantive security or model news.
- **This AI weather startup is out-forecasting government agencies** (TechCrunch AI) — General AI application; not security-relevant.
- **DuckDuckGo makes its no-AI search engine easier to access** (TechCrunch AI) — Product update; no security relevance.
- **Microsoft to unveil new AI models at Build** (The Verge AI) — Pre-announcement preview with no confirmed details.
- **Microsoft investigates Office Apps, Teams file access issues** (BleepingComputer) — Service outage; no security implication.
- **AI is blowing up music — How should the Grammys handle it?** (The Verge AI) — Opinion podcast; no news value.
- **AWS Weekly Roundup: Claude Opus 4.8 on AWS** (AWS News Blog) — Roundup post; substantive items covered by primary sources.
- **Strava blames zero-code AI apps and scrapers, tightens API access** (The Verge AI) — API access policy change; no security angle.
- **Race Against Time: Why Faster Vulnerability Alerts Matter** (BleepingComputer) — Vendor marketing piece for SecAlerts.
- **Weekly Recap: New Linux Flaw, PAN-OS Exploit, AI-Powered Attacks** (The Hacker News) — Meta-roundup; all component stories covered individually.
- **Beyond LLMs: Why Scalable Enterprise AI Adoption Depends on Agent Logic** (Hugging Face / IBM Research) — Enterprise thought-leadership marketing; no technical news.
- **Dragos Acquires xIoT Security Firm Phosphorus** (SecurityWeek) — M&A announcement; no direct practitioner impact.
- **Webinar tomorrow: From alert to resolution in network incident response** (BleepingComputer) — Promotional webinar advertisement.
- **Building the infrastructure for the Intelligence Age in Michigan** (OpenAI Blog) — Data center PR; no security angle.
- **As the Pentagon Pushes for Battlefield AI, Some Military Leaders Urge Caution** (SecurityWeek) — Policy opinion piece without technical news.
- **Microsoft fixes outage affecting MFA setup, MySignIn service** (BleepingComputer) — Service outage since resolved; no persistent security impact.
- **The Security Growth Platform: Why MSPs Are Moving Beyond vCISO Tools** (The Hacker News) — Vendor marketing content.
- **Microsoft fixes KB5089549 Windows security update install issues** (BleepingComputer) — Update installer bug fix; not a security vulnerability.
- **Meta's own AI was exploited to hijack Instagram accounts** (The Verge AI) — Duplicate; Krebs on Security version used as primary source.
- **Critical Windows Netlogon Vulnerability in Attackers' Crosshairs** (SecurityWeek) — Secondary source for item 3; BleepingComputer used as primary.
- **Recent Palo Alto Networks Vulnerability Exploited for Weeks** (SecurityWeek) — Secondary source for item 4; Dark Reading used as primary.
- **WP Maps Pro Vulnerability Exploited to Take Over WordPress Sites** (SecurityWeek) — Secondary source for item 6; The Hacker News used as primary.
