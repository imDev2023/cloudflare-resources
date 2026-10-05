---
description: You can now apply email link isolation based on disposition
title: Expanded Email Link Isolation
image: https://developers.cloudflare.com/changelog/post/2025-08-07-expanded-link-isolation/og.png?v=5856127086c70669
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 7, 2025

## Expanded Email Link Isolation

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-07-expanded-link-isolation/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

When you deploy MX or Inline, not only can you apply email link isolation to suspicious links in all emails (including benign), you can now also apply email link isolation to all links of a specified disposition. This provides more flexibility in controlling user actions within emails.

For example, you may want to deliver suspicious messages but isolate the links found within them so that users who choose to interact with the links will not accidentally expose your organization to threats. This means your end users are more secure than ever before.

![Expanded Email Link Isolation Configuration](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=497,format=webp/_astro/expanded-link-actions.DziIg6E8.jpg)

To isolate all links within a message based on the disposition, select **Settings** > **Link Actions** > **View** and select **Configure**. As with other other links you isolate, an interstitial will be provided to warn users that this site has been isolated and the link will be recrawled live to evaluate if there are any changes in our threat intel. Learn more about this feature on [Configure link actions ↗︎](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-link-actions/).

This feature is available across these Email security packages:

- **Enterprise**
- **Enterprise + PhishGuard**

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-07-expanded-link-isolation/#page","headline":"Expanded Email Link Isolation","description":"You can now apply email link isolation based on disposition","url":"https://developers.cloudflare.com/changelog/post/2025-08-07-expanded-link-isolation/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-07-expanded-link-isolation/og.png?v=5856127086c70669","dateModified":"2025-08-07","datePublished":"2025-08-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
