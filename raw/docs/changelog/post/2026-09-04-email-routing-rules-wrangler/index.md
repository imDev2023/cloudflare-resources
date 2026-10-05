---
description: Define the email addresses handled by a Worker and manage their Email Routing rules from Wrangler configuration.
title: Manage Email Routing rules with Wrangler
image: https://developers.cloudflare.com/changelog/post/2026-09-04-email-routing-rules-wrangler/og.png?v=2a13f591cacebec5
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 4, 2026

## Manage Email Routing rules with Wrangler

[Email Service](https://developers.cloudflare.com/email-service/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-04-email-routing-rules-wrangler/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now manage Email Routing rules that route emails to Workers from your Wrangler configuration. Add literal addresses or a catch-all address to the top-level `addresses` field:

```jsonc
{
  "$schema": "./node_modules/wrangler/config-schema.json",
  "name": "invoice-handler",
  "main": "src/index.ts",
  // Set this to today's date
  "compatibility_date": "2026-10-05",
  "addresses": [
    "invoice@yourdomain.com"
  ]
}
```

```toml
name = "invoice-handler"
main = "src/index.ts"
# Set this to today's date
compatibility_date = "2026-10-05"
addresses = ["invoice@yourdomain.com"]
```

When you run `wrangler deploy`, Wrangler creates rules for new addresses, updates existing rules managed by the Worker, and removes managed rules that are no longer in the configuration. Wrangler shows the planned changes and asks for confirmation before applying potentially destructive changes.

Email Routing rules created by Wrangler also appear in the dashboard but with an icon that identifies them.

![Email Routing rule created by Wrangler in dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2440,height=526,format=webp/_astro/wrangler-email-routing-rules-dash.BZQZlAJI.png)

Refer to [Configure rules with Wrangler](https://developers.cloudflare.com/email-service/configuration/email-routing-addresses/#configure-rules-with-wrangler) for more information.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-04-email-routing-rules-wrangler/#page","headline":"Manage Email Routing rules with Wrangler","description":"Define the email addresses handled by a Worker and manage their Email Routing rules from Wrangler configuration.","url":"https://developers.cloudflare.com/changelog/post/2026-09-04-email-routing-rules-wrangler/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-04-email-routing-rules-wrangler/og.png?v=2a13f591cacebec5","dateModified":"2026-09-04","datePublished":"2026-09-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
