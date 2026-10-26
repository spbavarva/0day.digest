---
title: "Two Critical Wasmtime Flaws Could Let WebAssembly Modules Escape Sandboxes"
date: 2026-10-26 11:52:41 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, privilege-escalation]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/two-critical-wasmtime-flaws-could-let.html
---

Two critical flaws in Wasmtime, a WebAssembly runtime that can be embedded
in other software, could let a malicious WebAssembly module escape the
sandbox meant to contain it, the project's maintainers say.

Exploitation requires an attacker to compile a module for a vulnerable
Wasmtime build, and one of the two flaws affects only ARM64 systems. Fixed
versions have been released.
