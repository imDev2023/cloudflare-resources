---
description: Wrangler now guides you through deploying static assets with interactive prompts and automatic configuration generation when no wrangler.jsonc file exists.
title: Deploy static sites to Workers without a configuration file
image: https://developers.cloudflare.com/changelog/post/2025-09-09-interactive-wrangler-assets/og.png?v=95b5860877ac2471
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 9, 2025

## Deploy static sites to Workers without a configuration file

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-09-interactive-wrangler-assets/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Deploying static site to Workers is now easier. When you run `wrangler deploy [directory]` or `wrangler deploy --assets [directory]` without an existing [configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/), [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/) now guides you through the deployment process with interactive prompts.

#### Before and after

**Before:** Required remembering multiple flags and parameters

```bash
wrangler deploy --assets ./dist --compatibility-date 2025-09-09 --name my-project
```

**After:** Simple directory deployment with guided setup

```bash
wrangler deploy dist
# Interactive prompts handle the rest as shown in the example flow below
```

#### What's new

**Interactive prompts for missing configuration:**

- Wrangler detects when you're trying to deploy a directory of static assets
- Prompts you to confirm the deployment type
- Asks for a project name (with smart defaults)
- Automatically sets the compatibility date to today

**Automatic configuration generation:**

- Creates a `wrangler.jsonc` file with your deployment settings
- Stores your choices for future deployments
- Eliminates the need to remember complex command-line flags

#### Example workflow

```bash
# Deploy your built static site
wrangler deploy dist

# Wrangler will prompt:
✔ It looks like you are trying to deploy a directory of static assets only. Is this correct? … yes
✔ What do you want to name your project? … my-astro-site

# Automatically generates a wrangler.jsonc file and adds it to your project:
{
  "name": "my-astro-site",
  "compatibility_date": "2025-09-09",
  "assets": {
    "directory": "dist"
  }
}

# Next time you run wrangler deploy, this will use the configuration in your newly generated wrangler.jsonc file
wrangler deploy
```

#### Requirements

- You must use Wrangler version 4.24.4 or later in order to use this feature

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-09-interactive-wrangler-assets/#page","headline":"Deploy static sites to Workers without a configuration file","description":"Wrangler now guides you through deploying static assets with interactive prompts and automatic configuration generation when no wrangler.jsonc file exists.","url":"https://developers.cloudflare.com/changelog/post/2025-09-09-interactive-wrangler-assets/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-09-interactive-wrangler-assets/og.png?v=95b5860877ac2471","dateModified":"2025-09-09","datePublished":"2025-09-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
