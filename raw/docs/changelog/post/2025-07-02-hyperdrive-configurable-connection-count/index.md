---
description: Hyperdrive configurations can now be set to use a specific number of connections to your origin database.
title: Hyperdrive now supports configuring the amount of database connections
image: https://developers.cloudflare.com/changelog/post/2025-07-02-hyperdrive-configurable-connection-count/og.png?v=ee6d80767e872554
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 3, 2025

## Hyperdrive now supports configuring the amount of database connections

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-07-02-hyperdrive-configurable-connection-count/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now specify the number of connections your Hyperdrive configuration uses to connect to your origin database.

All configurations have a minimum of 5 connections. The maximum connection count for a Hyperdrive configuration depends on the [Hyperdrive limits of your Workers plan](https://developers.cloudflare.com/hyperdrive/platform/limits/).

This feature allows you to right-size your connection pool based on your database capacity and application requirements. You can configure connection counts through the Cloudflare dashboard or API.

Refer to the [Hyperdrive configuration documentation](https://developers.cloudflare.com/hyperdrive/concepts/connection-pooling/) for more information.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-07-02-hyperdrive-configurable-connection-count/#page","headline":"Hyperdrive now supports configuring the amount of database connections","description":"Hyperdrive configurations can now be set to use a specific number of connections to your origin database.","url":"https://developers.cloudflare.com/changelog/post/2025-07-02-hyperdrive-configurable-connection-count/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-07-02-hyperdrive-configurable-connection-count/og.png?v=ee6d80767e872554","dateModified":"2025-07-03","datePublished":"2025-07-03","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
