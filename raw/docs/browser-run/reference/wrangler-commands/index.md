---
description: Manage Browser Run sessions from the command line using Wrangler.
title: Wrangler commands
image: https://developers.cloudflare.com/browser-run/reference/wrangler-commands/og.png?v=15281df5b45b166f
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/browser-run/llms.txt  
> Use this file to discover all available pages before exploring further.

# Wrangler commands

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/browser-run/reference/wrangler-commands/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Use `wrangler browser` commands to manage Browser Run sessions from the command line.

## `browser create`

Create a new Browser Run session

npmyarnpnpm

```
npx wrangler browser create
```

```
yarn wrangler browser create
```

```
pnpm wrangler browser create
```

- `--lab` `boolean` default: false

  Enable lab browser session with experimental Chrome features (e.g., WebMCP)
- `--keepAlive` `number` alias: --k

  Keep-alive duration in seconds (60-600)
- `--json` `boolean` default: false

  Return session info as JSON
- `--open` `boolean` Open DevTools in browser (default: true in interactive mode)

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

## `browser close`

Close a Browser Run session

npmyarnpnpm

```
npx wrangler browser close <SESSIONID>
```

```
yarn wrangler browser close <SESSIONID>
```

```
pnpm wrangler browser close <SESSIONID>
```

- `<SESSIONID>` `string` required

  The session ID to close
- `--json` `boolean` default: false

  Return result as JSON

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

## `browser list`

List active Browser Run sessions

npmyarnpnpm

```
npx wrangler browser list
```

```
yarn wrangler browser list
```

```
pnpm wrangler browser list
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

## `browser view`

View a live browser session

npmyarnpnpm

```
npx wrangler browser view [SESSIONID]
```

```
yarn wrangler browser view [SESSIONID]
```

```
pnpm wrangler browser view [SESSIONID]
```

- `[SESSIONID]` `string` The session ID to inspect (optional if only one session exists)
- `--target` `string` Target selector (matches id exactly, or url/title by substring)
- `--json` `boolean` default: false

  Return live browser session URL(s) as JSON
- `--open` `boolean` Open in browser (default: true in interactive mode)

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
