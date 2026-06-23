---
title: "FFmpeg Patches PixelSmash Flaw Enabling RCE on Jellyfin and DoS Elsewhere"
date: 2026-06-22 21:05:01 +0000
categories: [Daily Signal]
tags: [rce, vulnerability]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/ffmpeg-fixes-pixelsmash-flaw-in-widely-used-video-decoder/
---

FFmpeg has fixed a flaw dubbed "PixelSmash" in its widely used video decoder.
Under certain conditions the bug can be exploited for remote code execution
on Jellyfin servers, and it can trigger denial-of-service conditions in other
applications that bundle FFmpeg, including Kodi, Emby, Nextcloud, PhotoPrism,
and OBS Studio. Because FFmpeg ships inside so many downstream media
applications, patch timelines will vary by project — check each
application's release notes rather than assuming FFmpeg's own fix covers you.
