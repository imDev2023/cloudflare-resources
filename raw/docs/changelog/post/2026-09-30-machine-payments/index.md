---
description: Use x402 to pay for eligible AI Gateway inference requests directly from a stablecoin wallet.
title: Pay for AI inference with Machine Payments
image: https://developers.cloudflare.com/changelog/post/2026-09-30-machine-payments/og.png?v=164f18437b391155
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 30, 2026

## Pay for AI inference with Machine Payments

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-30-machine-payments/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway now supports Machine Payments in beta. With Machine Payments, clients can use the x402 protocol to pay for eligible inference requests directly from a stablecoin wallet instead of maintaining a prepaid credit balance.

Machine Payments is available for the `/ai/run` endpoint with select open models. To request x402 payment, authenticate with a Cloudflare API token and include the Cloudflare-specific `Payment-Method: x402` header:

```bash
curl -iX POST "https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run" \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Payment-Method: x402" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "z-ai/glm-4.7-flash",
    "input": {
      "messages": [
        {
          "role": "user",
          "content": "What is Cloudflare?"
        }
      ]
    }
  }'
```

An x402-compatible client handles the payment challenge, signs an authorization from the client's wallet, and retries the request. Machine Payments currently requires customers to be based in the United States and have a credit card on file.

For prerequisites, eligible models, and transaction details, refer to [Machine Payments (x402)](https://developers.cloudflare.com/ai-gateway/features/machine-payments/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-30-machine-payments/#page","headline":"Pay for AI inference with Machine Payments","description":"Use x402 to pay for eligible AI Gateway inference requests directly from a stablecoin wallet.","url":"https://developers.cloudflare.com/changelog/post/2026-09-30-machine-payments/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-30-machine-payments/og.png?v=164f18437b391155","dateModified":"2026-09-30","datePublished":"2026-09-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
