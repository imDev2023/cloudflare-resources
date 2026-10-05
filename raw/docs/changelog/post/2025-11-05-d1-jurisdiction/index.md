---
description: A D1 database can set a jurisdiction at creation, which limits the location to run and store the database.
title: D1 can restrict data localization with jurisdictions
image: https://developers.cloudflare.com/changelog/post/2025-11-05-d1-jurisdiction/og.png?v=6f8e5823e001ed18
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 5, 2025

## D1 can restrict data localization with jurisdictions

[D1](https://developers.cloudflare.com/d1/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-05-d1-jurisdiction/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now set a [jurisdiction](https://developers.cloudflare.com/d1/configuration/data-location/) when creating a D1 database to guarantee where your database runs and stores data. Jurisdictions can help you comply with data localization regulations such as GDPR. Supported jurisdictions include `eu` and `fedramp`.

A jurisdiction can only be set at database creation time via wrangler, REST API or the UI and cannot be added/updated after the database already exists.

```sh
npx wrangler@latest d1 create db-with-jurisdiction --jurisdiction eu
```

```sh
curl -X POST "https://api.cloudflare.com/client/v4/accounts/<account_id>/d1/database" \
     -H "Authorization: Bearer $TOKEN" \
     -H "Content-Type: application/json" \
     --data '{"name": "db-with-jurisdiction", "jurisdiction": "eu" }'
```

To learn more, visit D1's data location [documentation](https://developers.cloudflare.com/d1/configuration/data-location/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-05-d1-jurisdiction/#page","headline":"D1 can restrict data localization with jurisdictions","description":"A D1 database can set a jurisdiction at creation, which limits the location to run and store the database.","url":"https://developers.cloudflare.com/changelog/post/2025-11-05-d1-jurisdiction/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-05-d1-jurisdiction/og.png?v=6f8e5823e001ed18","dateModified":"2025-11-05","datePublished":"2025-11-05","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
