# Digest — 2026-09-15 PM

- Window: last 14h
- Raw items considered: 20
- Relevant: 10
- Skippable: 10

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Cisco Secure Email Gateway Zero-Day (CVE-2026-76461) Exploited to Gain Root Access — `2026-09-15-cisco-secure-email-gateway-zero-day-cve-2026-76461.md`
- [x] **[HIGH]** Human Attacker Exploits Marimo Notebook RCE, Reaches SSH Bastion in Eight Seconds — `2026-09-15-marimo-rce-human-attacker-ssh-bastion-eight-seconds.md`
- [x] **[HIGH]** 240,000 Affected by Data Breach at Japan's Digital Agency — `2026-09-15-japan-digital-agency-data-breach-240000.md`
- [x] **[HIGH]** Mass-Scanning Campaign Exploits Vite Flaw to Extract Cloud Credentials From Exposed Dev Servers — `2026-09-15-vite-flaw-mass-scanning-cloud-credentials.md`
- [x] **[HIGH]** LiteSpeed Enterprise Flaw Could Let One Hosting Account Gain Root Access on a Shared Server — `2026-09-15-litespeed-enterprise-flaw-root-access-shared-server.md`
- [x] **[HIGH]** China-Linked Hackers Exploit Chrome-Windows Flaw Chain to Deploy GRIMWEDGE Backdoor — `2026-09-15-china-hackers-chrome-windows-zero-day-grimwedge.md`
- [x] **[MEDIUM]** Suspected Black Axe Gang Leaders Face Cybercrime Charges in the US — `2026-09-15-black-axe-gang-leaders-cybercrime-charges.md`
- [x] **[INFORMATIONAL]** Salesforce and Nvidia Launch Koa, a Reasoning Model Built on Open-Weight Nemotron — `2026-09-15-salesforce-nvidia-koa-reasoning-model.md`
- [x] **[INFORMATIONAL]** Microsoft AI Code of Conduct Sets Cyberattack Boundaries, Chain of Command, Safety Constraints — `2026-09-15-microsoft-ai-code-of-conduct-cyberattack-boundaries.md`
- [x] **[INFORMATIONAL]** Is Big Tech's AI Slowdown a Safety Pact or a Cartel? — `2026-09-14-ai-labs-slowdown-safety-pact-or-cartel.md`

## Relevant (details)

### 1. Cisco Secure Email Gateway Zero-Day (CVE-2026-76461) Exploited to Gain Root Access
- **Source:** The Hacker News — https://thehackernews.com/2026/09/cisco-secure-email-gateway-flaw.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `zero-day`, `rce`, `vulnerability`
- **Slug:** `cisco-secure-email-gateway-zero-day-cve-2026-76461`
- **Must-know:** yes
- **Summary:** Cisco warned that CVE-2026-76461, a CVSS 9.8 flaw in AsyncOS for Secure Email Gateway caused by insufficient email-parsing validation, is under active exploitation. An unauthenticated remote attacker can execute arbitrary commands as root. Duplicate coverage from BleepingComputer and SecurityWeek was skipped in favor of this more detailed write-up.

### 2. Human Attacker Exploits Marimo Notebook RCE, Reaches SSH Bastion in Eight Seconds
- **Source:** The Hacker News — https://thehackernews.com/2026/09/human-attacker-exploits-marimo-rce.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `vulnerability`
- **Slug:** `marimo-rce-human-attacker-ssh-bastion-eight-seconds`
- **Must-know:** no
- **Summary:** Sysdig documented a human operator exploiting a Marimo notebook RCE and pivoting to an SSH bastion host within eight seconds of initial access. Highlights how fast skilled human attackers can move post-compromise, independent of AI tooling.

### 3. 240,000 Affected by Data Breach at Japan's Digital Agency
- **Source:** SecurityWeek — https://www.securityweek.com/240000-hit-by-data-breach-at-japans-digital-agency/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `vulnerability`
- **Slug:** `japan-digital-agency-data-breach-240000`
- **Must-know:** no
- **Summary:** Attackers exploited a VPN product vulnerability to steal personal data on roughly 240,000 people from Japan's Digital Agency. Vendor and vulnerability detail were not disclosed in the source summary.

### 4. Mass-Scanning Campaign Exploits Vite Flaw to Extract Cloud Credentials From Exposed Dev Servers
- **Source:** The Hacker News — https://thehackernews.com/2026/09/mass-scanning-campaign-exploits-vite.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cloud-security`
- **Slug:** `vite-flaw-mass-scanning-cloud-credentials`
- **Must-know:** no
- **Summary:** F5 Labs found an automated scanning campaign hitting internet-exposed Vite dev servers to steal AWS/Azure credentials and infrastructure state files. Opportunistic and broad rather than targeted.

