---
description: Connect to running Container instances with SSH through Wrangler.
title: SSH into running Container instances
image: https://developers.cloudflare.com/changelog/post/2026-03-12-ssh-support/og.png?v=f9f27f06cc011b4e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 12, 2026

## SSH into running Container instances

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-12-ssh-support/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now SSH into running Container instances using Wrangler. This is useful for debugging, inspecting running processes, or executing one-off commands inside a Container.

To connect, enable `wrangler_ssh` in your Container configuration and add your `ssh-ed25519` public key to `authorized_keys`:

```jsonc
{
	"containers": [
		{
			"wrangler_ssh": {
				"enabled": true
			},
			"authorized_keys": [
				{
					"name": "<NAME>",
					"public_key": "<YOUR_PUBLIC_KEY_HERE>"
				}
			]
		}
	]
}
```

```toml
[[containers]]
[containers.wrangler_ssh]
enabled = true

[[containers.authorized_keys]]
name = "<NAME>"
public_key = "<YOUR_PUBLIC_KEY_HERE>"
```

Then connect with:

```sh
wrangler containers ssh <INSTANCE_ID>
```

You can also run a single command without opening an interactive shell:

```sh
wrangler containers ssh <INSTANCE_ID> -- ls -al
```

Use `wrangler containers instances <APPLICATION>` to find the instance ID for a running Container.

For more information, refer to the [SSH documentation](https://developers.cloudflare.com/containers/guides/ssh/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-12-ssh-support/#page","headline":"SSH into running Container instances","description":"Connect to running Container instances with SSH through Wrangler.","url":"https://developers.cloudflare.com/changelog/post/2026-03-12-ssh-support/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-12-ssh-support/og.png?v=f9f27f06cc011b4e","dateModified":"2026-03-12","datePublished":"2026-03-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
