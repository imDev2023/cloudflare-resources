---
description: Restrict a Workers KV namespace to durably store data only within a specific jurisdiction, such as the EU, the US, or FedRAMP-compliant data centers.
title: Workers KV namespace jurisdictions are now generally available
image: https://developers.cloudflare.com/changelog/post/2026-10-02-kv-jurisdictions-ga/og.png?v=d33dc67eb9a92c8c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 2, 2026

## Workers KV namespace jurisdictions are now generally available

[KV](https://developers.cloudflare.com/kv/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-02-kv-jurisdictions-ga/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Jurisdictions for [Workers KV](https://developers.cloudflare.com/kv/) namespaces are now generally available. When you create a namespace, you can set a [jurisdiction](https://developers.cloudflare.com/kv/reference/data-location/) to make sure the namespace's data is only durably stored within that region. Jurisdictions can help you comply with data localization regulations such as GDPR or FedRAMP. Supported jurisdictions are `eu`, `us`, and `fedramp`.

A jurisdiction can only be set when a namespace is created, using the Cloudflare dashboard, Wrangler, the `cf` CLI, or the REST API, and cannot be added or changed afterwards.

```sh
npx wrangler@latest kv namespace create <NAMESPACE_NAME> --jurisdiction=eu
```

```sh
cf kv namespaces create --title <NAMESPACE_NAME> --jurisdiction eu
```

```sh
curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/storage/kv/namespaces" \
  --request POST \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "title": "<NAMESPACE_NAME>",
    "jurisdiction": "eu"
  }'
```

Workers can still access a namespace restricted to a jurisdiction from anywhere in the world, and KV data can be cached outside the jurisdiction on Cloudflare's network. The jurisdiction only controls where the namespace's data is durably stored.

To learn more, refer to [Data location](https://developers.cloudflare.com/kv/reference/data-location/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-10-02-kv-jurisdictions-ga/#page","headline":"Workers KV namespace jurisdictions are now generally available","description":"Restrict a Workers KV namespace to durably store data only within a specific jurisdiction, such as the EU, the US, or FedRAMP-compliant data centers.","url":"https://developers.cloudflare.com/changelog/post/2026-10-02-kv-jurisdictions-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-10-02-kv-jurisdictions-ga/og.png?v=d33dc67eb9a92c8c","dateModified":"2026-10-02","datePublished":"2026-10-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
