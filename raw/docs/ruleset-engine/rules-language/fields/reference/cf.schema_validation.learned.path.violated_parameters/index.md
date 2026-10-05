---
description: Names of path parameters detected as [violating the learned schema](/waf/detections/application-profiles/fields/#violated-parameters).
title: cf.schema_validation.learned.path.violated_parameters
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.schema\_validation.learned.path.violated\_parameters

`cf.schema_validation.learned.path.violated_parameters``Array<String>`

Names of path parameters detected as [violating the learned schema](https://developers.cloudflare.com/waf/detections/application-profiles/fields/#violated-parameters).

Example value:

```txt
["accountId"]
```

Example usage:

```txt
any(cf.schema_validation.learned.path.violated_parameters[*] == "accountId")
```

Categories:
- Request
