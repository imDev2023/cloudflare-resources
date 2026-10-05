---
description: The Credentials and Secrets DLP profile now includes predefined entries to detect Cloudflare User API Keys, User API Tokens, and Account Owned API Tokens across your environment.
title: Detect Cloudflare API tokens with DLP
image: https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-api-token-detections/og.png?v=084a3d38b5492320
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 14, 2026

## Detect Cloudflare API tokens with DLP

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-api-token-detections/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The **Credentials and Secrets** DLP profile now includes three new predefined entries for detecting Cloudflare API credentials:

| Entry name | Token prefix | Detects |
| --- | --- | --- |
| Cloudflare User API Key | `cfk_` | User-scoped API keys |
| Cloudflare User API Token | `cfut_` | User-scoped API tokens |
| Cloudflare Account Owned API Token | `cfat_` | Account-scoped API tokens |

These detections target the new [Cloudflare API credential format](https://developers.cloudflare.com/fundamentals/api/get-started/token-formats/), which uses a structured prefix and a CRC32 checksum suffix. The identifiable prefix makes it possible to detect leaked credentials with high confidence and low false positive rates — no surrounding context such as `Authorization: Bearer` headers is required.

Credentials generated before this format change will not be matched by these entries.

#### How to enable Cloudflare API token detections

1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **DLP** > **DLP Profiles**.
2. Select the **Credentials and Secrets** profile.
3. Turn on one or more of the new Cloudflare API token entries.
4. Use the profile in a Gateway HTTP policy to log or block traffic containing these credentials.

Example policy:

| Selector | Operator | Value | Action |
| --- | --- | --- | --- |
| DLP Profile | in | *Credentials and Secrets* | Block |

You can also enable individual entries to scope detection to specific credential types — for example, enabling **Account Owned API Token** detection without enabling **User API Key** detection.

For more information, refer to [predefined DLP profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-api-token-detections/#page","headline":"Detect Cloudflare API tokens with DLP","description":"The Credentials and Secrets DLP profile now includes predefined entries to detect Cloudflare User API Keys, User API Tokens, and Account Owned API Tokens across your environment.","url":"https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-api-token-detections/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-api-token-detections/og.png?v=084a3d38b5492320","dateModified":"2026-04-14","datePublished":"2026-04-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
