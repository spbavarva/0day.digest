---
layout: research-post
title: "Trinity of Chaos: Anatomy of the ShinyHunters Data-Extortion Machine"
date: 2026-06-15
categories: [Threat Research]
tags: [data-breach, shinyhunters, salesforce, snowflake, oauth, vishing, phishing, cloud-security, iam, detection]
toc: true
read_time: true
author: Sneh Bavarva
excerpt: "Since 2019, ShinyHunters has gone from selling scraped databases on RaidForums to running the largest SaaS data-extortion operation in history — 300+ breaches, 90+ named victims, and well over a billion records. This is the full profile: the 2020–2026 timeline, the complete victim roster (Tokopedia → Snowflake → Salesforce → Canvas), the three repeatable techniques, the Instructure kill chain, IOCs, and detection."
---

## Executive Summary

There is no implant to reverse-engineer here. **ShinyHunters** is a data-theft and extortion crew whose entire kill chain lives in the **identity, OAuth, and misconfiguration layer** — phone calls, consent screens, stolen tokens, and over-permissioned portals, not droppers and C2. That is precisely what makes it hard to stop: most of it is *authorized* traffic from the victim's own users and trusted third-party apps. CVE scanners have no surface to detect.

Active **since 2019** ("rooting your systems since '19," per their own ransom notes), the group has evolved through four distinct eras: **forum-era database theft** (2020–2023), the **Snowflake credential-replay wave** (2024, ~165 orgs), the **Salesforce vishing campaign + supergroup formation** (2025), and **industrialized SaaS extortion** (2026). Along the way ShinyHunters became the founding core of the **Scattered Lapsus$ Hunters (SLH)** supergroup — an alliance with **Scattered Spider** and **LAPSUS$** that styles itself the **"Trinity of Chaos"** under the parent brand **ShinyCorp**.

