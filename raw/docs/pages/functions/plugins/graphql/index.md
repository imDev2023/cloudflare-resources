---
description: Set up a GraphQL server on Cloudflare Pages using the GraphQL Pages Plugin.
title: GraphQL
image: https://developers.cloudflare.com/pages/functions/plugins/graphql/og.png?v=5c147cfc7e65c57a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/pages/llms.txt  
> Use this file to discover all available pages before exploring further.

# GraphQL

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/pages/functions/plugins/graphql/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The GraphQL Pages Plugin creates a GraphQL server which can respond to `application/json` and `application/graphql` `POST` requests. It responds with [the GraphQL Playground ↗︎](https://github.com/graphql/graphql-playground) for `GET` requests.

## Installation

npmyarnpnpmbun

```
npm i @cloudflare/pages-plugin-graphql
```

```
yarn add @cloudflare/pages-plugin-graphql
```

```
pnpm add @cloudflare/pages-plugin-graphql
```

```
bun add @cloudflare/pages-plugin-graphql
```

## Usage

```typescript
import graphQLPlugin from "@cloudflare/pages-plugin-graphql";
import {
	graphql,
	GraphQLSchema,
	GraphQLObjectType,
	GraphQLString,
} from "graphql";

const schema = new GraphQLSchema({
	query: new GraphQLObjectType({
		name: "RootQueryType",
		fields: {
			hello: {
				type: GraphQLString,
				resolve() {
					return "Hello, world!";
				},
			},
		},
	}),
});

export const onRequest: PagesFunction = graphQLPlugin({
	schema,
	graphql,
});
```

This Plugin only exposes a single route, so wherever it is mounted is wherever it will be available. In the above example, because it is mounted in `functions/graphql.ts`, the server will be available on `/graphql` of your Pages project.
