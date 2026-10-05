---
description: Distribute traffic across servers with load balancing.
title: Setup
image: https://developers.cloudflare.com/learning-paths/load-balancing/setup/og.png?v=b481811e79c7c2d5
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/learning-paths/llms.txt  
> Use this file to discover all available pages before exploring further.

# Setup

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/learning-paths/load-balancing/setup/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Create a load balancer that monitors endpoint health and intelligently routes traffic.

## Objectives

By the end of this module, you will be able to:

- Configure a monitor and health checks.
- Create a pool.
- Create a load balancer.
- Analyze traffic patterns.

## Prerequisites

- Multiple endpoints, either physical or cloud-based.
- Access to Load Balancing, available as an [add-on](https://developers.cloudflare.com/load-balancing/get-started/enable-load-balancing/) for any type of account.
- Two hostnames, one for test traffic and the other for production traffic.
