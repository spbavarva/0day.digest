---
title: "Researchers Demonstrate Ghostscript Sandbox-Escape RCE via Crafted File Uploads in Popular Apps"
date: 2026-11-22 05:03:41 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, appsec]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/researchers-demonstrate-ghostscript.html
---

Security firm pwn.ai demonstrated a now-patched Ghostscript flaw that lets
a crafted file escape the interpreter's security sandbox and execute
commands on the server processing it. Ghostscript is widely used on Linux
servers to convert uploaded PDFs, PostScript files, and images, often
invoked indirectly by other applications rather than called directly.

Because the conversion step is frequently hidden behind ordinary file
upload features, apps that don't call Ghostscript directly may still be
exposed. The flaw has already been patched upstream.
