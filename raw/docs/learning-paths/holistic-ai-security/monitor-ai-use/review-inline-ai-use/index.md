---
description: Monitor AI application usage via Shadow IT.
title: Review inline AI use
image: https://developers.cloudflare.com/learning-paths/holistic-ai-security/monitor-ai-use/review-inline-ai-use/og.png?v=3e2e02d4829f06d8
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/learning-paths/llms.txt  
> Use this file to discover all available pages before exploring further.

# Review inline AI use

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/learning-paths/holistic-ai-security/monitor-ai-use/review-inline-ai-use/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

To review how your organization uses AI apps, start with the Cloudflare [Shadow IT dashboard](https://developers.cloudflare.com/cloudflare-one/insights/analytics/shadow-it-discovery/). You can filter the dashboard by application type and sort by Artificial Intelligence, which allows you to take several valuable actions, such as:

- Reviewing application usage: See which applications your users are engaging with and how often, based on traffic from connected devices or sites.
- Accessing application details: Learn more about the applications in use by reviewing their entries in the App Library.
- Designating application status: Use a [status marker](https://developers.cloudflare.com/cloudflare-one/insights/analytics/shadow-it-discovery/#approval-status) to categorize applications, so you can apply specific security policies to them.

![Shadow IT dashboard showing utilization of application statuses (Approved, Unapproved, In Review, Unreviewed).](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2048,height=1308,format=webp/_astro/shadowit-dashboard-ai-apps.Dbzn4dka.png)

This approach is most relevant for applications that your organization has not yet sanctioned. For example, if your business uses Google Workspace and its primary AI tool is Gemini, you would likely mark Gemini as *Approved*. While you can configure more specific data loss policies later, you can also target approved applications with greater specificity to detect risks unique to your organization.

![The App Library filtered to show some of the supported Artificial Intelligence applications.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1641,height=712,format=webp/_astro/ai-app-type-app-library.C5AB815M.png)
