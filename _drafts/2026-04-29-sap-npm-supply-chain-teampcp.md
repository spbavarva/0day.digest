---
title: "Official SAP npm Packages Compromised in TeamPCP Supply-Chain Attack"
date: 2026-04-29 22:43:44 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/official-sap-npm-packages-compromised-to-steal-credentials/
---

Multiple official SAP npm packages were compromised in what researchers attribute to the TeamPCP threat actor, in a supply-chain attack designed to steal developer credentials and authentication tokens. The malicious packages were published under SAP's official npm namespace, making them highly trusted by downstream consumers and CI/CD pipelines.

Developers and pipelines that installed affected versions should treat all credentials and tokens on those systems as compromised and rotate them immediately. Audit package lock files for affected versions and review recent build logs for suspicious outbound connections. This attack follows the established TeamPCP pattern of targeting enterprise developer toolchains through official package namespaces — the same actor was linked to the Bitwarden KICS compromise earlier this month.
