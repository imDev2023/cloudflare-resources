---
description: Validate Stytch session tokens in Pages Functions using the Stytch Pages Plugin.
title: Stytch
image: https://developers.cloudflare.com/pages/functions/plugins/stytch/og.png?v=52b92c2a4a97432b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/pages/llms.txt  
> Use this file to discover all available pages before exploring further.

# Stytch

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/pages/functions/plugins/stytch/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The Stytch Pages Plugin is a middleware which validates all requests and their `session_token`.

## Installation

npmyarnpnpmbun

```
npm i @cloudflare/pages-plugin-stytch
```

```
yarn add @cloudflare/pages-plugin-stytch
```

```
pnpm add @cloudflare/pages-plugin-stytch
```

```
bun add @cloudflare/pages-plugin-stytch
```

## Usage

```typescript
import stytchPlugin from "@cloudflare/pages-plugin-stytch";
import { envs } from "@cloudflare/pages-plugin-stytch/api";

export const onRequest: PagesFunction = stytchPlugin({
	project_id: "YOUR_STYTCH_PROJECT_ID",
	secret: "YOUR_STYTCH_PROJECT_SECRET",
	env: envs.live,
});
```

We recommend storing your secret in KV rather than in plain text as above.

The Stytch Plugin takes a single argument, an object with several properties. `project_id` and `secret` are mandatory strings and can be found in [Stytch's dashboard ↗︎](https://stytch.com/dashboard/api-keys). `env` is also a mandatory string, and can be populated with the `envs.test` or `envs.live` variables in the API. By default, the Plugin validates a `session_token` cookie of the incoming request, but you can also optionally pass in a `session_token` or `session_jwt` string yourself if you are using some other mechanism to identify user sessions. Finally, you can also pass in a `session_duration_minutes` in order to extend the lifetime of the session. More information on these parameters can be found in [Stytch's documentation ↗︎](https://stytch.com/docs/api/session-auth).

The validated session response containing user information is made available to subsequent Pages Functions on `data.stytch.session`.
