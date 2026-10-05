---
description: The descriptions below detail the fields available for magic_bgp_logs.
title: Magic BGP Logs
image: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/magic_bgp_logs/og.png?v=a6e2ee5b4d3333fa
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/logs/llms.txt  
> Use this file to discover all available pages before exploring further.

# Magic BGP Logs

Last updated Sep 14, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/magic_bgp_logs/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The descriptions below detail the fields available for `magic_bgp_logs`.

## Direction

Type: `string`

Direction of the event relative to Cloudflare. Possible values are *to\_cloudflare* | *from\_cloudflare*, or empty for non-message events.

## EventData

Type: `object`

Payload describing the event. Schema depends on `EventKind`.  
*open\_message* carries `peer_asn`, `cloudflare_asn`, `bgp_id`, `hold_time`, and `capabilities`.  
*update\_message* carries `announced`, `as_path`, and `origin`.  
*notification\_message* carries `code`, `subcode`, and `reason`.  
*route\_refresh\_message* carries `afi` and `safi`.  
*bgp\_state\_transition* carries `from_state`, `to_state`, and `event`.  
*tcp\_handshake\_failed* carries `reason`, `message`, `src`, and `dst`.  
*stale\_path\_timer\_expired* carries `purged_route_count`.  
*session\_config\_changed* carries `disabled` and the changed fields.  
*filter\_config\_changed* carries `import` and `export` filter change flags.  
*redistribute\_config\_changed* carries a single boolean.

## EventKind

Type: `string`

BGP event type. Possible values are *open\_message* | *update\_message* | *notification\_message* | *route\_refresh\_message* | *bgp\_state\_transition* | *tcp\_handshake\_failed* | *stale\_path\_timer\_expired* | *session\_config\_changed* | *filter\_config\_changed* | *redistribute\_config\_changed*.

## EventTimestamp

Type: `int or string`

Timestamp of when the event occurred.

## TunnelID

Type: `string`

UUID (hex, no hyphens) of the IPsec / GRE tunnel the event belongs to.

## TunnelName

Type: `string`

Name of the IPsec / GRE tunnel the event belongs to.
