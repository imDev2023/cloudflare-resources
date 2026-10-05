---
description: Terraform v5.16.0 stabilizes a number of resources and known issues
title: Terraform v5.16.0 now available
image: https://developers.cloudflare.com/changelog/post/2026-01-20-terraform-v5.16.0-provider/og.png?v=8bee22d7ce99996f
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 20, 2026

## Terraform v5.16.0 now available

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Terraform](https://developers.cloudflare.com/terraform/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-20-terraform-v5.16.0-provider/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

In January 2025, we announced the launch of the new Terraform v5 Provider. We greatly appreciate the proactive engagement and valuable feedback from the Cloudflare community following the v5 release. In response, we've established a consistent and rapid [2-3 week cadence ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774) for releasing targeted improvements, demonstrating our commitment to stability and reliability.

With the help of the community, we have a growing number of resources that we have marked as [stable ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237), with that list continuing to grow with every release. The most used [resources ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237) are on track to be stable by the end of March 2026, when we will also be releasing a new migration tool to you migrate from v4 to v5 with ease.

Thank you for continuing to raise issues. They make our provider stronger and help us build products that reflect your needs.

This release includes bug fixes, the stabilization of even more popular resources, and more.

#### Features

- **custom\_pages:** add "waf\_challenge" as new supported error page type identifier in both resource and data source schemas
- **list:** enhance CIDR validator to check for normalized CIDR notation requiring network address for IPv4 and IPv6
- **magic\_wan\_gre\_tunnel:** add automatic\_return\_routing attribute for automatic routing control
- **magic\_wan\_gre\_tunnel:** add BGP configuration support with new BGP model attribute
- **magic\_wan\_gre\_tunnel:** add bgp\_status computed attribute for BGP connection status information
- **magic\_wan\_gre\_tunnel:** enhance schema with BGP-related attributes and validators
- **magic\_wan\_ipsec\_tunnel:** add automatic\_return\_routing attribute for automatic routing control
- **magic\_wan\_ipsec\_tunnel:** add BGP configuration support with new BGP model attribute
- **magic\_wan\_ipsec\_tunnel:** add bgp\_status computed attribute for BGP connection status information
- **magic\_wan\_ipsec\_tunnel:** add custom\_remote\_identities attribute for custom identity configuration
- **magic\_wan\_ipsec\_tunnel:** enhance schema with BGP and identity-related attributes
- **ruleset:** add request body buffering support
- **ruleset:** enhance ruleset data source with additional configuration options
- **workers\_script:** add observability logs attributes to list data source model
- **workers\_script:** enhance list data source schema with additional configuration options

#### Bug Fixes

- **account\_member**: fix resource importability issues
- **dns\_record:** remove unnecessary fmt.Sprintf wrapper around LoadTestCase call in test configuration helper function
- **load\_balancer:** fix session\_affinity\_ttl type expectations to match Float64 in initial creation and Int64 after migration
- **workers\_kv:** handle special characters correctly in URL encoding

#### Documentation

- **account\_subscription:** update schema description for rate\_plan.sets attribute to clarify it returns an array of strings
- **api\_shield:** add resource-level description for API Shield management of auth ID characteristics
- **api\_shield:** enhance auth\_id\_characteristics.name attribute description to include JWT token configuration format requirements
- **api\_shield:** specify JSONPath expression format for JWT claim locations
- **hyperdrive\_config:** add description attribute to name attribute explaining its purpose in dashboard and API identification
- **hyperdrive\_config:** apply description improvements across resource, data source, and list data source schemas
- **hyperdrive\_config:** improve schema descriptions for cache settings to clarify default values
- **hyperdrive\_config:** update port description to clarify defaults for different database types

#### For more information

- [Terraform Provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)
- [List of stabilized resources ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-20-terraform-v5.16.0-provider/#page","headline":"Terraform v5.16.0 now available","description":"Terraform v5.16.0 stabilizes a number of resources and known issues","url":"https://developers.cloudflare.com/changelog/post/2026-01-20-terraform-v5.16.0-provider/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-20-terraform-v5.16.0-provider/og.png?v=8bee22d7ce99996f","dateModified":"2026-01-20","datePublished":"2026-01-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
