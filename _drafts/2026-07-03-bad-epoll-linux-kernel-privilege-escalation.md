---
title: "New \"Bad Epoll\" Linux Kernel Flaw Lets Unprivileged Users Gain Root, Hits Android"
date: 2026-07-03 19:40:01 +0000
categories: [Daily Signal]
tags: [privilege-escalation, cve, vulnerability, anthropic]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/new-bad-epoll-linux-kernel-flaw-lets.html
---

A newly disclosed Linux kernel flaw dubbed Bad Epoll (CVE-2026-46242) lets an
unprivileged local user escalate to root. It affects Linux desktops,
servers, and Android, and a fix is already out. The bug sits in the same
stretch of kernel code where Anthropic's Mythos model previously flagged a
different, unrelated bug during automated review — Mythos caught one flaw in
that region but missed this one. Admins should prioritize patching affected
Linux and Android systems, especially multi-user or shared hosts where local
privilege escalation matters most.
