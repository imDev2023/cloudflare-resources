---
description: Configure DHCP relay on the Appliance.
title: DHCP relay
image: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-relay/og.png?v=617d9a1dedd78b4a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-wan/llms.txt  
> Use this file to discover all available pages before exploring further.

# DHCP relay

Last updated Aug 24, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-relay/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

DHCP Relay provides a way for DHCP clients to communicate with DHCP servers that are not available on the same local subnet/broadcast domain. When you enable DHCP Relay, Cloudflare One Appliance (formerly Magic WAN Connector) forwards DHCP discover messages to a predefined DHCP server, and routes the responses back to the original device that sent the discover message.

```
  	flowchart LR
  	accTitle: DHCP Relay diagram
  	accDescr: The graph shows Cloudflare One Appliance sending DHCP discover messages to a DHCP server offsite.
  			a(Cloudflare One Appliance) <--> b(Cloudflare/Cloudflare WAN) <--> c(DHCP server)

  			subgraph Site A
  			d[LAN 1] <--> a
  			e[LAN 2] <--> a
  			end

  			subgraph Site B
  			c
  			end
  			classDef orange fill:#f48120,color: black
  			class a,b,c orange

```

*The graph shows Cloudflare One Appliance sending DHCP discover messages to a DHCP server offsite.*

Caution

DHCP relay will not work if your DHCP server is behind a [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/). To enable DHCP relay functionality, use either a Cloudflare WAN IPsec/GRE tunnel or a CNI connection.

To configure DHCP relay:

1. Go to the **Connectors** page.

[Go to **Connectors** ↗](https://dash.cloudflare.com/?to=/:account/magic-networks/connections)

2. Go to the **Appliances** tab > **Profiles**.
3. Select your Cloudflare One Appliance > **Edit**.
4. Select **Network Configuration**.
5. In **LAN configuration**, select the LAN where you need to configure DHCP relay.
6. Select **Edit**.
7. Select **This is a DHCP Relay**.
8. In **Upstream DHCP server addresses**, enter the IP address of your DHCP server.
9. (Optional) If you need to add more DHCP server addresses, select **Add upstream DHCP server address** as many times as needed, and enter the new values.

Note

You will need your [account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/) and [API token](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/) to use the API.

Create a [`PUT` request](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/lans/methods/update/) to update the LAN where you want to enable DHCP relay:

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
						"dhcp_relay": {
								"server_addresses": [
										"192.0.2.1"
								]
						}
				}
		}
	}'
```
