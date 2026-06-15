---
layout: research-post
title: "Trinity of Chaos: Anatomy of the ShinyHunters SaaS Extortion Machine"
date: 2026-06-15
categories: [Threat Research]
tags: [data-breach, shinyhunters, salesforce, oauth, vishing, phishing, cloud-security, iam, detection]
toc: true
read_time: true
author: Sneh Bavarva
excerpt: "ShinyHunters doesn't ship malware — it steals identities. Through 2025–2026 the crew (now the core of the Scattered Lapsus$ Hunters 'Trinity of Chaos' supergroup) ran three repeatable plays — AiTM vishing, device-code phishing, and OAuth supply-chain token theft — to drain SaaS tenants at 40+ orgs, peaking with the 275M-record Instructure/Canvas breach. This is the consolidated profile: timeline, the three techniques, the Canvas kill chain, IOCs, and detection."
---

## Executive Summary

There is no implant to reverse-engineer here. **ShinyHunters** is a data-theft and extortion crew whose entire kill chain lives in the **identity and OAuth layer** — phone calls, consent screens, and misconfigured guest access, not droppers and C2. That is exactly what makes it hard to stop: most of it is *authorized* traffic from the victim's own users and trusted third-party apps.

Active **since 2019** ("rooting your systems since '19," per their own ransom notes), the group became the founding core of the **Scattered Lapsus$ Hunters (SLH)** supergroup in August 2025 — an alliance with **Scattered Spider** and **LAPSUS$** that styles itself the **"Trinity of Chaos"** and operates under the parent brand **ShinyCorp**. Across 2026 alone they have claimed **40+ breached organizations** and data on **400M+ people**, anchored by the **275-million-record Instructure / Canvas** breach that knocked the LMS offline during finals.

