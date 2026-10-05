---
title: Changelogs
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

Sep 23, 2024

[<h2>AI Crawl Control</h2>](https://developers.cloudflare.com/changelog/post/2024-09-23-ai-audit-launch/)

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

Every site on Cloudflare now has access to [**AI Audit**](https://developers.cloudflare.com/ai-crawl-control/), which summarizes the crawling behavior of popular and known AI services.

You can use this data to:

- Understand how and how often crawlers access your site (and which content is the most popular).
- Block specific AI bots accessing your site.
- Use Cloudflare to enforce your `robots.txt` policy via an automatic WAF rule.

![View AI bot activity with AI Audit](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1494,height=746,format=webp/_astro/ai-crawl-control-overview.Dr_yGKOC.png)

To get started, explore [AI audit](https://developers.cloudflare.com/ai-crawl-control/).

Sep 5, 2024

[<h2>One-click Cache Rules templates now available</h2>](https://developers.cloudflare.com/changelog/post/2024-09-05-cache-rules-templates/)

[Cache / CDN](https://developers.cloudflare.com/cache/)

You can now create optimized cache rules instantly with **one-click templates**, eliminating the complexity of manual rule configuration.

#### How it works

1. Navigate to **Rules** > **Templates** in your Cloudflare dashboard.
2. Select a template for your use case.
3. Click to apply the template with sensible defaults.
4. Customize as needed for your specific requirements.

#### Available cache templates

- **Cache everything**: Adjust the cache level for all requests.
- **Bypass cache for everything**: Bypass cache for all requests.
- **Cache default file extensions**: Replicate Page Rules caching behavior by making only default extensions eligible for cache.
- **Bypass cache on cookie**: Bypass cache for requests containing specific cookies.
- **Set edge cache time**: Cache responses with status code between 200 and 599 on the Cloudflare edge.
- **Set browser cache time**: Adjust how long a browser should cache a resource.

#### Get started

To get started, go to [**Rules > Templates** ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/caching/cache-rules) in the dashboard. For more information, refer to the [Cache Rules documentation](https://developers.cloudflare.com/cache/how-to/cache-rules/).

Sep 5, 2024

[<h2>New Rules Templates for One-Click Rule Creation</h2>](https://developers.cloudflare.com/changelog/post/2024-09-05-rules-templates/)

[Rules](https://developers.cloudflare.com/rules/)

Now, you can create **common rule configurations** in just **one click** using Rules Templates.

![Rules Templates](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=800,height=424,format=webp/_astro/rules-templates.DAV0GOXF.gif)

What you can do:

- **Pick a pre-built rule** – Choose from a library of templates.
- **One-click setup** – Deploy best practices instantly.
- **Customize as needed** – Adjust templates to fit your setup.

Template cards are now also available directly in the rule builder for each product.

Need more ideas? Check out the [Examples gallery](https://developers.cloudflare.com/rules/examples/) in our documentation.

Jul 19, 2024

[<h2>Regionalized Generic Tiered Cache for higher hit ratios</h2>](https://developers.cloudflare.com/changelog/post/2024-07-19-regionalized-generic-tiered-cache/)

[Cache / CDN](https://developers.cloudflare.com/cache/)

You can now achieve higher cache hit ratios with [Generic Global Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/#generic-global-tiered-cache). Regional content hashing routes content consistently to the same upper-tier data centers, eliminating redundant caching and reducing origin load.

#### How it works

Regional content hashing groups data centers by region and uses consistent hashing to route content to designated upper-tier caches:

- Same content always routes to the same upper-tier data center within a region.
- Eliminates redundant copies across multiple upper-tier caches.
- Increases the likelihood of cache HITs for the same content.

#### Example

A popular image requested from multiple edge locations in a region:

- **Before**: Cached at 3-4 different upper-tier data centers
- **After**: Cached at 1 designated upper-tier data center
- **Result**: 3-4x fewer cache MISSes, reducing origin load and improving performance

#### Get started

To get started, enable [Generic Global Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/#generic-global-tiered-cache) on your zone.

Jun 17, 2024

[<h2>Exchange user risk scores with Okta</h2>](https://developers.cloudflare.com/changelog/post/2024-06-17-okta-risk-exchange/)

[Risk Score](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/)

Beyond the controls in [Zero Trust](https://developers.cloudflare.com/cloudflare-one/), you can now [exchange user risk scores](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/#send-risk-score-to-okta) with Okta to inform SSO-level policies.

First, configure Cloudflare One to send user risk scores to Okta.

1. Set up the [Okta SSO integration](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/okta/).
2. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Integrations** > **Identity providers**.
3. In **Your identity providers**, locate your Okta integration and select **Edit**.
4. Turn on **Send risk score to Okta**.
5. Select **Save**.
6. Upon saving, Cloudflare One will display the well-known URL for your organization. Copy the value.

Next, configure Okta to receive your risk scores.

1. On your Okta admin dashboard, go to **Security** > **Device Integrations**.
2. Go to **Receive shared signals**, then select **Create stream**.
3. Name your integration. In **Set up integration with**, choose *Well-known URL*.
4. In **Well-known URL**, enter the well-known URL value provided by Cloudflare One.
5. Select **Create**.

Jun 16, 2024

[<h2>Explore product updates for Cloudflare One</h2>](https://developers.cloudflare.com/changelog/post/2024-06-16-cloudflare-one/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) [Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) [CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) [Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/) [Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/) [Email security](https://developers.cloudflare.com/cloudflare-one/email-security/) [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Multi-Cloud Networking](https://developers.cloudflare.com/multi-cloud-networking/) [Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/) [Network Flow](https://developers.cloudflare.com/network-flow/) [Magic Transit](https://developers.cloudflare.com/magic-transit/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) [Network Interconnect](https://developers.cloudflare.com/network-interconnect/) [Risk Score](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/) [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Welcome to your new home for product updates on [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/).

Our [new changelog](https://developers.cloudflare.com/changelog/) lets you read about changes in much more depth, offering in-depth examples, images, code samples, and even gifs.

If you are looking for older product updates, refer to the following locations.

<details>

<summary>

Older product updates

</summary>

- <a href="https://developers.cloudflare.com/cloudflare-one/changelog/access/">Access</a>
- <a href="https://developers.cloudflare.com/cloudflare-one/changelog/browser-isolation/">Browser Isolation</a>
- <a href="https://developers.cloudflare.com/cloudflare-one/changelog/casb/">CASB</a>
- <a href="https://developers.cloudflare.com/cloudflare-one/changelog/tunnel/">Cloudflare Tunnel</a>
- <a href="https://developers.cloudflare.com/cloudflare-one/changelog/dlp/">Data Loss Prevention</a>
- <a href="https://developers.cloudflare.com/cloudflare-one/changelog/dex/">Digital Experience Monitoring</a>
- <a href="https://developers.cloudflare.com/cloudflare-one/changelog/email-security/">Email security</a>
- <a href="https://developers.cloudflare.com/cloudflare-one/changelog/gateway/">Gateway</a>
- <a href="https://developers.cloudflare.com/multi-cloud-networking/changelog/">Multi-Cloud Networking</a>
- <a href="https://developers.cloudflare.com/cloudflare-network-firewall/changelog/">Cloudflare Network Firewall</a>
- <a href="https://developers.cloudflare.com/network-flow/changelog/">Magic Network Monitoring</a>
- <a href="https://developers.cloudflare.com/magic-transit/changelog/">Magic Transit</a>
- <a href="https://developers.cloudflare.com/cloudflare-wan/changelog/">Magic WAN</a>
- <a href="https://developers.cloudflare.com/network-interconnect/changelog/">Network Interconnect</a>
- <a href="https://developers.cloudflare.com/cloudflare-one/changelog/risk-score/">Risk score</a>
- <a href="https://developers.cloudflare.com/changelog/cloudflare-one-client/">Cloudflare One Client</a>

</details>

Feb 26, 2024

[<h2>Easily Exclude EU Visitors from RUM</h2>](https://developers.cloudflare.com/changelog/post/2025-02-25-rum-exclude-eu/)

[Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/)

You can now easily enable Real User Monitoring (RUM) monitoring for your hostnames, while safely dropping requests from visitors in the European Union to comply with GDPR and CCPA.

![RUM Enablement UI](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1101,height=1061,format=webp/_astro/2025-02-26-rum-eu.X0ZtbXWA.png)

Our Web Analytics product has always been centered on giving you insights into your users' experience that you need to provide the best quality experience, without sacrificing user privacy in the process.

To help with that aim, you can now selectively enable RUM monitoring for your hostname and exclude EU visitor data in a single click. If you opt for this option, we will drop all metrics collected by our EU data centers automatically.

You can learn more about what metrics are reported by Web Analytics and how it is collected [in the Web Analytics documentation](https://developers.cloudflare.com/web-analytics/data-metrics/). You can enable Web Analytics on any hostname by going to the [Web Analytics ↗︎](https://dash.cloudflare.com/?to=/:account/web-analytics/sites) section of the dashboard, selecting "Manage Site" for the hostname you want to monitor, and choosing the appropriate enablement option.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/53/#page","headline":"Changelogs","url":"https://developers.cloudflare.com/changelog/53/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
