---
description: Feedback for invalid submissions that prevent Email security from providing continuous protection
title: Invalid Submissions Feedback
image: https://developers.cloudflare.com/changelog/post/2025-09-23-invalid-submissions/og.png?v=8faac878528d1271
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 23, 2025

## Invalid Submissions Feedback

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-23-invalid-submissions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Email security relies on your submissions to continuously improve our detection models. However, we often receive submissions in formats that cannot be ingested, such as incomplete EMLs, screenshots, or text files.

To ensure all customer feedback is actionable, we have launched two new features to manage invalid submissions sent to our team and user [submission aliases](https://developers.cloudflare.com/cloudflare-one/email-security/settings/phish-submissions/submission-addresses/):

- **Email Notifications:** We now automatically notify users by email when they provide an invalid submission, educating them on the correct format. To disable notifications, go to **[Settings ↗︎](https://one.dash.cloudflare.com/?to=/:account/email-security/settings)** > **Invalid submission emails** and turn the feature off.

![EmailSec-Invalid-Submissions-Toggle](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1096,height=175,format=webp/_astro/EmailSec-Invalid-Submissions-Toggle.DXjbR6aX.png)

- **Invalid Submission dashboard:** You can quickly identify which users need education to provide valid submissions so Cloudflare can provide continuous protection.

![EmailSec-Invalid-Submissions-Dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1132,height=511,format=webp/_astro/EmailSec-Invalid-Submissions-Dashboard.zuf1on2n.png)

Learn more about this feature on [invalid submissions](https://developers.cloudflare.com/cloudflare-one/email-security/submissions/invalid-submissions/).

This feature is available across these Email security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-23-invalid-submissions/#page","headline":"Invalid Submissions Feedback","description":"Feedback for invalid submissions that prevent Email security from providing continuous protection","url":"https://developers.cloudflare.com/changelog/post/2025-09-23-invalid-submissions/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-23-invalid-submissions/og.png?v=8faac878528d1271","dateModified":"2025-09-23","datePublished":"2025-09-23","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
