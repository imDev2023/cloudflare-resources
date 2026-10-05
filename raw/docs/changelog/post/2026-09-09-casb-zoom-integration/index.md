---
description: Cloudflare CASB now scans Zoom for security misconfigurations and data risks across account settings, users, meetings, and recordings.
title: New CASB integration for Zoom
image: https://developers.cloudflare.com/changelog/post/2026-09-09-casb-zoom-integration/og.png?v=7f2304b47760b177
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 9, 2026

## New CASB integration for Zoom

[CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-09-casb-zoom-integration/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/) now integrates with [Zoom](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/zoom/). The integration connects through Cloudflare's pre-built OAuth application — no manual app setup in Zoom is required. After an initial scan, CASB continuously scans your Zoom account to surface new findings as your environment changes.

Zoom is widely used for meetings, webinars, and collaboration. Misconfigurations in account settings, meeting security controls, and recording access can expose organizations to data leakage, unauthorized access, and compliance risk. Cloudflare CASB ingests Zoom account data via API to surface security findings across these areas.

#### Key capabilities

Starting today, security teams can scan for security findings across the following assets:

- **Account settings** — Detect weak password policies, unlocked security controls, and two-factor authentication gaps across your Zoom account
- **User accounts** — Identify users not enforcing SSO, accounts with insecure host keys, unverified or inactive users, and unsafe overrides of account-level security settings
- **Meetings** — Surface meetings without passwords or waiting rooms, meetings using Personal Meeting IDs (PMIs), and meetings with external domain hosts
- **Recordings** — Detect publicly accessible cloud recordings, recordings without passcodes, and weak recording password configurations
- **Content** — Identify sensitive information in meeting and recording content via DLP Profile matching

#### Learn more

This [integration](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/zoom/) is available to all Cloudflare Zero Trust customers today. New customers can sign up and start with their first two integrations for free. Existing customers can enable the integration directly in the Cloudflare One dashboard under **Cloud & SaaS findings** > **Integrations**. The integration begins scanning immediately and surfaces findings in the dashboard within minutes.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-09-casb-zoom-integration/#page","headline":"New CASB integration for Zoom","description":"Cloudflare CASB now scans Zoom for security misconfigurations and data risks across account settings, users, meetings, and recordings.","url":"https://developers.cloudflare.com/changelog/post/2026-09-09-casb-zoom-integration/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-09-casb-zoom-integration/og.png?v=7f2304b47760b177","dateModified":"2026-09-09","datePublished":"2026-09-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
