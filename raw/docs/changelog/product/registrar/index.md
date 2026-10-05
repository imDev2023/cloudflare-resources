---
title: Registrar Changelog
image: https://developers.cloudflare.com/og-changelog.png
---

[Skip to content](#main-content)

All products

Product groups

AI

Analytics

Application performance

Application security

Cloudflare One

Consumer services

Core platform

Developer platform

Docs collections

Media

Network security

Privacy

Storage

Products

1.1.1.1 (DNS Resolver)

Access

Agent Lee

Agents

AI Crawl Control

AI Gateway

AI Search

Analytics

API Shield

Artifacts

Audit Logs

Automatic Platform Optimization

Basin

Basin Catalog

Basin Pipelines

Basin SQL

Billing

Bots

Browser Isolation

Browser Run

Cache / CDN

CASB

Cloudflare CLI

Cloudflare for SaaS

Cloudflare Fundamentals

Cloudflare Images

Cloudflare Mesh

Cloudflare Network Firewall

Cloudflare One

Cloudflare One Appliance

Cloudflare One Client

Cloudflare Tunnel

Cloudflare Tunnel for SASE

Cloudflare WAN

Cloudflare Web Analytics

Containers

D1

Data Localization Suite

Data Loss Prevention

Digital Experience Monitoring

DNS

Durable Objects

Email security

Email Service

Flagship

Gateway

Go SDK

Hyperdrive

KV

Load Balancing

Log Explorer

Logpush

Logpush Connectors

Logs

Magic Transit

Monetization Gateway

Multi-Cloud Networking

Network Flow

Network Interconnect

Organizations

Pages

Privacy Proxy

Queues

R2

Radar

Realtime

Registrar

Resource Tagging

Risk Score

Rules

Sandboxes

SDK

Secrets Store

Security Center

Security Overview

Speed

SSL/TLS

Stream

Support

Terraform

Turnstile

Vectorize

WAF

Web Search API

Workers

Workers AI

Workers Analytics Engine

Workers for Platforms

Workers VPC

Workflows

Zaraz

No products found.

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

Apr 15, 2025

[<h2>Cloudflare Registrar API is now in beta</h2>](https://developers.cloudflare.com/changelog/post/2026-04-15-registrar-api-beta/)

[Registrar](https://developers.cloudflare.com/registrar/)

Cloudflare Registrar API is now in beta.

You can now use the Cloudflare API to:

- Search for domain names.
- Check real-time availability and pricing.
- Register supported domains programmatically.

This beta supports a subset of popular extensions available through Cloudflare Registrar. Search returns suggestions across API-supported extensions, check confirms current availability and pricing, and registration starts a workflow that can complete immediately or be polled if it takes longer.

Because the Registrar API is part of the Cloudflare API, it can also be used in [Cloudflare MCP ↗︎](https://github.com/cloudflare/mcp) and other agent-driven workflows.

If you are using Cloudflare MCP or other agent-driven workflows, prompts can be as simple as:

- `Search for domain ideas for a coffee shop based in Evergreen, Colorado.`
- `Check whether example.com is available and show me the current price.`
- `Register example.com`

For supported operations, extension availability, and workflow details, refer to:

- [Registrar API guide ↗︎](https://developers.cloudflare.com/registrar/registrar-api/)
- [Registrar API reference ↗︎](https://developers.cloudflare.com/api/resources/registrar)

Mar 27, 2025

[<h2>Register and renew .ai and .shop domains at cost</h2>](https://developers.cloudflare.com/changelog/post/2025-03-27-ai-domains-available/)

[Registrar](https://developers.cloudflare.com/registrar/)

![Example search for .ai domains](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1788,height=818,format=webp/_astro/2025-03-27-ai-domains-available.D96eztke.png)

Cloudflare Registrar now supports `.ai` and `.shop` domains. These are two of our most highly-requested top-level domains (TLDs) and are great additions to the [300+ other TLDs we support ↗︎](https://domains.cloudflare.com/tlds).

Starting today, customers can:

- Register and renew these domains *at cost* without any markups or add-on fees
- Enjoy best-in-class security and performance with native integrations with Cloudflare DNS, CDN, and SSL services like one-click DNSSEC
- Combat domain hijacking with [Custom Domain Protection ↗︎](https://www.cloudflare.com/products/registrar/custom-domain-protection/) (available on enterprise plans)

We can't wait to see what AI and e-commerce projects you deploy on Cloudflare. To get started, transfer your domains to Cloudflare or [search for new ones to register ↗︎](https://domains.cloudflare.com/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product/registrar/#page","headline":"Registrar Changelog","url":"https://developers.cloudflare.com/changelog/product/registrar/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
