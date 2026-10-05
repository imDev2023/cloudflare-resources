---
description: Hyperdrive now automatically configures your Cloudflare Tunnel to connect to your private database.
title: Automatic configuration for private databases on Hyperdrive
image: https://developers.cloudflare.com/changelog/post/2025-01-28-hyperdrive-automated-private-database-configuration/og.png?v=4fe7ae44f17cc3a2
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 28, 2025

## Automatic configuration for private databases on Hyperdrive

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-01-28-hyperdrive-automated-private-database-configuration/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Hyperdrive now automatically configures your Cloudflare Tunnel to connect to your private database.

![Automatic configuration of Cloudflare Access and Service Token in the Cloudflare dashboard for Hyperdrive.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1814,height=922,format=webp/_astro/hyperdrive-private-database-automatic-configuration.BT4_KLwW.png)

When creating a Hyperdrive configuration for a private database, you only need to provide your database credentials and set up a Cloudflare Tunnel within the private network where your database is accessible. Hyperdrive will automatically create the Cloudflare Access, Service Token, and Policies needed to secure and restrict your Cloudflare Tunnel to the Hyperdrive configuration.

To create a Hyperdrive for a private database, you can follow the [Hyperdrive documentation](https://developers.cloudflare.com/hyperdrive/configuration/connect-to-private-database/). You can still manually create the Cloudflare Access, Service Token, and Policies if you prefer.

This feature is available from the Cloudflare dashboard.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-01-28-hyperdrive-automated-private-database-configuration/#page","headline":"Automatic configuration for private databases on Hyperdrive","description":"Hyperdrive now automatically configures your Cloudflare Tunnel to connect to your private database.","url":"https://developers.cloudflare.com/changelog/post/2025-01-28-hyperdrive-automated-private-database-configuration/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-01-28-hyperdrive-automated-private-database-configuration/og.png?v=4fe7ae44f17cc3a2","dateModified":"2025-01-28","datePublished":"2025-01-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
