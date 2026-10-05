---
description: Fields available for AI Security for Apps detections in rule expressions.
title: AI Security for Apps fields
image: https://developers.cloudflare.com/waf/detections/ai-security-for-apps/fields/og.png?v=faa8fd1008de4efe
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/waf/llms.txt  
> Use this file to discover all available pages before exploring further.

# AI Security for Apps fields

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/fields/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

When enabled, AI Security for Apps populates the following fields:

| Field | Description |
| --- | --- |
| LLM PII detected <br> [`cf.llm.prompt.pii_detected`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.pii_detected/) <br> `Boolean` | Indicates whether any personally identifiable information (PII) has been detected in the LLM prompt included in the request. |
| LLM PII categories <br> [`cf.llm.prompt.pii_categories`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.pii_categories/) <br> `Array<String>` | Array of string values with the personally identifiable information (PII) categories found in the LLM prompt included in the request.<br>[Category list](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.pii_categories/) |
| LLM Content detected <br> [`cf.llm.prompt.detected`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.detected/) <br> `Boolean` | Indicates whether Cloudflare detected an LLM prompt in the incoming request. |
| LLM Unsafe topic detected <br> [`cf.llm.prompt.unsafe_topic_detected`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.unsafe_topic_detected/) <br> `Boolean` | Indicates whether the incoming request includes any unsafe topic category in the LLM prompt. |
| LLM Unsafe topic categories <br> [`cf.llm.prompt.unsafe_topic_categories`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.unsafe_topic_categories/) <br> `Array<String>` | Array of string values with the type of unsafe topics detected in the LLM prompt.<br>[Category list](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.unsafe_topic_categories/) |
| LLM Injection score <br> [`cf.llm.prompt.injection_score`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.injection_score/) <br> `Number` | A score from 1–99 that represents the likelihood that the LLM prompt in the request is trying to perform a prompt injection attack. Lower scores indicate higher risk. |
| LLM Token count <br> [`cf.llm.prompt.token_count`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.token_count/) <br> `Number` | An estimated token count for the LLM prompt in the request. Refer to [Token counting](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/token-counting/) for details. |
| LLM Custom topic categories <br> [`cf.llm.prompt.custom_topic_categories`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.custom_topic_categories/) <br> `Map<Number>` | A map of custom topic labels to relevance scores (1–99). Lower scores indicate the prompt is more relevant to that topic. Only populated when [custom topics](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/unsafe-topics/#custom-topics) are configured. |
