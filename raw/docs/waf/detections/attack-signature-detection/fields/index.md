---
description: Reference Attack Signature Detection fields, example values, Security Rules usage, and Logpush mappings.
title: Fields
image: https://developers.cloudflare.com/waf/detections/attack-signature-detection/fields/og.png?v=c2d4bb2067552e8e
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/waf/llms.txt  
> Use this file to discover all available pages before exploring further.

# Fields

Last updated Sep 8, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/waf/detections/attack-signature-detection/fields/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Attack Signature Detection populates these request fields when signatures match:

| Field | Type | Meaning |
| --- | --- | --- |
| `cf.waf.signature.request.categories` | `Array<String>` | Categories associated with all matching signatures. A signature can have more than one category. |
| `cf.waf.signature.request.confidence` | `Array<String>` | Confidence values associated with matching signatures. Supported values are `high` and `low`. |
| `cf.waf.signature.request.refs` | `Array<String>` | Refs for matching signatures, up to 10 per request. Each Ref matches the corresponding Managed Rule public Rule ID. |

Note

Attack Signature Detection is available in Early Access. Contact your Cloudflare account team to request access.

All three fields are available in Security Analytics and Security Rules. You can reference them in rules created in the dashboard or through the API.

## Example values

The fields can contain values like these:

| Field | Example value |
| --- | --- |
| `cf.waf.signature.request.categories` | `["sqli", "cve-2025-55182"]` |
| `cf.waf.signature.request.confidence` | `["high"]` |
| `cf.waf.signature.request.refs` | `["d68f8101f6e14e25aefcaea69c530a29"]` |

## Rules language examples

Use `any()` to test array elements:

```txt
any(cf.waf.signature.request.categories[*] eq "sqli")
```

```txt
any(cf.waf.signature.request.confidence[*] eq "high")
```

```txt
any(cf.waf.signature.request.refs[*] eq "d68f8101f6e14e25aefcaea69c530a29")
```

For rollout guidance, refer to [Use attack signatures in Security Rules](https://developers.cloudflare.com/waf/detections/attack-signature-detection/use-attack-signatures-in-security-rules/).

## Logpush fields

Signature Refs and categories are available in Logpush:

| Rules field | Logpush field |
| --- | --- |
| `cf.waf.signature.request.refs` | [`wafRequestSignatureRefs`](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/http_requests/#wafrequestsignaturerefs) |
| `cf.waf.signature.request.categories` | [`wafRequestSignatureCategories`](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/http_requests/#wafrequestsignaturecategories) |

Only signature Ref and category mappings are available in Logpush.
