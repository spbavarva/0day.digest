---
title: "Microsoft Tests New Edge Lockdown Mode That Disables GPU APIs"
date: 2026-11-19 11:46:00 +0000
categories: [Daily Signal]
tags: [appsec, microsoft]
severity: informational
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/microsoft/microsoft-tests-new-edge-lockdown-mode-that-disables-gpu-apis/
---

Microsoft is developing a new Edge security feature called Lockdown Mode
that reduces the browser's attack surface by disabling the WebGL, WebGL2,
and WebGPU APIs. These GPU-exposed APIs have been a recurring source of
browser exploit primitives, so removing them trades some rendering
capability for a smaller attack surface. The feature is in testing and not
yet available to all users.
