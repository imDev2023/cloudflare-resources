---
description: User action logs for Remote Browser Isolation
title: Gain visibility into user actions in Zero Trust Browser Isolation sessions
image: https://developers.cloudflare.com/changelog/post/2025-03-03-user-action-logging/og.png?v=6895f77bf9330a40
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 4, 2025

## Gain visibility into user actions in Zero Trust Browser Isolation sessions

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-03-user-action-logging/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We're excited to announce that new logging capabilities for [Remote Browser Isolation (RBI)](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) through [Logpush](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/) are available in Beta starting today!

With these enhanced logs, administrators can gain visibility into end user behavior in the remote browser and track blocked data extraction attempts, along with the websites that triggered them, in an isolated session.

```json
{
	"AccountID": "$ACCOUNT_ID",
	"Decision": "block",
	"DomainName": "www.example.com",
	"Timestamp": "2025-02-27T23:15:06Z",
	"Type": "copy",
	"UserID": "$USER_ID"
}
```

User Actions available:

- **Copy & Paste**
- **Downloads & Uploads**
- **Printing**

Learn more about how to get started with Logpush in our [documentation](https://developers.cloudflare.com/logs/logpush/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-03-03-user-action-logging/#page","headline":"Gain visibility into user actions in Zero Trust Browser Isolation sessions","description":"User action logs for Remote Browser Isolation","url":"https://developers.cloudflare.com/changelog/post/2025-03-03-user-action-logging/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-03-03-user-action-logging/og.png?v=6895f77bf9330a40","dateModified":"2025-03-04","datePublished":"2025-03-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
