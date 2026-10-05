---
description: Cloudflare CASB now lets you configure webhook destinations, test delivery, and send posture finding instances to external systems.
title: Send CASB posture finding instances with webhooks
image: https://developers.cloudflare.com/changelog/post/2026-04-09-casb-webhooks/og.png?v=7e9386cfded19e85
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 9, 2026

## Send CASB posture finding instances with webhooks

[CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-09-casb-webhooks/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now use **CASB webhooks** in Cloudflare One to send posture finding instances to external systems such as chat platforms, ticketing systems, SIEMs, SOAR tools, and custom automation services.

This gives security teams a simple way to route CASB posture findings into the tools and workflows they already use for triage and response.

To get started, go to **Integrations** > **Webhooks** in the Cloudflare One dashboard to create a webhook destination. After you configure a webhook, open a posture finding instance and select **Send webhook** to send it.

#### Key capabilities

- **Flexible authentication** — Configure destinations using **None**, **Basic Auth**, **Bearer Auth**, **Static Headers**, or **HMAC-Signing**.
- **Built-in testing** — Use **Test delivery** to send a test request before sending a live finding instance.
- **Posture finding workflows** — Send posture finding instances directly from the finding details workflow in **Cloud & SaaS findings**.
- **HTTPS destinations** — Configure webhook destinations with public `https://` URLs.

#### Learn more

- Configure [CASB webhooks](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/webhooks/) in Cloudflare.
- Learn how to [manage findings](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/manage-findings/) in Cloudflare.

CASB webhooks are now available in Cloudflare One.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-09-casb-webhooks/#page","headline":"Send CASB posture finding instances with webhooks","description":"Cloudflare CASB now lets you configure webhook destinations, test delivery, and send posture finding instances to external systems.","url":"https://developers.cloudflare.com/changelog/post/2026-04-09-casb-webhooks/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-09-casb-webhooks/og.png?v=7e9386cfded19e85","dateModified":"2026-04-09","datePublished":"2026-04-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
