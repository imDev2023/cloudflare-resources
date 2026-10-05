---
description: View DDoS attack analytics in Security Analytics, Network Analytics, or the GraphQL API.
title: Analytics
image: https://developers.cloudflare.com/ddos-protection/reference/analytics/og.png?v=4911e84df72835f3
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# Analytics

Last updated May 5, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/reference/analytics/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can view DDoS analytics in different dashboards, depending on your service and plan:

- The [Security Events dashboard](https://developers.cloudflare.com/waf/analytics/security-events/) provides you with visibility into L7 security events that target your zone, including HTTP DDoS attacks and TCP attacks. The dashboard displays mitigations of HTTP DDoS attacks as HTTP DDoS events. These events are also available via [Cloudflare Logs](https://developers.cloudflare.com/logs/).
- The [Network Analytics dashboard](https://developers.cloudflare.com/analytics/network-analytics/) provides you with visibility into L3/4 traffic and DDoS attacks that target your IP ranges or Spectrum applications.

## Availability

| Service | Free | Pro | Business | Enterprise |
| --- | --- | --- | --- | --- |
| WAF/CDN | Sampled logs only | Security Events | Security Events | Security Events |
| Spectrum/BYOIP | – | – | – | Network Analytics |
| Magic Transit | – | – | – | Network Analytics |

## Remarks

In some situations, the analytics dashboards will not show you the ID of the DDoS managed rule that handled a packet/request. This means that an internal DDoS rule, which Cloudflare does not currently expose publicly, applied an action to the packet/request. These internal DDoS rules have a very low false positive rate and should always be enabled to protect your properties against DDoS attacks. For the same reason, DDoS rule IDs may also be unavailable in Cloudflare logs and API responses.
