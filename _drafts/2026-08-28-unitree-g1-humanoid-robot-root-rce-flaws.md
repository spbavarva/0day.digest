---
title: "Two Unitree G1 Humanoid Robot Flaws Enable Root RCE, One via Bluetooth"
date: 2026-08-28 12:07:24 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, cve]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/two-unitree-g1-edu-humanoid-robot-flaws.html
---

Researcher Olivier Laflamme disclosed two independent root remote code
execution chains affecting the Unitree G1 EDU humanoid robot, tracked as
CVE-2026-76639 and CVE-2026-76640. One chain uses a network-adjacent path
through the robot's chat_go and bashrunner components; the other reaches
root on the robot's Locomotion PC over Bluetooth Low Energy, requiring only
physical proximity rather than network access. Organizations deploying
Unitree G1 EDU robots should apply available patches and restrict
physical/BLE proximity to the devices until fixed.
