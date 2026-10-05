---
description: Configure DNS filtering for a network.
title: Onboard DNS for a network
image: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/onboard-dns/og.png?v=3c2d4fafeb27f25e
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/learning-paths/llms.txt  
> Use this file to discover all available pages before exploring further.

# Onboard DNS for a network

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/onboard-dns/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The fastest way to start filtering DNS queries is to change your DNS resolver to use a specific Gateway endpoint. You can make this change at the browser, OS, or router level.

Choose this option if:

- You want to try out DNS filtering without installing software.
- You do not need to filter by user identity.
- You want to apply blanket DNS policies to all devices in a physical location, such as a retail store or office.

## Change DNS resolver in browser

To configure your browser to send traffic to Gateway:

1. Obtain your DNS over HTTPS (DoH) address:
   1. Go to **Gateway** > **DNS locations**.
   2. Select **Add a location**.
   3. Enter a name for the location.
   4. Turn on **Set as Default DNS Location**.
   5. Select **Add location**.
   6. Copy your **DNS over HTTPS** hostname: `https://<YOUR_DOH_SUBDOMAIN>.cloudflare-gateway.com/dns-query`
2. Follow the configuration instructions for your browser:<details><summary>

   Mozilla Firefox</summary>

   1. In Firefox, go to **Settings**.
   2. In **Privacy &amp; Security**, go to **DNS over HTTPS**.
   3. Under **Enable secure DNS using**, select *Max Protection*.
   4. In **Choose provider**, choose *Custom*.
   5. In the field, enter <code>https://&lt;YOUR_DOH_SUBDOMAIN&gt;.cloudflare-gateway.com/dns-query</code>.

   Firefox is now configured to use your DoH endpoint. For more information on configuring DoH settings in Firefox, refer to <a href="https://support.mozilla.org/kb/dns-over-https">Mozilla's documentation ↗︎</a>.

   Note

   If you want to enforce DNS policies through the Cloudflare One Client instead of over DoH, you can disable DoH for your organization by blocking the <a href="https://support.mozilla.org/kb/canary-domain-use-application-dnsnet">Firefox DoH canary domain ↗︎</a>.</details>

<details><summary>

   Google Chrome</summary>

   1. In Chrome, go to **Settings** &gt; **Privacy and security** &gt; **Security**.
   2. Scroll down and turn on **Use secure DNS**.
   3. Select **With Custom**.
   4. In the **Enter custom provider** field, enter <code>https://&lt;YOUR_DOH_SUBDOMAIN&gt;.cloudflare-gateway.com/dns-query</code>.

   Read more about <a href="https://www.chromium.org/developers/dns-over-https">enabling DNS over HTTPS ↗︎</a> on Chrome.</details>

<details><summary>

   Microsoft Edge</summary>

   1. In Microsoft Edge, go to **Settings**.
   2. Select **Privacy, Search, and Services**, and scroll down to **Security**.
   3. Turn on **Use secure DNS**.
   4. Select **Choose a service provider**.
   5. In the **Enter custom provider** field, enter <code>https://&lt;YOUR_DOH_SUBDOMAIN&gt;.cloudflare-gateway.com/dns-query</code>.</details>

<details><summary>

   Brave</summary>

   1. In Brave, go to **Settings** &gt; **Security and Privacy** &gt; **Security**.
   2. Turn on **Use secure DNS**.
   3. Select **With Custom**.
   4. In the **Enter custom provider** field, enter <code>https://&lt;YOUR_DOH_SUBDOMAIN&gt;.cloudflare-gateway.com/dns-query</code>.</details>

<details><summary>

   Safari</summary>

Currently, Safari does not support DNS over HTTPS.</details>

3. Verify that third-party firewall or TLS decryption software does not inspect or block traffic to the DoH endpoint: `https://<YOUR_DOH_SUBDOMAIN>.cloudflare-gateway.com/dns-query`.

DNS filtering is now turned on for this browser.

To configure your router or OS, or to add additional DNS endpoints, refer to [DNS locations](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/locations/).
