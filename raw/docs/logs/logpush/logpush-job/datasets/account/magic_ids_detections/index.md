---
description: The descriptions below detail the fields available for magic_ids_detections.
title: Magic IDS Detections
image: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/magic_ids_detections/og.png?v=c4ab8a08ceef2e37
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/logs/llms.txt  
> Use this file to discover all available pages before exploring further.

# Magic IDS Detections

Last updated Sep 14, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/magic_ids_detections/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The descriptions below detail the fields available for `magic_ids_detections`.

## Action

Type: `string`

What action was taken on the packet. Possible values are *pass* | *block*.

## ColoCity

Type: `string`

The city where the detection occurred.

## ColoCode

Type: `string`

The IATA airport code corresponding to where the detection occurred.

## DestinationIP

Type: `string`

The destination IP of the packet which triggered the detection.

## DestinationPort

Type: `int`

The destination port of the packet which triggered the detection. It is set to 0 if the protocol field is set to *any*.

## Protocol

Type: `string`

The layer 4 protocol of the packet which triggered the detection. Possible values are *tcp* | *udp* | *any*. Variant *any* means a detection occurred at a lower layer (such as IP).

## SignatureID

Type: `int`

The signature ID of the detection.

## SignatureMessage

Type: `string`

The signature message of the detection. Describes what the packet is attempting to do.

## SignatureRevision

Type: `int`

The signature revision of the detection.

## SourceIP

Type: `string`

The source IP of packet which triggered the detection.

## SourcePort

Type: `int`

The source port of the packet which triggered the detection. It is set to 0 if the protocol field is set to *any*.

## Timestamp

Type: `int or string`

A timestamp of when the detection occurred.
