---
title: "'Pack2TheRoot' PackageKit Race Condition Lets Unprivileged Linux Users Escalate to Root"
date: 2026-04-27 10:10:14 +0000
categories: [Daily Signal]
tags: [vulnerability, privilege-escalation, cve]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/easily-exploitable-pack2theroot-linux-vulnerability-leads-to-root-access/
---

A race condition vulnerability dubbed "Pack2TheRoot" in PackageKit, the Linux package management middleware, allows unprivileged local users to escalate to root. Researchers describe the bug as easily exploitable.

PackageKit is present across major Linux distributions including Fedora, Ubuntu, and openSUSE. Its role as a mechanism to install software without direct root access makes it a high-value local privilege escalation target. Patch PackageKit installations promptly; in environments where local privilege escalation is in the threat model, consider restricting PackageKit access to privileged users until patched.
