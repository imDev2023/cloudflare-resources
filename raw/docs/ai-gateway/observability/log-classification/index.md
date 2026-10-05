---
description: Classify AI Gateway traffic by task and assess whether each model matches the task requirements.
title: Log classification
image: https://developers.cloudflare.com/ai-gateway/observability/log-classification/og.png?v=eb778ae20a73dbdd
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ai-gateway/llms.txt  
> Use this file to discover all available pages before exploring further.

# Log classification

Last updated Sep 24, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ai-gateway/observability/log-classification/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Log classification analyzes the request and response content stored in AI Gateway logs. It classifies eligible traffic by task and assesses whether the model used matches the task requirements.

These results power **Task and model analysis** in [User Insights](https://developers.cloudflare.com/ai-gateway/observability/user-insights/). Log classification is turned off by default. You must turn it on for each gateway individually.

## Classification results

### Tasks by model

AI Gateway assigns task classifications such as debugging, code planning, code Q&A, text drafting, and coding. The **Tasks by model** chart shows how token usage and estimated spend are distributed across these classifications for each model.

### Model fit

AI Gateway compares the task requirements with the capabilities of the model used. It classifies model fit as **Overkill**, **Appropriate**, **Underpowered**, or **Could not assess**. You can compare these results by token usage or estimated spend.

## What Cloudflare processes

When log classification is turned on, Cloudflare may process stored request and response content, including:

- Prompts
- Model responses
- Request metadata
- Identifiers used to associate related requests into a conversation

Cloudflare uses this information to generate task and model-fit classifications for AI Gateway analysis features.

Log classification is not required to use AI Gateway or standard log collection. Turning on this setting allows Cloudflare to analyze eligible logs for the selected gateway as described on this page. This setting is gateway-specific: turning it on for one gateway does not turn it on for other gateways in your account.

## Requirements and behavior

- **Collect logs** must also be turned on for the gateway.
- Only activity recorded while both **Collect logs** and **Log classification** are turned on is eligible for classification.
- Turning off **Collect logs** also turns off log classification.
- Turning off **Log classification** prevents new gateway activity from being classified. Work already in progress and previously generated results remain subject to applicable retention and deletion policies.

## Turn on log classification

1. In the Cloudflare dashboard, go to **AI Gateway**. [Go to **AI Gateway** ↗](https://dash.cloudflare.com/?to=/:account/ai/ai-gateway)
2. Select a gateway, then go to **Settings**.
3. Turn on **Collect logs**.
4. Turn on **Log classification**.

## Turn off log classification

To stop classifying new activity, go to your gateway's **Settings** and turn off **Log classification**.

You can continue collecting logs without turning on classification.
