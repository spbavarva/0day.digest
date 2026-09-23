---
title: "Critical Next.js ImageResponse Flaw Can Lead to Server Code Execution via Crafted SVG"
date: 2026-09-23 07:04:40 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, appsec]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/critical-nextjs-imageresponse-flaw-can.html
---

A new security vulnerability in Next.js could allow attackers to run
code on a server via ImageResponse, the feature that generates Open
Graph and other social preview images, Vercel said. The risk applies
when an app puts values an attacker controls, such as text read from
the request URL, into the image.

Vercel, which develops Next.js, fixed the flaw on September 22.
Applications using ImageResponse with any user-influenced input
should update to the patched version.
