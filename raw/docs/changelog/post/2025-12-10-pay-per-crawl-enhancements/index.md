---
description: Pay Per Crawl adds Discovery API for crawler content discovery, custom in-band pricing for dynamic content pricing, granular URI-based configuration, and enhanced error handling with standardized crawler-error codes.
title: Pay Per Crawl (Private beta) - Discovery API, custom pricing, and advanced configuration
image: https://developers.cloudflare.com/changelog/post/2025-12-10-pay-per-crawl-enhancements/og.png?v=2b0c5a1d855409fb
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 10, 2025

## Pay Per Crawl (Private beta) - Discovery API, custom pricing, and advanced configuration

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-10-pay-per-crawl-enhancements/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Pay Per Crawl is introducing enhancements for both AI crawler operators and site owners, focusing on programmatic discovery, flexible pricing models, and granular configuration control.

#### For AI crawler operators

#### Discovery API

A new authenticated API endpoint allows verified crawlers to programmatically discover domains participating in Pay Per Crawl. Crawlers can use this to build optimized crawl queues, cache domain lists, and identify new participating sites. This eliminates the need to discover payable content through trial requests.

The API endpoint is `GET https://crawlers-api.ai-audit.cfdata.org/charged_zones` and requires Web Bot Auth authentication. Refer to [Discover payable content](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/discover-payable-content/) for authentication steps, request parameters, and response schema.

#### Payment header signature requirement

Payment headers (`crawler-exact-price` or `crawler-max-price`) must now be included in the Web Bot Auth `signature-input` header components. This security enhancement prevents payment header tampering, ensures authenticated payment intent, validates crawler identity with payment commitment, and protects against replay attacks with modified pricing. Crawlers must add their payment header to the list of signed components when [constructing the signature-input header](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/crawl-pages/#22-sign-your-request-with-web-bot-auth).

#### New `crawler-error` header

Pay Per Crawl error responses now include a new `crawler-error` header with 11 specific [error codes](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/error-codes/) for programmatic handling. Error response bodies remain unchanged for compatibility. These codes enable robust error handling, automated retry logic, and accurate spending tracking.

#### For site owners

#### Configure free pages

Site owners can now offer free access to specific pages like homepages, navigation, or discovery pages while charging for other content. Create a [Configuration Rule](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/advanced-configuration/#disable-pay-per-crawl-by-uri-pattern) in **Rules** > **Configuration Rules**, set your URI pattern using wildcard, exact, or prefix matching on the **URI Full** field, and enable the **Disable Pay Per Crawl** setting. When disabled for a URI pattern, crawler requests pass through without blocking or charging.

Some paths are always free to crawl. These paths are: `/robots.txt`, `/sitemap.xml`, `/security.txt`, `/.well-known/security.txt`, `/crawlers.json`.

#### Get started

**AI crawler operators**: [Discover payable content](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/discover-payable-content/) | [Crawl pages](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/crawl-pages/)

**Site owners**: [Advanced configuration](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/advanced-configuration/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-10-pay-per-crawl-enhancements/#page","headline":"Pay Per Crawl (Private beta) - Discovery API, custom pricing, and advanced configuration","description":"Pay Per Crawl adds Discovery API for crawler content discovery, custom in-band pricing for dynamic content pricing, granular URI-based configuration, and enhanced error handling with standardized crawler-error codes.","url":"https://developers.cloudflare.com/changelog/post/2025-12-10-pay-per-crawl-enhancements/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-12-10-pay-per-crawl-enhancements/og.png?v=2b0c5a1d855409fb","dateModified":"2025-12-10","datePublished":"2025-12-10","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
