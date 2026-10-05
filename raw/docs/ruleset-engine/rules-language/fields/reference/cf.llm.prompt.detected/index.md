---
description: Indicates whether Cloudflare detected an LLM prompt in the incoming request.
title: cf.llm.prompt.detected
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.llm.prompt.detected

`cf.llm.prompt.detected``Boolean`

Indicates whether Cloudflare detected an LLM prompt in the incoming request.

When a prompt is not present, the other LLM-related fields will have default values.

Requires a Cloudflare Enterprise plan. You must also enable [AI Security for Apps](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/).

Categories:
- Request
