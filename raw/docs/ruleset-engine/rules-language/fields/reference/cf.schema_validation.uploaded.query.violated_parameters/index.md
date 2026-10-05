---
description: Names of query parameters detected as [violating the uploaded schema](/waf/detections/application-profiles/fields/#violated-parameters).
title: cf.schema_validation.uploaded.query.violated_parameters
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.schema\_validation.uploaded.query.violated\_parameters

`cf.schema_validation.uploaded.query.violated_parameters``Array<String>`

Names of query parameters detected as [violating the uploaded schema](https://developers.cloudflare.com/waf/detections/application-profiles/fields/#violated-parameters).

Example value:

```txt
["bookingId"]
```

Example usage:

```txt
any(cf.schema_validation.uploaded.query.violated_parameters[*] == "bookingId")
```

Categories:
- Request
