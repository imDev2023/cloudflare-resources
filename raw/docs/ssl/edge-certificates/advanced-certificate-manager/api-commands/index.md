---
description: API commands for managing advanced certificates.
title: API commands
image: https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/api-commands/og.png?v=ae3be2b9666e4a3e
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ssl/llms.txt  
> Use this file to discover all available pages before exploring further.

# API commands

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/api-commands/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Use the following API commands to manage advanced certificates. If you are using our API for the first time, review our [API documentation](https://developers.cloudflare.com/fundamentals/api/).

| Command | Method | Endpoint | Additional notes |
| --- | --- | --- | --- |
| [Order advanced certificate](https://developers.cloudflare.com/api/resources/ssl/subresources/certificate_packs/methods/create/) | `POST` | `zones/<<ZONE_ID>>/ssl/certificate_packs/order` | |
| [Restart certificate validation](https://developers.cloudflare.com/api/resources/ssl/subresources/certificate_packs/methods/edit/) | `PATCH` | `zones/<<ZONE_ID>>/ssl/certificate_packs/<<ID>>` | For a Certificate Pack in a `validation_timed_out` status. |
| [Delete certificate pack](https://developers.cloudflare.com/api/resources/ssl/subresources/certificate_packs/methods/delete/) | `DELETE` | `zones/<<ZONE_ID>>/ssl/certificate_packs/<<ID>>` | |
| [List certificate packs in a zone](https://developers.cloudflare.com/api/resources/ssl/subresources/certificate_packs/methods/list/) | `GET` | `zones/<<ZONE_ID>>/ssl/certificate_packs?status=all` | This API call returns all certificate packs for a domain (Universal, Custom, and Advanced). |
| List Cipher Suite settings: [Get zone setting](https://developers.cloudflare.com/api/resources/zones/subresources/settings/methods/get/) with `ciphers` as the setting name in the URI path | `GET` | `zones/<<ZONE_ID>>/settings/ciphers` | |
| Change Cipher Suite settings: [Edit zone setting](https://developers.cloudflare.com/api/resources/zones/subresources/settings/methods/edit/) with `ciphers` as the setting name in the URI path | `PATCH` | `zones/<<ZONE_ID>>/settings/ciphers` | To restore default settings, send a blank array in the `value` parameter. |
