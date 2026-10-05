---
description: Connect Hyperdrive to private databases through a Workers VPC service, with TLS verification, observability, and reusable services across configurations.
title: Hyperdrive support for private databases with Workers VPC
image: https://developers.cloudflare.com/changelog/post/2026-04-29-hyperdrive-vpc-private-databases/og.png?v=b3e75c3d56ca927a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 29, 2026

## Hyperdrive support for private databases with Workers VPC

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-29-hyperdrive-vpc-private-databases/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now connect Hyperdrive to a private database through a [Workers VPC service](https://developers.cloudflare.com/workers-vpc/). This is the recommended way to connect Hyperdrive to a private database that is not exposed to the public Internet.

When creating a Hyperdrive configuration in the Cloudflare dashboard, choose **Connect to private database** and then **Workers VPC**. From there, you can select an existing VPC service or create a new one inline by picking a Cloudflare Tunnel and entering your origin host and TCP port.

You can also create a Hyperdrive configuration backed by a Workers VPC service from the command line:

```sh
npx wrangler hyperdrive create my-vpc-database \
  --service-id <YOUR_VPC_SERVICE_ID> \
  --database <DATABASE_NAME> \
  --user <DATABASE_USER> \
  --password <DATABASE_PASSWORD> \
  --scheme postgresql
```

Workers VPC services are reusable across Hyperdrive configurations and can also be bound directly to Workers, so you can share the same private connection across multiple products.

To get started, refer to [Connect Hyperdrive to a private database using Workers VPC](https://developers.cloudflare.com/hyperdrive/configuration/connect-to-private-database-vpc/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-29-hyperdrive-vpc-private-databases/#page","headline":"Hyperdrive support for private databases with Workers VPC","description":"Connect Hyperdrive to private databases through a Workers VPC service, with TLS verification, observability, and reusable services across configurations.","url":"https://developers.cloudflare.com/changelog/post/2026-04-29-hyperdrive-vpc-private-databases/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-29-hyperdrive-vpc-private-databases/og.png?v=b3e75c3d56ca927a","dateModified":"2026-04-29","datePublished":"2026-04-29","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
