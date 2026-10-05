---
description: Enhance policies with threat indicator feeds.
title: Use indicator feeds to improve security policies
image: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/understand-policies/indicator-feeds/og.png?v=3ac508f0babf75f4
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/learning-paths/llms.txt  
> Use this file to discover all available pages before exploring further.

# Use indicator feeds to improve security policies

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/understand-policies/indicator-feeds/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

When building DNS, network, or HTTP policies to block malicious activity for your organization, you can use external indicator feeds supplied by Cloudflare and other third-party providers.

## Subscribe to indicator feeds

Cloudflare threat intelligence data consists of a data exchange between providers and subscribers.

A provider is an organization that has a set of data that they are interested in sharing with other Cloudflare organizations. Any organization can be a provider. Examples of current providers are Government Cyber Defense groups.

Subscribers can be any Cloudflare customer that wants to secure their environment further by creating rules based on provider datasets. Subscribers must be authorized by a provider. Authorization is granted using the [Grant permission to indicator feed endpoint](https://developers.cloudflare.com/api/resources/intel/subresources/indicator_feeds/subresources/permissions/methods/create/).

To subscribe to an indicator feed, contact your account team. For more information, refer to [Custom Indicator Feeds](https://developers.cloudflare.com/security-center/indicator-feeds/).
