---
description: Evaluate how well your website supports AI agents, bots, and automated discovery protocols with the new Agent Readiness report
title: Agent Readiness scores now available in URL Scanner via the Cloudflare Dashboard
image: https://developers.cloudflare.com/changelog/post/2026-05-12-URL-scanner-report-agent-readiness/og.png?v=4e9e4b99ec108e4a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 12, 2026

## Agent Readiness scores now available in URL Scanner via the Cloudflare Dashboard

[Security Center](https://developers.cloudflare.com/security-center/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-12-URL-scanner-report-agent-readiness/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We’ve added a new **Agent Readiness** tab to URL Scanner reports accessible via the Cloudflare dashboard. This feature evaluates your site against emerging AI standards and provides six specialized scores to help you optimize for the next generation of AI agents and automated discovery.

The Internet is shifting from a human-read web to a machine-read web. AI agents now browse, interact with, and even perform transactions on websites. If a site isn't "agent-ready," these bots may consume excessive bandwidth, fail to find critical information, or be unable to navigate your services efficiently.

This update provides material value by breaking down readiness into six actionable categories:

- **Basic Web Presence**
- **Discoverability**
- **Content Accessibility**
- **Bot Access Control**
- **Protocol Discovery**
- **Commerce**

#### Accessing the report

You can view these scores for any scanned URL directly in the dashboard or via our API.

- **Dashboard:** Go to **Protect & Connect > Application Security > Investigate**. After running a scan, select the **Agent Readiness** tab in the report.
- **API:** Use the [URL Scanner API ↗︎](https://developers.cloudflare.com/radar/investigate/url-scanner/) to programmatically retrieve these scores for your infrastructure.

To learn more about the methodology behind these scores, refer to the [blogpost ↗︎](https://blog.cloudflare.com/agent-readiness/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-12-URL-scanner-report-agent-readiness/#page","headline":"Agent Readiness scores now available in URL Scanner via the Cloudflare Dashboard","description":"Evaluate how well your website supports AI agents, bots, and automated discovery protocols with the new Agent Readiness report","url":"https://developers.cloudflare.com/changelog/post/2026-05-12-URL-scanner-report-agent-readiness/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-12-URL-scanner-report-agent-readiness/og.png?v=4e9e4b99ec108e4a","dateModified":"2026-05-12","datePublished":"2026-05-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
