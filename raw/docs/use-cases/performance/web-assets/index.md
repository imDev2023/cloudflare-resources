---
description: Speed up page rendering by minifying HTML, CSS, and JavaScript and loading third-party scripts server-side.
title: Optimize web assets
image: https://developers.cloudflare.com/use-cases/performance/web-assets/og.png?v=0d8ec5f170d00dd9
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/use-cases/llms.txt  
> Use this file to discover all available pages before exploring further.

# Optimize web assets

Last updated Apr 24, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/use-cases/performance/web-assets/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Unoptimized HTML, CSS, and JavaScript increase page weight and slow down rendering. Cloudflare Speed automatically minifies and compresses these assets, while Zaraz loads third-party analytics and marketing tags server-side to avoid blocking page rendering.

## Solutions

### Speed

Improve the performance of your website or web application. [Learn more about Speed](https://developers.cloudflare.com/speed/).

- **Minification** - Remove whitespace and unnecessary characters from HTML, CSS, and JavaScript automatically
- **Compression** - Brotli and Gzip compression applied to all text-based assets at the edge
- **Core Web Vitals** - Improve Largest Contentful Paint (LCP), Interaction to Next Paint (INP), and Cumulative Layout Shift (CLS) scores by deferring non-critical scripts and optimizing asset delivery

### Zaraz

Server-side loading of third-party tools to improve performance and privacy. [Learn more about Zaraz](https://developers.cloudflare.com/zaraz/).

- **Third-party optimization** - Load analytics, marketing tags, and other third-party tools through Cloudflare without blocking page rendering

## Get started

1. [Enable Speed optimizations](https://developers.cloudflare.com/speed/optimization/)
2. [Zaraz get started](https://developers.cloudflare.com/zaraz/get-started/)
