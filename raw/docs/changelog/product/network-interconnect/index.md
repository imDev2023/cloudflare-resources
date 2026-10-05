---
title: Network Interconnect Changelog
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

Mar 24, 2026

[<h2>Interconnects moved to Connectors</h2>](https://developers.cloudflare.com/changelog/post/2026-03-24-interconnects-navigation-update/)

[Network Interconnect](https://developers.cloudflare.com/network-interconnect/)

The top-level **Interconnects** page in the Cloudflare dashboard has been removed. Interconnects are now located under **Connectors** > **Interconnects**.

Your existing configurations and functionality remain the same.

Jun 20, 2025

[<h2>CNI maintenance alerts</h2>](https://developers.cloudflare.com/changelog/post/2025-06-20-cni-maintenance-alerts/)

[Network Interconnect](https://developers.cloudflare.com/network-interconnect/)

Customers using Cloudflare Network Interconnect with the v1 dataplane can now subscribe to maintenance alert emails. These alerts notify you of planned maintenance windows that may affect your CNI circuits.

For more information, refer to [Monitoring and alerts](https://developers.cloudflare.com/network-interconnect/monitoring-and-alerts/).

Dec 17, 2024

[<h2>Establish BGP peering over Direct CNI circuits</h2>](https://developers.cloudflare.com/changelog/post/2024-12-17-bgp-support-cni/)

[Magic Transit](https://developers.cloudflare.com/magic-transit/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) [Network Interconnect](https://developers.cloudflare.com/network-interconnect/)

Magic WAN and Magic Transit customers can use the Cloudflare dashboard to configure and manage BGP peering between their networks and their Magic routing table when using a Direct CNI on-ramp.

Using BGP peering allows customers to:

- Automate the process of adding or removing networks and subnets.
- Take advantage of failure detection and session recovery features.

With this functionality, customers can:

- Establish an eBGP session between their devices and the Magic WAN / Magic Transit service when connected via CNI.
- Secure the session by MD5 authentication to prevent misconfigurations.
- Exchange routes dynamically between their devices and their Magic routing table.

Refer to [Magic WAN BGP peering](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-routes/#configure-bgp-routes) or [Magic Transit BGP peering](https://developers.cloudflare.com/magic-transit/how-to/configure-routes/#configure-bgp-routes) to learn more about this feature and how to set it up.

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

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product/network-interconnect/#page","headline":"Network Interconnect Changelog","url":"https://developers.cloudflare.com/changelog/product/network-interconnect/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
