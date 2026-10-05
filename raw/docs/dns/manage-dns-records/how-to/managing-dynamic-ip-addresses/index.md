---
description: Update DNS records automatically for dynamic IP addresses.
title: Dynamically update DNS records
image: https://developers.cloudflare.com/dns/manage-dns-records/how-to/managing-dynamic-ip-addresses/og.png?v=7951fef7f1076411
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/dns/llms.txt  
> Use this file to discover all available pages before exploring further.

# Dynamically update DNS records

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/dns/manage-dns-records/how-to/managing-dynamic-ip-addresses/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Most Internet service providers and some hosting providers dynamically update their customer's IP addresses. If this situation applies to you, you need an automated solution to dynamically update your DNS records in Cloudflare.

## Cloudflare API

Create a script to monitor IP address changes and then have that script push changes to the [Cloudflare API](https://developers.cloudflare.com/api/resources/dns/subresources/records/methods/update/).

## ddclient

[ddclient ↗︎](https://github.com/ddclient/ddclient) is a third-party Perl client used to update dynamic DNS entries for accounts on various DNS providers.
