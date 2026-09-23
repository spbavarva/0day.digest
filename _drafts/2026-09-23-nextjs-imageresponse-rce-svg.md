---
title: "Critical Next.js ImageResponse Flaw Enables Server RCE via Crafted SVG"
date: 2026-09-23 07:04:40 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, appsec]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/critical-nextjs-imageresponse-flaw-can.html
---

A critical vulnerability in Next.js's ImageResponse feature, used to
generate Open Graph and social preview images, can lead to
server-side code execution. The risk applies when an application
feeds attacker-controlled values, such as text from a request URL,
into the generated image.

Vercel fixed the flaw on September 22. Teams using ImageResponse with
user-controlled input should update Next.js immediately; no active
exploitation has been reported.
