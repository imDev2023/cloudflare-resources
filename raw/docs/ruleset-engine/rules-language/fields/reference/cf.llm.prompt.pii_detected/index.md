---
description: Indicates whether any personally identifiable information (PII) has been detected in the LLM prompt included in the request.
title: cf.llm.prompt.pii_detected
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.llm.prompt.pii\_detected

`cf.llm.prompt.pii_detected``Boolean`

Indicates whether any personally identifiable information (PII) has been detected in the LLM prompt included in the request.

Equivalent to checking if the [`cf.llm.prompt.pii_categories`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.pii_categories/) field is not empty.

Requires a Cloudflare Enterprise plan. You must also enable [AI Security for Apps](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/).

Categories:
- Request
