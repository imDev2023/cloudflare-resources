---
description: Contains the specific code for 1XXX Cloudflare errors.
title: cf.response.1xxx_code
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.response.1xxx\_code

`cf.response.1xxx_code``Integer`

Contains the specific code for 1XXX Cloudflare errors.

Use this field to differentiate between 1XXX errors associated with the same HTTP status code. The default value is `0`.

For a list of 1XXX errors, refer to [Troubleshooting Cloudflare 1XXX errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/).

**Note**: This field is only available in [Response Header Transform Rules](https://developers.cloudflare.com/rules/transform/response-header-modification/) and [Custom Errors](https://developers.cloudflare.com/rules/custom-errors/).

Example value:

```txt
1020
```

Categories:
- Response
