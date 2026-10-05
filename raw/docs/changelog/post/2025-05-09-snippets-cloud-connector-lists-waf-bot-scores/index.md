---
description: Snippets and Cloud Connector now support user-defined IP, AS, and Hostname Custom Lists — plus Bot Score and WAF Attack Score in Snippets.
title: More ways to match — Snippets now support Custom Lists, Bot Score, and WAF Attack Score
image: https://developers.cloudflare.com/changelog/post/2025-05-09-snippets-cloud-connector-lists-waf-bot-scores/og.png?v=eded7cb4602e7288
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 9, 2025

## More ways to match — Snippets now support Custom Lists, Bot Score, and WAF Attack Score

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-09-snippets-cloud-connector-lists-waf-bot-scores/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now use IP, Autonomous System (AS), and Hostname [custom lists](https://developers.cloudflare.com/waf/tools/lists/custom-lists/) to route traffic to [Snippets](https://developers.cloudflare.com/rules/snippets/) and [Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/), giving you greater precision and control over how you match and process requests at the edge.

In Snippets, you can now also match on [Bot Score](https://developers.cloudflare.com/bots/concepts/bot-score/) and [WAF Attack Score](https://developers.cloudflare.com/waf/detections/attack-score/), unlocking smarter edge logic for everything from request filtering and mitigation to [tarpitting](https://developers.cloudflare.com/rules/snippets/examples/slow-suspicious-requests/) and logging.

**What’s new:**

- [Custom lists](https://developers.cloudflare.com/waf/tools/lists/custom-lists/) matching – Snippets and Cloud Connector now support user-created IP, AS, and Hostname lists via dashboard or [Lists API](https://developers.cloudflare.com/api/resources/rules/subresources/lists/methods/list/). Great for shared logic across zones.
- [Bot Score](https://developers.cloudflare.com/bots/concepts/bot-score/) and [WAF Attack Score](https://developers.cloudflare.com/waf/detections/attack-score/) – Use Cloudflare’s intelligent traffic signals to detect bots or attacks and take advanced, tailored actions with just a few lines of code.

![New fields in Snippets](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1383,height=1351,format=webp/_astro/snippets-lists-scores.D05l6zgc.png)

These enhancements unlock new possibilities for building smarter traffic workflows with minimal code and maximum efficiency.

Learn more in the [Snippets](https://developers.cloudflare.com/rules/snippets/) and [Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/) documentation.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-09-snippets-cloud-connector-lists-waf-bot-scores/#page","headline":"More ways to match — Snippets now support Custom Lists, Bot Score, and WAF Attack Score","description":"Snippets and Cloud Connector now support user-defined IP, AS, and Hostname Custom Lists — plus Bot Score and WAF Attack Score in Snippets.","url":"https://developers.cloudflare.com/changelog/post/2025-05-09-snippets-cloud-connector-lists-waf-bot-scores/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-05-09-snippets-cloud-connector-lists-waf-bot-scores/og.png?v=eded7cb4602e7288","dateModified":"2025-05-09","datePublished":"2025-05-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
