---
description: Wrangler now supports the CLOUDFLARE_ENV environment variable to select the active environment without using the --env flag.
title: Select Wrangler environments using the CLOUDFLARE_ENV environment variable
image: https://developers.cloudflare.com/changelog/post/2025-11-09-cloudflare-env-variable/og.png?v=a53c81fd3148bea8
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 9, 2025

## Select Wrangler environments using the CLOUDFLARE\_ENV environment variable

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-09-cloudflare-env-variable/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Wrangler now supports using the `CLOUDFLARE_ENV` [environment variable](https://developers.cloudflare.com/workers/wrangler/system-environment-variables/#supported-environment-variables) to select the active [environment](https://developers.cloudflare.com/workers/wrangler/environments/) for your Worker commands. This provides a more flexible way to manage environments, especially when working with build tools and CI/CD pipelines.

#### What's new

**Environment selection via environment variable:**

- Set `CLOUDFLARE_ENV` to specify which environment to use for Wrangler commands
- Works with all Wrangler commands that support the `--env` flag
- The `--env` command line argument takes precedence over the `CLOUDFLARE_ENV` environment variable

#### Example usage

```bash
# Deploy to the production environment using CLOUDFLARE_ENV
CLOUDFLARE_ENV=production wrangler deploy

# Upload a version to the staging environment
CLOUDFLARE_ENV=staging wrangler versions upload

# The --env flag takes precedence over CLOUDFLARE_ENV
CLOUDFLARE_ENV=dev wrangler deploy --env production
# This will deploy to production, not dev
```

#### Use with build tools

The `CLOUDFLARE_ENV` environment variable is particularly useful when working with build tools like Vite. You can set the environment once during the build process, and it will be used for both building and deploying your Worker:

```bash
# Set the environment for both build and deploy
CLOUDFLARE_ENV=production npm run build & wrangler deploy
```

When using `@cloudflare/vite-plugin`, the build process generates a ["redirected deploy config"](https://developers.cloudflare.com/workers/wrangler/configuration/#generated-wrangler-configuration) that is flattened to only contain the active environment. Wrangler will validate that the environment specified matches the environment used during the build to prevent accidentally deploying a Worker built for one environment to a different environment.

#### Learn more

- [System environment variables](https://developers.cloudflare.com/workers/wrangler/system-environment-variables/)
- [Environments](https://developers.cloudflare.com/workers/wrangler/environments/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-09-cloudflare-env-variable/#page","headline":"Select Wrangler environments using the CLOUDFLARE_ENV environment variable","description":"Wrangler now supports the CLOUDFLARE_ENV environment variable to select the active environment without using the --env flag.","url":"https://developers.cloudflare.com/changelog/post/2025-11-09-cloudflare-env-variable/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-09-cloudflare-env-variable/og.png?v=a53c81fd3148bea8","dateModified":"2025-11-09","datePublished":"2025-11-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
