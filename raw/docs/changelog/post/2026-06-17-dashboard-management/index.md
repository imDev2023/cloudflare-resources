---
description: Create and manage Artifacts namespaces, repos, files, forks, and repo tokens from the Cloudflare dashboard.
title: Manage Artifacts from the Cloudflare dashboard
image: https://developers.cloudflare.com/changelog/post/2026-06-17-dashboard-management/og.png?v=a455a3d00de6090b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 17, 2026

## Manage Artifacts from the Cloudflare dashboard

[Artifacts](https://developers.cloudflare.com/artifacts/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-17-dashboard-management/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now configure [Artifacts](https://developers.cloudflare.com/artifacts/concepts/how-artifacts-works/) namespaces, repos, and tokens directly from the Cloudflare dashboard.

Artifacts is Git-compatible storage that lets you store repos on Cloudflare and interact with them using standard Git workflows.

You can view and create [namespaces](https://developers.cloudflare.com/artifacts/concepts/namespaces/#use-namespaces-as-containers), which are top-level containers for repos:

![Artifacts namespaces dashboard showing namespace search and create namespace controls](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1804,height=598,format=webp/_astro/dashboard-namespaces.0BJelWZh.png)

You can view, create, fork, and search repos within a namespace:

![Artifacts repositories dashboard showing repo source, access, and created columns](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1874,height=592,format=webp/_astro/dashboard-repositories.M9P9JUL_.png)

You can open a repo to view its files and copy its Git remote URL.

![Artifacts repository overview showing files, commits, token management, and quick actions](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2194,height=806,format=webp/_astro/dashboard-repo-overview.CSHxrCW2.png)

You can also provision tokens directly from the dashboard to scope Git access to a single repo, with read tokens for clone, fetch, and pull workflows, or write tokens when a client needs to push changes.

To get started, go to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) and select **Storage & databases** > **Artifacts**.

If you are enrolled in the Artifacts beta, you can use the dashboard to set up Artifacts. If you would like to join the beta, complete the [request form ↗︎](https://forms.gle/DwBoPRa3CWQ8ajFp7).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-17-dashboard-management/#page","headline":"Manage Artifacts from the Cloudflare dashboard","description":"Create and manage Artifacts namespaces, repos, files, forks, and repo tokens from the Cloudflare dashboard.","url":"https://developers.cloudflare.com/changelog/post/2026-06-17-dashboard-management/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-17-dashboard-management/og.png?v=a455a3d00de6090b","dateModified":"2026-06-17","datePublished":"2026-06-17","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
