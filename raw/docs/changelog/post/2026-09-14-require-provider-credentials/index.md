---
description: Prevent third-party provider requests from falling back to Unified Billing when provider credentials are unavailable.
title: Prevent Unified Billing fallback for BYOK third-party providers
image: https://developers.cloudflare.com/changelog/post/2026-09-14-require-provider-credentials/og.png?v=aaec8520e9d59882
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 14, 2026

## Prevent Unified Billing fallback for BYOK third-party providers

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-14-require-provider-credentials/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway can now require credentials for third-party provider requests. Credentials must accompany the request or be stored on the gateway. This setting prevents fallback to Unified Billing with Cloudflare-managed credentials.

Turn on **Require provider credentials** in your gateway settings. To use the API, set `byok_only` to `true` in the request body of a [`PUT` request to update the gateway](https://developers.cloudflare.com/api/resources/ai_gateway/methods/update/):

```json
{
	"byok_only": true
}
```

To require provider credentials for one third-party request, set the `cf-aig-no-wholesale` header to `true`. This header cannot relax the gateway setting.

Requests without applicable credentials then return an HTTP `400` response. Workers AI requests remain allowed, and the setting does not change their configured billing mode.

For configuration details and request-level controls, refer to [Prevent Unified Billing fallback for BYOK third-party providers](https://developers.cloudflare.com/ai-gateway/features/unified-billing/#prevent-unified-billing-fallback-for-byok-third-party-providers).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-14-require-provider-credentials/#page","headline":"Prevent Unified Billing fallback for BYOK third-party providers","description":"Prevent third-party provider requests from falling back to Unified Billing when provider credentials are unavailable.","url":"https://developers.cloudflare.com/changelog/post/2026-09-14-require-provider-credentials/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-14-require-provider-credentials/og.png?v=aaec8520e9d59882","dateModified":"2026-09-14","datePublished":"2026-09-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
