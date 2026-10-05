---
description: The descriptions below detail the fields available for turnstile_events.
title: Turnstile Events
image: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/turnstile_events/og.png?v=1951fe6b2d065078
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/logs/llms.txt  
> Use this file to discover all available pages before exploring further.

# Turnstile Events

Last updated Sep 14, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/turnstile_events/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The descriptions below detail the fields available for `turnstile_events`.

## ASN

Type: `int`

The visitor's autonomous system number (ASN).

## Action

Type: `string`

The Turnstile widget action string configured by the customer.

## BrowserMajor

Type: `int`

The major version of the visitor's browser.

## BrowserName

Type: `string`

The name of the visitor's browser (for example, 'Chrome', 'Firefox').

## ClientIP

Type: `string`

IP address of the visitor.

## CountryCode

Type: `string`

The 2-letter ISO-3166 country code of the visitor.

## EventType

Type: `string`

The type of Turnstile event. Possible values are *challenge\_issued* | *challenge\_non\_interactive\_solved* | *challenge\_interactive\_solved* | *challenge\_non\_interactive\_siteverify\_solved* | *challenge\_interactive\_siteverify\_solved* | *challenge\_clearance\_siteverify\_solved* | *challenge\_siteverify\_failed\_double\_redemption* | *challenge\_siteverify\_failed\_invalid\_token* | *challenge\_siteverify\_failed\_other* | *challenge\_siteverify\_ratelimited*.

## Hostname

Type: `string`

The hostname where the Turnstile widget was loaded.

## OSMajor

Type: `int`

The major version of the visitor's operating system.

## OSName

Type: `string`

The name of the visitor's operating system (for example, 'Windows', 'macOS').

## Sitekey

Type: `string`

The Turnstile sitekey (widget identifier).

## Timestamp

Type: `int or string`

The date and time the event was logged.

## UserAgent

Type: `string`

The visitor's full user agent string.
