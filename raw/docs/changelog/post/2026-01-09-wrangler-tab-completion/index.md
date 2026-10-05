---
description: Wrangler now supports shell tab completions for Bash, Zsh, Fish, and PowerShell, making it faster to navigate commands and flags.
title: Shell tab completions for Wrangler CLI
image: https://developers.cloudflare.com/changelog/post/2026-01-09-wrangler-tab-completion/og.png?v=c5edb96c7bf14a17
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 9, 2026

## Shell tab completions for Wrangler CLI

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-09-wrangler-tab-completion/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Wrangler now includes built-in shell tab completion support, making it faster and easier to navigate commands without memorizing every option. Press Tab as you type to autocomplete commands, subcommands, flags, and even option values like log levels.

Tab completions are supported for Bash, Zsh, Fish, and PowerShell.

#### Setup

Generate the completion script for your shell and add it to your configuration file:

```sh
# Bash
wrangler complete bash >> ~/.bashrc

# Zsh
wrangler complete zsh >> ~/.zshrc

# Fish
wrangler complete fish >> ~/.config/fish/config.fish

# PowerShell
wrangler complete powershell >> $PROFILE
```

After adding the script, restart your terminal or source your configuration file for the changes to take effect. Then you can simply press Tab to see available completions:

```sh
wrangler d<TAB>          # completes to 'deploy', 'dev', 'd1', etc.
wrangler kv <TAB>        # shows subcommands: namespace, key, bulk
```

Tab completions are dynamically generated from Wrangler's command registry, so they stay up-to-date as new commands and options are added. This feature is powered by [`@bomb.sh/tab` ↗︎](https://github.com/bombshell-dev/tab/).

See the [`wrangler complete` documentation](https://developers.cloudflare.com/workers/wrangler/commands/general/#complete) for more details.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-09-wrangler-tab-completion/#page","headline":"Shell tab completions for Wrangler CLI","description":"Wrangler now supports shell tab completions for Bash, Zsh, Fish, and PowerShell, making it faster to navigate commands and flags.","url":"https://developers.cloudflare.com/changelog/post/2026-01-09-wrangler-tab-completion/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-09-wrangler-tab-completion/og.png?v=c5edb96c7bf14a17","dateModified":"2026-01-09","datePublished":"2026-01-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
