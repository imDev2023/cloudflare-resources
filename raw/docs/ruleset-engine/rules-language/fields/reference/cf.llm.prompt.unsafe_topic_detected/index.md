---
description: Indicates whether the incoming request includes any unsafe topic category in the LLM prompt.
title: cf.llm.prompt.unsafe_topic_detected
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.llm.prompt.unsafe\_topic\_detected

`cf.llm.prompt.unsafe_topic_detected``Boolean`

Indicates whether the incoming request includes any unsafe topic category in the LLM prompt.

Equivalent to checking if the [`cf.llm.prompt.unsafe_topic_categories`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.unsafe_topic_categories/) field is not empty.

Requires a Cloudflare Enterprise plan. You must also enable [AI Security for Apps](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/).

Categories:
- Request
