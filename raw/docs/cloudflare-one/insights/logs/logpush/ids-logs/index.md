---
description: IDS logs in Zero Trust analytics.
title: IDS logs
image: https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/ids-logs/og.png?v=fecd289401f068fa
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-one/llms.txt  
> Use this file to discover all available pages before exploring further.

# IDS logs

Last updated Apr 29, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/ids-logs/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can use Logpush with [Cloudflare Network Firewall IDS](https://developers.cloudflare.com/cloudflare-network-firewall/about/ids/) (Intrusion Detection System) to export logs of detected threats. IDS monitors your network traffic for a wide range of known threat signatures, including attacks such as ransomware, data exfiltration, and network scanning.

## Set up Logpush for IDS

1. Consult the [Logpush Destination docs](https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/#destination) to learn about what destinations Logpush supports. The documentation will also instruct you on how to correctly format the destination URL for Logpush.
2. Follow the [Manage Logpush with cURL](https://developers.cloudflare.com/logs/logpush/examples/example-logpush-curl/) tutorial to validate your Logpush destination and define a Logpush job.

## Notes on using Logpush with IDS

- Magic IDS is an account-scoped dataset. Unlike zone-specific datasets that apply to a single domain, account-scoped datasets use a different API endpoint. Replace the string `/zone/<ZONE_ID>` in the Cloudflare API URLs in the tutorial with `/account/<ACCOUNT_ID>`.
- Consult the [Magic IDS Detection fields doc](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/magic_ids_detections/) to know what fields you want configured for the job.
- When creating the Logpush job, the dataset field should equal `magic_ids_detections`.
- Timestamps default to `unixnano` format (nanoseconds since the Unix epoch, January 1, 1970). If your destination expects a different format (such as RFC 3339), refer to [Logpush Options](https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/#options) for available timestamp formats. In the Logpush API configuration string, options are appended after the field list.
