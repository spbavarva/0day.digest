---
title: "Apple Patches iOS Bug That Let FBI Recover Deleted Signal Messages via Retained Notifications"
date: 2026-04-22 20:58:58 +0000
categories: [Daily Signal]
tags: [vulnerability, apple, privacy, ios]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/apple-fixes-ios-bug-that-retained-deleted-notification-data/
---

Apple released out-of-band security updates for iOS and iPadOS to fix a Notification Services flaw
where notifications marked for deletion remained stored on-device rather than being purged. The bug
enabled law enforcement to recover deleted Signal messages by accessing the retained notification
data, undermining the deletion guarantees that end-to-end encrypted messaging apps rely on.

The flaw affects the OS-level handling of ephemeral notification content, not Signal itself. Users
should update to the latest iOS and iPadOS versions immediately. Developers building privacy-sensitive
apps that depend on notification deletion semantics should verify behavior on updated devices.
