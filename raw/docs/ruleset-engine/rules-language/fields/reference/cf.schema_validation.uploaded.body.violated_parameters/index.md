---
description: The JSON path of a detected request body [violation of the uploaded schema](/waf/detections/application-profiles/fields/#violated-parameters).
title: cf.schema_validation.uploaded.body.violated_parameters
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.schema\_validation.uploaded.body.violated\_parameters

`cf.schema_validation.uploaded.body.violated_parameters``Array<String>`

The JSON path of a detected request body [violation of the uploaded schema](https://developers.cloudflare.com/waf/detections/application-profiles/fields/#violated-parameters).

Body validation reports the first detected violation. A value of `$` identifies the body without a more specific path.

Example value:

```txt
["$"]
```

Example usage:

```txt
any(cf.schema_validation.uploaded.body.violated_parameters[*] == "$")
```

Categories:
- Request
