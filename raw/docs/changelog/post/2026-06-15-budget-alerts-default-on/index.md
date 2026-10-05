---
description: Eligible Pay-as-you-go accounts now receive an automatic $10 budget alert at the start of each new billing cycle. You can edit the threshold or remove the alert at any time.
title: Budget alerts now on by default for Pay-as-you-go accounts
image: https://developers.cloudflare.com/changelog/post/2026-06-15-budget-alerts-default-on/og.png?v=0c1eeccd5ec07d2b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 20, 2026

## Budget alerts now on by default for Pay-as-you-go accounts

[Billing](https://developers.cloudflare.com/billing/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-15-budget-alerts-default-on/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We are turning on budget alerts by default for eligible Pay-as-you-go accounts. If your account does not already have a budget alert, Cloudflare will create one for you with a $10 account-level threshold. Your default alert will enable at the turn of your next billing cycle, so it will not fire based on usage you have already incurred.

We are rolling this out in cohorts over the coming weeks, so eligible accounts may see their default alert appear at different times.

The default alert behaves exactly like an alert you would create yourself. When your cumulative usage-based spend this cycle reaches the threshold, you receive an email notification. The alert is informational only. It does not cap your usage or impact your account in any way.

Usage is processed once per day for the prior day's activity, so budget alerts fire the day after the threshold is reached rather than in real time.

Budget alerts only consider spend on usage-based products. Recurring subscription fees, such as the Workers Paid plan fee or other monthly plan charges, are not included in the threshold calculation.

You can change the threshold, add additional alerts, or remove the default alert entirely from **Manage Account** > **Billing** > **Billable Usage**, or from your Notifications settings. If you already configured your own budget alert, nothing changes.

Enterprise contract accounts are not in scope.

For more information, refer to the [Budget alerts documentation](https://developers.cloudflare.com/billing/manage/budget-alerts/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-15-budget-alerts-default-on/#page","headline":"Budget alerts now on by default for Pay-as-you-go accounts","description":"Eligible Pay-as-you-go accounts now receive an automatic $10 budget alert at the start of each new billing cycle. You can edit the threshold or remove the alert at any time.","url":"https://developers.cloudflare.com/changelog/post/2026-06-15-budget-alerts-default-on/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-15-budget-alerts-default-on/og.png?v=0c1eeccd5ec07d2b","dateModified":"2026-07-20","datePublished":"2026-07-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
