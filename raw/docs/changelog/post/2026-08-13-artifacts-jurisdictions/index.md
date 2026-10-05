---
description: Ensure Artifacts stores and processes repo data only within a selected jurisdiction.
title: Data localization support for Artifacts
image: https://developers.cloudflare.com/changelog/post/2026-08-13-artifacts-jurisdictions/og.png?v=40eb0f0ccb415cb1
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 13, 2026

## Data localization support for Artifacts

[Artifacts](https://developers.cloudflare.com/artifacts/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-13-artifacts-jurisdictions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Artifacts now supports jurisdictions, allowing you to select the European Union or the United States as the only location where repo data is stored and processed.

Select a jurisdiction when you create a namespace. Every repo in that namespace automatically uses the selected jurisdiction.

```bash
curl --request POST \
  "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/artifacts/namespaces" \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "namespace": "my-eu-namespace",
    "jurisdiction": "eu"
  }'
```

Jurisdictions cannot be changed after namespace creation. If you omit the jurisdiction, Artifacts creates an unrestricted namespace.

For supported jurisdictions and usage details, refer to [Data localization](https://developers.cloudflare.com/artifacts/guides/data-localization/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-13-artifacts-jurisdictions/#page","headline":"Data localization support for Artifacts","description":"Ensure Artifacts stores and processes repo data only within a selected jurisdiction.","url":"https://developers.cloudflare.com/changelog/post/2026-08-13-artifacts-jurisdictions/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-13-artifacts-jurisdictions/og.png?v=40eb0f0ccb415cb1","dateModified":"2026-08-13","datePublished":"2026-08-13","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
