---
description: Review Workers for Platforms pricing for requests, CPU time, and scripts, including usage allotments and overage costs.
title: Pricing
image: https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/pricing/og.png?v=17e5a884921ba441
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-for-platforms/llms.txt  
> Use this file to discover all available pages before exploring further.

# Pricing

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/pricing/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The Workers for Platforms Paid plan is **$25 monthly**. Workers for Platforms can be purchased through the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers-for-platforms).

Workers for Platforms comes with the following usage allotments and overage pricing.

|  | Requests<sup>1</sup> <sup>2</sup> | Duration | CPU time<sup>2</sup> | Scripts |
| --- | --- | --- | --- | --- |
|  | 20 million requests included per month <br><br> +$0.30 per additional million | No charge or limit for duration | 60 million CPU milliseconds included per month<br><br> +$0.02 per additional million CPU milliseconds<br><br> Max of 30 seconds of CPU time per invocation <br> Max of 15 minutes of CPU time per [Cron Trigger](https://developers.cloudflare.com/workers/configuration/cron-triggers/) or [Queue Consumer](https://developers.cloudflare.com/queues/configuration/javascript-apis/#consumer) invocation | 1000 scripts <br> <br>+$0.02 per additional script |

<sup>1</sup> Inbound requests to your Worker. Cloudflare does not bill for [subrequests](https://developers.cloudflare.com/workers/platform/limits/#subrequests) you make from your Worker.  
<sup>2</sup> Workers for Platforms only charges for 1 request across the chain of [dispatch Worker](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dynamic-dispatch-worker) -> [user Worker](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#user-workers) -> [outbound Worker](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/outbound-workers/). CPU time is charged across these Workers.

## Example pricing:

A Workers for Platforms project that serves 100 million requests per month, uses an average of 10 milliseconds (ms) of CPU time per request and uses 1200 scripts would have the following estimated costs:

|  | Monthly Costs | Formula |
| --- | --- | --- |
| **Subscription** | $25.00 | |
| **Requests** | $24.00 | (100,000,000 requests - 20,000,000 included requests) / 1,000,000 \* $0.30 |
| **CPU time** | $18.80 | ((10 ms of CPU time per request \* 100,000,000 requests) - 60,000,000 included CPU ms) / 1,000,000 \* $0.02 |
| **Scripts** | $4.00 | (1200 scripts - 1000 included scripts) \* $0.02 |
| **Total** | $71.80 | |

Custom limits

Set [custom limits](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/custom-limits/) for user Workers to get control over your Cloudflare bill, prevent accidental runaway bills or denial-of-wallet attacks. Configure the maximum amount of CPU time that can be used per invocation by [defining custom limits in your dispatch Worker](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/custom-limits/#set-custom-limits).
