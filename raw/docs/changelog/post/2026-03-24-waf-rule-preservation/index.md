---
description: You can now extend the AI Crawl Control WAF rule with custom user agents, path-based exceptions, and additional expression clauses without affecting your AI Crawl Control settings.
title: Advanced WAF customization for AI Crawl Control blocks
image: https://developers.cloudflare.com/changelog/post/2026-03-24-waf-rule-preservation/og.png?v=b1d864deb939da05
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 24, 2026

## Advanced WAF customization for AI Crawl Control blocks

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-24-waf-rule-preservation/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Crawl Control now supports extending the underlying WAF rule with custom modifications. Any changes you make directly in the WAF custom rules editor — such as adding path-based exceptions, extra user agents, or additional expression clauses — are preserved when you update crawler actions in AI Crawl Control.

If the WAF rule expression has been modified in a way AI Crawl Control cannot parse, a warning banner appears on the **Crawlers** page with a link to view the rule directly in WAF.

For more information, refer to [WAF rule management](https://developers.cloudflare.com/ai-crawl-control/features/manage-ai-crawlers/#waf-rule-management).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-24-waf-rule-preservation/#page","headline":"Advanced WAF customization for AI Crawl Control blocks","description":"You can now extend the AI Crawl Control WAF rule with custom user agents, path-based exceptions, and additional expression clauses without affecting your AI Crawl Control settings.","url":"https://developers.cloudflare.com/changelog/post/2026-03-24-waf-rule-preservation/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-24-waf-rule-preservation/og.png?v=b1d864deb939da05","dateModified":"2026-03-24","datePublished":"2026-03-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
