---
description: Cloudflare's CASB integration with the Claude Compliance API gives security teams visibility into posture, data, and compliance risks across their organization's use of Claude.
title: CASB adds support for Claude Compliance API
image: https://developers.cloudflare.com/changelog/post/2026-05-19-casb-claude-compliance-api/og.png?v=36b587239d3b1266
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 19, 2026

## CASB adds support for Claude Compliance API

[CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-19-casb-claude-compliance-api/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/anthropic/) now integrates with the [Claude Compliance API ↗︎](https://support.claude.com/en/articles/13015708-access-the-compliance-api). This enhancement gives security teams visibility into Claude usage patterns, admin activity, and compliance-relevant events across their organization.

The Claude Compliance API provides structured access to audit logs and administrative actions within Claude Enterprise and Claude Platform. Cloudflare CASB ingests this data to surface security findings that help organizations enhance their security posture and enforce AI governance.

#### Key capabilities

Starting today, security teams can scan for security findings across the following assets:

- **Public projects** — Projects set to public visibility
- **Project attachment** — Files and documents added to projects that violate DLP policies
- **Chat files** — User-uploaded and provider-generated files that violate DLP policies
- **Chat messages** — User prompts and provider responses that violate DLP policies
- **Artifacts** — Provider-generated documents and files that violate DLP policies

#### Learn more

This [integration](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/anthropic/) is available to all Cloudflare One customers. New Cloudflare customers can sign up and start with their first two integrations for free. Existing customers can enable the integration directly in the dashboard. The integration begins scanning immediately and surfaces findings in the dashboard within minutes.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-19-casb-claude-compliance-api/#page","headline":"CASB adds support for Claude Compliance API","description":"Cloudflare's CASB integration with the Claude Compliance API gives security teams visibility into posture, data, and compliance risks across their organization's use of Claude.","url":"https://developers.cloudflare.com/changelog/post/2026-05-19-casb-claude-compliance-api/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-19-casb-claude-compliance-api/og.png?v=36b587239d3b1266","dateModified":"2026-05-19","datePublished":"2026-05-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
