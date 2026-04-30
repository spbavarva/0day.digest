---
title: "Vect 2.0 Ransomware Behaves as Wiper Due to Encryption Design Flaw"
date: 2026-04-29 15:23:53 +0000
categories: [Daily Signal]
tags: [ransomware, malware, supply-chain]
severity: high
must_know: false
sources:
  - name: Dark Reading
    url: https://www.darkreading.com/threat-intelligence/vect-ransomware-wiper-design-error
---

Vect 2.0 ransomware, deployed against victims of the TeamPCP supply chain attacks, was found to permanently destroy data rather than encrypt it for ransom due to a design error in its file-handling logic. The malware's encryption implementation is broken, meaning no valid decryptor exists even if a ransom payment is made.

Victims of the TeamPCP supply chain incident who were subsequently hit with Vect 2.0 should not pay any ransom demand — recovery must come from backups. The wiper behavior compounds the supply chain attack's impact: organizations already compromised via the initial vector now face potential data destruction rather than recoverable encryption. Incident responders should verify whether affected systems retain viable backup snapshots before negotiating.
