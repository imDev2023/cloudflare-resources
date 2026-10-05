---
description: A map of custom topic labels to relevance scores (1–99) for the LLM prompt in the request.
title: cf.llm.prompt.custom_topic_categories
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.llm.prompt.custom\_topic\_categories

`cf.llm.prompt.custom_topic_categories``Map<Number>`

A map of custom topic labels to relevance scores (1–99) for the LLM prompt in the request.

Lower scores indicate the prompt is more relevant to that topic. Only populated when [custom topics](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/unsafe-topics/#custom-topics) are configured.

Requires a Cloudflare Enterprise plan. You must also enable [AI Security for Apps](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/).

Example usage:

```txt
# Matches requests where the prompt is highly relevant to the "competitors" custom topic:
(cf.llm.prompt.custom_topic_categories["competitors"] lt 30)
```

Categories:
- Request
