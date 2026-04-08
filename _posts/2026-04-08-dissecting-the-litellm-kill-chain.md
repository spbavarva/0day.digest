---
title: "Dissecting the LiteLLM Kill Chain"
date: 2026-04-08 20:00:00 +0000
categories: [Threat Research]
tags: [supply-chain, pypi, llm, malware-analysis]
---

The LiteLLM compromise that landed on PyPI yesterday is a textbook example of
the "trust gradient" attack: a popular OSS package, a maintainer who reuses
credentials across services, and a build pipeline that publishes whatever the
maintainer pushes. Here's the kill chain reconstructed from the artifacts that
have surfaced so far.

## 1. Initial access — credential reuse

The attackers ("TeamPCP") got into the maintainer's PyPI account through a
password reused on a smaller forum that was breached six months ago. PyPI's 2FA
was enabled but the attacker had a stolen recovery code from the same dump.
Lesson one: recovery codes are credentials. Treat them like root passwords.

## 2. Staging — silent prerelease

Rather than publish a malicious version directly, the attackers first uploaded
two normal-looking patch versions (`1.82.6` and `1.82.6-post1`) to verify their
publish access without tripping any alarms. These passed unnoticed for ~18 hours.

## 3. Payload delivery — targeted infostealer

The malicious payload landed in `1.82.7` and `1.82.8`. It used a familiar but
effective trick: a `setup.py` post-install hook that imports a module from
`litellm/_internal/_telemetry.py`. That file was new, base64-encoded, and only
ran when imported in a Python REPL or Jupyter context (i.e., a developer
machine, not a production container).

The payload itself walked common secret locations:

```python
TARGETS = [
    "~/.aws/credentials",
    "~/.ssh/id_rsa",
    "~/.config/gcloud/credentials.db",
    "~/.netrc",
    "./.env",
    "./.env.local",
]
```

…and exfiltrated to a Cloudflare Workers endpoint disguised as an analytics
domain. Total dwell time before detection: roughly 14 hours.

## 4. Detection and rollback

A security researcher running PyPI release diff monitoring flagged the new
`_telemetry.py` file. PyPI yanked both versions within 90 minutes of the
report; the maintainer rotated credentials and force-rolled to `1.82.9`.

## What to do

- **Pin exact versions** with hashes (`pip install --require-hashes`).
- **Run installs in ephemeral containers**, not on dev laptops.
- **Audit `pip install` egress** — there's no good reason for a package to
  phone home to a Workers endpoint at install time.
- **Rotate any credential** that may have been on disk on a machine that
  installed `litellm` 1.82.7 or 1.82.8 in the last 48 hours.

The takeaway is uncomfortable: nothing about this attack required a 0day or
sophisticated tradecraft. It worked because supply chain trust is still mostly
vibes.
