---
description: Maintain separate logins and switch between Cloudflare accounts per project, without re-running wrangler login.
title: Work across multiple accounts with Wrangler auth profiles
image: https://developers.cloudflare.com/changelog/post/2026-07-02-wrangler-auth-profiles/og.png?v=623f0328d7cc7d1a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 2, 2026

## Work across multiple accounts with Wrangler auth profiles

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-02-wrangler-auth-profiles/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/) now supports auth profiles: named logins that you scope to specific Cloudflare accounts and switch between automatically, based on the directory you are working in.

A profile is a named OAuth login bound to a directory. Commands run in that directory, and its subdirectories, use the matching account — so you can move between accounts without re-running `wrangler login`.

Use profiles to keep a separate login for each client when working at an agency, or to separate staging and production into different accounts. Pair a profile with an `account_id` in your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) so a command cannot reach the wrong account.

```sh
# Create a profile for each account, choosing which accounts it can reach
wrangler auth create client-a
wrangler auth activate client-a ~/clients/client-a

wrangler auth create client-b
wrangler auth activate client-b ~/clients/client-b
```

Use the `--profile` flag to run a single command with a specific profile:

```sh
wrangler deploy --profile personal
```

In CI and other automated environments, `CLOUDFLARE_API_TOKEN` still takes precedence over all profiles.

For setup, the resolution order, and the full command reference, refer to [Authentication profiles](https://developers.cloudflare.com/workers/wrangler/profiles/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-02-wrangler-auth-profiles/#page","headline":"Work across multiple accounts with Wrangler auth profiles","description":"Maintain separate logins and switch between Cloudflare accounts per project, without re-running wrangler login.","url":"https://developers.cloudflare.com/changelog/post/2026-07-02-wrangler-auth-profiles/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-02-wrangler-auth-profiles/og.png?v=623f0328d7cc7d1a","dateModified":"2026-07-02","datePublished":"2026-07-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
