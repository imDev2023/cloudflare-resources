---
description: Logpush now supports subrequest merging for the http_requests dataset, delivering one log line per visitor request.
title: Logpush subrequest merging for HTTP requests
image: https://developers.cloudflare.com/changelog/post/2026-04-21-logpush-subrequests-merging/og.png?v=d3c0d92e90c41ea0
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 21, 2026

## Logpush subrequest merging for HTTP requests

[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-21-logpush-subrequests-merging/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

When a Cloudflare Worker intercepts a visitor request, it can dispatch additional outbound fetch calls called subrequests. By default, each subrequest generates its own log entry in Logpush, resulting in multiple log lines per visitor request. With subrequest merging enabled, subrequest data is embedded as a nested array field on the parent log record instead.

#### What's new

- New subrequest\_merging field on Logpush jobs — Set "merge\_subrequests": true when creating or updating an http\_requests Logpush job to enable the feature.
- New Subrequests log field — When subrequest merging is enabled, a Subrequests field ( `array\<object\>`) is added to each parent request log record. Each element in the array contains the standard http\_requests fields for that subrequest.

#### Limitations

- Applies to the http\_requests (zone-scoped) dataset only.
- A maximum of 50 subrequests are merged per parent request. Subrequests beyond this limit are passed through unmodified as individual log entries.
- Subrequests must complete within 5 minutes of the visitor request. Subrequests that exceed this window are passed through unmodified.
- Subrequests that do not qualify appear as separate log entries — no data is lost.
- Subrequest merging is being gradually rolled out and is not yet available on all zones. Contact your account team for concerns or to ensure it is enabled for your zone.
- For more information, refer to [Subrequests](https://developers.cloudflare.com/logs/logpush/logpush-job/subrequests/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-21-logpush-subrequests-merging/#page","headline":"Logpush subrequest merging for HTTP requests","description":"Logpush now supports subrequest merging for the http_requests dataset, delivering one log line per visitor request.","url":"https://developers.cloudflare.com/changelog/post/2026-04-21-logpush-subrequests-merging/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-21-logpush-subrequests-merging/og.png?v=d3c0d92e90c41ea0","dateModified":"2026-04-21","datePublished":"2026-04-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
