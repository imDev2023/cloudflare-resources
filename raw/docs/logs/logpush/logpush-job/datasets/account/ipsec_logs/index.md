---
description: The descriptions below detail the fields available for ipsec_logs.
title: IPSec Logs
image: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/ipsec_logs/og.png?v=6d24ad03b6c09295
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/logs/llms.txt  
> Use this file to discover all available pages before exploring further.

# IPSec Logs

Last updated Sep 14, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/ipsec_logs/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The descriptions below detail the fields available for `ipsec_logs`.

## Level

Type: `string`

The level of the log.

## LocalIP

Type: `string`

The local IP address associated with the log.

## LocalPort

Type: `int`

The local port associated with the log.

## Message

Type: `string`

The log message. IKEv2 ciphersuite is logged here for handshake messages.

## RemoteIP

Type: `string`

The remote IP address associated with the log.

## RemotePort

Type: `int`

The remote port associated with the log.

## Timestamp

Type: `int or string`

Timestamp at which the log occurred.
