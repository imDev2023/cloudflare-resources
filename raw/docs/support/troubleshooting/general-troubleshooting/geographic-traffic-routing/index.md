---
description: Understand anycast routing to non-local data centers.
title: Cloudflare traffic not being sent to the geographically closest data center
image: https://developers.cloudflare.com/support/troubleshooting/general-troubleshooting/geographic-traffic-routing/og.png?v=f178434cc78d153f
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Cloudflare traffic not being sent to the geographically closest data center

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/general-troubleshooting/geographic-traffic-routing/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Due to the way routing on [Cloudflare's Anycast network ↗︎](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/) works, requests may be sent to data center locations that are not necessarily the closest geographically. We are continuously adding capacity to our global network and enhancing our automated traffic engineering systems to intelligently manage congestion and other network events. While we always strive to provide the best possible performance by serving traffic from the closest location, our top priority is reliability.

In instances where performance and reliability are in conflict, our systems are designed to prioritize a stable connection over a local one.
