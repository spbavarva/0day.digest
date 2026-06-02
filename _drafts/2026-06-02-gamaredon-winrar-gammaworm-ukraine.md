---
title: "Gamaredon Exploits WinRAR CVE-2025-8088 to Deploy GammaWorm and GammaSteel Against Ukraine"
date: 2026-06-02 18:21:00 +0000
categories: [Daily Signal]
tags: [malware, vulnerability, cve, phishing]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/gamaredon-exploits-winrar-to-deliver.html
---

The Russian threat group Gamaredon is actively exploiting CVE-2025-8088, a path traversal vulnerability in WinRAR, to deliver a malware chain targeting Ukraine. The attack begins with a weaponized WinRAR archive that exploits the path traversal flaw to launch GammaPhish, an HTML Application payload, which then retrieves GammaWorm for self-propagation and GammaSteel for data theft. Sekoia researchers attributed the campaign to Gamaredon based on established TTPs. Organizations in Ukraine and allied sectors using WinRAR should apply the relevant patch immediately and review indicators of compromise for this campaign.
