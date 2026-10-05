---
description: The JSON path of a detected request body [violation of the learned schema](/waf/detections/application-profiles/fields/#violated-parameters).
title: cf.schema_validation.learned.body.violated_parameters
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.schema\_validation.learned.body.violated\_parameters

`cf.schema_validation.learned.body.violated_parameters``Array<String>`

The JSON path of a detected request body [violation of the learned schema](https://developers.cloudflare.com/waf/detections/application-profiles/fields/#violated-parameters).

Body validation reports the first detected violation. A value of `$` identifies the body without a more specific path.

Example value:

```txt
["$"]
```

Categories:
- Request
