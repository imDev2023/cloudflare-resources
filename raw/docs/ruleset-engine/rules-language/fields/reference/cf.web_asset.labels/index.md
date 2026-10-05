---
description: An array of labels associated with the operation matched by the request.
title: cf.web_asset.labels
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.web\_asset.labels

`cf.web_asset.labels``Array<String>`

An array of labels associated with the operation matched by the request.

Use this field to create rules based on labels applied to operations in Web Assets, including API endpoints. For more information, refer to [Label operations](https://developers.cloudflare.com/security/web-assets/label-operations/).

Example value:

```txt
["cf-log-in"]
```

Example usage:

```txt
any(cf.web_asset.labels[*] == "cf-log-in")
```

Categories:
- Request
