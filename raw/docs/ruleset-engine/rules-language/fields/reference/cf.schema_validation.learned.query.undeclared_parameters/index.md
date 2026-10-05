---
description: Names of query parameters detected in the request but [not declared in the learned schema](/waf/detections/application-profiles/fields/#undeclared-query-parameters).
title: cf.schema_validation.learned.query.undeclared_parameters
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.schema\_validation.learned.query.undeclared\_parameters

`cf.schema_validation.learned.query.undeclared_parameters``Array<String>`

Names of query parameters detected in the request but [not declared in the learned schema](https://developers.cloudflare.com/waf/detections/application-profiles/fields/#undeclared-query-parameters).

Query parameter names are URL-decoded.

Example value:

```txt
["utm"]
```

Example usage:

```txt
any(cf.schema_validation.learned.query.undeclared_parameters[*] == "utm")
```

Categories:
- Request
