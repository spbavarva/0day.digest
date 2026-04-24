---
title: "Anthropic Launches Personal App Connectors for Claude: Spotify, Uber, TurboTax, and More"
date: 2026-04-24 22:27:00 +0000
categories: [Daily Signal]
tags: [anthropic, ai-launch]
severity: informational
must_know: false
sources:
  - name: The Verge AI
    url: https://www.theverge.com/ai-artificial-intelligence/917871/anthropic-claude-personal-app-connectors
---

Anthropic expanded Claude's integration ecosystem to personal apps including Audible, Spotify,
Uber, AllTrails, TripAdvisor, Instacart, and TurboTax, building on existing work-app integrations
with Microsoft 365 and others. The connectors use OAuth-based authorization flows to grant
Claude access to user data within connected apps.

From a security standpoint, users connecting apps that handle financial data (TurboTax) or
location/movement patterns (AllTrails, Uber) should carefully review the data access scopes
requested during the OAuth flow. The expanded attack surface for prompt injection attacks also
grows with each new integration — a compromised data source could potentially influence Claude
actions in connected apps.
