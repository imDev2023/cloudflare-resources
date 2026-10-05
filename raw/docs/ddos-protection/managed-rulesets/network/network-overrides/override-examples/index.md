---
description: Example override configurations for Network-layer DDoS Attack Protection rules.
title: Override examples
image: https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/override-examples/og.png?v=5f2c7cd87900684d
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ddos-protection/llms.txt  
> Use this file to discover all available pages before exploring further.

# Override examples

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/override-examples/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Use cases

The following scenarios detail how you can make use of override rules as a solution to common Network DDoS Protection issues.

### VPN traffic is blocked by a UDP rule

If you have VPN traffic concentrated to a single or a few single destination IP addresses and the traffic is being blocked by a UDP rule, you can create an override rule for the UDP rule to the destination IPs or ranges.

Note

The override only applies to the detection and not the fingerprint generated and used for mitigation. Refer to [Important remarks](https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/override-expressions/#important-remarks) for more information.

### Attack traffic is flagged by the adaptive rule based on UDP and destination port

If you recognize that the traffic flagged by the adaptive rule based on UDP and destination port is an attack, you create an override rule to enable the adaptive rule in mitigation mode, setting the action to block the traffic.

### Minimize the risk of false positives impacting production traffic

To avoid disruptions during initial deployment, you can create a *Log* only – *Essentially Off* ruleset override that allows all traffic while logging detection results. This lets you safely observe and analyze DDoS activity before enabling enforcement.

1. In the Cloudflare dashboard, go to the **Security rules** page. [Go to **Security rules** ↗](https://dash.cloudflare.com/?to=/:account/:zone/security/security-rules)
2. Go to the **DDoS protection** tab.
3. On **HTTP DDoS attack protection**, select **Create override**.
4. Set the **Scope** to *Apply to all incoming requests*.
5. Under **Ruleset configuration**:
   - Set the **Ruleset action** to *Log*.
   - Set the **Ruleset sensitivity** to *Essentially Off*.
6. Select **Save**.
