---
title: Organizations Changelog
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

Jul 17, 2026

[<h2>Distributor, MSSP, and Agency partners can manage Organization members directly</h2>](https://developers.cloudflare.com/changelog/post/2026-07-17-distributor-mssp-self-serve-members/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Organizations](https://developers.cloudflare.com/fundamentals/organizations/)

Distributor, MSSP, and Agency partners on Cloudflare [Organizations](https://developers.cloudflare.com/fundamentals/organizations/) can now add and manage Organization Members directly from the Cloudflare dashboard, without help from Cloudflare.

Previously, adding a member to a Distributor, MSSP, or Agency Organization was a manual, Cloudflare-assisted process that required a request to Cloudflare and enrollment in a closed beta, and the dashboard **Add member** flow was blocked for these Organizations.

Now, Organization admins can add members themselves from **Organization** > **Members** > **Add member**, with no beta enrollment required.

New members receive access to the Organization's accounts through the same implicit-access model already used for enterprise Organizations. The **Accounts** list and the account switcher classify Distributor, MSSP, and Agency Organizations consistently with enterprise Organizations, so their accounts are labeled and grouped correctly in the dashboard.

Agency partners also gain access to the Organizations dashboard, while retaining access to their existing Tenant management dashboard.

Distributor, MSSP, and Agency Organizations are currently in beta.

For more information, refer to [Manage Organization members](https://developers.cloudflare.com/fundamentals/organizations/manage-members/).

Apr 6, 2026

[<h2>Organizations is now in public beta for enterprises</h2>](https://developers.cloudflare.com/changelog/post/2026-04-06-organizations-public-beta/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Organizations](https://developers.cloudflare.com/fundamentals/organizations/)

We're announcing the public beta of **Organizations** for enterprise customers, a new top-level Cloudflare container that lets Cloudflare customers manage multiple accounts, members, analytics, and shared policies from one centralized location.

**What's New**

**Organizations \[BETA]**: [Organizations](https://developers.cloudflare.com/fundamentals/organizations/) are a new top-level container for centrally managing multiple accounts. Each Organization supports up to 500 accounts and 5000 zones, giving larger teams a single place to administer resources at scale.

**Self-serve onboarding**: Enterprise customers can [create an Organization](https://developers.cloudflare.com/fundamentals/organizations/setup/) in the dashboard and assign accounts where they are already Super Administrators.

**Centralized Account Management**: At launch, every Organization member has the Organization Super Admin role. Organization Super Admins can invite other users and manage any child account under the Organization implicitly. **Shared policies**: Share [WAF](https://developers.cloudflare.com/waf/custom-rules/) or [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/tiered-policies/organizations/) policies across multiple accounts within your Organization to simplify centralized policy management. **Implicit access**: Members of an Organization automatically receive Super Administrator permissions across child accounts, removing the need for explicit membership on each account. Additional Org-level roles will be available over the course of the year.

**Unified analytics**: View, filter, and download aggregate HTTP analytics across all Organization child accounts from a single dashboard for centralized visibility into traffic patterns and security events.

**Terraform provider support**: Manage Organizations with infrastructure as code from day one. Provision organizations, assign accounts, and configure settings programmatically with the [Cloudflare Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/organization).

**Shared policies**: Share [WAF](https://developers.cloudflare.com/waf/custom-rules/) or [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) policies across multiple accounts within your Organization to simplify centralized policy management.

Note

Organizations is in Public Beta. You must have an Enterprise account to create an organization, but once created, you can add accounts of any plan type where you are a Super Administrator.

For more info:

- [Get started with Organizations](https://developers.cloudflare.com/fundamentals/organizations/)
- [Set up your Organization](https://developers.cloudflare.com/fundamentals/organizations/setup/)
- [Review limitations](https://developers.cloudflare.com/fundamentals/organizations/limitations/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product/organizations/#page","headline":"Organizations Changelog","url":"https://developers.cloudflare.com/changelog/product/organizations/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
