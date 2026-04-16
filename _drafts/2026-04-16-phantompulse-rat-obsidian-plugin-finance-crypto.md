---
title: "PHANTOMPULSE RAT Delivered via Obsidian Plugin Abuse in Targeted Finance and Crypto Attacks"
date: 2026-04-16 11:02:00 +0000
categories: [Daily Signal]
tags: [malware, phishing, rce]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/04/obsidian-plugin-abuse-delivers.html
---

Elastic Security Labs (tracking as REF6598) has documented a novel social engineering
campaign abusing Obsidian, a popular cross-platform note-taking application, as an initial
access vector for a previously undocumented Windows remote access trojan called
PHANTOMPULSE. Targets are individuals in the financial and cryptocurrency sectors.

The technique is notable for exploiting trust in the Obsidian plugin ecosystem rather than
conventional phishing lures or drive-by exploits. Attackers direct victims to install
malicious plugins that load PHANTOMPULSE, granting full remote access to the compromised
host. Finance and crypto personnel who use Obsidian for research or note-taking are the
primary risk group.

Defenders should enforce application allow-listing policies for Obsidian plugin installs,
especially on endpoints with access to trading platforms or cryptocurrency wallets.
