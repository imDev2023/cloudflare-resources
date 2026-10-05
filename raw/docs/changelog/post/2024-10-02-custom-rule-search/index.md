---
description: New UI improvements for Magic Firewall
title: Search for custom rules using rule name and/or ID
image: https://developers.cloudflare.com/changelog/post/2024-10-02-custom-rule-search/og.png?v=07f05a6bbb080b5a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 2, 2024

## Search for custom rules using rule name and/or ID

[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2024-10-02-custom-rule-search/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The Magic Firewall dashboard now allows you to search custom rules using the rule name and/or ID.

1. Log into the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) and select your account.
2. Go to **Analytics & Logs** > **Network Analytics**.
3. Select **Magic Firewall**.
4. Add a filter for **Rule ID**.

![Search for firewall rules with rule IDs](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1032,height=801,format=webp/_astro/search-with-rule-id.DJgzqgKk.png)

Additionally, the rule ID URL link has been added to Network Analytics.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2024-10-02-custom-rule-search/#page","headline":"Search for custom rules using rule name and/or ID","description":"New UI improvements for Magic Firewall","url":"https://developers.cloudflare.com/changelog/post/2024-10-02-custom-rule-search/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2024-10-02-custom-rule-search/og.png?v=07f05a6bbb080b5a","dateModified":"2024-10-02","datePublished":"2024-10-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
