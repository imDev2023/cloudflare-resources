---
description: Protect APIs with schema validation, rate limiting, and authentication.
title: Secure API endpoints
image: https://developers.cloudflare.com/use-cases/application-security/api-endpoints/og.png?v=bcdfa15a5ae66400
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/use-cases/llms.txt  
> Use this file to discover all available pages before exploring further.

# Secure API endpoints

Last updated Apr 24, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/use-cases/application-security/api-endpoints/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

API endpoints are vulnerable to schema violations, abuse, and unauthorized access. Cloudflare API Shield validates requests against your OpenAPI specification, and mutual TLS (mTLS) authenticates known clients with certificates.

## Solutions

### API Shield

Discover, secure, and monitor your APIs. [Learn more about API Shield](https://developers.cloudflare.com/api-shield/).

- **API discovery** - Automatically identify API endpoints in your traffic, including undocumented ones
- **Schema validation** - Reject requests that do not conform to your OpenAPI specification
- **Sequence mitigation** - Detect and block API abuse patterns such as out-of-order requests

### mTLS

Mutual TLS client certificate authentication. [Learn more about mTLS](https://developers.cloudflare.com/ssl/client-certificates/).

- **mTLS authentication** - Require client certificates for machine-to-machine API access

## Get started

1. [API Shield get started](https://developers.cloudflare.com/api-shield/get-started/)
2. [Set up mTLS](https://developers.cloudflare.com/ssl/client-certificates/)
