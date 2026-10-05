---
description: The descriptions below detail the fields available for biso_user_actions.
title: Browser Isolation User Actions
image: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/biso_user_actions/og.png?v=35aa7932f341c7cf
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/logs/llms.txt  
> Use this file to discover all available pages before exploring further.

# Browser Isolation User Actions

Last updated Sep 14, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/biso_user_actions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The descriptions below detail the fields available for `biso_user_actions`.

## AccountID

Type: `string`

The Cloudflare account ID.

## Decision

Type: `string`

The decision applied ('allow' or 'block').

## DomainName

Type: `string`

The domain name in the URL.

## Metadata

Type: `string`

Additional information specific to a user action (JSON string).

## Timestamp

Type: `int or string`

The date and time.

## Type

Type: `string`

The user action type (for example, 'copy', 'paste', 'download').

## URL

Type: `string`

The URL of the webpage where a user action was performed.

## UserEmail

Type: `string`

The user email.

## UserID

Type: `string`

The user ID.
