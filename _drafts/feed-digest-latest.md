# Digest — 2026-05-16 PM

- Window: last 14h
- Raw items considered: 6
- Relevant: 3
- Skippable: 3

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Funnel Builder WordPress Plugin Flaw Actively Exploited for WooCommerce Payment Skimming — `2026-05-16-funnel-builder-woocommerce-skimmer-active-exploit.md`
- [x] **[CRITICAL]** PoC Published for Critical NGINX Vulnerability Patched This Week — `2026-05-16-nginx-critical-vulnerability-poc-published.md`
- [x] **[HIGH]** Secret Blizzard Evolves Kazuar Backdoor into Modular P2P Botnet — `2026-05-16-secret-blizzard-kazuar-p2p-botnet.md`

## Relevant (details)

### 1. Funnel Builder WordPress Plugin Flaw Actively Exploited for WooCommerce Payment Skimming
- **Source:** The Hacker News — https://thehackernews.com/2026/05/funnel-builder-flaw-under-active.html
- **Severity:** critical
- **Tags:** `xss`, `vulnerability`, `appsec`, `zero-day`
- **Summary:** A critical, CVE-less vulnerability in the Funnel Builder WordPress plugin is under active exploitation, injecting malicious JavaScript into WooCommerce checkout pages to skim payment card data. Sansec published details this week; store operators should audit checkout pages and deactivate the plugin until a patch is confirmed.

### 2. PoC Published for Critical NGINX Vulnerability Patched This Week
- **Source:** SecurityWeek — https://www.securityweek.com/poc-code-published-for-critical-nginx-vulnerability/
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`
- **Summary:** A critical NGINX flaw reportedly present since 2008 was patched this week in NGINX Plus and open source. PoC code is now public, shortening the window before opportunistic exploitation begins; administrators should patch immediately.

### 3. Secret Blizzard Evolves Kazuar Backdoor into Modular P2P Botnet
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/russian-hackers-turn-kazuar-backdoor-into-modular-p2p-botnet/
- **Severity:** high
- **Tags:** `malware`, `vulnerability`, `nation-state`
- **Summary:** Russian APT Secret Blizzard has re-architected its Kazuar backdoor as a modular P2P botnet, eliminating centralized C2 and improving resilience against takedowns. The upgrade reflects a longer-term investment in persistence and durable collection infrastructure.

## Skippable

- **Quoting Julia Evans** — Simon Willison. CSS learning reflection quote; no security or AI news value.
- **Sony tries to explain that its AI Camera Assistant doesn't suck** — The Verge AI. Consumer camera feature clarification; no security angle, not a model launch or AI safety issue.
- **OpenAI co-founder Greg Brockman reportedly takes charge of product strategy** — TechCrunch AI. Internal org reshuffling; no model release, technical capability, or security substance.
