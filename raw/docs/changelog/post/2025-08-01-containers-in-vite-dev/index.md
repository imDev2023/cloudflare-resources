---
description: The Cloudflare Vite plugin now supports configuring Containers in your Worker
title: Develop locally with Containers and the Cloudflare Vite plugin
image: https://developers.cloudflare.com/changelog/post/2025-08-01-containers-in-vite-dev/og.png?v=2c34a9f64f8726f0
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 1, 2025

## Develop locally with Containers and the Cloudflare Vite plugin

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-01-containers-in-vite-dev/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now configure and run [Containers](https://developers.cloudflare.com/containers) alongside your [Worker](https://developers.cloudflare.com/workers) during local development when using the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/). Previously, you could only develop locally when using [Wrangler](https://developers.cloudflare.com/workers/wrangler/) as your local development server.

#### Configuration

You can simply configure your Worker and your Container(s) in your Wrangler configuration file:

```jsonc
{
  "name": "container-starter",
  "main": "src/index.js",
  "containers": [
    {
      "class_name": "MyContainer",
      "image": "./Dockerfile",
      "instances": 5
    }
  ],
  "durable_objects": {
    "bindings": [
      {
        "class_name": "MyContainer",
        "name": "MY_CONTAINER"
      }
    ]
  },
  "migrations": [
    {
      "new_sqlite_classes": [
        "MyContainer"
      ],
      "tag": "v1"
    }
  ],
}
```

```toml
name = "container-starter"
main = "src/index.js"

[[containers]]
class_name = "MyContainer"
image = "./Dockerfile"
instances = 5

[[durable_objects.bindings]]
class_name = "MyContainer"
name = "MY_CONTAINER"

[[migrations]]
new_sqlite_classes = [ "MyContainer" ]
tag = "v1"
```

#### Worker Code

Once your Worker and Containers are configured, you can access the Container instances from your Worker code:

```ts
import { Container, getContainer } from "@cloudflare/containers";

export class MyContainer extends Container {
  defaultPort = 4000; // Port the container is listening on
  sleepAfter = "10m"; // Stop the instance if requests not sent for 10 minutes
}

async fetch(request, env) {
  const { "session-id": sessionId } = await request.json();
  // Get the container instance for the given session ID
  const containerInstance = getContainer(env.MY_CONTAINER, sessionId)
  // Pass the request to the container instance on its default port
  return containerInstance.fetch(request);
}
```

#### Local development

To develop your Worker locally, start a local dev server by running

```sh
vite dev
```

in your terminal.

#### Resources

Learn more about [Cloudflare Containers ↗︎](https://developers.cloudflare.com/containers/) or the [Cloudflare Vite plugin ↗︎](https://developers.cloudflare.com/workers/vite-plugin/) in our developer docs.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-01-containers-in-vite-dev/#page","headline":"Develop locally with Containers and the Cloudflare Vite plugin","description":"The Cloudflare Vite plugin now supports configuring Containers in your Worker","url":"https://developers.cloudflare.com/changelog/post/2025-08-01-containers-in-vite-dev/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-01-containers-in-vite-dev/og.png?v=2c34a9f64f8726f0","dateModified":"2025-08-01","datePublished":"2025-08-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
