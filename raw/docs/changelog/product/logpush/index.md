---
title: Logpush Changelog
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

[<h2>Logpush is now available on all plans with usage-based pricing</h2>](https://developers.cloudflare.com/changelog/post/2026-09-30-logpush-usage-based-pricing/)

[Logpush](https://developers.cloudflare.com/logs/logpush/) [Logs](https://developers.cloudflare.com/logs/)

Cloudflare Logpush is now available on Free, Pro, Business, and Enterprise plans with usage-based pricing. Free, Pro, and Business customers can enable Logpush through self-service. Enterprise customers continue to work with their account team. Logpush Transformers are also now generally available.

Each account receives included monthly usage before charges apply:

- **Internal exports**: 25 GB per month, then $0.03 per additional GB.
- **External exports**: 25 GB per month, then $0.10 per additional GB.
- **Transformations**: 1 GB per month, then $0.04 per additional GB.

R2 and Pipelines use the internal destination rate. All other destinations use the external destination rate.

Existing Enterprise contracts retain their current Logpush pricing through renewal. Workers Logpush for Workers Trace Events retains request-based pricing, and OpenTelemetry destinations retain event-based Workers Observability pricing.

For complete rates, measurement details, and billing examples, refer to [Logpush pricing](https://developers.cloudflare.com/logs/logpush/pricing/).

Sep 30, 2026

[<h2>Transformers are now generally available</h2>](https://developers.cloudflare.com/changelog/post/2026-09-30-transformers-ga/)

[Logpush](https://developers.cloudflare.com/logs/logpush/) [Logs](https://developers.cloudflare.com/logs/)

Transformers are now generally available for supported Logpush datasets on Free, Pro, Business, and Enterprise plans. Use SQL to filter records, reshape fields, redact sensitive values, compute new fields, or add metadata before Logpush delivers each batch.

Create and preview Transformers in Transformer Studio or through the Cloudflare API, then attach them to eligible account-scoped or zone-scoped Logpush jobs that use NDJSON output. Cloudflare validates each query against the dataset schema before saving it.

Each account includes 1 GB of transformation input per month. Additional input costs $0.04 per GB. For setup instructions, supported SQL, limits, and examples, refer to [Transformers](https://developers.cloudflare.com/logs/logpush/transformers/). For billing details, refer to [Logpush pricing](https://developers.cloudflare.com/logs/logpush/pricing/).

Sep 18, 2026

[<h2>Filter DDoS attack traffic from Logpush jobs</h2>](https://developers.cloudflare.com/changelog/post/2026-09-18-filter-ddos-attack-traffic/)

[Logpush](https://developers.cloudflare.com/logs/logpush/) [Logs](https://developers.cloudflare.com/logs/)

Logpush jobs can now exclude identified distributed denial-of-service (DDoS) attack traffic. This option reduces attack traffic in delivered logs.

It supports the `http_requests`, `firewall_events`, and `network_analytics_logs` datasets.

In the dashboard, select **Exclude DDoS attack traffic** under **Advanced Options**. With the API, add this field to a job request:

```json
{
	"filter_attack_traffic": true
}
```

For more information, refer to [API configuration](https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/#ddos-attack-traffic).

Apr 14, 2026

[<h2>Logpush to BigQuery — Cloudflare dashboard support</h2>](https://developers.cloudflare.com/changelog/post/2026-04-14-bigquery-dashboard-support/)

[Logpush](https://developers.cloudflare.com/logs/logpush/) [Logs](https://developers.cloudflare.com/logs/)

You can now configure Logpush jobs to Google BigQuery directly from the Cloudflare dashboard, in addition to the existing API-based setup.

Previously, setting up a BigQuery Logpush destination required using the Logpush API. Now you can create and manage BigQuery Logpush jobs from the **Logpush** page in the Cloudflare dashboard by selecting **Google BigQuery** as the destination and entering your Google Cloud project ID, dataset ID, table ID, and service account credentials.

For more information, refer to [Enable Logpush to Google BigQuery](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/bigquery/).

Mar 25, 2026

[<h2>Logpush — More granular timestamps</h2>](https://developers.cloudflare.com/changelog/post/2026-03-25-logpush-granular-timestamps/)

[Logpush](https://developers.cloudflare.com/logs/logpush/) [Logs](https://developers.cloudflare.com/logs/)

Logpush now supports higher-precision timestamp formats for log output. You can configure jobs to output timestamps at millisecond or nanosecond precision. This is available in both the Logpush UI in the Cloudflare dashboard and the [Logpush API](https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/).

To use the new formats, set `timestamp_format` in your Logpush job's `output_options`:

- `rfc3339ms` — `2024-02-17T23:52:01.123Z`
- `rfc3339ns` — `2024-02-17T23:52:01.123456789Z`

Default timestamp formats apply unless explicitly set. The dashboard defaults to `rfc3339` and the API defaults to `unixnano`.

For more information, refer to the [Log output options](https://developers.cloudflare.com/logs/logpush/logpush-job/log-output-options/) documentation.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product/logpush/#page","headline":"Logpush Changelog","url":"https://developers.cloudflare.com/changelog/product/logpush/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
