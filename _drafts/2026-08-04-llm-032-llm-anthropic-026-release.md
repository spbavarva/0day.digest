---
title: "LLM 0.32 and llm-anthropic 0.26 Add Reasoning Traces, Responses API Support, New Claude Models"
date: 2026-08-04 23:58:24 +0000
categories: [Daily Signal]
tags: [llm, anthropic, ai-launch]
severity: informational
must_know: false
sources:
  - name: Simon Willison
    url: https://simonwillison.net/2026/Aug/4/new-release-of-llm/#atom-everything
---

Simon Willison released LLM 0.32, the most significant update to his
LLM CLI project since its initial launch.

The release adds visible reasoning traces for reasoning models,
server-side provider tools, redesigned content-addressable SQLite logs,
and support for the OpenAI Responses API.

A companion llm-anthropic 0.26 release adds support for new
claude-fable-5, claude-sonnet-5, and claude-opus-5 models, plus
server-side WebSearch, WebFetch, CodeExecution, and AnthropicMCP tools
accessible through LLM's `-T` interface.
