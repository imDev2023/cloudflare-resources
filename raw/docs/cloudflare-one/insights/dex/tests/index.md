---
description: Synthetic tests resources and guides for Zero Trust analytics.
title: Synthetic tests
image: https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/og.png?v=b5d7efa154f9e2f2
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-one/llms.txt  
> Use this file to discover all available pages before exploring further.

# Synthetic tests

Last updated Sep 4, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

With Digital Experience Monitoring (DEX), you can test if your devices can connect to a private or public endpoint through the Cloudflare One Client. Tests allow you to monitor availability for a given application and investigate performance issues reported by your end users.

Cloudflare One Client devices automatically send device-state telemetry to DEX. Synthetic tests are separate, optional checks that administrators create for specific public or private endpoints.

DEX tests will only run when the Cloudflare One Client is turned on, whereas [fleet status](https://developers.cloudflare.com/cloudflare-one/insights/dex/monitoring/#fleet-status) metrics are always available.

To control which users or groups run a test, use [DEX rules](https://developers.cloudflare.com/cloudflare-one/insights/dex/rules/).

- [HTTP test](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/http/)
- [Traceroute test](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/traceroute/)
- [View test results](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/view-results/)

## Export DEX application test logs

You can use [Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/) to export [DEX application test](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/dex_application_tests/) data to [R2](https://developers.cloudflare.com/r2/) (Cloudflare's object storage), a third-party cloud storage bucket, or a Security Information and Event Management (SIEM) tool. This is useful if you need to retain test data beyond the [7-day log retention period](https://developers.cloudflare.com/cloudflare-one/insights/logs/#log-retention) or correlate DEX data with other log sources.
