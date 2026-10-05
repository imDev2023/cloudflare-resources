---
description: Configure DNS over HTTPS in your browser.
title: Configure DoH on your browser
image: https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/encrypted-dns-browsers/og.png?v=c8162ea05be77aaf
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/1.1.1.1/llms.txt  
> Use this file to discover all available pages before exploring further.

# Configure DoH on your browser

Last updated May 5, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/encrypted-dns-browsers/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Several browsers support DNS over HTTPS (DoH), which encrypts your DNS queries to protect them from monitoring and tampering.

Some browsers might already have this setting enabled.

Note

[1.1.1.1 for Families](https://developers.cloudflare.com/1.1.1.1/setup/#1111-for-families) provides additional filtering to block malware, phishing, or adult content. To use it, follow the steps below but, instead of choosing the default 1.1.1.1 option, refer to [Set up](https://developers.cloudflare.com/1.1.1.1/setup/#dns-over-https-doh) and specify the URL you want to use.

## Mozilla Firefox

1. Select the menu button > **Settings**.
2. In the **Privacy & Security** menu, scroll down to the **Enable secure DNS using:** section.
3. Select **Increased Protection** or **Max Protection**. By default, it will use the **Cloudflare** provider.
4. If this is not the case, select **Cloudflare** in the **Choose Provider** dropdown.

## Google Chrome

1. Select the three-dot menu in your browser > **Settings**.
2. Select **Privacy and security** > **Security**.
3. Scroll down and enable **Use secure DNS**.
4. Select the **With** option, and from the drop-down menu choose *Cloudflare (1.1.1.1)*.

## Microsoft Edge

1. Select the three-dot menu in your browser > **Settings**.
2. Select **Privacy, Search, and Services**, and scroll down to **Security**.
3. Enable **Use secure DNS**.
4. Select **Choose a service provider**.
5. Select the **Enter custom provider** drop-down menu and choose *Cloudflare (1.1.1.1)*.

## Brave

1. Select the menu button in your browser > **Settings**.
2. Select **Privacy and security** > **Security**.
3. Under **Advanced**, enable **Use secure DNS**.
4. From the **Select DNS provider** drop-down menu, choose *Cloudflare (1.1.1.1)*.

## Check if the browser is configured correctly

Visit [1.1.1.1 help page ↗︎](https://one.one.one.one/help) and check if `Using DNS over HTTPS (DoH)` shows `Yes`.
