---
description: Configure Logpush to send logs to a destination.
title: Enable destinations
image: https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/og.png?v=898c45ca7727a1cb
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/logs/llms.txt  
> Use this file to discover all available pages before exploring further.

# Enable destinations

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Enable pushing logs to your storage service, SIEM solution, or log management provider.

Note

Note that you will need to allowlist IP addresses to accept incoming Cloudflare Logpush traffic. Refer to [Cloudflare IPs ↗︎](https://www.cloudflare.com/ips/) for the complete list of IPs. If you prefer to have a dedicated IP, you can use dedicated [Dedicated Egress IPs for Cloudflare Logpush](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/egress-ip/).

- [Enable Cloudflare R2](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/r2/)
- [Enable Basin Pipelines](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/pipelines/)
- [Enable HTTP destination](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/http/)
- [Enable Amazon S3](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/aws-s3/)
- [Enable S3-compatible endpoints](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/s3-compatible-endpoints/)
- [Enable Datadog](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/datadog/)
- [Enable Elastic](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/elastic/)
- [Enable Google Cloud Storage](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/google-cloud-storage/)
- [Enable Google BigQuery](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/bigquery/)
- [Enable Microsoft Azure](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/azure/)
- [Enable New Relic](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/new-relic/)
- [Enable SentinelOne](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/sentinelone/)
- [Enable Splunk](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/splunk/)
- [Enable Sumo Logic](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/sumo-logic/)
- [Enable Amazon Kinesis](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/kinesis/)
- [Enable IBM QRadar](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/ibm-qradar/)
- [Enable IBM Cloud Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/ibm-cloud-logs/)
- [Enable other providers](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/other-providers/)
- [Third-party integrations](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/third-party/)
- [Dedicated Egress IP for Logpush](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/egress-ip/)
