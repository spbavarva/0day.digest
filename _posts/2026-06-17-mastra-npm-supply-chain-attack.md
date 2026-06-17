---
title: "144 Mastra npm Packages Compromised in Supply Chain Attack"
date: 2026-06-17 07:38:24 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, llm, malware]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/144-mastra-npm-packages-compromised-via.html
---

As many as 144 npm packages under the "@mastra/*" namespace — used by the
open-source Mastra framework for building AI applications — were compromised
in a supply chain attack tracked as "easy-day-js." A single hijacked npm
account ("ehindero") was used to mass-publish malicious versions of the
packages. The compromise was jointly identified by JFrog, SafeDep, Socket,
and StepSecurity. Teams depending on Mastra should audit lockfiles for
affected versions, rotate credentials exposed to build environments that
pulled the packages, and pin to known-good releases until the namespace is
confirmed clean.
