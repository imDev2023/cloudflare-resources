---
description: A score from 1–99 that represents the likelihood that the LLM prompt in the request is trying to perform a prompt injection attack.
title: cf.llm.prompt.injection_score
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.llm.prompt.injection\_score

`cf.llm.prompt.injection_score``Number`

A score from 1–99 that represents the likelihood that the LLM prompt in the request is trying to perform a prompt injection attack.

A low score (for example, below `20`) indicates that there is a high probability that the LLM prompt in the request is trying to perform a prompt injection attack.

The special score `100` indicates that Cloudflare did not score the request.

Requires a Cloudflare Enterprise plan. You must also enable [AI Security for Apps](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/).

Categories:
- Request
