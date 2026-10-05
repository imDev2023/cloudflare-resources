---
description: Manage Artifacts namespaces, repositories, and repo-scoped tokens using Wrangler.
title: Artifacts
image: https://developers.cloudflare.com/workers/wrangler/commands/artifacts/og.png?v=6748fe79cedf9f1b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/workers/llms.txt  
> Use this file to discover all available pages before exploring further.

# Artifacts

Last updated May 18, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/workers/wrangler/commands/artifacts/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Manage [Artifacts](https://developers.cloudflare.com/artifacts/) namespaces, repositories, and repo-scoped tokens using Wrangler. Private beta

## `artifacts namespaces list`

List Artifacts namespaces

npmyarnpnpm

```
npx wrangler artifacts namespaces list
```

```
yarn wrangler artifacts namespaces list
```

```
pnpm wrangler artifacts namespaces list
```

- `--json` `boolean` default: false

  Return output as JSON

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

## `artifacts namespaces get`

Get an Artifacts namespace

npmyarnpnpm

```
npx wrangler artifacts namespaces get <NAME>
```

```
yarn wrangler artifacts namespaces get <NAME>
```

```
pnpm wrangler artifacts namespaces get <NAME>
```

- `<NAME>` `string` required

  The Artifacts namespace name
- `--json` `boolean` default: false

  Return output as JSON

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

## `artifacts repos create`

Create an Artifacts repository

npmyarnpnpm

```
npx wrangler artifacts repos create <NAME>
```

```
yarn wrangler artifacts repos create <NAME>
```

```
pnpm wrangler artifacts repos create <NAME>
```

- `<NAME>` `string` required

  The Artifacts repository name
- `--namespace` `string` required

  The Artifacts namespace name
- `--description` `string` An optional description for the repository
- `--default-branch` `string` The default branch for the repository
- `--read-only` `boolean` Create the repository as read-only
- `--json` `boolean` default: false

  Return output as JSON

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

## `artifacts repos list`

List Artifacts repositories in a namespace

npmyarnpnpm

```
npx wrangler artifacts repos list
```

```
yarn wrangler artifacts repos list
```

```
pnpm wrangler artifacts repos list
```

- `--namespace` `string` required

  The Artifacts namespace name
- `--json` `boolean` default: false

  Return output as JSON

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

## `artifacts repos get`

Get an Artifacts repository

npmyarnpnpm

```
npx wrangler artifacts repos get <NAME>
```

```
yarn wrangler artifacts repos get <NAME>
```

```
pnpm wrangler artifacts repos get <NAME>
```

- `<NAME>` `string` required

  The Artifacts repository name
- `--namespace` `string` required

  The Artifacts namespace name
- `--json` `boolean` default: false

  Return output as JSON

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

## `artifacts repos delete`

Delete an Artifacts repository

npmyarnpnpm

```
npx wrangler artifacts repos delete <NAME>
```

```
yarn wrangler artifacts repos delete <NAME>
```

```
pnpm wrangler artifacts repos delete <NAME>
```

- `<NAME>` `string` required

  The Artifacts repository name
- `--namespace` `string` required

  The Artifacts namespace name
- `--force` `boolean` alias: --ydefault: false

  Skip confirmation
- `--json` `boolean` default: false

  Return output as JSON

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

## `artifacts repos issue-token`

Issue a repo-scoped Artifacts token

npmyarnpnpm

```
npx wrangler artifacts repos issue-token <REPO>
```

```
yarn wrangler artifacts repos issue-token <REPO>
```

```
pnpm wrangler artifacts repos issue-token <REPO>
```

- `<REPO>` `string` required

  The Artifacts repository name
- `--namespace` `string` required

  The Artifacts namespace name
- `--scope` `string` The token scope
- `--ttl` `number` The token TTL in seconds
- `--json` `boolean` default: false

  Return output as JSON

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
