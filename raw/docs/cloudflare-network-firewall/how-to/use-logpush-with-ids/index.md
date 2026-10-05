---
description: Send IDS events to Logpush destinations.
title: Use Logpush with IDS
image: https://developers.cloudflare.com/cloudflare-network-firewall/how-to/use-logpush-with-ids/og.png?v=cb21c3b7ed433edc
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-network-firewall/llms.txt  
> Use this file to discover all available pages before exploring further.

# Use Logpush with IDS

Last updated May 6, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-network-firewall/how-to/use-logpush-with-ids/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can use Logpush with Cloudflare Network Firewall (formerly Magic Firewall) IDS to log detected risks:

1. Consult the [Logpush Destination docs](https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/#destination) to learn about what destinations Logpush supports. The documentation will also instruct you on how to correctly format the destination URL for Logpush.
2. Follow the [Manage Lopush with cURL](https://developers.cloudflare.com/logs/logpush/examples/example-logpush-curl/) tutorial to validate your Logpush destination and define a Logpush job.

## Notes on using Logpush with IDS

- Magic IDS is an account-scoped dataset. This means the string `/zone/<ZONE_ID>` in the Cloudflare API URLs in the tutorial should be replaced with `/account/<ACCOUNT_ID>`.
- Consult the [Magic IDS Detection fields doc](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/magic_ids_detections/) to know what fields you want configured for the job.
- When creating the Logpush job, the dataset field should equal `magic_ids_detections`.
- Timestamps by default are unixnano. Consult the [Logpush Options docs](https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/#options) to learn what format you can choose that will be compatible with your destination and/or expectations. Note that all options must be added *after* all fields you want from the Logpush job, akin to URL parameters.
