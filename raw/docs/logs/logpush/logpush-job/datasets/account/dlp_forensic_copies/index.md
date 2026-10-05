---
description: The descriptions below detail the fields available for dlp_forensic_copies.
title: DLP Forensic Copies
image: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/dlp_forensic_copies/og.png?v=16e5ec0c22c58095
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/logs/llms.txt  
> Use this file to discover all available pages before exploring further.

# DLP Forensic Copies

Last updated Sep 14, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/dlp_forensic_copies/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The descriptions below detail the fields available for `dlp_forensic_copies`.

## AccountID

Type: `string`

Cloudflare account ID.

## Datetime

Type: `int or string`

The date and time the corresponding HTTP request was made.

## ForensicCopyID

Type: `string`

The unique ID for this particular forensic copy.

## GatewayRequestID

Type: `string`

Cloudflare request ID, as found in Gateway logs.

## Headers

Type: `object`

String key-value pairs for a selection of HTTP headers on the associated request/response.

## Payload

Type: `string`

Captured request/response data, base64-encoded.

## Phase

Type: `string`

Phase of the HTTP request this forensic copy was captured from (that is, "request" or "response").

## TriggeredRuleID

Type: `string`

The ID of the Gateway firewall rule that triggered this forensic copy.
