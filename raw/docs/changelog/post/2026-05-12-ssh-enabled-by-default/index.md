---
description: SSH through Wrangler is now enabled by default. Add a public key to connect, or opt out in your Container configuration.
title: SSH through Wrangler is now enabled by default for Containers
image: https://developers.cloudflare.com/changelog/post/2026-05-12-ssh-enabled-by-default/og.png?v=c6a7c47ed31e0246
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 12, 2026

## SSH through Wrangler is now enabled by default for Containers

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-12-ssh-enabled-by-default/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

SSH through Wrangler is now enabled by default for [Containers](https://developers.cloudflare.com/containers/). Previously, you had to set `ssh.enabled` to `true` in your Container configuration before you could connect.

This change does not expose any publicly accessible ports on your Container. The SSH service is reachable only through [`wrangler containers ssh`](https://developers.cloudflare.com/workers/wrangler/commands/containers/#containers-ssh), which authenticates against your Cloudflare account. You also need to add an `ssh-ed25519` public key to `authorized_keys` before anyone can connect, so enabling SSH alone does not grant access.

To connect, add a public key to your Container configuration and run `wrangler containers ssh <INSTANCE_ID>`:

```jsonc
{
	"containers": [
		{
			"authorized_keys": [
				{
					"name": "<NAME>",
					"public_key": "<YOUR_PUBLIC_KEY_HERE>",
				},
			],
		},
	],
}
```

```toml
[[containers]]
[[containers.authorized_keys]]
name = "<NAME>"
public_key = "<YOUR_PUBLIC_KEY_HERE>"
```

To disable SSH, set `ssh.enabled` to `false` in your Container configuration:

```jsonc
{
	"containers": [
		{
			"ssh": {
				"enabled": false,
			},
		},
	],
}
```

```toml
[[containers]]
[containers.ssh]
enabled = false
```

For more information, refer to the [SSH documentation](https://developers.cloudflare.com/containers/guides/ssh/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-12-ssh-enabled-by-default/#page","headline":"SSH through Wrangler is now enabled by default for Containers","description":"SSH through Wrangler is now enabled by default. Add a public key to connect, or opt out in your Container configuration.","url":"https://developers.cloudflare.com/changelog/post/2026-05-12-ssh-enabled-by-default/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-12-ssh-enabled-by-default/og.png?v=c6a7c47ed31e0246","dateModified":"2026-05-12","datePublished":"2026-05-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
