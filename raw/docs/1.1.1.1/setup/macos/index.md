---
description: Configure 1.1.1.1 on macOS.
title: macOS
image: https://developers.cloudflare.com/1.1.1.1/setup/macos/og.png?v=eecc84a6a6fd944f
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/1.1.1.1/llms.txt  
> Use this file to discover all available pages before exploring further.

# macOS

Last updated May 1, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/1.1.1.1/setup/macos/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

These steps configure 1.1.1.1 as the DNS resolver for a specific network service (such as Wi-Fi or Ethernet) on your Mac.

Take note of any DNS addresses you might have set up, and save them in a safe place in case you need to use them later.

1. Go to **System Settings**. You can find it by pressing `CMD + Space` on your keyboard and typing `System Settings`.
2. Go to **Network**.
3. Select a network service.
4. Select **Details**.
5. Go to **DNS**.
6. Under **DNS Servers**, select **Add**.
7. Depending on what you want to configure, choose one of the following DNS addresses for IPv4:<details><summary>

   Use 1.1.1.1 resolver</summary>

   ```txt
   1.1.1.1
   1.0.0.1
   ```

   </details>

<details><summary>

   Block malware with 1.1.1.1 for Families</summary>

   ```txt
   1.1.1.2
   1.0.0.2
   ```

   </details>

<details><summary>

   Block malware and adult content with 1.1.1.1 for Families</summary>

   ```txt
   1.1.1.3
   1.0.0.3
   ```

   </details>

8. Depending on what you want to configure, choose one of the following DNS addresses for IPv6:<details><summary>

   Use 1.1.1.1 resolver</summary>

   ```txt
   2606:4700:4700::1111
   2606:4700:4700::1001
   ```

   </details>

<details><summary>

   Block malware with 1.1.1.1 for Families</summary>

   ```txt
   2606:4700:4700::1112
   2606:4700:4700::1002
   ```

   </details>

<details><summary>

   Block malware and adult content with 1.1.1.1 for Families</summary>

   ```txt
   2606:4700:4700::1113
   2606:4700:4700::1003
   ```

   </details>

9. Select **OK**.

Note

Setting up a static IP address to configure a DNS server may prevent you from connecting to some public Wi-Fi networks that use captive portals — these are the web pages some wireless networks employ to let users log in and use their services.

If you are experiencing connectivity issues related to captive portals:

1. Remove the static IP addresses from the device or disable the 1.1.1.1 app.
2. Connect to the Wi-Fi network.
3. Once the connection has been established, re-add the static IP addresses or enable the 1.1.1.1 app.

## Encrypt your DNS queries

1.1.1.1 supports DNS over TLS (DoT) and DNS over HTTPS (DoH), two standards developed for encrypting plaintext DNS traffic. This prevents untrustworthy entities from interpreting and manipulating your queries. For more information on how to encrypt your DNS queries, please refer to the [Encrypted DNS documentation](https://developers.cloudflare.com/1.1.1.1/encryption/).
