---
description: Pay-as-you-go customers can now monitor daily usage costs and set spend thresholds with proactive email notifications.
title: Introducing Billable Usage dashboard and Budget alerts
image: https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/og.png?v=1d2b87805220a6e8
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 21, 2026

## Introducing Billable Usage dashboard and Budget alerts

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Pay-as-you-go customers can now monitor usage-based costs and configure spend alerts through two new features: the Billable Usage dashboard and Budget alerts.

#### Billable Usage dashboard

The Billable Usage dashboard provides daily visibility into usage-based costs across your Cloudflare account. The data comes from the same system that generates your monthly invoice, so the figures match your bill.

The dashboard displays:

- A bar chart showing daily usage charges for your billing period
- A sortable table breaking down usage by product, including total usage, billable usage, and cumulative costs
- Ability to view previous billing periods

Usage data aligns to your billing cycle, not the calendar month. The total usage cost shown at the end of a completed billing period matches the usage overage charges on your corresponding invoice.

To access the dashboard, go to **Manage Account** > **Billing** > **Billable Usage**.

![Screenshot of the Billable Usage dashboard in the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1033,height=757,format=webp/_astro/billable-usage-dashboard.CQvMdtrp.png)

#### Budget alerts

Budget alerts allow you to set dollar-based thresholds for your account-level usage spend. You receive an email notification when your projected monthly spend reaches your configured threshold, giving you proactive visibility into your bill before month-end.

To configure a budget alert:

1. Go to **Manage Account** > **Billing** > **Billable Usage**.
2. Select **Set Budget Alert**.
3. Enter a budget threshold amount greater than $0.
4. Select **Create**.

Alternatively, configure alerts via **Notifications** > **Add** > **Budget Alert**.

![Create Budget Alert modal in the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=315,height=374,format=webp/_astro/budget-alert-modal.BjIzGOLV.png)

You can create multiple budget alerts at different dollar amounts. The notifications system automatically deduplicates alerts if multiple thresholds trigger at the same time. Budget alerts are calculated daily based on your usage trends and fire once per billing cycle when your projected spend first crosses your threshold.

Both features are available to Pay-as-you-go accounts with usage-based products (Workers, R2, Images, etc.). Enterprise contract accounts are not supported.

For more information, refer to the [Usage based billing documentation](https://developers.cloudflare.com/billing/understand/usage-based-billing/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/#page","headline":"Introducing Billable Usage dashboard and Budget alerts","description":"Pay-as-you-go customers can now monitor daily usage costs and set spend thresholds with proactive email notifications.","url":"https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/og.png?v=1d2b87805220a6e8","dateModified":"2026-04-21","datePublished":"2026-04-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
