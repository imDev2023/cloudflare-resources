---
description: Track and manage user submission status directly in the Cloudflare Zero Trust dashboard
title: User Submission Triage Status Tracking
image: https://developers.cloudflare.com/changelog/post/2026-04-07-triage-status-tracking/og.png?v=a3b48010773f3344
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 7, 2026

## User Submission Triage Status Tracking

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-07-triage-status-tracking/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Email security now supports **Triage Status Tracking for User Submissions**. This enhancement gives SOC teams a streamlined way to track, manage, and prioritize user-submitted emails directly within the Cloudflare One dashboard.

- The User Submissions table now includes a **Status** column with three states: **Unreviewed** (new submissions awaiting triage), **Reviewed** (submissions assessed by the SOC team), and **Escalated** (submissions escalated to team submissions for further investigation). Analysts can quickly update statuses and filter the table to focus on what needs attention.
- SOC teams can now organize their triage workflows, avoid duplicate reviews, and make sure critical threats get escalated for deeper investigation—bringing order to the chaos of high-volume submission management.

Triage Status Tracking is **automatically available** for all Email security customers using the user submissions feature. No additional configuration is required; customers just need to make sure user submissions are being sent to their user submission aliases.

This applies to all Email security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-07-triage-status-tracking/#page","headline":"User Submission Triage Status Tracking","description":"Track and manage user submission status directly in the Cloudflare Zero Trust dashboard","url":"https://developers.cloudflare.com/changelog/post/2026-04-07-triage-status-tracking/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-07-triage-status-tracking/og.png?v=a3b48010773f3344","dateModified":"2026-04-07","datePublished":"2026-04-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
