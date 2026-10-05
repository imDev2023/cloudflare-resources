---
description: Enable automatic mitigation of random prefix attacks in the Cloudflare dashboard or via the API.
title: Setup
image: https://developers.cloudflare.com/dns/dns-firewall/random-prefix-attacks/setup/og.png?v=96bb1374ef08a9cd
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/dns/llms.txt  
> Use this file to discover all available pages before exploring further.

# Setup

Last updated Jul 10, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/dns/dns-firewall/random-prefix-attacks/setup/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

In order to enable automatic mitigation of [random prefix attacks](https://developers.cloudflare.com/dns/dns-firewall/random-prefix-attacks/about/):

1. Set up [DNS Firewall](https://developers.cloudflare.com/dns/dns-firewall/setup/).
2. Enable attack mitigation on your DNS Firewall cluster.
   1. In the Cloudflare dashboard, go to the **DNS Firewall Clusters** page. [Go to **Clusters** ↗](https://dash.cloudflare.com/?to=/:account/dns-firewall/clusters)
   2. Select the cluster you want to update, then select **Edit**.
   3. Turn on **Attack mitigation** and choose whether Cloudflare should only mitigate attacks when the upstream is unhealthy.
   4. Select **Save**.

   Send a [`PATCH` request](https://developers.cloudflare.com/api/resources/dns_firewall/methods/edit/) to update your DNS Firewall cluster:<details><summary>

   Required API token permissions</summary>

At least one of the following <a href="https://developers.cloudflare.com/fundamentals/api/reference/permissions/">token permissions</a> is required:
   - <code>DNS Firewall Write</code></details>

   *Update DNS Firewall Clusterbash*

   

   ```bash
   curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/dns_firewall/$DNS_FIREWALL_ID" \
   	--request PATCH \
   	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
   	--json '{
   		"attack_mitigation": {
   				"enabled": true,
   				"only_when_upstream_unhealthy": true
   		}
   	}'
   ```



Once you turn on attack mitigation, Cloudflare returns a `REFUSED` response to queries that are part of a random prefix attack.

Note

If you do not specify otherwise, Cloudflare automatically sets the `only_when_upstream_unhealthy` parameter to true, which means that Cloudflare will only mitigate attacks when we detect that the upstream is unresponsive (possibly as a result of an attack).