### 5. LiteSpeed Enterprise Flaw Could Let One Hosting Account Gain Root Access on a Shared Server
- **Source:** The Hacker News — https://thehackernews.com/2026/09/litespeed-enterprise-flaw-could-let-one.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `privilege-escalation`, `vulnerability`
- **Slug:** `litespeed-enterprise-flaw-root-access-shared-server`
- **Must-know:** no
- **Summary:** cPanel warned that a critical LiteSpeed Web Server Enterprise flaw lets a low-privilege shared-hosting account escalate to root, exposing other tenants on the same server. No CVE ID or patch status was included in the source summary.

### 6. China-Linked Hackers Exploit Chrome-Windows Flaw Chain to Deploy GRIMWEDGE Backdoor
- **Source:** The Hacker News — https://thehackernews.com/2026/09/china-linked-hackers-exploit-chrome.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `vulnerability`
- **Slug:** `china-hackers-chrome-windows-zero-day-grimwedge`
- **Must-know:** no
- **Summary:** Volexity attributes a spear-phishing campaign (UTA0560) to a China-linked actor exploiting recently patched Chrome and Windows flaws to drop the GRIMWEDGE backdoor, targeting NGOs since September 1, 2026.

### 7. Suspected Black Axe Gang Leaders Face Cybercrime Charges in the US
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/black-axe-gang-members-extradited-to-us-face-cybercrime-charges/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `cybercrime`
- **Slug:** `black-axe-gang-leaders-cybercrime-charges`
- **Must-know:** no
- **Summary:** Five alleged leaders of the Black Axe cybercrime syndicate were extradited to the US to face wire fraud and money laundering charges tied to global financial fraud operations.

### 8. Salesforce and Nvidia Launch Koa, a Reasoning Model Built on Open-Weight Nemotron
- **Source:** TechCrunch AI — https://techcrunch.com/2026/09/15/salesforce-and-nvidias-new-reasoning-model-is-everything-the-ai-labs-should-fear/
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `model-release`, `ai-launch`
- **Slug:** `salesforce-nvidia-koa-reasoning-model`
- **Must-know:** no
- **Summary:** Salesforce and Nvidia released Koa, a reasoning model built on Nvidia's open-weight Nemotron model and trained for sales, marketing, and customer-support tasks.

### 9. Microsoft AI Code of Conduct Sets Cyberattack Boundaries, Chain of Command, Safety Constraints
- **Source:** SecurityWeek — https://www.securityweek.com/microsoft-ai-code-of-conduct-sets-cyberattack-boundaries-chain-of-command-safety-constraints/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `ai-safety`, `microsoft`
- **Slug:** `microsoft-ai-code-of-conduct-cyberattack-boundaries`
- **Must-know:** no
- **Summary:** Microsoft published a "Humanist AI Code of Conduct" distinguishing defensive cyber research from operational attack capability, setting boundaries, chain of command, and safety constraints for AI cyber use.

### 10. Is Big Tech's AI Slowdown a Safety Pact or a Cartel?
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/995186/is-big-techs-ai-slowdown-a-safety-pact-or-a-cartel
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `ai-safety`
- **Slug:** `ai-labs-slowdown-safety-pact-or-cartel`
- **Must-know:** no
- **Summary:** OpenAI, Anthropic, Google DeepMind, and SpaceX leaders reportedly agreed to slow AI development pace over the weekend, prompting debate over whether the move is a genuine safety pact or anticompetitive coordination among dominant labs.

## Skippable

- **[Virtual Event] What Every Enterprise Should Know About Securing Cloud Assets in the Age of AI** — Dark Reading. Event promotion, not news.
- **[Virtual Event] Building a Secure AI Strategy for the Enterprise** — Dark Reading. Event promotion, not news.
- **Attack Chains, Not Just Attack Surfaces: Why Testing Individual Techniques Misses the Point** — The Hacker News. Opinion/methodology piece without concrete news value.
- **Apple Patches 200 Vulnerabilities With New iOS 27, macOS Golden Gate 27 Releases** — SecurityWeek. Routine patch release; no single CVE flagged as critical and actively exploited.
- **1Password's AI patching benchmark is misleading** — Trail of Bits. Opinion/critique of another vendor's report, not independent news.
- **Hacked HBO Max Reddit Account Used for Malware Delivery via ClickFix Attack** — SecurityWeek. Single compromised account distributing malware via a known technique (ClickFix), no novel detail.
- **Microsoft confirms KB5002914 Excel update breaks copy and paste** — BleepingComputer. Functionality bug, not a security issue.
- **Cisco patches Secure Email Gateway zero-day exploited in attacks** — BleepingComputer. Duplicate coverage of the Cisco Secure Email Gateway zero-day; The Hacker News write-up had more technical detail.
- **Root RCE Zero-Day in Cisco Secure Email Gateway Under Active Exploitation** — SecurityWeek. Duplicate coverage of the same Cisco zero-day; consolidated into The Hacker News item.
- **Jensen Huang took a call from Trump, and showed off something else, too** — TechCrunch AI. Gossip/color piece, no substantive AI or security news.
