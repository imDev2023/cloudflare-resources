---
description: Ensure Artifacts stores and processes repo data only within a selected jurisdiction.
title: Data localization
image: https://developers.cloudflare.com/artifacts/guides/data-localization/og.png?v=c3960a5e5d71fe81
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/artifacts/llms.txt  
> Use this file to discover all available pages before exploring further.

# Data localization

Last updated Aug 13, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/artifacts/guides/data-localization/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Artifacts jurisdictions ensure repo data is stored and processed only within a selected location. Set a jurisdiction when you create a namespace to apply the restriction to every repo in that namespace.

## Supported jurisdictions

Artifacts supports the following jurisdictions:

| Jurisdiction | Location |
| --- | --- |
| `eu` | European Union |
| `us` | United States |

## Create a namespace with a jurisdiction

To restrict a namespace to the European Union, set `jurisdiction` to `eu` when you create the namespace:

```bash
curl --request POST \
  "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/artifacts/namespaces" \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "namespace": "my-eu-namespace",
    "jurisdiction": "eu"
  }'
```

The selected jurisdiction applies to every repo in the namespace. You cannot change the jurisdiction after creating the namespace. The `jurisdiction` parameter is optional. If you omit it, the namespace remains unrestricted.

For endpoint details, refer to the [Artifacts REST API reference](https://developers.cloudflare.com/artifacts/api/rest-api/#create-a-namespace).
