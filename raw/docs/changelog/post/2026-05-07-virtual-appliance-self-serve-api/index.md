---
description: Create, rotate, and delete Cloudflare One Virtual Appliance instances and license keys directly through the API and Terraform.
title: Self-serve provisioning of Cloudflare One Virtual Appliance via API
image: https://developers.cloudflare.com/changelog/post/2026-05-07-virtual-appliance-self-serve-api/og.png?v=19897d9896505b82
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 7, 2026

## Self-serve provisioning of Cloudflare One Virtual Appliance via API

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-07-virtual-appliance-self-serve-api/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now create, rotate, and delete Cloudflare One Virtual Appliance instances and their license keys directly via the API and Terraform.

- Create a virtual appliance and receive a license key: `POST /accounts/{account_id}/magic/connectors` with `device.provision_license: true`.
- Rotate the license key for an existing virtual appliance: `PATCH /accounts/{account_id}/magic/connectors/{connector_id}` with `provision_license: true`. The previous key is immediately and irrevocably revoked.
- Delete a virtual appliance to release the associated licensed device.

The license key is returned in the response only once, at create or rotate time. Copy and store it securely.

For details, refer to [Configure a Cloudflare One Virtual Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-07-virtual-appliance-self-serve-api/#page","headline":"Self-serve provisioning of Cloudflare One Virtual Appliance via API","description":"Create, rotate, and delete Cloudflare One Virtual Appliance instances and license keys directly through the API and Terraform.","url":"https://developers.cloudflare.com/changelog/post/2026-05-07-virtual-appliance-self-serve-api/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-07-virtual-appliance-self-serve-api/og.png?v=19897d9896505b82","dateModified":"2026-05-07","datePublished":"2026-05-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
