---
title: "Microsoft VibeVoice: MIT-Licensed Speech-to-Text Model with Built-In Speaker Diarization"
date: 2026-04-27 23:46:56 +0000
categories: [Daily Signal]
tags: [model-release, microsoft]
severity: informational
must_know: false
sources:
  - name: Simon Willison
    url: https://simonwillison.net/2026/Apr/27/vibevoice/#atom-everything
---

Microsoft released VibeVoice in January 2026 — a Whisper-style automatic speech recognition model under the MIT license that integrates speaker diarization directly into the model architecture rather than as a post-processing step. The model is available in a full 17.3GB variant and a 4-bit quantized MLX version (5.71GB) optimized for Apple Silicon. Developer Simon Willison notes it runs locally via a one-liner using the mlx-audio library.

The MIT license makes VibeVoice viable for commercial deployment without the restrictions of some competing models. For security and compliance teams, locally-run transcription with diarization eliminates the data-egress concern of cloud transcription APIs, relevant for call center and interview recording workflows handling sensitive conversations.
