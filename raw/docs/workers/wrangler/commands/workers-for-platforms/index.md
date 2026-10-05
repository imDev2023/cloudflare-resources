---
description: Wrangler commands for managing Workers for Platforms dispatch namespaces.
title: Workers for Platforms
image: https://developers.cloudflare.com/workers/wrangler/commands/workers-for-platforms/og.png?v=71d2e50bea2db143
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/workers/llms.txt  
> Use this file to discover all available pages before exploring further.

# Workers for Platforms

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/workers/wrangler/commands/workers-for-platforms/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Wrangler commands for managing Workers for Platforms [dispatch namespace](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dispatch-namespace) using Wrangler.

## `dispatch-namespace list`

List all dispatch namespaces

npmyarnpnpm

```
npx wrangler dispatch-namespace list
```

```
yarn wrangler dispatch-namespace list
```

```
pnpm wrangler dispatch-namespace list
```

<details>

<summary>

Global flags

</summary>

- <code>--v</code><code>boolean</code> alias: --version

  Show version number
- <code>--cwd</code><code>string</code>Run as if Wrangler was started in the specified directory instead of the current working directory
- <code>--config</code><code>string</code> alias: --c

  Path to Wrangler configuration file
- <code>--env</code><code>string</code> alias: --e

  Environment to use for operations, and for selecting .env and .dev.vars files
- <code>--env-file</code><code>string</code>Path to an .env file to load - can be specified multiple times - values from earlier files are overridden by values in later files
- <code>--install-skills</code><code>boolean</code> default: false

  Install Cloudflare skills for detected AI coding agents before running the command
- <code>--profile</code><code>string</code>Use a specific auth profile

</details>

## `dispatch-namespace get`

Get information about a dispatch namespace

npmyarnpnpm

```
npx wrangler dispatch-namespace get <NAME>
```

```
yarn wrangler dispatch-namespace get <NAME>
```

```
pnpm wrangler dispatch-namespace get <NAME>
```

- `<NAME>` `string` required

  Name of the dispatch namespace

<details>

<summary>

Global flags

</summary>

- <code>--v</code><code>boolean</code> alias: --version

  Show version number
- <code>--cwd</code><code>string</code>Run as if Wrangler was started in the specified directory instead of the current working directory
- <code>--config</code><code>string</code> alias: --c

  Path to Wrangler configuration file
- <code>--env</code><code>string</code> alias: --e

  Environment to use for operations, and for selecting .env and .dev.vars files
- <code>--env-file</code><code>string</code>Path to an .env file to load - can be specified multiple times - values from earlier files are overridden by values in later files
- <code>--install-skills</code><code>boolean</code> default: false

  Install Cloudflare skills for detected AI coding agents before running the command
- <code>--profile</code><code>string</code>Use a specific auth profile

</details>

## `dispatch-namespace create`

Create a dispatch namespace

npmyarnpnpm

```
npx wrangler dispatch-namespace create <NAME>
```

```
yarn wrangler dispatch-namespace create <NAME>
```

```
pnpm wrangler dispatch-namespace create <NAME>
```

- `<NAME>` `string` required

  Name of the dispatch namespace

<details>

<summary>

Global flags

</summary>

- <code>--v</code><code>boolean</code> alias: --version

  Show version number
- <code>--cwd</code><code>string</code>Run as if Wrangler was started in the specified directory instead of the current working directory
- <code>--config</code><code>string</code> alias: --c

  Path to Wrangler configuration file
- <code>--env</code><code>string</code> alias: --e

  Environment to use for operations, and for selecting .env and .dev.vars files
- <code>--env-file</code><code>string</code>Path to an .env file to load - can be specified multiple times - values from earlier files are overridden by values in later files
- <code>--install-skills</code><code>boolean</code> default: false

  Install Cloudflare skills for detected AI coding agents before running the command
- <code>--profile</code><code>string</code>Use a specific auth profile

</details>

## `dispatch-namespace delete`

Delete a dispatch namespace

npmyarnpnpm

```
npx wrangler dispatch-namespace delete <NAME>
```

```
yarn wrangler dispatch-namespace delete <NAME>
```

```
pnpm wrangler dispatch-namespace delete <NAME>
```

- `<NAME>` `string` required

  Name of the dispatch namespace

<details>

<summary>

Global flags

</summary>

- <code>--v</code><code>boolean</code> alias: --version

  Show version number
- <code>--cwd</code><code>string</code>Run as if Wrangler was started in the specified directory instead of the current working directory
- <code>--config</code><code>string</code> alias: --c

  Path to Wrangler configuration file
- <code>--env</code><code>string</code> alias: --e

  Environment to use for operations, and for selecting .env and .dev.vars files
- <code>--env-file</code><code>string</code>Path to an .env file to load - can be specified multiple times - values from earlier files are overridden by values in later files
- <code>--install-skills</code><code>boolean</code> default: false

  Install Cloudflare skills for detected AI coding agents before running the command
- <code>--profile</code><code>string</code>Use a specific auth profile

</details>

Note

You must delete all user Workers in the dispatch namespace before it can be deleted.

## `dispatch-namespace rename`

Rename a dispatch namespace

npmyarnpnpm

```
npx wrangler dispatch-namespace rename <OLDNAME> <NEWNAME>
```

```
yarn wrangler dispatch-namespace rename <OLDNAME> <NEWNAME>
```

```
pnpm wrangler dispatch-namespace rename <OLDNAME> <NEWNAME>
```

- `<OLDNAME>` `string` required

  Name of the dispatch namespace
- `<NEWNAME>` `string` required

  New name of the dispatch namespace

<details>

<summary>

Global flags

</summary>

- <code>--v</code><code>boolean</code> alias: --version

  Show version number
- <code>--cwd</code><code>string</code>Run as if Wrangler was started in the specified directory instead of the current working directory
- <code>--config</code><code>string</code> alias: --c

  Path to Wrangler configuration file
- <code>--env</code><code>string</code> alias: --e

  Environment to use for operations, and for selecting .env and .dev.vars files
- <code>--env-file</code><code>string</code>Path to an .env file to load - can be specified multiple times - values from earlier files are overridden by values in later files
- <code>--install-skills</code><code>boolean</code> default: false

  Install Cloudflare skills for detected AI coding agents before running the command
- <code>--profile</code><code>string</code>Use a specific auth profile

</details>
