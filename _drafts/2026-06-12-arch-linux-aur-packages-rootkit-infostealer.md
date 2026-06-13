---
title: "400+ Arch Linux AUR Packages Compromised With Rootkit and Infostealer"
date: 2026-06-12 17:03:55 +0000
categories: [Daily Signal]
tags: [supply-chain, malware, privilege-escalation]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/over-400-arch-linux-packages-compromised-to-push-rootkit-infostealer/
---

More than 400 packages in the Arch User Repository (AUR) have been found
distributing a Linux rootkit and infostealer malware. The malware targets
credentials and access tokens on systems where the compromised packages were
installed.

AUR is a community-maintained repository, and packages installed from it via
AUR helpers don't go through the same review process as Arch's official repos.

Anyone who has installed AUR packages recently should audit their installed
package list against the eventual list of compromised packages, check for
unfamiliar rootkit components, and rotate any credentials or access tokens
stored on affected systems.
