---
description: Create egress policies for IP consistency.
title: Use egress policies to deliver consistent egress IPs
image: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-egress-policies/egress-policies/og.png?v=b6a652a5a11bc197
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/learning-paths/llms.txt  
> Use this file to discover all available pages before exploring further.

# Use egress policies to deliver consistent egress IPs

Last updated May 1, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-egress-policies/egress-policies/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

Only available on Enterprise plans.

Egress policies allow you to determine whether your organization's traffic egresses via the default Cloudflare IP or via a [dedicated egress IP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/) assigned to your account.

To create a new egress policy:

1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Traffic policies** > **Egress policies**.
2. Select **Add a policy**.
3. Name the policy.
4. Build a logical expression that defines the traffic you want to control egress for. For example, you can add a policy to configure all traffic destined for a third-party network to use a static source IP:

   | Policy name | Selector | Operator | Value | Egress method |
   | --- | --- | --- | --- | --- |
   | Access third-party provider | Destination IP | is | `198.51.100.158` | Dedicated Cloudflare egress IPs |
   | Primary IPv4 address | IPv6 address |
   | --- | --- |
   | `203.0.113.88` | `2001:db8::/32` |
5. Select **Create policy**.

For more information, refer to [Egress policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/).
