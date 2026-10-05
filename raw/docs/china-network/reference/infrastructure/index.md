---
description: China data center locations, network IP addresses, and API endpoints.
title: Infrastructure
image: https://developers.cloudflare.com/china-network/reference/infrastructure/og.png?v=4e6968730ad90cf4
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/china-network/llms.txt  
> Use this file to discover all available pages before exploring further.

# Infrastructure

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/china-network/reference/infrastructure/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## China data centers

For up-to-date information, refer to the [Cloudflare China Network ↗︎](https://www.cloudflare.com/china-network/) page.

### Network IP addresses

Cloudflare publishes a list of IP addresses for JD Cloud data centers, used by Cloudflare when connecting to the origin networks of customers to retrieve assets. These addresses are not the same IP addresses returned to website visitors as part of DNS resolution.

You can obtain the list of JD Cloud data center IP addresses via Cloudflare API. Use the [Cloudflare/JD Cloud IP Details](https://developers.cloudflare.com/api/resources/ips/methods/list/) operation with the `networks=jdcloud` query string parameter:

*Cloudflare/JD Cloud IP Detailsbash*

```bash
curl "https://api.cloudflare.com/client/v4/ips?networks=jdcloud" \
	--request GET
```

```json
{
	"result": {
		"ipv4_cidrs": [
			// (...)
		],
		"ipv6_cidrs": [
			// (...)
		],
		"jdcloud_cidrs": [
			// (...)
		],
		"etag": "<ETAG>"
	},
	"success": true,
	"errors": [],
	"messages": []
}
```

The `jdcloud_cidrs` array lists the IP addresses of JD Cloud data centers.

Cloudflare will add new IP addresses to this list 30 days in advance before connecting from those IP addresses to an origin server. If you are using the China Network on JD Cloud, you should update your firewalls to reflect any IP address changes at least once every 30 days.
