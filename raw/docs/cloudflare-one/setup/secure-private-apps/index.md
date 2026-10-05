---
description: Provide browser-based access to internal web applications, SSH servers, and remote desktops without installing software on user devices.
title: Secure private apps
image: https://developers.cloudflare.com/cloudflare-one/setup/secure-private-apps/og.png?v=4ccf8f46562fb97c
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-one/llms.txt  
> Use this file to discover all available pages before exploring further.

# Secure private apps

Last updated Apr 17, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-one/setup/secure-private-apps/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Access lets users reach internal applications through a browser without a VPN or client software on their device. You connect your application to Cloudflare using a secure connection called a tunnel, then protect it with policies that control who can access it. For more background, refer to [What is clientless access?](https://developers.cloudflare.com/learning-paths/clientless-access/concepts/what-is-clientless-access/).

How you set this up depends on the type of application you are securing. Choose the scenario that matches your use case:

### [Private web application](https://developers.cloudflare.com/cloudflare-one/setup/secure-private-apps/private-web-app/)

Connect an internal web application to Cloudflare and control who can access it. Best for applications like company intranets, internal wikis, or admin panels.

### [Clientless SSH](https://developers.cloudflare.com/cloudflare-one/setup/secure-private-apps/clientless-ssh/)

Provide in-browser command line access to an internal server without SSH client software on the user's device.

### [In-browser remote desktop](https://developers.cloudflare.com/cloudflare-one/setup/secure-private-apps/in-browser-rdp/)

Provide in-browser remote desktop access to Windows hosts without remote desktop client software on the user's device.

Note

For in-depth guidance on clientless access and advanced configuration, refer to the [Clientless access learning path](https://developers.cloudflare.com/learning-paths/clientless-access/concepts/what-is-clientless-access/).
