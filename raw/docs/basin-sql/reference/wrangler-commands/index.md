---
description: Wrangler commands for querying data with Basin SQL.
title: Wrangler commands
image: https://developers.cloudflare.com/basin-sql/reference/wrangler-commands/og.png?v=04f1cc0e595fd0ce
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/basin-sql/llms.txt  
> Use this file to discover all available pages before exploring further.

# Wrangler commands

Last updated Oct 1, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/basin-sql/reference/wrangler-commands/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Use the `basin sql` command family to query a warehouse:

npmyarnpnpm

```
npx wrangler basin sql query <WAREHOUSE_NAME> "SELECT * FROM <NAMESPACE>.<TABLE> LIMIT 10"
```

```
yarn wrangler basin sql query <WAREHOUSE_NAME> "SELECT * FROM <NAMESPACE>.<TABLE> LIMIT 10"
```

```
pnpm wrangler basin sql query <WAREHOUSE_NAME> "SELECT * FROM <NAMESPACE>.<TABLE> LIMIT 10"
```
