---
description: Understand how Cloudflare's proxy interacts with Google Analytics tracking and how to use GA with Zaraz.
title: Cloudflare and Google Analytics
image: https://developers.cloudflare.com/fundamentals/reference/google-analytics/og.png?v=1a309ded02052d18
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/fundamentals/llms.txt  
> Use this file to discover all available pages before exploring further.

# Cloudflare and Google Analytics

Last updated Apr 20, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/fundamentals/reference/google-analytics/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Using Cloudflare does not affect Google Analytics (GA) tracking if it is added to the website [in one of ways recommended by Google ↗︎](https://support.google.com/analytics/answer/9304153#add-tag).

## Standard GA setup

Cloudflare proxies traffic to your origin web server, but the GA JavaScript code never actually sends traffic to your server. Instead, it executes directly in a user's browser and does not interact with Cloudflare.

Cloudflare only affects analytics tools that read logs directly from your web server (like awstats).

Note

To troubleshoot potential issues with Google Analytics, refer to [Common GA setup mistakes ↗︎](https://support.google.com/analytics/answer/1009683).

## Zaraz

As an alternative to the standard setup of Google Analytics with tag/snippet, Cloudflare offers a way to use Google Analytics with [Zaraz](https://developers.cloudflare.com/zaraz/). Zaraz is a solution that allows Google Analytics to collect data without its script loaded on the website. If GA is set up this way, then not all features may be available.

Note

Details about features of Google Analytics that are unavailable with Zaraz can be found in [Zaraz FAQ](https://developers.cloudflare.com/zaraz/faq/#tools)
