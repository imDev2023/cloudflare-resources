---
description: The descriptions below detail the fields available for websocket_analytics.
title: WebSocket Analytics
image: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/websocket_analytics/og.png?v=03f2626e7f9a69c9
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/logs/llms.txt  
> Use this file to discover all available pages before exploring further.

# WebSocket Analytics

Last updated Sep 14, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/websocket_analytics/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The descriptions below detail the fields available for `websocket_analytics`.

## BytesReceivedClient

Type: `int`

Number of bytes received from the client.

## BytesReceivedOrigin

Type: `int`

Number of bytes received from the origin.

## BytesSentClient

Type: `int`

Number of bytes sent to the client.

## BytesSentOrigin

Type: `int`

Number of bytes sent to the origin.

## ClientASN

Type: `int`

The client's autonomous system number (ASN).

## ClientIP

Type: `string`

The client IP address.

## ClientRequestHost

Type: `string`

The host requested by the client in the WebSocket upgrade request.

## ClientRequestPath

Type: `string`

The path requested by the client in the WebSocket upgrade request.

## ClientRequestUserAgent

Type: `string`

The user agent reported by the client.

## ColoCode

Type: `string`

IATA airport code of the data center that handled the connection.

## ConnectionCloseReason

Type: `string`

The edge proxy classification for why the WebSocket connection ended. *none* means the proxy observed no classified error or timeout.  
Possible values are *none* | *unspecifiedError* | *timedOut* | *peerReset* | *upstreamReset* | *protocolViolation* | *peerNoError*.

## ConnectionCloseSource

Type: `string`

The side where the edge proxy observed the connection close. This field does not necessarily identify which side initiated the close. *both* means the proxy observed closure in both directions and does not identify which direction closed first.  
Possible values are *upstream* | *downstream* | *me* | *both*. Unrecognized classifications can appear as raw internal values.

## ConnectionID

Type: `string`

Unique identifier of the WebSocket connection, hex-encoded.

## ConnectionTransportCloseCode

Type: `int`

A reportable transport-level close code observed. For Transport Layer Security (TLS) connections, the low byte contains the TLS alert description. A TLS `close_notify` alert is not reported. A value of 0 means no reportable code was observed or the connection used plain TCP. The most significant bit indicates the source: 0 = proxy-initiated, 1 = peer-initiated.

## EdgeEndTimestamp

Type: `int or string`

Timestamp at which the WebSocket connection closed. To specify the timestamp format, refer to [Output types](https://developers.cloudflare.com/logs/logpush/logpush-job/log-output-options/#output-types).

## EdgeStartTimestamp

Type: `int or string`

Timestamp at which the WebSocket connection was established. To specify the timestamp format, refer to [Output types](https://developers.cloudflare.com/logs/logpush/logpush-job/log-output-options/#output-types).

## RayID

Type: `string`

The Ray ID of the WebSocket upgrade request.
