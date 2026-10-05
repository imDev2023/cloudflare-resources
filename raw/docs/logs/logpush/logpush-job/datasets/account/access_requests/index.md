---
description: The descriptions below detail the fields available for access_requests.
title: Access requests
image: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/access_requests/og.png?v=85aad334ec6914d3
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/logs/llms.txt  
> Use this file to discover all available pages before exploring further.

# Access requests

Last updated Sep 14, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/access_requests/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The descriptions below detail the fields available for `access_requests`.

## Action

Type: `string`

What type of record is this. *login* | *logout*.

## Allowed

Type: `bool`

If request was allowed or denied.

## AppDomain

Type: `string`

The domain of the Application that Access is protecting.

## AppUUID

Type: `string`

Access Application UUID.

## Connection

Type: `string`

Identity provider used for the login.

## Country

Type: `string`

Request's country of origin.

## CreatedAt

Type: `int or string`

The date and time the corresponding access request was made (for example, '2021-07-27T00:01:07Z').

## Email

Type: `string`

Email of the user who logged in.

## IPAddress

Type: `string`

The IP address of the client.

## PurposeJustificationPrompt

Type: `string`

Message prompted to the client when accessing the application.

## PurposeJustificationResponse

Type: `string`

Justification given by the client when accessing the application.

## RayID

Type: `string`

Identifier of the request.

## TemporaryAccessApprovers

Type: `array[string]`

List of approvers for this access request.

## TemporaryAccessDuration

Type: `int`

Approved duration for this access request.

## UserUID

Type: `string`

The uid of the user who logged in.
