---
title: Browser Isolation Changelog
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

Sep 30, 2026

[<h2>Role-based access control for Browser Isolation policies</h2>](https://developers.cloudflare.com/changelog/post/2026-09-30-browser-isolation-rbac/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

[Isolation policies](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/) support role-based access control (RBAC). Because isolation policies are Gateway HTTP policies with the *Isolate* action, Gateway's account-level and resource-scoped roles apply to them directly.

Use the `Zero Trust HTTP Policies Admin` account-level role to grant access to all HTTP policies in the account. You can also assign a [resource-scoped role](https://developers.cloudflare.com/cloudflare-one/traffic-policies/granular-permissions/) to let a team member manage a specific isolation policy without exposing other Gateway resources.

[Policy settings](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/#policy-settings) such as copy/paste, file download/upload, keyboard, and printing are part of the policy object and follow the same permissions.

For setup instructions, refer to [Granular permissions for Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/granular-permissions/).

Sep 9, 2026

[<h2>Improved iOS tap-to-type experience for Browser Isolation</h2>](https://developers.cloudflare.com/changelog/post/2026-09-09-ios-tap-to-type/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) has improved the tap-to-type experience for users on iOS devices.

Previously, Browser Isolation displayed a full-screen overlay with the message `tap to type` when users focused a text field. The prompt now appears inline over the focused text field, reducing disruption when users enter text in isolated sessions.

If the focused text field is too small to display the full prompt, Browser Isolation displays a keyboard icon in the center of the text field instead.

![Inline tap-to-type prompt over a focused text field in Browser Isolation](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1320,height=605,format=webp/_astro/tap-to-type.UmUg_KNp.jpg)

iOS users should tap twice to begin entering text. This update applies automatically to Browser Isolation sessions on iOS.

For more information on why this interaction is required, refer to [iOS limitations](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/known-limitations/#ios).

Jul 7, 2026

[<h2>Browser Isolation support for authorization proxy endpoints</h2>](https://developers.cloudflare.com/changelog/post/2026-07-07-authorization-proxy-endpoint-support/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) now supports Gateway [authorization proxy endpoints](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint). You can apply [HTTP Isolate policies](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/) to traffic routed through authorization proxy endpoints, the same way you can for traffic from the Cloudflare One Client.

Previously, only [source IP proxy endpoints](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#source-ip-endpoint) supported Browser Isolation, and only with non-identity policies. Because authorization proxy endpoints authenticate users through an identity provider, you can now apply identity-based Isolate policies to PAC file-proxied traffic without requiring the Cloudflare One Client.

To get started, [create an authorization proxy endpoint](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint) and [build an Isolate policy](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/).

Apr 10, 2026

[<h2>Canvas Remoting optimizes performance for productivity applications</h2>](https://developers.cloudflare.com/changelog/post/2026-04-10-canvas-remoting-performance/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)

Remote Browser Isolation now supports **Canvas Remoting**, improving performance for HTML5 Canvas applications by sending vector draw commands instead of rasterized bitmaps.

#### Key improvements

- **10x bandwidth reduction:** Microsoft Word and other Office apps use 90% less bandwidth
- **Smooth performance:** Google Sheets maintains consistent 30fps rendering
- **Responsive terminals:** Web-based development environments and AI notebooks work in real-time
- **Zero configuration:** Enabled by default for all Browser Isolation customers

#### How it works

Instead of sending rasterized bitmaps for every Canvas update, Browser Isolation now:

1. Captures Canvas draw commands at the source
2. Converts them to lightweight vector instructions
3. Renders Canvas content on the client

This reduces bandwidth from hundreds of kilobytes per second to tens of kilobytes per second.

#### Managing Canvas Remoting

To temporarily disable for troubleshooting:

- Right-click the isolated webpage background
- Select **Disable Canvas Remoting**
- Re-enable the same way by selecting **Enable Canvas Remoting**

#### Limitations

Currently supports 2D Canvas contexts only. WebGL and 3D graphics applications continue using bitmap rendering. For more information, refer to [Canvas Remoting](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/canvas-remoting/).

May 13, 2025

[<h2>SAML HTTP-POST bindings support for RBI</h2>](https://developers.cloudflare.com/changelog/post/2025-05-13-rbi-saml-post-support/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)

Remote Browser Isolation (RBI) now supports SAML HTTP-POST bindings, enabling seamless authentication for SSO-enabled applications that rely on POST-based SAML responses from Identity Providers (IdPs) within a Remote Browser Isolation session. This update resolves a previous limitation that caused `405` errors during login and improves compatibility with multi-factor authentication (MFA) flows.

With expanded support for major IdPs like Okta and Azure AD, this enhancement delivers a more consistent and user-friendly experience across authentication workflows. Learn how to [set up Remote Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/).

May 1, 2025

[<h2>Browser Isolation Overview page for Zero Trust</h2>](https://developers.cloudflare.com/changelog/post/2025-05-01-browser-isolation-overview-page/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)

A new **Browser Isolation Overview** page is now available in the Cloudflare Zero Trust dashboard. This centralized view simplifies the management of [Remote Browser Isolation (RBI)](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) deployments, providing:

- **Streamlined Onboarding:** Easily set up and manage isolation policies from one location.
- **Quick Testing:** Validate [clientless web application isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/) with ease.
- **Simplified Configuration:** Configure [isolated access applications](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/isolate-application/) and policies efficiently.
- **Centralized Monitoring:** Track aggregate usage and blocked actions.

This update consolidates previously disparate settings, accelerating deployment, improving visibility into isolation activity, and making it easier to ensure your protections are working effectively.

![Browser Isolation Overview](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1717,height=1286,format=webp/_astro/browser-isolation-overview.Ljd5ax_O.png)

To access the new overview, log in to your Cloudflare [Zero Trust dashboard ↗︎](https://one.dash.cloudflare.com/) and find Browser Isolation in the side navigation bar.

Mar 4, 2025

[<h2>Gain visibility into user actions in Zero Trust Browser Isolation sessions</h2>](https://developers.cloudflare.com/changelog/post/2025-03-03-user-action-logging/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)

We're excited to announce that new logging capabilities for [Remote Browser Isolation (RBI)](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) through [Logpush](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/) are available in Beta starting today!

With these enhanced logs, administrators can gain visibility into end user behavior in the remote browser and track blocked data extraction attempts, along with the websites that triggered them, in an isolated session.

```json
{
	"AccountID": "$ACCOUNT_ID",
	"Decision": "block",
	"DomainName": "www.example.com",
	"Timestamp": "2025-02-27T23:15:06Z",
	"Type": "copy",
	"UserID": "$USER_ID"
}
```

User Actions available:

- **Copy & Paste**
- **Downloads & Uploads**
- **Printing**

Learn more about how to get started with Logpush in our [documentation](https://developers.cloudflare.com/logs/logpush/).

Nov 21, 2024

[<h2>Improved non-English keyboard support</h2>](https://developers.cloudflare.com/changelog/post/2024-11-21-non-english-keyboard/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)

You can now type in languages that use diacritics (like á or ç) and character-based scripts (such as Chinese, Japanese, and Korean) directly within the remote browser. The isolated browser now properly recognizes non-English keyboard input, eliminating the need to copy and paste content from a local browser or device.

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
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product/browser-isolation/#page","headline":"Browser Isolation Changelog","url":"https://developers.cloudflare.com/changelog/product/browser-isolation/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
