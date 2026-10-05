---
description: Install Terraform and configure the Cloudflare provider on your operating system.
title: Get started
image: https://developers.cloudflare.com/terraform/installing/og.png?v=9ec0e980c476f62b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/terraform/llms.txt  
> Use this file to discover all available pages before exploring further.

# Get started

Last updated Oct 2, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/terraform/installing/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Install the latest version of the Terraform CLI from [HashiCorp's official installation guide ↗︎](https://developer.hashicorp.com/terraform/install).

Caution

Terraform maintains your configuration state, which can be broken when you make configuration changes through both Terraform and either the Cloudflare Dashboard or API.

To avoid this state, make sure you manage Terraform resources only in Terraform. For more details, refer to our [best practices](https://developers.cloudflare.com/terraform/advanced-topics/best-practices/).

## Mac

```sh
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
```

## Linux

Install via your distribution's package manager:

```sh
sudo apt install terraform
```

## Windows

Download the installer from [HashiCorp's installation page ↗︎](https://developer.hashicorp.com/terraform/install) and follow the setup instructions.
