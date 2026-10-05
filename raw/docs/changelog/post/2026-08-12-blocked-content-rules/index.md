---
description: Create plaintext or regular expression rules that block emails based on subject or body content.
title: Block emails by content with blocked content rules
image: https://developers.cloudflare.com/changelog/post/2026-08-12-blocked-content-rules/og.png?v=ed9130df6a558ae7
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 12, 2026

## Block emails by content with blocked content rules

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-12-blocked-content-rules/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Email security now lets administrators write their own content-based blocking rules. A new **Blocked content** area under **Policies & rules** lets you define a plaintext string or a regular expression, choose whether to scan the message subject, body, or both, and automatically block any message that matches.

- Create rules using either **plaintext** matches or **regular expressions** — useful for blocking targeted phishing campaigns, known-bad phrases, or content patterns unique to your organization.
- Choose the **search location** for each rule: **subject**, **body**, or **subject and body**.
- Use the built-in **regular expression checker** to validate your pattern against sample text before saving, so you can confirm the rule matches what you expect and avoid false positives.
- Matching messages are marked with a malicious [disposition](https://developers.cloudflare.com/cloudflare-one/email-security/reference/dispositions-and-attributes/) and prevented from reaching users' inboxes.

Blocked content rules currently only support the block action.

This feature is available for the following Email security packages:

- **Enterprise**
- **Enterprise + PhishGuard**

To get started, refer to [Blocked content](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/blocked-content/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-12-blocked-content-rules/#page","headline":"Block emails by content with blocked content rules","description":"Create plaintext or regular expression rules that block emails based on subject or body content.","url":"https://developers.cloudflare.com/changelog/post/2026-08-12-blocked-content-rules/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-12-blocked-content-rules/og.png?v=ed9130df6a558ae7","dateModified":"2026-08-12","datePublished":"2026-08-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
