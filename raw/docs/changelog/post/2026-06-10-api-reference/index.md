---
description: Manage Flagship apps and feature flags programmatically with the Cloudflare API.
title: Flagship API reference now available
image: https://developers.cloudflare.com/changelog/post/2026-06-10-api-reference/og.png?v=654bef754469a803
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 10, 2026

## Flagship API reference now available

[Flagship](https://developers.cloudflare.com/flagship/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-10-api-reference/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The **[Flagship API reference](https://developers.cloudflare.com/api/resources/flagship/)** is now available. You can use the Cloudflare API to create and update apps, and to create, update, delete, and list feature flags without using the dashboard.

For example, create a new boolean flag with the API:

```bash
curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/flagship/apps/$APP_ID/flags \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  -d '{
    "key": "new-checkout",
    "enabled": true,
    "default_variation": "off",
    "variations": {
      "off": false,
      "on": true
    },
    "rules": []
  }'
```

To create an API token, go to [Account API Tokens ↗︎](https://dash.cloudflare.com/?to=/:account/api-tokens) in the Cloudflare dashboard and search for Flagship.

The API reference includes endpoints for Flagship apps, flags, changelog entries, and flag evaluation. Agents can also use the [Flagship reference in the Cloudflare skill ↗︎](https://github.com/cloudflare/skills/tree/main/skills/cloudflare/references/flagship) to create and manage Flagship resources.

Refer to the [Flagship documentation](https://developers.cloudflare.com/flagship/) to learn more about evaluating feature flags from your applications.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-10-api-reference/#page","headline":"Flagship API reference now available","description":"Manage Flagship apps and feature flags programmatically with the Cloudflare API.","url":"https://developers.cloudflare.com/changelog/post/2026-06-10-api-reference/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-10-api-reference/og.png?v=654bef754469a803","dateModified":"2026-06-10","datePublished":"2026-06-10","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
