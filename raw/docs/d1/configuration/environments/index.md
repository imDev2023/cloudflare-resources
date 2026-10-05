---
description: Configure separate D1 databases for staging and production Wrangler environments.
title: Environments
image: https://developers.cloudflare.com/d1/configuration/environments/og.png?v=c0cb3fe5fbb0bbde
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/d1/llms.txt  
> Use this file to discover all available pages before exploring further.

# Environments

Last updated Sep 17, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/d1/configuration/environments/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Environments](https://developers.cloudflare.com/workers/wrangler/environments/) are different contexts that your code runs in. Cloudflare Developer Platform allows you to create and manage different environments. Through environments, you can deploy the same project to multiple places under multiple names.

To specify different D1 databases for different environments, use the following syntax in your Wrangler file:

```jsonc
{
	"env": {
		// This is a staging environment
		"staging": {
			"d1_databases": [
				{
					"binding": "<BINDING_NAME_1>",
					"database_name": "<DATABASE_NAME_1>",
					"database_id": "<UUID1>"
				}
			]
		},
		// This is a production environment
		"production": {
			"d1_databases": [
				{
					"binding": "<BINDING_NAME_2>",
					"database_name": "<DATABASE_NAME_2>",
					"database_id": "<UUID2>"
				}
			]
		}
	}
}
```

```toml
[[env.staging.d1_databases]]
binding = "<BINDING_NAME_1>"
database_name = "<DATABASE_NAME_1>"
database_id = "<UUID1>"

[[env.production.d1_databases]]
binding = "<BINDING_NAME_2>"
database_name = "<DATABASE_NAME_2>"
database_id = "<UUID2>"
```

In the code above, the `staging` environment is using a different database (`DATABASE_NAME_1`) than the `production` environment (`DATABASE_NAME_2`).

## Anatomy of Wrangler file

If you need to specify different D1 databases for different environments, your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) may contain bindings that resemble the following:

```jsonc
{
	"env": {
		"production": {
			"d1_databases": [
				{
					"binding": "DB",
					"database_name": "DATABASE_NAME",
					"database_id": "DATABASE_ID"
				}
			]
		}
	}
}
```

```toml
[[env.production.d1_databases]]
binding = "DB"
database_name = "DATABASE_NAME"
database_id = "DATABASE_ID"
```

In the above configuration:

- `[[env.production.d1_databases]]` creates an object `production` under `env` with a property `d1_databases`, where `d1_databases` is an array of objects, since you can create multiple D1 bindings in case you have more than one database.
- Any property below the line in the form `<key> = <value>` is a property of an object within the `d1_databases` array.

Therefore, the above binding is equivalent to:

```json
{
  "env": {
    "production": {
      "d1_databases": [
        {
          "binding": "DB",
          "database_name": "DATABASE_NAME",
          "database_id": "DATABASE_ID"
        }
      ]
    }
  }
}
```

### Example

```jsonc
{
	"env": {
		"staging": {
			"d1_databases": [
				{
					"binding": "BINDING_NAME_1",
					"database_name": "DATABASE_NAME_1",
					"database_id": "UUID_1"
				}
			]
		},
		"production": {
			"d1_databases": [
				{
					"binding": "BINDING_NAME_2",
					"database_name": "DATABASE_NAME_2",
					"database_id": "UUID_2"
				}
			]
		}
	}
}
```

```toml
[[env.staging.d1_databases]]
binding = "BINDING_NAME_1"
database_name = "DATABASE_NAME_1"
database_id = "UUID_1"

[[env.production.d1_databases]]
binding = "BINDING_NAME_2"
database_name = "DATABASE_NAME_2"
database_id = "UUID_2"
```

The above is equivalent to the following structure in JSON:

```json
{
  "env": {
    "production": {
      "d1_databases": [
        {
          "binding": "BINDING_NAME_2",
          "database_id": "UUID_2",
          "database_name": "DATABASE_NAME_2"
        }
      ]
    },
    "staging": {
      "d1_databases": [
        {
          "binding": "BINDING_NAME_1",
          "database_id": "UUID_1",
          "database_name": "DATABASE_NAME_1"
        }
      ]
    }
  }
}
```
