---
description: The descriptions below detail the fields available for nel_reports.
title: NEL reports
image: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/nel_reports/og.png?v=ed0928d644a926c0
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/logs/llms.txt  
> Use this file to discover all available pages before exploring further.

# NEL reports

Last updated Sep 14, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/nel_reports/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The descriptions below detail the fields available for `nel_reports`.

## ClientIPASN

Type: `int`

Client ASN.

## ClientIPASNDescription

Type: `string`

Client ASN description.

## ClientIPCountry

Type: `string`

Client country.

## LastKnownGoodColoCode

Type: `string`

IATA airport code of colo client connected to.

## Phase

Type: `string`

The phase of connection the error occurred in; *dns* | *connection* | *application* | *unknown*.

## Timestamp

Type: `int or string`

Timestamp for error report.

## Type

Type: `string`

The type of error in the phase.
