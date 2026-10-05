---
description: Resources in the Cloudflare Terraform Provider that have sensitive properties will not show those values in logs.
title: Cloudflare Terraform Provider now properly redacts sensitive values
image: https://developers.cloudflare.com/changelog/post/2025-03-21-sensitive-values-redacted/og.png?v=239534a7ba369a7f
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 21, 2025

## Cloudflare Terraform Provider now properly redacts sensitive values

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-21-sensitive-values-redacted/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

In the [Cloudflare Terraform Provider ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) versions 5.2.0 and above, sensitive properties of resources are redacted in logs. Sensitive properties in [Cloudflare's OpenAPI Schema ↗︎](https://raw.githubusercontent.com/cloudflare/api-schemas/refs/heads/main/openapi.yaml) are now annotated with `x-sensitive: true`. This results in proper auto-generation of the corresponding Terraform resources, and prevents sensitive values from being shown when you run Terraform commands.

This issue affected [resources ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) related to these products and features:

- Alerts and Audit Logs
- Device API
- DLP
- DNS
- Magic Visibility
- Magic WAN
- TLS Certs and Hostnames
- Tunnels
- Turnstile
- Workers
- Zaraz

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-03-21-sensitive-values-redacted/#page","headline":"Cloudflare Terraform Provider now properly redacts sensitive values","description":"Resources in the Cloudflare Terraform Provider that have sensitive properties will not show those values in logs.","url":"https://developers.cloudflare.com/changelog/post/2025-03-21-sensitive-values-redacted/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-03-21-sensitive-values-redacted/og.png?v=239534a7ba369a7f","dateModified":"2025-03-21","datePublished":"2025-03-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
