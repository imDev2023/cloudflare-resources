---
description: The Cloudflare Status page has a new design, Markdown output for AI agents, and a notification system that runs independently of Cloudflare.
title: New Cloudflare Status page
image: https://developers.cloudflare.com/changelog/post/2026-08-11-new-status-page/og.png?v=e72ab54a387727ba
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 11, 2026

## New Cloudflare Status page

[Support](https://developers.cloudflare.com/support/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-11-new-status-page/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The Cloudflare Status page at [www.cloudflarestatus.com ↗︎](https://www.cloudflarestatus.com/) has been rebuilt. It is available at the same address, and every previously documented [Status API ↗︎](https://www.cloudflarestatus.com/api) endpoint remains supported, so existing bookmarks, integrations, and monitoring continue to work.

#### Notifications that fire even when Cloudflare is down

The status page now has its own notification system, delivered independently of Cloudflare infrastructure. You can subscribe by email, webhook, Slack, Discord, or Google Chat.

The **Maintenance Notification** and **Incident Alerts** in [Cloudflare Notifications](https://developers.cloudflare.com/notifications/) remain supported, and deliver to the destinations already configured on your account.

#### Markdown for AI agents

Every page on the status page returns Markdown when requested with an `Accept: text/markdown` header, so agents can read the current status without parsing HTML:

```sh
curl -H "Accept: text/markdown" https://www.cloudflarestatus.com/locations
```

#### Separate feeds for incidents and maintenance

Incidents and maintenance are published as separate feeds, each available in RSS and Atom, so you can subscribe to one without the other:

```txt
https://www.cloudflarestatus.com/api/v3/incidents.rss
https://www.cloudflarestatus.com/api/v3/incidents.atom
https://www.cloudflarestatus.com/api/v3/maintenance.rss
https://www.cloudflarestatus.com/api/v3/maintenance.atom
```

For more information, refer to [Cloudflare Status](https://developers.cloudflare.com/support/cloudflare-status/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-11-new-status-page/#page","headline":"New Cloudflare Status page","description":"The Cloudflare Status page has a new design, Markdown output for AI agents, and a notification system that runs independently of Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-08-11-new-status-page/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-11-new-status-page/og.png?v=e72ab54a387727ba","dateModified":"2026-08-11","datePublished":"2026-08-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
