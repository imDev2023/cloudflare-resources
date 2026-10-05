---
description: "Use the new enabled property on live inputs to programmatically control whether a live input accepts incoming broadcasts.\n"
title: Stream live inputs can now be disabled and enabled
image: https://developers.cloudflare.com/changelog/post/2026-02-24-disable-live-inputs/og.png?v=b70531611a447b16
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 24, 2026

## Stream live inputs can now be disabled and enabled

[Stream](https://developers.cloudflare.com/stream/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-24-disable-live-inputs/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now disable a live input to reject incoming RTMPS and SRT connections. When a live input is disabled, any broadcast attempts will fail to connect.

This gives you more control over your live inputs:

- Temporarily pause an input without deleting it
- Programmatically end creator broadcasts
- Prevent new broadcasts from starting on a specific input

To disable a live input via the API, set the `enabled` property to `false`:

```bash
curl --request PUT \
https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/live_inputs/{input_id} \
--header "Authorization: Bearer <API_TOKEN>" \
--data '{"enabled": false}'
```

You can also disable or enable a live input from the **Live inputs** list page or the live input detail page in the Dashboard.

All existing live inputs remain enabled by default. For more information, refer to [Start a live stream](https://developers.cloudflare.com/stream/stream-live/start-stream-live/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-24-disable-live-inputs/#page","headline":"Stream live inputs can now be disabled and enabled","description":"Use the new enabled property on live inputs to programmatically control whether a live input accepts incoming broadcasts.","url":"https://developers.cloudflare.com/changelog/post/2026-02-24-disable-live-inputs/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-24-disable-live-inputs/og.png?v=b70531611a447b16","dateModified":"2026-02-24","datePublished":"2026-02-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
