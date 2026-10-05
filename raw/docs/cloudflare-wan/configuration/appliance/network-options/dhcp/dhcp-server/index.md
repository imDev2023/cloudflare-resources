---
description: Configure the Appliance DHCP server.
title: DHCP server
image: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-server/og.png?v=6a3bc96d55f0bfdf
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-wan/llms.txt  
> Use this file to discover all available pages before exploring further.

# DHCP server

Last updated Aug 24, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-server/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

When you use a static IP address, Cloudflare One Appliance (formerly Magic WAN Connector) can also act as a DHCP server in your network. To enable this feature:

1. Go to the **Connectors** page.

[Go to **Connectors** ↗](https://dash.cloudflare.com/?to=/:account/magic-networks/connections)

2. Go to the **Appliances** tab > **Profiles**.
3. Select the Cloudflare One Appliance you want to configure > **Edit**.
4. Select **Network Configuration** > **LAN configuration**.
5. In **LAN configuration**, select the LAN where you want to enable DHCP server.
6. Select **Edit**.
7. Under **Static addressing**, select **This is a DHCP Server**. You also have to specify:
   - The DNS server address. You can have more than one IP address. Select **Add DNS Server** for each server you want to add.
   - The DHCP pool start
   - The DHCP pool end

Note

You will need your [account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/) and [API token](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/) to use the API.

Create a [`PUT` request](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/lans/methods/update/) to update the LAN where you want to enable DHCP server:

Example:

<details>

<summary>

Required API token permissions

</summary>

At least one of the following <a href="https://developers.cloudflare.com/fundamentals/api/reference/permissions/">token permissions</a> is required:

- <code>Magic WAN Write</code>
- <code>Magic Transit Write</code>

</details>

*Update Site LANbash*

```bash
curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/magic/sites/$SITE_ID/lans/$LAN_ID" \
	--request PUT \
	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
	--json '{
		"lan": {
				"static_addressing": {
						"dhcp_server": {
								"dhcp_pool_end": "<IP_ADDRESS>",
								"dhcp_pool_start": "<IP_ADDRESS>",
								"dns_server": "<IP_ADDRESS>"
						}
				}
		}
	}'
```
