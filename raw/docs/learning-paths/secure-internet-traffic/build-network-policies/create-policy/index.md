---
description: Build your first Gateway network policy.
title: Create your first network policy
image: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-network-policies/create-policy/og.png?v=787a6f98574bb97d
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/learning-paths/llms.txt  
> Use this file to discover all available pages before exploring further.

# Create your first network policy

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-network-policies/create-policy/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can control network-level traffic by filtering requests by selectors such as IP addresses and ports. You can also integrate network policies with an [identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) to apply identity-based filtering.

To create a new network policy:

1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Traffic policies** > **Firewall policies**.
2. In the **Network** tab, select **Add a network policy**.
3. Name the policy.
4. Under **Traffic**, build a logical expression that defines the traffic you want to allow or block.
5. Choose an **Action** to take when traffic matches the logical expression. For example, you can use a list of [device serial numbers](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/corp-device/) to ensure users can only access an application if they connect with the Cloudflare One Client from a company device:

   | Selector | Operator | Value | Logic | Action |
   | --- | --- | --- | --- | --- |
   | SNI Domain | is | `internalapp.com` | And | Block |
   | Passed Device Posture Checks | not in | *Device serial numbers* |  |  |
6. Select **Create policy**.

1. [Create an API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with the following permissions:

   | Type | Item | Permission |
   | --- | --- | --- |
   | Account | Zero Trust | Edit |
2. (Optional) Configure your API environment variables to include your [account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/) and API token.
3. Send a `POST` request to the [Create a Zero Trust Gateway rule](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/rules/methods/create/) endpoint. For example, you can use a list of [device serial numbers](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/corp-device/) to ensure users can only access an application if they connect with the Cloudflare One Client from a company device:

   *Create a Zero Trust Gateway rulebash*

   

   ```bash
   curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/gateway/rules" \
   	--request POST \
   	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
   	--json '{
   		"name": "Enforce device posture",
   		"description": "Ensure only devices in Zero Trust organization can connect to application",
   		"precedence": 0,
   		"enabled": true,
   		"action": "block",
   		"filters": [
   				"l4"
   		],
   		"traffic": "any(net.sni.domains[*] == \"internalapp.com\")",
   		"identity": "",
   		"device_posture": "not(any(device_posture.checks.passed[*] in {\"LIST_UUID\"}))"
   	}'
   ```



```sh
{
	 "success": true,
	 "errors": [],
	 "messages": []
}
```

The API will respond with a summary of the policy and the result of your request.

For more information, refer to [network policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/).
