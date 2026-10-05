---
description: Automate the setup of a Cloudflare subdomain zone for Enterprise accounts using Terraform.
title: Create a subdomain zone using Terraform
image: https://developers.cloudflare.com/terraform/how-to/create-secondary-zone/og.png?v=ef45add96f9523a2
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/terraform/llms.txt  
> Use this file to discover all available pages before exploring further.

# Create a subdomain zone using Terraform

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/terraform/how-to/create-secondary-zone/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A [subdomain zone](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/) lets you manage a subdomain in a separate Cloudflare zone from the parent domain. This is useful for access control and team management. This guide shows how to automate the setup using the [Cloudflare Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs). It is only available for Enterprise accounts

> NOTE: subdomain setup is only available for Enterprise accounts

## Prerequisites

- Terraform installed. Refer to [Get started](https://developers.cloudflare.com/terraform/installing/).
- Your Cloudflare account ID and a configured provider block. Refer to [Initialize Terraform](https://developers.cloudflare.com/terraform/tutorial/initialize-terraform/).

## Create the zone

Create a `cloudflare_zone` resource for the subdomain zone. The following example creates a zone for `subdomain.example.com`:

```hcl
resource "cloudflare_zone" "subdomain_example_com" {
  account = {
    id = var.cloudflare_account_id
  }
  name = "subdomain.example.com"
  type = "full"
}
```

Terraform creates the zone in a **Pending** state. You must add NS delegation records to the parent zone before Cloudflare activates it.

Note

Refer to the [cloudflare\_zone docs ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zone) in the Terraform provider documentation when you need to reference other zone properties.

## Related resources

- [Subdomain setup](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/)
- [`cloudflare_zone` resource ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zone)
- [`cloudflare_dns_record` resource ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/dns_record)
