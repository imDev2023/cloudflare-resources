---
description: Configuration Rules now let you selectively enable or disable Polish with WebP format for precise control over image optimization.
title: Fine-tune image optimization — WebP now supported in Configuration Rules
image: https://developers.cloudflare.com/changelog/post/2025-05-30-configuration-rules-webp/og.png?v=0db194bc9e111419
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 30, 2025

## Fine-tune image optimization — WebP now supported in Configuration Rules

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-30-configuration-rules-webp/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now enable [Polish](https://developers.cloudflare.com/images/polish/activate-polish/) with the `webp` format directly in [Configuration Rules](https://developers.cloudflare.com/rules/configuration-rules/), allowing you to optimize image delivery for specific routes, user agents, or A/B tests — without applying changes zone-wide.

**What’s new:**

- [WebP](https://developers.cloudflare.com/images/polish/compression/#webp) is now a supported [value](https://developers.cloudflare.com/rules/configuration-rules/settings/#polish) in the **Polish** setting for Configuration Rules.

This gives you more precise control over how images are compressed and delivered, whether you're targeting modern browsers, running experiments, or tailoring performance by geography or device type.

Learn more in the [Polish](https://developers.cloudflare.com/images/polish/) and [Configuration Rules](https://developers.cloudflare.com/rules/configuration-rules/) documentation.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-30-configuration-rules-webp/#page","headline":"Fine-tune image optimization — WebP now supported in Configuration Rules","description":"Configuration Rules now let you selectively enable or disable Polish with WebP format for precise control over image optimization.","url":"https://developers.cloudflare.com/changelog/post/2025-05-30-configuration-rules-webp/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-05-30-configuration-rules-webp/og.png?v=0db194bc9e111419","dateModified":"2025-05-30","datePublished":"2025-05-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
