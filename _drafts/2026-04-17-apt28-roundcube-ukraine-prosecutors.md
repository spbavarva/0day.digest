---
title: "APT28 Exploits Roundcube Webmail to Target Ukrainian Prosecutors and Anti-Corruption Agencies"
date: 2026-04-17 14:12:00 +0000
categories: [Daily Signal]
tags: [rce, phishing, apt]
severity: high
must_know: false
sources:
  - name: The Record (Recorded Future)
    url: https://therecord.media/ukraine-confirms-suspected-apt28-campaign-targeting-prosecutors
---

Ukraine has confirmed an APT28 (Russian GRU) campaign targeting prosecutors and anti-corruption
agencies via vulnerabilities in the Roundcube open-source webmail platform. The attack executes
malicious code when a victim simply opens a malicious email in Roundcube — requiring no additional
user interaction beyond opening the message.

Roundcube is widely deployed in government and enterprise environments, particularly across Eastern
Europe. The near-zero-click attack vector makes this an urgent patching priority. The targeting of
anti-corruption and prosecutorial bodies fits an established Russian intelligence pattern of
monitoring and undermining oversight mechanisms in Ukraine and neighboring states.

Organizations running Roundcube should immediately apply all available patches and review server
logs for signs of exploitation. Restricting external email delivery to Roundcube instances and
enabling enhanced logging on webmail servers is advised pending full remediation.