This post consolidates the [Mandiant/GTIG](https://cloud.google.com/blog/topics/threat-intelligence/expansion-shinyhunters-saas-data-theft), [Push Security](https://pushsecurity.com/blog/analyzing-the-instructure-breach), and [Black Kite](https://blackkite.com/blog/shinyhunters-and-the-salesforce-experience-cloud-campaign-how-misconfigured-portals-create-supply-chain-risk) analyses into one actor profile: the three repeatable techniques, the Canvas kill chain, a defanged IoC table, and deployable detection logic. **No CVE underpins most of this** — it is configuration and social engineering, which is why patch-based defenses miss it entirely.

---

## Timeline

| Date | Event |
|---|---|
| **2019–2021** | ShinyHunters era of bulk database theft and dark-web sales |
| **2024** | Snowflake campaign — infostealer-harvested creds replayed against MFA-less tenants (~165 orgs) |
| **Sep 2025** | Salesforce **Experience Cloud** guest-access campaign begins; **Instructure** business systems breached via social engineering (stage 1) |
| **Aug 2025** | **Scattered Lapsus$ Hunters** supergroup forms ("Trinity of Chaos") |
| **Oct 2025** | BreachForums seized by US/French law enforcement; group keeps operating via Telegram + DLS |
| **Jan 2026** | Mandiant tracks vishing clusters **UNC6661 / UNC6671** (access) + **UNC6240** (extortion); new "SHINYHUNTERS" leak site launches; **37.5× spike** in device-code phishing |
| **Mar 2026** | Large-scale **Salesforce Experience Cloud** extortion wave; weaponized **AuraInspector**; "pay by Mar 14" threats |
| **Apr 14, 2026** | [McGraw-Hill](https://spbavarva.github.io/0day.digest/posts/mcgraw-hill-shinyhunters-salesforce-45m-records/) confirms breach — 45M records via Salesforce misconfig |
| **Apr 24, 2026** | **ADT** breach via vishing → Okta SSO (~5.5M people) |
| **Apr 28, 2026** | [Medtronic](https://spbavarva.github.io/0day.digest/posts/medtronic-breach-shinyhunters-9m-records/) confirms breach — 9M records |
| **Apr 29 – May 7, 2026** | **Instructure / Canvas** breach (stage 2) — Free-For-Teacher abuse; **3.65 TB / ~275M individuals / ~8,800 institutions**; Canvas taken offline May 7, login page defaced with ransom note; FFT program permanently killed |
| **Jun 11, 2026** | **Nexstar** listed — 1.1M Salesforce records, "contact by Jun 14" |
| **Jun 12, 2026** | [Oracle ERP zero-day](https://spbavarva.github.io/0day.digest/posts/shinyhunters-oracle-zero-day-higher-ed/) exploited against US universities |

---

## The Three Techniques

ShinyHunters reuses the same three plays against almost every target. All three end the same way: a valid, authorized session inside a SaaS tenant — then bulk export.

### 1. Vishing + AiTM phishing
A live caller impersonates IT ("mandatory passkey rollout / compliance update"), pushes the victim to a lookalike SSO page (`<company>sso.com`, `<company>internal.com`, `<company>okta.com`), and **relays credentials + MFA codes in real time** to the real IdP — capturing the session token. Push tracked **400+ domains across 4 infrastructure clusters**. Because the lure arrives by phone, it is **invisible to email-layer anti-phishing**.
> Victims: SoundCloud (~30M), Panera (~14M), Match Group (10M+), Betterment (~20M), ADT (5.5M).

### 2. Vishing + device-code phishing
The standout. Attackers abuse the **OAuth 2.0 device-authorization flow** — registering a fake app (e.g. spoofing *Salesforce DataLoader*) requesting broad API scopes, then getting the victim to type an attacker-supplied code into a **legitimate** Microsoft/IdP verification page. **This defeats all MFA, including passkeys**, because it attacks the *authorization* layer, not login. Mandiant logged a **37.5× increase** in this technique in 2026; the Salesforce wave alone hit **1,000+ orgs / ~1.5B records**.
> Victims: Coca-Cola EP, Cisco, Qantas, LVMH, Adidas, Google.

### 3. OAuth supply-chain token theft
Compromise one SaaS vendor, steal its **OAuth/refresh tokens**, pivot into every downstream customer. The 2025 **Salesloft/Drift** compromise was the blueprint (TruffleHog over the vendor's GitHub → Drift tokens → customer Salesforce). The **2026 Anodot** compromise repeated it.
> Victims: Rockstar (78.6M), Vimeo (119K), Zara/Inditex (197K). Also Gainsight.

**Recurring surface — Salesforce Experience Cloud:** the `/s/sfsites/aura` endpoint, abused via **misconfigured guest-user access** (guest enabled + object/field read + API access). The group weaponized Mandiant's own **AuraInspector** tool to scan the internet for over-permissioned portals at scale.

---

## Deep Dive: Instructure / Canvas

The Canvas breach is the campaign in miniature — **two stages, eight months apart**:

- **Stage 1 (Sep 2025):** Instructure's **Salesforce** business systems breached via social engineering. Quiet, contained, the foothold.
- **Stage 2 (Apr–May 2026):** attackers exploited the **Free-For-Teacher (FFT)** account program to reach **Canvas itself**, exfiltrating **3.65 TB** — names, emails, student IDs, private messages — across **~8,800 institutions** during final-exam season. Instructure pulled Canvas offline on **May 7**, restored it the next day, and **permanently shut down FFT**.

When Instructure shipped "security patches" instead of negotiating, ShinyHunters defaced the login page with this note:

![ShinyHunters ransom note defacing the Canvas login page, April–May 2026]({{ '/assets/img/posts/shinyhunters-instructure-ransom-note.png' | relative_url }})
_ShinyHunters' Canvas ransom note: "rooting your systems since '19," a `pay_or_leak/` payment path, an `instructure_affected_schools_list.txt` proof file, and a Tox/onion contact. The 12 May 2026 deadline and "did some 'security patches'" jab are textbook SLH extortion theater._

The note itself is intelligence: the taunt about "security patches" confirms attacker persistence *through* remediation, and the `AFFECTED_SCHOOLS.TXT` download is the group's standard proof-of-theft pressure tactic.

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
- **AiTM:** newly registered look-alike domains (`<yourco>sso.com`, `<yourco>internal.com`) — monitor cert-transparency feeds.

**Defenses that actually work against this crew:** FIDO2/passkeys *plus* **disabling or tightly scoping the OAuth device-code flow** (passkeys alone do **not** stop technique #2); OAuth app-consent governance and allow-listing; locking down Salesforce Experience Cloud guest profiles (run AuraInspector yourself first); and help-desk identity-verification procedures hardened against vishing.

---

## Myths & Misinformation

**"Passkeys/MFA stop ShinyHunters."** — **FALSE.** Device-code phishing (technique #2) targets the authorization layer and bypasses all MFA, passkeys included. You also need to restrict the device-code flow and govern OAuth consent.

**"It was a Salesforce / Canvas zero-day."** — **MISLEADING.** The overwhelming majority is **misconfiguration + social engineering** — guest-access misconfig, vishing, stolen OAuth tokens. The Canvas breach abused the Free-For-Teacher *program*, not a memory-corruption bug.

**"Instructure resolved it on May 6."** — **MISLEADING.** Canvas was **re-defaced on May 7** after the "security patches," forcing it offline and the permanent shutdown of FFT.

**"ShinyHunters is just Scattered Spider."** — **MISLEADING.** They overlap inside the SLH supergroup and share TTPs, but are distinct lineages; Mandiant tracks separate clusters (UNC6040/6395 vs. the UNC66xx vishing clusters).

---

## References

1. Mandiant / Google Threat Intelligence — [Tracking the Expansion of ShinyHunters-Branded SaaS Data Theft](https://cloud.google.com/blog/topics/threat-intelligence/expansion-shinyhunters-saas-data-theft)
2. Push Security — [How Three Techniques Are Behind ShinyHunters' 2026 Campaigns (Instructure breach analysis)](https://pushsecurity.com/blog/analyzing-the-instructure-breach)
3. Black Kite — [ShinyHunters and the Salesforce Experience Cloud Campaign](https://blackkite.com/blog/shinyhunters-and-the-salesforce-experience-cloud-campaign-how-misconfigured-portals-create-supply-chain-risk)
4. SOCRadar — [ShinyHunters Breached Instructure: 275 Million Students, Teachers and Staff](https://socradar.io/blog/shinyhunters-breach-instructure-students-teachers/)
5. Halcyon — [Education Sector in the Crosshairs: ShinyHunters' Extortion Campaign Against Instructure](https://www.halcyon.ai/ransomware-alerts/education-sector-in-the-crosshairs-shinyhunters-extortion-campaign-against-instructure)
6. Bitdefender — [FBI Warns Students and Staff After Canvas Breach](https://www.bitdefender.com/en-us/blog/hotforsecurity/fbi-shinyhunters-canvas-breach)
7. Cybersecurity Magazine — [Canvas Hack: Why Did Instructure Pay Ransom to ShinyHunters?](https://cybermagazine.com/news/canvas-hack-why-did-instructure-pay-ransom-to-shinyhunters)
8. Huntress — [ShinyHunters Threat Actor Profile: TTPs, IoCs & Attacks](https://www.huntress.com/threat-library/threat-actors/shinyhunters)
9. Wikipedia — [Scattered Lapsus$ Hunters](https://en.wikipedia.org/wiki/Scattered_Lapsus$_Hunters) · [2026 Canvas data breach](https://en.wikipedia.org/wiki/2026_Canvas_security_incident)
10. Help Net Security — [ShinyHunters Claims New Campaign Targeting Salesforce Experience Cloud Sites](https://www.helpnetsecurity.com/2026/03/11/shinyhunters-salesforce-aura-data-breach/)
