---
description: Install the Pulumi CLI on Mac, Linux, or Windows and verify your installation.
title: Get started
image: https://developers.cloudflare.com/pulumi/installing/og.png?v=d6faf26d33c97ab2
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/pulumi/llms.txt  
> Use this file to discover all available pages before exploring further.

# Get started

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/pulumi/installing/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Follow the recommended steps for your operating system below. For official instructions on installing Pulumi and other install options, refer to [Install Pulumi ↗︎](https://www.pulumi.com/docs/install/).

Note

Pulumi is free, open source, and optionally pairs with the [Pulumi Cloud ↗︎](https://www.pulumi.com/product/pulumi-cloud/) to make managing infrastructure secure, reliable, and hassle-free.

Caution

To avoid resource management conflicts, it’s **always** recommended to manage Pulumi-controlled resources via Pulumi.

## Installation

### Mac

Install via Homebrew package manager.

```sh
brew install pulumi/tap/pulumi
```

### Linux

Use the installation script.

```sh
curl -fsSL https://get.pulumi.com | sh
```

### Windows

1. Download the latest installer from the [Pulumi Repository ↗︎](https://github.com/pulumi/pulumi-winget/releases/latest)
2. Double click the MSI file and complete the wizard.

## Verify installation

To verify your installation, run the following in the terminal:

```sh
pulumi version
```

Note

For upgrades and installation alternatives, refer to [Install Pulumi ↗︎](https://www.pulumi.com/docs/install/).

## Next steps

Follow the [Hello World tutorial](https://developers.cloudflare.com/pulumi/tutorial/hello-world/) to write a simple Pulumi program. It takes about 10 minutes to complete.
