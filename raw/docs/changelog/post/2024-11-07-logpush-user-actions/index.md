---
description: Send user action logs for Email security to an endpoint of your choice with Cloudflare Logpush.
title: Use Logpush for Email security user actions
image: https://developers.cloudflare.com/changelog/post/2024-11-07-logpush-user-actions/og.png?v=9b049934aeb12038
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 7, 2024

## Use Logpush for Email security user actions

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2024-11-07-logpush-user-actions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now send user action logs for Email security to an endpoint of your choice with Cloudflare Logpush.

Filter logs matching specific criteria you have set or select from multiple fields you want to send. For all users, we will log the date and time, user ID, IP address, details about the message they accessed, and what actions they took.

When creating a new Logpush job, remember to select **Audit logs** as the dataset and filter by:

- **Field**: `"ResourceType"`
- **Operator**: `"starts with"`
- **Value**: `"email_security"`.

![Logpush-user-actions](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=829,height=454,format=webp/_astro/Logpush-User-Actions.D14fWgmq.png)

For more information, refer to [Enable user action logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/email-security-logs/#enable-user-action-logs).

This feature is available across all Email security packages:

- **Enterprise**
- **Enterprise + PhishGuard**

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2024-11-07-logpush-user-actions/#page","headline":"Use Logpush for Email security user actions","description":"Send user action logs for Email security to an endpoint of your choice with Cloudflare Logpush.","url":"https://developers.cloudflare.com/changelog/post/2024-11-07-logpush-user-actions/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2024-11-07-logpush-user-actions/og.png?v=9b049934aeb12038","dateModified":"2024-11-07","datePublished":"2024-11-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
