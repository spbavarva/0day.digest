# Digest — 2026-09-26 PM

- Window: last 14h
- Raw items considered: 17
- Relevant: 11
- Skippable: 6

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** ShinyHunters Bypass WAFs to Resume Mass Exploitation of Oracle PeopleSoft Flaw — `2026-09-26-oracle-peoplesoft-waf-bypass-cve-2026-35273.md`
- [x] **[HIGH]** Lunex Stealer Abuses AMD Driver to Disable Security Tools, Steal Browser Credentials — `2026-09-26-lunex-stealer-amd-driver-clickfix.md`
- [x] **[INFORMATIONAL]** China and US Agree to Establish AI Safety Communication Channel — `2026-09-26-china-us-ai-safety-channel.md`
- [x] **[HIGH]** OpenAI Pauses Training of Its Most Capable Models After Sandbox Escape — `2026-09-26-openai-pauses-training-most-capable-models.md`
- [x] **[CRITICAL]** Compromised GitHub Actions Re-Enabled With Mini Shai-Hulud Payload Still Live — `2026-09-26-github-actions-mini-shai-hulud-still-active.md`
- [x] **[MEDIUM]** OpenAI Says Its AI Agents Accidentally Uploaded User Images to Third-Party Sites — `2026-09-26-openai-agents-uploaded-images-third-party-sites.md`
- [x] **[HIGH]** New x47.c Windows Botnet Weaponizes xAI's Grok for AI API Draining — `2026-09-26-x47c-windows-botnet-xai-grok.md`
- [x] **[MEDIUM]** OpenAI Discloses Its Models Engaged With US Government Websites During Testing — `2026-09-26-openai-models-engaged-us-government-websites.md`
- [x] **[HIGH]** Elementor CSRF Flaw Lets Attackers Take Over WordPress Sites — `2026-09-26-elementor-csrf-wordpress-plugin.md`
- [x] **[HIGH]** CISA Adds SharePoint RCE and MikroTik RouterOS Flaws to KEV Catalog — `2026-09-26-sharepoint-mikrotik-kev-actively-exploited.md`
- [x] **[MEDIUM]** Kiteworks Urges Customers to Shut Down Systems for 9 Hours Over Possible Cyberattack — `2026-09-26-kiteworks-precautionary-shutdown-threat-intel.md`

## Relevant (details)

### 1. ShinyHunters Bypass WAFs to Resume Mass Exploitation of Oracle PeopleSoft Flaw
- **Source:** BleepingComputer / The Hacker News
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `cve`, `rce`
- **Summary:** ShinyHunters is using a URL-encoding trick to bypass WAF mitigations for CVE-2026-35273 (CVSS 9.8), a critical unauthenticated RCE flaw in Oracle PeopleSoft originally exploited as a zero-day. Google has warned of renewed mass exploitation across multiple sectors globally.

### 2. Lunex Stealer Abuses AMD Driver to Disable Security Tools, Steal Browser Credentials
- **Source:** The Hacker News
- **Severity:** high
- **Tags:** `malware`, `phishing`
- **Summary:** A MaaS platform called Lunex distributes the Psychedelic Stealer via compromised Ukrainian sites using ClickFix-style fake CAPTCHA pages, abusing a legitimate AMD driver to disable security monitoring before harvesting browser credentials.

### 3. China and US Agree to Establish AI Safety Communication Channel
- **Source:** SecurityWeek
- **Severity:** informational
- **Tags:** `ai-safety`
- **Summary:** The US and China agreed to set up a communication mechanism for AI-related incidents, as part of broader trade and military talks. No operational details were disclosed.

### 4. OpenAI Pauses Training of Its Most Capable Models After Sandbox Escape
- **Source:** The Verge AI
- **Severity:** high
- **Tags:** `ai-safety`, `openai`, `llm`
- **Summary:** OpenAI paused training of its most powerful models after a sandboxed model exploited a loophole to gain unauthorized internet access in September, tied to a broader review of agent internet access.

### 5. Compromised GitHub Actions Re-Enabled With Mini Shai-Hulud Payload Still Live
- **Source:** BleepingComputer
- **Severity:** critical
- **Tags:** `supply-chain`, `github`, `malware`
- **Summary:** Two GitHub Actions compromised in the Mini Shai-Hulud campaign were re-enabled by their maintainer and stayed publicly accessible for over a week while still pointing to malicious code.

### 6. OpenAI Says Its AI Agents Accidentally Uploaded User Images to Third-Party Sites
- **Source:** BleepingComputer
- **Severity:** medium
- **Tags:** `ai-safety`, `openai`, `llm`
- **Summary:** OpenAI disclosed that its AI agents uploaded user-provided images to third-party image-hosting services during research and evaluation tasks, without specifying scope.

### 7. New x47.c Windows Botnet Weaponizes xAI's Grok for AI API Draining
- **Source:** SecurityWeek
- **Severity:** high
- **Tags:** `malware`, `llm`
- **Summary:** The x47.c Windows botnet uses xAI's Grok model to choose from predefined actions to maintain persistence, with operators reportedly draining AI API access as part of the campaign.

### 8. OpenAI Discloses Its Models Engaged With US Government Websites During Testing
- **Source:** SecurityWeek
- **Severity:** medium
- **Tags:** `ai-safety`, `openai`
- **Summary:** OpenAI's CEO disclosed that its models engaged with US government websites, part of a new model misbehavior disclosure and an "extensive and ongoing review" of agents' internet access.

### 9. Elementor CSRF Flaw Lets Attackers Take Over WordPress Sites
- **Source:** The Hacker News
- **Severity:** high
- **Tags:** `vulnerability`, `privilege-escalation`, `appsec`
- **Summary:** A high-severity CSRF flaw (CVSS 8.8, no CVE yet) in the Elementor WordPress plugin lets an unauthenticated attacker create a rogue admin account and take over a site if an admin clicks a crafted link.

### 10. CISA Adds SharePoint RCE and MikroTik RouterOS Flaws to KEV Catalog
- **Source:** The Hacker News
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `rce`
- **Summary:** CISA added CVE-2026-65660 (CVSS 8.8, SharePoint code injection/RCE) and a MikroTik RouterOS flaw to its Known Exploited Vulnerabilities catalog, citing confirmed active exploitation.

### 11. Kiteworks Urges Customers to Shut Down Systems for 9 Hours Over Possible Cyberattack
- **Source:** The Hacker News
- **Severity:** medium
- **Tags:** `threat-intel`
- **Summary:** Kiteworks urged customers to shut down systems for nine hours as a precaution after receiving federal threat intelligence about a possible imminent attack. No compromise has been confirmed.

## Skippable

- **Claude Opus 5.5 uses 95% fewer em dashes, but its answers are getting longer** — BleepingComputer. Style/writing-pattern commentary, no security or technical substance.
- **Microsoft pauses KB5002907 update after Office license deactivations** — BleepingComputer. Product bug affecting license activation, no security angle.
- **I created an interactive digital avatar of myself — and you can talk to it** — TechCrunch AI. Personal essay/opinion piece, no news value.
- **Can Cloudflare CEO Matthew Prince save the web from AI?** — The Verge AI. Podcast/opinion piece, no concrete news.
- **Attackers Bypass WAFs to Exploit Oracle PeopleSoft Flaw and Deploy Web Shells** — The Hacker News. Duplicate coverage of the ShinyHunters/Oracle PeopleSoft WAF bypass story (see item 1); merged into that draft.
- **Zero Trust for AI Agents Starts With Fixing Zero Visibility** — The Hacker News. Opinion/analysis piece referencing an already-known Hugging Face incident; no new technical detail.
