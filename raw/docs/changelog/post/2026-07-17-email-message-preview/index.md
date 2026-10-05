---
description: Inspect the HTML, text, headers, attachments, and raw source of sent emails from the Email Service Activity log.
title: Preview sent emails in the Activity log
image: https://developers.cloudflare.com/changelog/post/2026-07-17-email-message-preview/og.png?v=177e4ca65be97127
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 17, 2026

## Preview sent emails in the Activity log

[Email Service](https://developers.cloudflare.com/email-service/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-17-email-message-preview/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now preview the content of sent emails directly from the Email Service Activity log. Expand a sent email and open the new **Preview** section to inspect the message as it was sent, across tabs for the rendered **HTML** body, the **Text** body, the **Headers**, the **Attachments**, and the full **Raw** [RFC 5322 ↗︎](https://datatracker.ietf.org/doc/html/rfc5322) source.

![The rendered HTML preview of a sent email in the Email Service Activity log](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2864,height=1172,format=webp/_astro/email-message-preview.Bj6Lk8Y6.png)

Previously, the Activity log surfaced delivery and authentication metadata but not the message content, making rendering and content issues harder to debug. Message preview closes that gap.

To make messages previewable, turn on **Email preview** in your sending domain's settings. Previews cover messages sent while the setting is turned on and are retained for about seven days. Sending domains onboarded on or after 2026-07-02 have **Email preview** turned on automatically.

![The Email preview setting in a sending domain's settings](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2256,height=264,format=webp/_astro/email-preview-setting.XEd1WIiO.png)

Refer to [Email logs](https://developers.cloudflare.com/email-service/observability/logs/#message-preview) for more information.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-17-email-message-preview/#page","headline":"Preview sent emails in the Activity log","description":"Inspect the HTML, text, headers, attachments, and raw source of sent emails from the Email Service Activity log.","url":"https://developers.cloudflare.com/changelog/post/2026-07-17-email-message-preview/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-17-email-message-preview/og.png?v=177e4ca65be97127","dateModified":"2026-07-17","datePublished":"2026-07-17","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
