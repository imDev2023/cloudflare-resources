---
description: Detect and score risky browsing behavior by integrating Cloudflare Gateway DNS signals into User Risk Scoring.
title: User risk scoring for high risk browsing activity
image: https://developers.cloudflare.com/changelog/post/2026-04-08-high-risk-browsing/og.png?v=279c951be0e5144c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 8, 2026

## User risk scoring for high risk browsing activity

[Risk Score](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-08-high-risk-browsing/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare One's **User Risk Scoring** now incorporates direct signals from **Gateway DNS traffic patterns**. This update allows security teams to automatically elevate a user's risk score when they visit high-risk or malicious domains, providing a more holistic view of internal threats.

#### Why this matters

Browsing activity is a primary indicator of potential compromise. By tying Gateway DNS logs to specific users, administrators can now flag individuals interacting with:

- **Security threats**: Domains associated with malware, phishing, or command-and-control (C2) centers.
- **High-risk content**: Categories such as questionable content or violence that may violate corporate compliance.

Even if a Gateway policy is set to **Block** the traffic, the interaction is still captured as a "hit" to ensure the user's risk profile reflects the attempted activity.

#### New risk behaviors

Two new behaviors are now available in the dashboard:

- **Suspicious Security Domain Visited**: Triggers when a user visits a domain in the security threats or security risk categories.
- **High risk domain visited**: Triggers when a user visits domains categorized as questionable content, violence, or CIPA.

To learn more and get started, refer to the [User Risk Scoring documentation](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-08-high-risk-browsing/#page","headline":"User risk scoring for high risk browsing activity","description":"Detect and score risky browsing behavior by integrating Cloudflare Gateway DNS signals into User Risk Scoring.","url":"https://developers.cloudflare.com/changelog/post/2026-04-08-high-risk-browsing/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-08-high-risk-browsing/og.png?v=279c951be0e5144c","dateModified":"2026-04-08","datePublished":"2026-04-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
