---
description: Make your website temporarily unavailable during large changes using Cloudflare Workers, Waiting Room, or Access.
title: Maintenance mode
image: https://developers.cloudflare.com/fundamentals/performance/maintenance-mode/og.png?v=e0a220861f558387
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/fundamentals/llms.txt  
> Use this file to discover all available pages before exploring further.

# Maintenance mode

Last updated Apr 20, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/fundamentals/performance/maintenance-mode/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

If you need to make large changes to your website, you may want to make your site temporarily unavailable.

## With code

If you are familiar with code, [create a Worker](https://developers.cloudflare.com/workers/get-started/guide/) that returns an [HTML page](https://developers.cloudflare.com/workers/examples/return-html/) to any site visitors.

![Workers maintenance page returned instead of your website](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=618,height=271,format=webp/_astro/workers-page.DnkGi-jv.png)

## Without code

### Business and Enterprise

For a maintenance page without code, Business and Enterprise uses can create a [Cloudflare Waiting Room](https://developers.cloudflare.com/waiting-room/how-to/create-waiting-room/).

Certain customization and queue options depend on your [plan](https://developers.cloudflare.com/waiting-room/plans/).

![Waiting room page returned instead of your website](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1042,height=544,format=webp/_astro/waiting-room-page.C-z8rg-V.png)

### All plans

Users on all plans can [create an Access application](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/). Make sure to limit your [Access policy](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/policy-management/#create-a-policy) to only include yourself and any collaborators.

If needed, you can also further [customize the login page](https://developers.cloudflare.com/cloudflare-one/reusable-components/custom-pages/access-login-page/).

![Example Access login page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=618,height=510,format=webp/_astro/access-page.C47nT0tE.png)
