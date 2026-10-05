---
description: Examples of rules for mitigating requests containing leaked credentials.
title: Example mitigation rules
image: https://developers.cloudflare.com/waf/detections/leaked-credentials/examples/og.png?v=23ffe249e1a10e47
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/waf/llms.txt  
> Use this file to discover all available pages before exploring further.

# Example mitigation rules

Last updated May 5, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/waf/detections/leaked-credentials/examples/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Rate limit suspicious logins with leaked credentials

Note

Access to the `cf.waf.credential_check.username_and_password_leaked` field requires a Pro plan or above.

[Create a rate limiting rule](https://developers.cloudflare.com/waf/rate-limiting-rules/create-zone-dashboard/) using [account takeover (ATO) detection](https://developers.cloudflare.com/bots/additional-configurations/detection-ids/account-takeover-detections/) and leaked credentials fields to limit volumetric attacks from particular IP addresses, JA4 Fingerprints, or countries.

The following example rule applies rate limiting to requests with a specific [ATO detection ID](https://developers.cloudflare.com/bots/additional-configurations/detection-ids/account-takeover-detections/) (corresponding to `Observes all login traffic to the zone`) that contain a previously leaked username and password:

**When incoming requests match**:  
`(any(cf.bot_management.detection_ids[*] eq 201326593) and cf.waf.credential_check.username_and_password_leaked)`

**With the same characteristics**: *IP*

When rate exceeds:

- **Requests**: `5`
- **Period**: *1 minute*

## Challenge requests containing leaked credentials

Note

Access to the *User and Password Leaked* (`cf.waf.credential_check.username_and_password_leaked`) field requires a Pro plan or above.

[Create a custom rule](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/) that challenges requests containing a previously leaked set of credentials (username and password).

- **Expression**: If you use the Expression Builder, configure the following expression:

  | Field | Operator | Value |
  | --- | --- | --- |
  | User and Password Leaked | equals | True |

  If you use the Expression Editor, enter the following expression:

  ```txt
  (cf.waf.credential_check.username_and_password_leaked)
  ```


- **Action**: *Managed Challenge*

---
