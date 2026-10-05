---
description: Monitor and secure generative AI usage.
title: Monitor AI usage at your organization
image: https://developers.cloudflare.com/learning-paths/holistic-ai-security/monitor-ai-use/og.png?v=63981e69ae635429
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/learning-paths/llms.txt  
> Use this file to discover all available pages before exploring further.

# Monitor AI usage at your organization

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/learning-paths/holistic-ai-security/monitor-ai-use/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Monitoring AI usage is one of the first steps in assessing holistic risk. Cloudflare provides a number of ways to understand both sanctioned and unsanctioned use of AI and chat applications within your Zero Trust deployment. Reviewing your detected usage should give you a sense of which AI apps are used in your organization as well as what type of policies you need to create based on what should be supported versus restricted.

After you begin to understand your organization's AI usage, you should develop a balanced perspective on what constitutes sanctioned use of a tool. A good practice is to review applications in phases and then apply security policies based on those phases. For example, you can apply different security policies to applications that are considered approved, unapproved, unreviewed, or in review until they pass your corporate security standards and data privacy reviews.

This section will detail options for assessing and understanding that risk by using inline (client) and out-of-band (API CASB) based methods.
