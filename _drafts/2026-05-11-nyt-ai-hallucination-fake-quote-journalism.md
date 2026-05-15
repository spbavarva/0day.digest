---
title: "New York Times Corrects Story After Reporter Published AI-Generated Fake Quote as Real"
date: 2026-05-10 23:58:49 +0000
categories: [Daily Signal]
tags: [ai-safety, llm]
severity: informational
must_know: false
sources:
  - name: Simon Willison
    url: https://simonwillison.net/2026/May/10/new-york-times-editors-note/#atom-everything
---

The New York Times issued a correction after a reporter attributed to a politician a direct quotation that was
in fact an AI-generated summary of his views — rendered by the AI as a quote — without verifying it against
source material. The politician did not use those words in the referenced speech.

This is a concrete LLM hallucination failure mode in a high-stakes editorial context: AI research tools that
summarize and reframe content can silently convert paraphrases into fabricated direct quotes. Newsroom AI usage
policies should explicitly require human verification of any AI-generated attribution or quoted statements
before publication, and treat AI summaries as drafts, not citable sources.
