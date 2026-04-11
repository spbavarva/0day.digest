---
title: "Citizen Lab: Law Enforcement Used Webloc to Track 500 Million Devices via Ad Data"
date: 2026-04-11 06:02:00 +0000
categories: [Daily Signal]
tags: [surveillance, privacy, data-breach]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/04/citizen-lab-law-enforcement-used-webloc.html
---

Citizen Lab published findings on Webloc, a commercial geolocation surveillance system
built on advertising bid-stream data, used by Hungarian domestic intelligence, El
Salvador's national police, and multiple U.S. law enforcement agencies. The tool was
developed by Israeli firm Cobwebs Technologies and is now sold by Penlink following the
two companies' merger in July 2023. Webloc reportedly tracked approximately 500 million
devices globally without requiring device compromise — relying instead on data harvested
from advertising networks. The exposure highlights that advertising SDKs embedded in
ordinary mobile apps can feed commercial surveillance products purchased by governments.
Practitioners in privacy-sensitive environments should audit third-party SDK inclusions
and consider the downstream use of location data they collect or transmit.
