---
title: Cloudflare CLI Changelog
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

Sep 28, 2026

[<h2>Cloudflare CLI is now in beta</h2>](https://developers.cloudflare.com/changelog/post/2026-09-28-cloudflare-cli-beta/)

[Workers](https://developers.cloudflare.com/workers/) [Cloudflare CLI](https://developers.cloudflare.com/cf/)

The [Cloudflare CLI](https://developers.cloudflare.com/cf/), `cf`, is now in beta. `cf` is one command-line interface for the public Cloudflare API and for Workers projects. Use it to manage zones, DNS, storage, and security settings, and to create, develop, and deploy Workers, without switching between tools.

Install `cf` globally, then sign in:

npmyarnpnpmbun

```
npm install --global cf
```

```
yarn global add cf
```

```
pnpm add --global cf
```

```
bun add --global cf
```

```sh
cf auth login
```

With `cf`, you can:

- **Manage resources across Cloudflare.** More than 2,900 commands cover the public Cloudflare API, and most print their results as JSON.
- **Create and deploy Workers.** `cf init` creates a project that uses [`cloudflare.config.ts`](https://developers.cloudflare.com/cf/projects/cloudflare-config/), a typed configuration file. `cf dev`, `cf build`, and `cf deploy` develop, build, and deploy it.
- **Move from Wrangler.** `cf migrate` converts a Wrangler configuration file to `cloudflare.config.ts`. You can also run `cf` resource commands in an existing Wrangler project without migrating it.
- **Work with coding agents.** `cf cli search` finds the command for a task from a plain-language description, so an agent can find and run commands without prior knowledge of `cf`.

`cf` is in beta. Commands, configuration, and Build Output can change before the stable release.

To get started, refer to [Install and sign in](https://developers.cloudflare.com/cf/get-started/). To move an existing project, refer to [Migrate a Wrangler project](https://developers.cloudflare.com/cf/wrangler/migrate/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product/cf/#page","headline":"Cloudflare CLI Changelog","url":"https://developers.cloudflare.com/changelog/product/cf/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
