---
title: "Two Critical Wasmtime Flaws Allow Sandbox Escape via Malicious WebAssembly Modules"
date: 2026-10-26 11:52:41 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, rce]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/two-critical-wasmtime-flaws-could-let.html
---

Two critical vulnerabilities in Wasmtime, a WebAssembly runtime embedded in
other software, could let a malicious WebAssembly module escape its
intended sandbox.

Exploitation requires an attacker-controlled build compiled against a
vulnerable Wasmtime version, and one of the two flaws affects only ARM64
systems. The maintainers have released fixed versions. Projects embedding
Wasmtime should update immediately.
