---
description: Track and estimate token-based costs across AI providers using AI Gateway cost metrics.
title: Costs
image: https://developers.cloudflare.com/ai-gateway/observability/costs/og.png?v=28f49b7fcb66382a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ai-gateway/llms.txt  
> Use this file to discover all available pages before exploring further.

# Costs

Last updated Sep 24, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ai-gateway/observability/costs/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cost metrics are only available for endpoints where the models return token data and the model name in their responses.

## Track costs across AI providers

AI Gateway makes it easier to monitor and estimate token based costs across all your AI providers. This can help you:

- Understand and compare usage costs between providers.
- Monitor trends and estimate spend using consistent metrics.
- Apply custom pricing logic to match negotiated rates.

Note

The cost metric is an **estimation** based on the number of tokens sent and received in requests. While this metric can help you monitor and predict cost trends, refer to your provider's dashboard for the most **accurate** cost details.

Caution

Providers may introduce new models or change their pricing. If you notice outdated cost data or are using a model not yet supported by our cost tracking, please [submit a request ↗︎](https://forms.gle/8kRa73wRnvq7bxL48)

## Custom costs

AI Gateway allows users to set custom costs when operating under special pricing agreements or negotiated rates. Custom costs can be applied at the request level, and when applied, they will override the default or public model costs. For more information on configuration of custom costs, please visit the [Custom Costs](https://developers.cloudflare.com/ai-gateway/configuration/custom-costs/) configuration page.
