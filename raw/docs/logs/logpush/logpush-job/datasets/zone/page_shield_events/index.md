---
description: The descriptions below detail the fields available for page_shield_events.
title: Page Shield events
image: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/page_shield_events/og.png?v=7ad0e55ca089d273
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/logs/llms.txt  
> Use this file to discover all available pages before exploring further.

# Page Shield events

Last updated Sep 14, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/page_shield_events/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The descriptions below detail the fields available for `page_shield_events`.

## Action

Type: `string`

The action which was taken against the violation.  
Possible values are *log* | *allow*.

## CSPDirective

Type: `string`

The violated directive in the report.

## Host

Type: `string`

The host where the resource was seen on.

## PageURL

Type: `string`

The page URL the violation was seen on.

## PolicyID

Type: `string`

The ID of the policy which was violated.

## ResourceType

Type: `string`

The resource type of the violated directive. Possible values are 'script', 'connection', or 'other' for unmonitored resource types.

## Timestamp

Type: `int or string`

The timestamp of when the report was received.

## URL

Type: `string`

The resource URL.

## URLContainsCDNCGIPath (deprecated)

Type: `bool`

Whether the resource URL contains the '/cdn-cgi/' path.

## URLHost

Type: `string`

The domain host of the URL.