By most counts the group is now linked to **300+ breaches and 90+ named organizations**, with **2026 alone** accounting for **40+ orgs and 400M+ people** — anchored by the **275-million-record Instructure / Canvas** breach. This post consolidates [Mandiant/GTIG](https://cloud.google.com/blog/topics/threat-intelligence/expansion-shinyhunters-saas-data-theft), [Push Security](https://pushsecurity.com/blog/analyzing-the-instructure-breach), [Black Kite](https://blackkite.com/blog/shinyhunters-and-the-salesforce-experience-cloud-campaign-how-misconfigured-portals-create-supply-chain-risk), and [SOCRadar](https://socradar.io/blog/dark-web-profile-shinyhunters/) into one profile.

> **Record counts below are frequently attacker claims** posted to extortion sites and are often larger than what victims later confirm. Treat them as upper bounds, flagged where known.

---

## Actor Profile

| | |
|---|---|
| **Names / aliases** | ShinyHunters, ShinyCorp; founding member of **Scattered Lapsus$ Hunters (SLH)** / "Trinity of Chaos" |
| **Mandiant clusters** | **UNC6040** (Salesforce vishing), **UNC6395** (Salesloft/Drift OAuth), **UNC6661 / UNC6671** (2026 vishing access), **UNC6240** (extortion/negotiation) |
| **Active since** | 2019 (forum sales 2020) |
| **Allies** | Scattered Spider (UNC3944), LAPSUS$ |
| **Forums / leak sites** | RaidForums → BreachForums V1 → **BreachForums V2** (group-run) → "SHINYHUNTERS" DLS |
| **Motive** | Financial — data theft + "pay-or-leak" extortion (no encryption ransomware) |
| **Law enforcement** | Sébastien Raoult ("Sezyo Kaizen") arrested 2022, sentenced 2024 (~3 yrs, $5M restitution); BreachForums seized by US/French LE, Oct 2025 — **operations continued**, confirming a distributed structure |

---

## Timeline

### Era 1 — Forum-era database theft (2020–2023)

| Date | Victim | Scale (claimed) | Method |
|---|---|---|---|
| Jan 2020 | Mathway | ~25M | Data theft, sold on dark web |
| May 2020 | **Tokopedia** | 91M | Unsecured infrastructure |
| May 2020 | **Microsoft private GitHub** | ~500GB sampled | Repo access (MS disputed impact) |
| 2020 | Wattpad | 271M | Credential/DB theft |
| 2020 | Unacademy / BigBasket / Wishbone / Bonobos | 22M / 20M / — / 7M | DB theft, forum sales |
| Jan 2021 | Pixlr / NitroPDF / MeetMindful | 1.9M / 77M / 2.28M | Unsecured AWS buckets |
| Aug 2022 | **AT&T** | 73M (SSN/DOB) | Reposted on BreachForums 2024 |
| Sep 2023 | Pizza Hut Australia | 30M orders | Unauthorized AWS access |

### Era 2 — Snowflake credential replay (2024)

Account-takeover against **~165 Snowflake customer tenants lacking MFA**, using credentials harvested from infostealer infections dating back to 2020.

| Victim | Scale (claimed) |
|---|---|
| **Ticketmaster** | 560–590M |
| **AT&T** | call/text records ~110M |
| **Santander** | 30M |
| Advance Auto Parts, LendingTree, Neiman Marcus, Bausch Health | various |

### Era 3 — Salesforce vishing + supergroup (2025)

Vishing → Salesforce OAuth abuse (**UNC6040**) and OAuth supply-chain token theft via **Salesloft/Drift** (**UNC6395**). The crew formed the **SLH supergroup in Aug 2025**; one ransom note claimed **91 orgs** compromised.

| Sector | Victims |
|---|---|
| Tech | **Google** (corp Salesforce), **Cisco**, **Workday** |
| Aviation | **Qantas**, **Air France–KLM** |
| Luxury | **LVMH** (Louis Vuitton, Dior, Tiffany & Co.), **Chanel**, **Cartier**, **Pandora** |
| Apparel/Insurance | **Adidas**, **Allianz Life** |

> **Oct 2025:** BreachForums seized by US/French law enforcement; SLH doxxes ICE/DHS/FBI/DOJ officials. Operations continued via Telegram + DLS.

### Era 4 — Industrialized SaaS extortion (2026)

| Date | Victim | Scale (claimed) | Method |
|---|---|---|---|
| Jan 2026 | Mandiant tracks **UNC6661/6671/6240**; **37.5×** device-code phishing spike; new SHINYHUNTERS DLS | — | — |
| Mar 2026 | Salesforce **Experience Cloud** wave (weaponized **AuraInspector**) | "hundreds" of orgs | Guest-access misconfig |
| Apr 1 | **Charter Communications** | 4.9M | Vishing → MS Entra account |
| Apr 14 | [McGraw-Hill](https://spbavarva.github.io/0day.digest/posts/mcgraw-hill-shinyhunters-salesforce-45m-records/) | 45M (≈13.5M confirmed) | Salesforce misconfig |
| Apr 24 | **ADT** | 5.5M | Vishing → Okta SSO |
| Apr 28 | [Medtronic](https://spbavarva.github.io/0day.digest/posts/medtronic-breach-shinyhunters-9m-records/) | 9M | Extortion |
| Apr 29 – May 7 | **Instructure / Canvas** | **275M / 3.65 TB / ~8,800 institutions** | Free-For-Teacher abuse (stage 2; Salesforce foothold Sep 2025) |
| May 2026 | **DentaQuest** | 2.6M (PII + PHI/Medicaid) | Pay-or-leak |
| May 2026 | **Carnival** / **Kemper** | 6M / 13M | Data theft |
| 2026 | **Rockstar Games** / Vimeo / Zara-Inditex | 78.6M / 119K / 197K | **Anodot** OAuth supply chain |
| 2026 | SoundCloud / Panera / Match Group / Betterment | ~30M / ~14M / 10M+ / ~20M | AiTM vishing |
| 2026 | **Telus** | 1+ petabyte | Data theft |
| 2026 | 7-Eleven, Pitney Bowes, Canada Goose, Canada Life, Odido, Figure, **European Commission** | various | Mixed |
| Jun 11 | **Nexstar** | 1.1M Salesforce records | Extortion listing |
| Jun 12 | [Oracle ERP zero-day → US universities](https://spbavarva.github.io/0day.digest/posts/shinyhunters-oracle-zero-day-higher-ed/) | — | Zero-day exploitation |

---

## The Three Techniques

Across all four eras, ShinyHunters reuses a small set of repeatable plays. The 2026 machine runs on three. All three end the same way: a valid, authorized session inside a SaaS tenant → bulk export → extortion.

### 1. Vishing + AiTM phishing
A live caller impersonates IT ("mandatory passkey rollout / compliance update"), pushes the victim to a lookalike SSO page (`<company>sso.com`, `<company>internal.com`, `<company>okta.com`), and **relays credentials + MFA codes in real time** to the real IdP — capturing the session token. Push tracked **400+ domains across 4 infrastructure clusters**. Because the lure arrives by phone, it is **invisible to email-layer anti-phishing**.
> Victims: SoundCloud, Panera, Match Group, Betterment, ADT, Charter.

### 2. Vishing + device-code phishing
The standout. Attackers abuse the **OAuth 2.0 device-authorization flow** — registering a fake app (e.g. spoofing *Salesforce DataLoader*) requesting broad API scopes, then getting the victim to type an attacker-supplied code into a **legitimate** Microsoft/IdP verification page. **This defeats all MFA, including passkeys**, because it attacks the *authorization* layer, not login. Mandiant logged a **37.5× increase** in 2026; the Salesforce wave alone hit **1,000+ orgs / ~1.5B records**.
> Victims: Google, Cisco, Qantas, LVMH, Adidas.

### 3. OAuth supply-chain token theft
Compromise one SaaS vendor, steal its **OAuth/refresh tokens**, pivot into every downstream customer. The 2025 **Salesloft/Drift** compromise was the blueprint (TruffleHog over the vendor's GitHub → Drift tokens → customer Salesforce). The **2026 Anodot** compromise repeated it; Gainsight was also abused.
> Victims: Rockstar (78.6M), Vimeo, Zara/Inditex.

**Plus two persistent surfaces:** **Salesforce Experience Cloud** guest-access abuse (the `/s/sfsites/aura` endpoint, scanned at scale with a weaponized copy of Mandiant's **AuraInspector**), and **infostealer-credential replay** against MFA-less tenants (the 2024 Snowflake playbook).

---

## Deep Dive: Instructure / Canvas

The Canvas breach is the campaign in miniature — **two stages, eight months apart**:

- **Stage 1 (Sep 2025):** Instructure's **Salesforce** business systems breached via social engineering. Quiet, contained, the foothold.
- **Stage 2 (Apr–May 2026):** attackers exploited the **Free-For-Teacher (FFT)** account program to reach **Canvas itself**, exfiltrating **3.65 TB** — names, emails, student IDs, private messages — across **~8,800 institutions** during final-exam season. Instructure pulled Canvas offline on **May 7**, restored it the next day, and **permanently shut down FFT**.

When Instructure shipped "security patches" instead of negotiating, ShinyHunters defaced the login page with this note:

![ShinyHunters ransom note defacing the Canvas login page, May 2026]({{ '/assets/img/posts/shinyhunters-instructure-ransom-note.png' | relative_url }})
_ShinyHunters' Canvas ransom note: "rooting your systems since '19," a `pay_or_leak/` payment path, an `instructure_affected_schools_list.txt` proof file, and a Tox/onion contact. The "did some 'security patches'" jab confirms attacker persistence through remediation — textbook SLH extortion theater._

---

## Indicators of Compromise

| Type | Indicator | Context |
|---|---|---|
| IP (UNC6661) | `24.242.93[.]122`, `23.234.100[.]107`, `73.135.228[.]98`, `149.50.97[.]144` (PL), `67.21.178[.]234` | Vishing / initial access |
| IP (UNC6671) | `142.127.171[.]133`, `76.64.54[.]159`, `76.70.74[.]63`, `206.170.208[.]23`, `68.73.213[.]196` | Parallel access cluster |
| Proxy/VPN | Mullvad, Oxylabs, NetNut, 9Proxy, Infatica, nsocks | Source-IP laundering |
| Domain pattern | `<co>sso[.]com`, `my<co>internal[.]com`, `<co>okta[.]com`, `<co>azure[.]com` | AiTM lures (NICENIC / Tucows reg.) |
| Malicious OAuth app | `ToogleBox Recall` | Deletes Okta "security method enrolled" emails to hide MFA registration |
| Fake OAuth app | spoofed `Salesforce DataLoader` | Device-code consent grant |
| Extortion infra (Canvas) | `91.215.85[.]103/pay_or_leak/`, `shnyhntww34phqoa6dcgnvps2yu7dlwzmy5lkvejwjdo6z7bmgshzayd[.]onion` | Leak site + proof file `instructure_affected_schools_list.txt` |
| Contact | `shinycorp[@]tutanota.com`, `shinygroup[@]onionmail.com`, Tox | Negotiation channels |

*All indicators are defanged. Re-fang only inside controlled threat-intel platforms (MISP, VirusTotal, your SIEM).*

---

## Detection & Hunting

Patch scanners are blind here. Hunt in **identity and SaaS audit logs** instead (adapted from Mandiant's Google SecOps rules):

- **Device-code grants:** alert on OAuth device-authorization consent to apps with broad scopes (`full`, `api`, `offline_access`), especially first-seen app names mimicking known tools (`DataLoader`, `Recall`).
- **Okta admin anomalies:** admin role grants, policy/zone edits, or factor enrollment **from anonymized/VPN IPs** (`mullvad|oxylabs|9proxy|netnut|infatica|nsocks`).
- **MFA-notification deletion:** mailbox `SoftDelete/HardDelete/MoveToDeletedItems` on subjects matching `new (mfa|security method|device) enrolled|registered` — the tell for hidden MFA registration via `ToogleBox Recall`.
- **Bulk SaaS export:** O365/SharePoint `FileDownloaded` via **PowerShell** user-agent; ≥50 files spanning ≥3 document extensions in a short window; Salesforce bulk-API/DataLoader pulls from new IPs.
- **Snowflake/DB legacy:** logins to MFA-less tenants from infostealer-associated IPs; large `COPY INTO`/bulk export jobs.
- **AiTM:** newly registered look-alike domains (`<yourco>sso.com`, `<yourco>internal.com`) via cert-transparency feeds.

**Defenses that actually work:** FIDO2/passkeys *plus* **disabling or tightly scoping the OAuth device-code flow** (passkeys alone do **not** stop technique #2); OAuth app-consent governance and allow-listing; locking down Salesforce Experience Cloud guest profiles (run AuraInspector yourself first); enforcing MFA on every Snowflake/DB tenant; and help-desk identity-verification hardened against vishing.

---

## Myths & Misinformation

**"Passkeys/MFA stop ShinyHunters."** — **FALSE.** Device-code phishing targets the authorization layer and bypasses all MFA, passkeys included. You also need to restrict the device-code flow and govern OAuth consent.

**"It was a Salesforce / Snowflake / Canvas zero-day."** — **MISLEADING.** The overwhelming majority is **misconfiguration + social engineering + stolen tokens** — guest-access misconfig, vishing, MFA-less tenants, OAuth abuse. The Canvas breach abused the Free-For-Teacher *program*, not a memory-corruption bug. (The Jun 2026 Oracle ERP case is the rare genuine zero-day.)

**"Instructure resolved it on May 6."** — **MISLEADING.** Canvas was **re-defaced on May 7** after the "security patches," forcing it offline and the permanent shutdown of FFT.

**"The arrests / BreachForums takedown ended them."** — **FALSE.** Sébastien Raoult's conviction and the Oct 2025 BreachForums seizure barely dented output; the 2026 wave is their most prolific yet. The structure is distributed.

**"ShinyHunters is just Scattered Spider."** — **MISLEADING.** They overlap inside the SLH supergroup and share TTPs, but are distinct lineages; Mandiant tracks separate clusters.

---

## References

1. Mandiant / Google Threat Intelligence — [Tracking the Expansion of ShinyHunters-Branded SaaS Data Theft](https://cloud.google.com/blog/topics/threat-intelligence/expansion-shinyhunters-saas-data-theft)
2. Push Security — [How Three Techniques Are Behind ShinyHunters' 2026 Campaigns (Instructure analysis)](https://pushsecurity.com/blog/analyzing-the-instructure-breach)
3. Black Kite — [ShinyHunters and the Salesforce Experience Cloud Campaign](https://blackkite.com/blog/shinyhunters-and-the-salesforce-experience-cloud-campaign-how-misconfigured-portals-create-supply-chain-risk)
4. SOCRadar — [Dark Web Profile: ShinyHunters](https://socradar.io/blog/dark-web-profile-shinyhunters/) · [Instructure breach: 275M exposed](https://socradar.io/blog/shinyhunters-breach-instructure-students-teachers/)
5. Security Boulevard / Sendmarc — [ShinyHunters: The Group Behind 300+ Breaches](https://securityboulevard.com/2026/05/shinyhunters-the-group-behind-300-breaches/)
6. Computer Weekly — [ShinyHunters Salesforce Cyber Attacks Explained](https://www.computerweekly.com/feature/ShinyHunters-Salesforce-cyber-attacks-explained-What-you-need-to-know)
7. Push Security — [Snowflake: Looking Back on 2024's Landmark Security Event](https://pushsecurity.com/blog/snowflake-retro)
8. TechRadar — [Charter Communications confirms breach](https://www.techradar.com/pro/security/charter-communications-confirms-data-breach-shinyhunters-blamed-after-threat-to-leak-user-info-online) · [DentaQuest 2.6M breach](https://www.techradar.com/pro/security/2-6-million-dentaquest-accounts-exposed-by-data-breach-shinyhunters-claim-234gb-of-data-stolen)
9. Halcyon — [Education Sector in the Crosshairs: ShinyHunters vs Instructure](https://www.halcyon.ai/ransomware-alerts/education-sector-in-the-crosshairs-shinyhunters-extortion-campaign-against-instructure)
10. Bitdefender — [FBI Warns Students and Staff After Canvas Breach](https://www.bitdefender.com/en-us/blog/hotforsecurity/fbi-shinyhunters-canvas-breach)
11. Wikipedia — [Scattered Lapsus$ Hunters](https://en.wikipedia.org/wiki/Scattered_Lapsus$_Hunters) · [2026 Canvas data breach](https://en.wikipedia.org/wiki/2026_Canvas_security_incident)
12. Huntress — [ShinyHunters Threat Actor Profile](https://www.huntress.com/threat-library/threat-actors/shinyhunters)
