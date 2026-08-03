# Digest — 2026-08-03 AM

- Window: last 14h
- Raw items considered: 11
- Relevant: 8
- Skippable: 3

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[MEDIUM]** Novel Attack Surface Found in Passwordless Authentication — `2026-08-03-passkey-mfa-bypass-attack-surface.md`
- [x] **[HIGH]** Midnight Blizzard Linked to Public Wi-Fi Gateway Credential Theft — `2026-08-03-midnight-blizzard-wifi-gateway-credential-theft.md`
- [x] **[HIGH]** Iran-Linked Water Utility Cyberattacks Expand to 7 US States — `2026-08-03-us-water-utility-cyberattacks-expand.md`
- [x] **[MEDIUM]** Thermo Fisher Patches DNA File Tampering Flaw — `2026-08-03-thermo-fisher-dna-file-tampering-cve-2026-17583.md`
- [x] **[CRITICAL]** N-able: Attackers Bypassed Incomplete Fix for N-central Auth Flaw — `2026-08-03-n-able-n-central-auth-bypass-cve-2026-18577.md`
- [x] **[HIGH]** Hugging Face Diffusers Flaws Allow Arbitrary Code Execution via Model Repos — `2026-08-03-huggingface-diffusers-rce-flaws.md`
- [x] **[INFORMATIONAL]** OpenAI Teases Astra, Its Next Major AI Model — `2026-08-02-openai-teases-astra-model.md`
- [x] **[CRITICAL]** COLDCARD Wallet RNG Flaw Likely Linked to $88M Bitcoin Theft — `2026-08-02-coldcard-wallet-rng-flaw-bitcoin-theft.md`

## Relevant (details)

### 1. Novel Attack Surface Found in Passwordless Authentication
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/passwordless-authentication-security-risks/
- **Severity:** medium
- **Tags:** `vulnerability`, `appsec`, `authentication`
- **Summary:** Unit 42 researchers describe how relying parties that fail to validate the "User Verified" flag during passkey ceremonies reduce passwordless MFA to a single factor. The gap applies broadly across FIDO2/WebAuthn deployments rather than one product.

### 2. Midnight Blizzard Linked to Public Wi-Fi Gateway Credential Theft
- **Source:** SecurityWeek — https://www.securityweek.com/russian-state-apt-linked-to-recent-public-wi-fi-gateway-hacking/
- **Severity:** high
- **Tags:** `microsoft`, `apt`
- **Summary:** Russian state actor Midnight Blizzard has been stealing Microsoft account credentials via compromised public Wi-Fi at hospitality venues. The campaign targets travelers rather than a single organization's network.

### 3. Iran-Linked Water Utility Cyberattacks Expand to 7 US States
- **Source:** SecurityWeek — https://www.securityweek.com/us-water-cyberattacks-extend-beyond-minnesota-to-at-least-6-other-states/
- **Severity:** high
- **Tags:** `critical-infrastructure`
- **Summary:** Cyberattacks on US water utilities attributed to Iran-linked actors have spread beyond Minnesota to at least six more states, including Michigan, South Dakota, and Georgia. No operational impact at the additional utilities has been confirmed.

### 4. Thermo Fisher Patches DNA File Tampering Flaw
- **Source:** The Hacker News — https://thehackernews.com/2026/08/thermo-fisher-patches-flaw-that-could.html
- **Severity:** medium
- **Tags:** `vulnerability`, `cve`
- **Summary:** Thermo Fisher patched CVE-2026-17583 in its Applied Biosystems human identification software, which could allow forensic DNA data files to be tampered with nearly undetectably. The tampering requires lab controls to be circumvented first.

### 5. N-able: Attackers Bypassed Incomplete Fix for N-central Auth Flaw
- **Source:** The Hacker News — https://thehackernews.com/2026/08/n-able-says-attackers-take-over-n.html
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`
- **Summary:** Attackers exploited an authentication bypass (CVE-2026-18577) in N-able's N-central RMM platform to gain admin access after the vendor's initial fix proved incomplete. N-central is used by MSPs, so compromise can cascade to customer systems.

### 6. Hugging Face Diffusers Flaws Allow Arbitrary Code Execution via Model Repos
- **Source:** The Hacker News — https://thehackernews.com/2026/08/hugging-face-diffusers-flaws-could-let.html
- **Severity:** high
- **Tags:** `supply-chain`, `rce`, `llm`
- **Summary:** Three high-severity flaws in Hugging Face's Diffusers library let malicious model repositories bypass `trust_remote_code` and execute arbitrary code on machines that load them. This extends the AI supply chain's attack surface to model repo files themselves.

### 7. OpenAI Teases Astra, Its Next Major AI Model
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/artificial-intelligence/openai-teases-astra-its-next-major-ai-model-after-it-solves-10-long-standing-math-problems/
- **Severity:** informational
- **Tags:** `openai`, `ai-launch`, `model-release`
- **Summary:** OpenAI teased Astra, an unreleased model for complex, long-running tasks, saying an internal version produced ten notable math and theoretical CS advances. No release date has been announced.

### 8. COLDCARD Wallet RNG Flaw Likely Linked to $88M Bitcoin Theft
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/coldcard-wallet-rng-flaw-likely-linked-to-88-million-bitcoin-theft/
- **Severity:** critical
- **Tags:** `vulnerability`, `cryptocurrency`
- **Summary:** A flawed random number generator in COLDCARD hardware wallet firmware is likely linked to the theft of an estimated $88.6 million in Bitcoin from thousands of affected wallets. The flaw allowed attackers to predict or reconstruct private keys from weak seed generation.

## Skippable

- **A Marc Benioff-backed startup thinks AI can solve the AI deployment problem** — TechCrunch AI. Startup funding announcement with no security angle.
- **condense-json 1.0** — Simon Willison. Minor personal library release note, no security or major AI substance.
- **Sam Altman and AI's decel debate** — TechCrunch AI. Opinion/podcast commentary without news value.
