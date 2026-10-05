---
description: You can now use remote bindings with OpenNext applications.
title: Remote bindings (beta) now works with Next.js — connect to remote resources (D1, KV, R2, etc.) during local development
image: https://developers.cloudflare.com/changelog/post/2025-06-25-getPlatformProxy-support-remote-bindings/og.png?v=7e20dfadeb7eac3d
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 30, 2025

## Remote bindings (beta) now works with Next.js — connect to remote resources (D1, KV, R2, etc.) during local development

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-25-getPlatformProxy-support-remote-bindings/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We [recently announced ↗︎](https://github.com/cloudflare/workers-sdk/discussions/9660) our public beta for [remote bindings](https://developers.cloudflare.com/workers/local-development/#remote-bindings), which allow you to connect to deployed resources running on your Cloudflare account (like [R2 buckets](https://developers.cloudflare.com/r2) or [D1 databases](https://developers.cloudflare.com/d1)) while running a local development session.

Now, you can use remote bindings with your Next.js applications through the [`@opennextjs/cloudflare` adaptor ↗︎](https://opennext.js.org/cloudflare/bindings#remote-bindings) by enabling the experimental feature in your `next.config.ts`:

```diff
- initOpenNextCloudflareForDev();
+ initOpenNextCloudflareForDev({
+  experimental: { remoteBindings: true }
+ });
```

Then, all you have to do is specify which bindings you want connected to the deployed resource on your Cloudflare account via the `experimental_remote` flag in your binding definition:

```jsonc
{
	"r2_buckets": [
		{
			"bucket_name": "testing-bucket",
			"binding": "MY_BUCKET",
			"experimental_remote": true,
		},
	],
}
```

```toml
[[r2_buckets]]
bucket_name = "testing-bucket"
binding = "MY_BUCKET"
experimental_remote = true
```

You can then run `next dev` to start a local development session (or start a preview with `opennextjs-cloudflare preview`), and all requests to `env.MY_BUCKET` will be proxied to the remote `testing-bucket` — rather than the [default local binding simulations](https://developers.cloudflare.com/workers/local-development/#bindings-during-local-development).

#### Remote bindings & ISR

Remote bindings are also used during the build process, which comes with significant benefits for pages using [Incremental Static Regeneration (ISR) ↗︎](https://opennext.js.org/aws/inner_workings/components/server/node#isrssg). During the build step for an ISR page, your server executes the page's code just as it would for normal user requests. If a page needs data to display (like fetching user info from [KV](https://developers.cloudflare.com/kv)), those requests are actually made. The server then uses this fetched data to render the final HTML.

Data fetching is a critical part of this process, as the finished HTML is only as good as the data it was built with. If the build process can't fetch real data, you end up with a pre-rendered page that's empty or incomplete.

**With remote bindings support in OpenNext,** your pre-rendered pages are built with real data from the start. The build process uses any configured remote bindings, and any data fetching occurs against the deployed resources on your Cloudflare account.

**Want to learn more?** Get started with [remote bindings and OpenNext ↗︎](https://opennext.js.org/cloudflare/bindings#remote-bindings).

**Have feedback?** Join the discussion in our [beta announcement ↗︎](https://github.com/cloudflare/workers-sdk/discussions/9660) to share feedback or report any issues.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-25-getPlatformProxy-support-remote-bindings/#page","headline":"Remote bindings (beta) now works with Next.js — connect to remote resources (D1, KV, R2, etc.) during local development","description":"You can now use remote bindings with OpenNext applications.","url":"https://developers.cloudflare.com/changelog/post/2025-06-25-getPlatformProxy-support-remote-bindings/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-06-25-getPlatformProxy-support-remote-bindings/og.png?v=7e20dfadeb7eac3d","dateModified":"2025-06-30","datePublished":"2025-06-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
