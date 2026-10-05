---
description: Page through complete result sets in the dashboard and API, up from the previous 1,000-record cap
title: Unlimited result paging in Investigations
image: https://developers.cloudflare.com/changelog/post/2026-03-15-infinite-paging-investigations/og.png?v=5845a2a9aecbef05
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 15, 2026

## Unlimited result paging in Investigations

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-15-infinite-paging-investigations/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Investigations now support unlimited result paging in both the dashboard and the API, removing the previous 1,000-record cap. Security teams can page through complete result sets when searching across large mail volumes, giving SOC analysts and automated workflows deeper visibility for forensics and threat hunting.

In the dashboard, infinite paging is now supported in the Investigations view. The 1,000-record ceiling has been removed, so you can navigate through the full result set directly in the UI. The [Investigations API](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/methods/list) now returns up to 10,000 records per page (up from 1,000), with no cap on total result volume across pages.

For high-volume use cases, we recommend:

- **[Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/email-security-logs/) to a SIEM** for full-fidelity datasets and long-term retention.
- **SOAR playbooks** against the async bulk action API for large-scale remediation. Bulk actions initiated from the dashboard remain capped at 1,000 messages per action.
- **The Investigations API** for report exports larger than 1,000 results, which is the dashboard download cap.

This applies to all Email Security packages:

- **Advantage**
- **Enterprise**
- **Enterprise + PhishGuard**

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-15-infinite-paging-investigations/#page","headline":"Unlimited result paging in Investigations","description":"Page through complete result sets in the dashboard and API, up from the previous 1,000-record cap","url":"https://developers.cloudflare.com/changelog/post/2026-03-15-infinite-paging-investigations/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-15-infinite-paging-investigations/og.png?v=5845a2a9aecbef05","dateModified":"2026-03-15","datePublished":"2026-03-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
