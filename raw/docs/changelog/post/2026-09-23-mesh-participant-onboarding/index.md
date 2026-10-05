---
description: Deploy Mesh nodes with guided setup, find client installers and your organization name, and manage every participant from one table.
title: Add Mesh participants with guided onboarding
image: https://developers.cloudflare.com/changelog/post/2026-09-23-mesh-participant-onboarding/og.png?v=9fe69fa250e01451
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 23, 2026

## Add Mesh participants with guided onboarding

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare Mesh](https://developers.cloudflare.com/mesh/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-23-mesh-participant-onboarding/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/) now makes it faster to add and manage participants from the dashboard. Select **Add participant** from **Networking** > **Mesh** to deploy a [Mesh node](https://developers.cloudflare.com/mesh/get-started/) or find the information needed to connect a [client device](https://developers.cloudflare.com/mesh/guides/connect-client-devices/).

![Adding a Cloudflare Mesh node through the guided dashboard workflow](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1200,height=680,format=webp/_astro/guided-participant-onboarding-clicks.B0r-5ElX.gif)

The updated dashboard includes the following improvements:

- **More Mesh node deployment options** — Install a node on Linux, Kubernetes, Docker Compose, or Docker CLI. The dashboard provides requirements, commands, configuration, and links for each method. Refer to [Run Mesh in Docker / Kubernetes](https://developers.cloudflare.com/mesh/guides/run-mesh-in-containers/) for container deployment details.
- **Client device installation guidance** — Access platform-specific [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/) installers, mobile QR codes, and your Cloudflare One organization name. Use the organization name to log in from the client after installation.
- **Unified participant management** — View [Mesh nodes and enrolled client devices](https://developers.cloudflare.com/mesh/guides/connect-client-devices/#1-enroll-the-cloudflare-one-client) in one table. Search devices, filter participants by type or status, open device details, and load additional results from each participant source. If one source fails, participants from the other source remain available while you retry the request.

You must still install the Cloudflare One Client, log in to your organization, and test the connection.

For complete setup instructions, refer to [Get started with Cloudflare Mesh](https://developers.cloudflare.com/mesh/get-started/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-23-mesh-participant-onboarding/#page","headline":"Add Mesh participants with guided onboarding","description":"Deploy Mesh nodes with guided setup, find client installers and your organization name, and manage every participant from one table.","url":"https://developers.cloudflare.com/changelog/post/2026-09-23-mesh-participant-onboarding/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-23-mesh-participant-onboarding/og.png?v=9fe69fa250e01451","dateModified":"2026-09-23","datePublished":"2026-09-23","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
