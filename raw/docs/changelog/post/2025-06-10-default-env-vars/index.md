---
description: Workers Builds now automatically injects environment variables containingGit metadata, including the commit SHA and branch name.
title: Access git commit sha and branch name as environment variables in Workers Builds
image: https://developers.cloudflare.com/changelog/post/2025-06-10-default-env-vars/og.png?v=b3f988c407c2ddcb
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 10, 2025

## Access git commit sha and branch name as environment variables in Workers Builds

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-10-default-env-vars/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/) connects your Worker to a [Git repository](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/), and automates building and deploying your code on each pushed change.

To make CI/CD pipelines even more flexible, Workers Builds now automatically injects [default environment variables](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/#environment-variables) into your build process (much like the defaults in [Cloudflare Pages projects](https://developers.cloudflare.com/pages/configuration/build-configuration/#environment-variables)). You can use these variables to customize your build process based on the deployment context, such as the branch or commit.

The following environment variables are injected by default:

| Environment Variable | Injected value | Example use-case |
| --- | --- | --- |
| `CI` | `true` | Changing build behavior when run on CI versus locally |
| `WORKERS_CI` | `1` | Changing build behavior when run on Workers Builds versus locally |
| `WORKERS_CI_BUILD_UUID` | `<build-uuid-of-current-build>` | Passing the Build UUID along to custom workflows |
| `WORKERS_CI_COMMIT_SHA` | `<sha1-hash-of-current-commit>` | Passing current commit ID to error reporting, for example, Sentry |
| `WORKERS_CI_BRANCH` | `<branch-name-from-push-event` | Customizing build based on branch, for example, disabling debug logging on `production` |

You can override these default values and add your own custom environment variables by navigating to **your Worker** > **Settings** > **Environment variables**.

Learn more in the [Build configuration documentation](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/#environment-variables).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-10-default-env-vars/#page","headline":"Access git commit sha and branch name as environment variables in Workers Builds","description":"Workers Builds now automatically injects environment variables containingGit metadata, including the commit SHA and branch name.","url":"https://developers.cloudflare.com/changelog/post/2025-06-10-default-env-vars/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-06-10-default-env-vars/og.png?v=b3f988c407c2ddcb","dateModified":"2025-06-10","datePublished":"2025-06-10","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
