---
title: "Rust Supply Chain Attack Plants Build-Time Malware in Crates with 245M Downloads"
date: 2026-08-20 20:22:35 +0000
categories: [Daily Signal]
tags: [supply-chain, malware, rust, github]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/rust-supply-chain-attack-puts-build.html
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/hackers-poison-arrayref-rust-crate-to-push-infostealer-malware/
---

The Rust Project removed malicious versions of three widely used crates —
arrayref 0.3.10, internment 0.8.7, and append-only-vec 0.1.9 — from
crates.io after a compromised maintainer account published releases
containing a typosquatted dependency. That dependency's build script
downloaded and executed a remote payload during compilation, so any project
that ran `cargo build` against the poisoned versions could have run
attacker code. BleepingComputer reports the payload behaved as an
infostealer. Combined, the three crates have roughly 245 million downloads.
Developers who built against these versions recently should audit for
compromise and rotate credentials present on affected machines.
