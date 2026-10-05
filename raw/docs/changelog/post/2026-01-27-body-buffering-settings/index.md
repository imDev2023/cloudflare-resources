---
description: New settings in Configuration Rules let you control how Cloudflare buffers HTTP request and response bodies before forwarding to origin or client.
title: Control request and response body buffering in Configuration Rules
image: https://developers.cloudflare.com/changelog/post/2026-01-27-body-buffering-settings/og.png?v=3570eea76a3d52c6
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 27, 2026

## Control request and response body buffering in Configuration Rules

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-27-body-buffering-settings/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now control how Cloudflare buffers HTTP request and response bodies using two new settings in [Configuration Rules](https://developers.cloudflare.com/rules/configuration-rules/).

#### Request body buffering

Controls how Cloudflare buffers HTTP request bodies before forwarding them to your origin server:

| Mode | Behavior |
| --- | --- |
| **Standard** (default) | Cloudflare can inspect a prefix of the request body for enabled functionality such as WAF and Bot Management. |
| **Full** | Buffers the entire request body before sending to origin. |
| **None** | No buffering — the request body streams directly to origin without inspection. |

#### Response body buffering

Controls how Cloudflare buffers HTTP response bodies before forwarding them to the client:

| Mode | Behavior |
| --- | --- |
| **Standard** (default) | Cloudflare can inspect a prefix of the response body for enabled functionality. |
| **None** | No buffering — the response body streams directly to the client without inspection. |

Caution

Setting body buffering to **None** may break security functionality that requires body inspection, including the Web Application Firewall (WAF) and Bot Management. Ensure that any paths where you disable buffering do not require security inspection.

#### API example

```json
{
  "action": "set_config",
  "action_parameters": {
    "request_body_buffering": "standard",
    "response_body_buffering": "none"
  }
}
```

For more information, refer to [Configuration Rules](https://developers.cloudflare.com/rules/configuration-rules/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-27-body-buffering-settings/#page","headline":"Control request and response body buffering in Configuration Rules","description":"New settings in Configuration Rules let you control how Cloudflare buffers HTTP request and response bodies before forwarding to origin or client.","url":"https://developers.cloudflare.com/changelog/post/2026-01-27-body-buffering-settings/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-27-body-buffering-settings/og.png?v=3570eea76a3d52c6","dateModified":"2026-01-27","datePublished":"2026-01-27","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
