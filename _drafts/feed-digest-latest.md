# Digest — 2026-07-04 AM

- Window: last 14h
- Raw items considered: 5
- Relevant: 2
- Skippable: 3

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** Unpatched Flaws Disclosed in Filesystem Bundled Into Millions of Embedded Devices — `2026-07-03-fatfs-filesystem-flaws-embedded-devices.md`
- [x] **[HIGH]** New "Bad Epoll" Linux Kernel Flaw Lets Unprivileged Users Gain Root, Hits Android — `2026-07-03-bad-epoll-linux-kernel-privilege-escalation.md`

## Relevant (details)

### 1. Unpatched Flaws Disclosed in Filesystem Bundled Into Millions of Embedded Devices
- **Source:** The Hacker News — https://thehackernews.com/2026/07/unpatched-flaws-disclosed-in-filesystem.html
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `supply-chain`, `embedded-security`
- **Summary:** runZero disclosed seven unpatched vulnerabilities in FatFs, a filesystem library embedded in firmware across security cameras, drones, industrial controllers, and hardware crypto wallets. The flaws matter because of FatFs's broad footprint across millions of embedded devices.

### 2. New "Bad Epoll" Linux Kernel Flaw Lets Unprivileged Users Gain Root, Hits Android
- **Source:** The Hacker News — https://thehackernews.com/2026/07/new-bad-epoll-linux-kernel-flaw-lets.html
- **Severity:** high
- **Tags:** `privilege-escalation`, `cve`, `vulnerability`, `anthropic`
- **Summary:** CVE-2026-46242 ("Bad Epoll") lets an unprivileged local user gain root on Linux and Android; a fix is already available. The flaw sits in kernel code where Anthropic's Mythos model previously caught a different, unrelated bug but missed this one.

## Skippable

- **Open Source AI Gap Map** — Simon Willison. Coverage of a third-party index/dataset project cataloging open source AI products; no security angle and not a lab launch.
- **Quoting Josh W. Comeau** — Simon Willison. Opinion/commentary from a course creator about declining sales attributed to AI; no news or security value.
- **The only AI glossary you'll need this year** — TechCrunch AI. Reference/explainer content defining AI terminology; no news value.
