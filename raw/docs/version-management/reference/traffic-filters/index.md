---
description: Route traffic to specific environments with filters.
title: Traffic filters
image: https://developers.cloudflare.com/version-management/reference/traffic-filters/og.png?v=f00eb82e9b5b2e75
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/version-management/llms.txt  
> Use this file to discover all available pages before exploring further.

# Traffic filters

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/version-management/reference/traffic-filters/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

When you [create an environment](https://developers.cloudflare.com/version-management/how-to/environments/#create-environment), you specify a traffic filter for that environment. This filter ensures that all traffic reaching the environment and, by extension, the configuration changes associated with the environment's version is intentional.

To send traffic to a specific environment, send requests to your zone that match the pattern specified in your filter. These could be characteristics such as **Edge Server IP**, **Cookie**, **Hostname**, or **User Agent**.

To make sure requests are reaching an environment, review the [Metrics](https://developers.cloudflare.com/version-management/how-to/versions/#view-metrics) associated with your environment. These metrics will also help you evaluate whether your configuration changes are affecting traffic in the way you expect.
