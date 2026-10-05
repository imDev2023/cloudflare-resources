---
description: Opt in to encrypt Wrangler's OAuth tokens at rest using a key held in macOS Keychain, libsecret, or Windows Credential Manager.
title: Store Wrangler's OAuth credentials in your OS keychain
image: https://developers.cloudflare.com/changelog/post/2026-06-03-wrangler-keyring-credential-storage/og.png?v=7bdd8111854607a1
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 3, 2026

## Store Wrangler's OAuth credentials in your OS keychain

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-03-wrangler-keyring-credential-storage/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Wrangler](https://developers.cloudflare.com/workers/wrangler/) can now store the OAuth credentials returned by `wrangler login` in an [AES-256-GCM ↗︎](https://en.wikipedia.org/wiki/Galois/Counter_Mode)-encrypted file, with the encryption key held in your operating system keychain. The default behavior is unchanged — credentials still live in a plaintext TOML file unless you opt in.

To opt in, run:

```sh
npx wrangler login --use-keyring
```

The choice is persisted across Wrangler invocations. Opt back out with `npx wrangler login --no-use-keyring`, or override the preference for a single command with the `CLOUDFLARE_AUTH_USE_KEYRING` environment variable.

`wrangler whoami` now reports where credentials are stored:

```sh
🔐 Credentials are stored in: Encrypted file (~/.config/.wrangler/config/default.enc) with key in macOS Keychain (service=wrangler, account=default)
```

Per-platform backends:

- **macOS** uses the built-in Keychain via `/usr/bin/security`.
- **Linux** uses [libsecret ↗︎](https://wiki.gnome.org/Projects/Libsecret) via the `secret-tool` CLI from the `libsecret-tools` package.
- **Windows** uses Credential Manager via [`@napi-rs/keyring` ↗︎](https://www.npmjs.com/package/@napi-rs/keyring), installed on-demand the first time you opt in.

Refer to [Storing OAuth credentials in the OS keychain](https://developers.cloudflare.com/workers/wrangler/commands/general/#storing-oauth-credentials-in-the-os-keychain) for the full details, including the migration behavior on opt-in/opt-out and the `CLOUDFLARE_AUTH_USE_KEYRING` environment variable.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-03-wrangler-keyring-credential-storage/#page","headline":"Store Wrangler's OAuth credentials in your OS keychain","description":"Opt in to encrypt Wrangler's OAuth tokens at rest using a key held in macOS Keychain, libsecret, or Windows Credential Manager.","url":"https://developers.cloudflare.com/changelog/post/2026-06-03-wrangler-keyring-credential-storage/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-03-wrangler-keyring-credential-storage/og.png?v=7bdd8111854607a1","dateModified":"2026-06-03","datePublished":"2026-06-03","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
