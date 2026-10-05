---
description: Use a Worker to add configurable delays to requests with low bot scores.
title: Delay action
image: https://developers.cloudflare.com/bots/workers-templates/delay-action/og.png?v=c990697ddea61b7b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/bots/llms.txt  
> Use this file to discover all available pages before exploring further.

# Delay action

Last updated May 5, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/bots/workers-templates/delay-action/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Customers with a Bot Management and a [Workers](https://developers.cloudflare.com/workers/) subscription can use the template below to introduce a delay to requests that are likely from bots.

The template sets a minimum and maximum delay, and delays requests where the bot score is less than 30 and the URI path starts with `/exampleURI`.

```js
// Configurable Variables
const PATH_START = "/exampleURI";
const DELAY_FROM = 5; // in seconds
const DELAY_TO = 10; // in seconds

export default {
	async fetch(request, env, ctx) {
		const url = new URL(request.url);
		const botScore = request.cf.botManagement.score;

		if (url.pathname.startsWith(PATH_START) && botScore < 30) {
			// Random delay between DELAY_FROM and DELAY_TO seconds
			const delay =
				Math.floor(Math.random() * (DELAY_TO - DELAY_FROM + 1)) + DELAY_FROM;
			await new Promise((resolve) => setTimeout(resolve, delay * 1000));

			// Fetch the original request
			return fetch(request);
		}

		// Fetch the original request without delay
		return fetch(request);
	},
};
```

*Workers templatets*

```ts
// Configurable Variables
const PATH_START = '/exampleURI';
const DELAY_FROM = 5; // in seconds
const DELAY_TO = 10; // in seconds

export default {
  async fetch(request, env, ctx): Promise<Response> {
    const url = new URL(request.url);
    const botScore = request.cf.botManagement.score

    if (url.pathname.startsWith(PATH_START) && botScore < 30) {
      // Random delay between DELAY_FROM and DELAY_TO seconds
      const delay = Math.floor(Math.random() * (DELAY_TO - DELAY_FROM + 1)) + DELAY_FROM;
      await new Promise(resolve => setTimeout(resolve, delay * 1000));

      // Fetch the original request
      return fetch(request);
    }

    // Fetch the original request without delay
    return fetch(request);
  },
} satisfies ExportedHandler<Env>;
```
