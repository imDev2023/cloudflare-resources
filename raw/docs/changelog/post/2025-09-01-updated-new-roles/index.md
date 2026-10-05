---
description: More granular controls for Email security roles
title: Updated Email security roles
image: https://developers.cloudflare.com/changelog/post/2025-09-01-updated-new-roles/og.png?v=d4a8689fbd9cf730
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 1, 2025

## Updated Email security roles

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-01-updated-new-roles/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

To provide more granular controls, we refined the [existing roles](https://developers.cloudflare.com/cloudflare-one/roles-permissions/#email-security-roles) for Email security and launched a new Email security role as well.

All Email security roles no longer have read or write access to any of the other Zero Trust products:

- **Email Configuration Admin**
- **Email Integration Admin**
- **Email security Read Only**
- **Email security Analyst**
- **Email security Policy Admin**
- **Email security Reporting**

To configure [Data Loss Prevention (DLP)](https://developers.cloudflare.com/cloudflare-one/email-security/outbound-dlp/) or [Remote Browser Isolation (RBI)](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/#set-up-clientless-web-isolation), you now need to be an admin for the Zero Trust dashboard with the **Cloudflare Zero Trust** role.

Also through customer feedback, we have created a new additive role to allow **Email security Analyst** to create, edit, and delete Email security policies, without needing to provide access via the **Email Configuration Admin** role. This role is called **Email security Policy Admin**, which can read all settings, but has write access to [allow policies](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/allow-policies/), [trusted domains](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/trusted-domains/), and [blocked senders](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/blocked-senders/).

This feature is available across these Email security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-01-updated-new-roles/#page","headline":"Updated Email security roles","description":"More granular controls for Email security roles","url":"https://developers.cloudflare.com/changelog/post/2025-09-01-updated-new-roles/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-01-updated-new-roles/og.png?v=d4a8689fbd9cf730","dateModified":"2025-09-01","datePublished":"2025-09-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
