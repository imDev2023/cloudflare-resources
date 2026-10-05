---
description: Configure 1.1.1.1 on Microsoft Azure virtual networks.
title: Azure
image: https://developers.cloudflare.com/1.1.1.1/setup/azure/og.png?v=c05dd93dfd38c8d6
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/1.1.1.1/llms.txt  
> Use this file to discover all available pages before exploring further.

# Azure

Last updated May 6, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/1.1.1.1/setup/azure/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

These steps configure 1.1.1.1 as the DNS resolver for an Azure Virtual Network (VNet). This applies to all resources in the VNet, including virtual machines.

1. Log in to your Azure portal.
2. From the Azure portal side menu, select **Virtual Networks**.
3. Select the virtual network you want to configure.
4. Select **DNS Servers** > **Custom**, and add two entries:

   ```txt
   1.1.1.1
   1.0.0.1
   ```


5. Select **Save**.
