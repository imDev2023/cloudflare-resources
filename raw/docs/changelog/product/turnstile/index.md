---
title: Turnstile Changelog
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

Aug 10, 2026

[<h2>Turnstile Spin is now generally available</h2>](https://developers.cloudflare.com/changelog/post/2026-08-10-turnstile-spin-ga/)

[Turnstile](https://developers.cloudflare.com/turnstile/)

[Turnstile Spin](https://developers.cloudflare.com/turnstile/spin/) is now generally available with three setup paths for creating a Turnstile widget and wiring canonical server-side siteverify into your existing backend. Start in the dashboard, with Wrangler, or from your AI coding agent. All three paths create the same widget. You can complete the integration by hand or have your agent embed the widget, wire siteverify, and validate it.

#### Server-side verification

Turnstile setup has two parts: embed the widget in your frontend, then call siteverify from your backend. Without the second part, the widget appears on the page but does not protect the request.

- The skill includes insertion snippets for Next.js (App Router and Pages Router), Astro, SvelteKit, Hugo, and vanilla HTML. For other frameworks, the agent proposes a generic pattern and asks you to confirm it first.
- The Turnstile dashboard flags existing widgets with no matching siteverify traffic. Select **Fix with Spin** to copy a prompt that guides your agent through wiring siteverify into your backend.
- Before finishing, the agent runs a real Turnstile token through your protected endpoint, checks that it passes, then replays the token to confirm the endpoint rejects it on the second try. If a check fails, the agent stops and shows you where.

#### Run Spin

You can run Spin three ways:

- In the **Turnstile dashboard**, select **Set up with Spin**, enter your domains, then select **Set up**. Spin creates the widget and returns the sitekey, secret, and a prompt for your agent.
- From the `Wrangler CLI`, run [`wrangler turnstile widget create`](https://developers.cloudflare.com/turnstile/spin/#set-up-from-the-wrangler-cli). Wrangler prints the sitekey and secret. You wire the frontend and siteverify by hand.
- From your **AI coding agent**, paste the [Spin prompt](https://developers.cloudflare.com/turnstile/spin/#set-up-from-an-ai-coding-agent) into Claude Code, Cursor, Codex, OpenCode, or GitHub Copilot Chat. Your agent fetches the skill, creates the widget, then embeds it and wires siteverify.

To get started, refer to the [Turnstile Spin documentation](https://developers.cloudflare.com/turnstile/spin/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product/turnstile/#page","headline":"Turnstile Changelog","url":"https://developers.cloudflare.com/changelog/product/turnstile/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
