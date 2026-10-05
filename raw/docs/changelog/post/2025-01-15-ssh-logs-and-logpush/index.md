---
description: Easily configure automatic export of SSH command logs to third-party storage destinations or to security information and event management (SIEM) tools.
title: Export SSH command logs with Access for Infrastructure using Logpush
image: https://developers.cloudflare.com/changelog/post/2025-01-15-ssh-logs-and-logpush/og.png?v=593567be860d47a6
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 15, 2025

## Export SSH command logs with Access for Infrastructure using Logpush

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-01-15-ssh-logs-and-logpush/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Availability

Only available on Enterprise plans.

Cloudflare now allows you to send SSH command logs to storage destinations configured in [Logpush](https://developers.cloudflare.com/logs/logpush/), including third-party destinations. Once exported, analyze and audit the data as best fits your organization! For a list of available data fields, refer to the [SSH logs dataset](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/ssh_logs/).

To set up a Logpush job, refer to [Logpush integration](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-01-15-ssh-logs-and-logpush/#page","headline":"Export SSH command logs with Access for Infrastructure using Logpush","description":"Easily configure automatic export of SSH command logs to third-party storage destinations or to security information and event management (SIEM) tools.","url":"https://developers.cloudflare.com/changelog/post/2025-01-15-ssh-logs-and-logpush/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-01-15-ssh-logs-and-logpush/og.png?v=593567be860d47a6","dateModified":"2025-01-15","datePublished":"2025-01-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
