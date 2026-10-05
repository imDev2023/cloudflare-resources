---
title: Core platform Changelog
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

Jan 29, 2025

[<h2>New Snippets Code Editor</h2>](https://developers.cloudflare.com/changelog/post/2025-01-29-snippets-code-editor/)

[Rules](https://developers.cloudflare.com/rules/)

The new [Snippets](https://developers.cloudflare.com/rules/snippets/) code editor lets you edit Snippet code and rule in one place, making it easier to test and deploy changes without switching between pages.

![New Snippets code editor](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3446,height=1690,format=webp/_astro/snippets-new-editor.CaoIu2_-.png)

What’s new:

- **Single-page editing for code and rule** – No need to jump between screens.
- **Auto-complete & syntax highlighting** – Get suggestions and avoid mistakes.
- **Code formatting & refactoring** – Write cleaner, more readable code.

Try it now in [Rules > Snippets ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/rules/snippets).

Jan 9, 2025

[<h2>New Rules Overview Interface</h2>](https://developers.cloudflare.com/changelog/post/2025-01-09-rules-overview/)

[Rules](https://developers.cloudflare.com/rules/)

**Rules Overview** gives you a single page to manage all your [Cloudflare Rules](https://developers.cloudflare.com/rules/).

What you can do:

- **See all your rules in one place** – No more clicking around.
- **Find rules faster** – Search by name.
- **Understand execution order** – See how rules run in sequence.
- **Debug easily** – Use [Trace](https://developers.cloudflare.com/rules/trace-request/) without switching tabs.

Check it out in [Rules > Overview ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/rules/overview).

Dec 19, 2024

[<h2>Troubleshoot tunnels with diagnostic logs</h2>](https://developers.cloudflare.com/changelog/post/2024-12-19-diagnostic-logs/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

The latest `cloudflared` build [2024.12.2 ↗︎](https://github.com/cloudflare/cloudflared/releases/tag/2024.12.2) introduces the ability to collect all the diagnostic logs needed to troubleshoot a `cloudflared` instance.

A diagnostic report collects data from a single instance of `cloudflared` running on the local machine and outputs it to a `cloudflared-diag` file.

For more information, refer to [Diagnostic logs](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/diag-logs/).

Dec 11, 2024

[<h2>Terraform Support for Snippets</h2>](https://developers.cloudflare.com/changelog/post/2024-12-11-terraform-snippets/)

[Rules](https://developers.cloudflare.com/rules/)

Now, you can manage [Cloudflare Snippets](https://developers.cloudflare.com/rules/snippets/) with [Terraform](https://developers.cloudflare.com/terraform/). Use infrastructure-as-code to deploy and update Snippet code and rules without manual changes in the dashboard.

Example Terraform configuration:

```tf
resource "cloudflare_snippet" "my_snippet" {
	zone_id  = "<ZONE_ID>"
	name = "my_test_snippet_1"
	main_module = "file1.js"
	files {
		name = "file1.js"
		content = file("file1.js")
	}
}

resource "cloudflare_snippet_rules" "cookie_snippet_rule" {
	zone_id  = "<ZONE_ID>"
	rules {
		enabled = true
		expression = "http.cookie eq \"a=b\""
		description = "Trigger snippet on specific cookie"
		snippet_name = "my_test_snippet_1"
	}
	depends_on = [cloudflare_snippet.my_snippet]
}
```

Learn more in the [Configure Snippets using Terraform](https://developers.cloudflare.com/rules/snippets/create-terraform/) documentation.

Nov 22, 2024

[<h2>Cloud Connector Now Supports R2</h2>](https://developers.cloudflare.com/changelog/post/2024-11-22-cloud-connector-r2/)

[Rules](https://developers.cloudflare.com/rules/)

Now, you can use [Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/) to route traffic to your [R2 buckets](https://developers.cloudflare.com/r2/) based on URLs, headers, geolocation, and more.

Example setup:

```bash
curl --request PUT \
"https://api.cloudflare.com/client/v4/zones/{zone_id}/cloud_connector/rules" \
--header "Authorization: Bearer <API_TOKEN>" \
--header "Content-Type: application/json" \
--data '[
  {
    "expression": "http.request.uri.path wildcard \"/images/*\"",
    "provider": "cloudflare_r2",
    "description": "Connect to R2 bucket containing images",
    "parameters": {
      "host": "mybucketcustomdomain.example.com"
    }
  }
]'
```

Get started using [Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/) documentation.

Oct 23, 2024

[<h2>Simplified UI for URL Rewrites</h2>](https://developers.cloudflare.com/changelog/post/2024-10-23-url-rewrites-wildcard/)

[Rules](https://developers.cloudflare.com/rules/)

It’s now easy to create **wildcard-based [URL Rewrites](https://developers.cloudflare.com/rules/transform/url-rewrite/)**. No need for complex functions—just define your patterns and go.

![Rules Overview Interface](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1158,height=1305,format=webp/_astro/create-url-rewrite-rule.DIgpB8IB.png)

What’s improved:

- **Full wildcard support** – Create rewrite patterns using intuitive interface.
- **Simplified rule creation** – No need for complex functions.

Try it via [creating a Rewrite URL rule in the dashboard](https://developers.cloudflare.com/rules/transform/url-rewrite/create-dashboard/#wildcard-pattern-parameters).

Oct 8, 2024

[<h2>New fields added to Gateway-related datasets in Cloudflare Logs</h2>](https://developers.cloudflare.com/changelog/post/2024-10-08-new-gateway-fields/)

[Logs](https://developers.cloudflare.com/logs/)

Cloudflare has introduced new fields to two Gateway-related datasets in Cloudflare Logs:

- **Gateway HTTP**: `ApplicationIDs`, `ApplicationNames`, `CategoryIDs`, `CategoryNames`, `DestinationIPContinentCode`, `DestinationIPCountryCode`, `ProxyEndpoint`, `SourceIPContinentCode`, `SourceIPCountryCode`, `VirtualNetworkID`, and `VirtualNetworkName`.
- **Gateway Network**: `ApplicationIDs`, `ApplicationNames`, `DestinationIPContinentCode`, `DestinationIPCountryCode`, `ProxyEndpoint`, `SourceIPContinentCode`, `SourceIPCountryCode`, `TransportProtocol`, `VirtualNetworkID`, and `VirtualNetworkName`.

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

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product-group/core-platform/9/#page","headline":"Core platform Changelog","url":"https://developers.cloudflare.com/changelog/product-group/core-platform/9/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
