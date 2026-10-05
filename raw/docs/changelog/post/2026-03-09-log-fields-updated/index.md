---
description: New MCP Portal Logs dataset is now available, along with new fields for multiple Logpush datasets in Cloudflare Logs.
title: New MCP Portal Logs dataset and new fields across multiple Logpush datasets in Cloudflare Logs
image: https://developers.cloudflare.com/changelog/post/2026-03-09-log-fields-updated/og.png?v=37655141ba8f5e9e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 9, 2026

## New MCP Portal Logs dataset and new fields across multiple Logpush datasets in Cloudflare Logs

[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-09-log-fields-updated/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare has added new fields across multiple [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/):

#### New dataset

- **MCP Portal Logs**: A new dataset with fields including `ClientCountry`, `ClientIP`, `ColoCode`, `Datetime`, `Error`, `Method`, `PortalAUD`, `PortalID`, `PromptGetName`, `ResourceReadURI`, `ServerAUD`, `ServerID`, `ServerResponseDurationMs`, `ServerURL`, `SessionID`, `Success`, `ToolCallName`, `UserEmail`, and `UserID`.

#### New fields in existing datasets

- **DEX Application Tests**: `HTTPRedirectEndMs`, `HTTPRedirectStartMs`, `HTTPResponseBody`, and `HTTPResponseHeaders`.
- **DEX Device State Events**: `ExperimentalExtra`.
- **Firewall Events**: `FraudUserID`.
- **Gateway HTTP**: `AppControlInfo` and `ApplicationStatuses`.
- **Gateway DNS**: `InternalDNSDurationMs`.
- **HTTP Requests**: `FraudEmailRisk`, `FraudUserID`, and `PayPerCrawlStatus`.
- **Network Analytics Logs**: `DNSQueryName`, `DNSQueryType`, and `PFPCustomTag`.
- **WARP Toggle Changes**: `UserEmail`.
- **WARP Config Changes**: `UserEmail`.
- **Zero Trust Network Session Logs**: `SNI`.

For the complete field definitions for each dataset, refer to [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-09-log-fields-updated/#page","headline":"New MCP Portal Logs dataset and new fields across multiple Logpush datasets in Cloudflare Logs","description":"New MCP Portal Logs dataset is now available, along with new fields for multiple Logpush datasets in Cloudflare Logs.","url":"https://developers.cloudflare.com/changelog/post/2026-03-09-log-fields-updated/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-09-log-fields-updated/og.png?v=37655141ba8f5e9e","dateModified":"2026-03-09","datePublished":"2026-03-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
