---
title: Risk Score Changelog
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

Apr 8, 2026

[<h2>User risk scoring for high risk browsing activity</h2>](https://developers.cloudflare.com/changelog/post/2026-04-08-high-risk-browsing/)

[Risk Score](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/)

Cloudflare One's **User Risk Scoring** now incorporates direct signals from **Gateway DNS traffic patterns**. This update allows security teams to automatically elevate a user's risk score when they visit high-risk or malicious domains, providing a more holistic view of internal threats.

#### Why this matters

Browsing activity is a primary indicator of potential compromise. By tying Gateway DNS logs to specific users, administrators can now flag individuals interacting with:

- **Security threats**: Domains associated with malware, phishing, or command-and-control (C2) centers.
- **High-risk content**: Categories such as questionable content or violence that may violate corporate compliance.

Even if a Gateway policy is set to **Block** the traffic, the interaction is still captured as a "hit" to ensure the user's risk profile reflects the attempted activity.

#### New risk behaviors

Two new behaviors are now available in the dashboard:

- **Suspicious Security Domain Visited**: Triggers when a user visits a domain in the security threats or security risk categories.
- **High risk domain visited**: Triggers when a user visits domains categorized as questionable content, violence, or CIPA.

To learn more and get started, refer to the [User Risk Scoring documentation](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/).

Jan 15, 2026

[<h2>Support for CrowdStrike device scores in User Risk Scoring</h2>](https://developers.cloudflare.com/changelog/post/2026-1-15-crowdstrike-score/)

[Risk Score](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/)

Cloudflare One has expanded its \[User Risk Scoring] (/cloudflare-one/insights/risk-score/) capabilities by introducing two new behaviors for organizations using the \[CrowdStrike integration] (/cloudflare-one/integrations/service-providers/crowdstrike/).

Administrators can now automatically escalate the risk score of a user if their device matches specific CrowdStrike Zero Trust Assessment (ZTA) score ranges. This allows for more granular security policies that respond dynamically to the health of the endpoint.

New risk behaviors The following risk scoring behaviors are now available:

- CrowdStrike low device score: Automatically increases a user's risk score when the connected device reports a "Low" score from CrowdStrike.
- CrowdStrike medium device score: Automatically increases a user's risk score when the connected device reports a "Medium" score from CrowdStrike.

These scores are derived from \[CrowdStrike device posture attributes] (/cloudflare-one/integrations/service-providers/crowdstrike/#device-posture-attributes), including OS signals and sensor configurations.

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

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product/risk-score/#page","headline":"Risk Score Changelog","url":"https://developers.cloudflare.com/changelog/product/risk-score/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
