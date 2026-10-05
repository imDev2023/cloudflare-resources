---
description: Multiple improvements to the Workers Terraform resources and SDKs including fixes for plan diffs, file uploads, and Python Workers support.
title: Terraform provider improvements — Python Workers support, smaller plan diffs, and API SDK fixes
image: https://developers.cloudflare.com/changelog/post/2025-08-14-workers-terraform-and-sdk-improvements/og.png?v=9b3787249cf3e4cc
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 14, 2025

## Terraform provider improvements — Python Workers support, smaller plan diffs, and API SDK fixes

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-14-workers-terraform-and-sdk-improvements/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The recent [Cloudflare Terraform Provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script) and SDK releases (such as [cloudflare-typescript ↗︎](https://github.com/cloudflare/cloudflare-typescript)) bring significant improvements to the Workers developer experience. These updates focus on reliability, performance, and adding [Python Workers](https://developers.cloudflare.com/workers/languages/python/) support.

#### Terraform Improvements

#### Fixed Unwarranted Plan Diffs

Resolved several issues with the `cloudflare_workers_script` resource that resulted in unwarranted plan diffs, including:

- Using Durable Objects migrations
- Using some bindings such as `secret_text`
- Using smart placement

A resource should never show a plan diff if there isn't an actual change. This fix reduces unnecessary noise in your Terraform plan and is available in Cloudflare Terraform Provider 5.8.0.

#### Improved File Management

You can now specify `content_file` and `content_sha256` instead of `content`. This prevents the Workers script content from being stored in the state file which greatly reduces plan diff size and noise. If your workflow synced plans remotely, this should now happen much faster since there is less data to sync. This is available in Cloudflare Terraform Provider 5.7.0.

```tf
resource "cloudflare_workers_script" "my_worker" {
  account_id      = "123456789"
  script_name     = "my_worker"
  main_module     = "worker.mjs"
  content_file    = "worker.mjs"
  content_sha256  = filesha256("worker.mjs")
}
```

#### Assets Headers and Redirects Support

Fixed the `cloudflare_workers_script` resource to properly support headers and redirects for Assets:

```tf
resource "cloudflare_workers_script" "my_worker" {
  account_id      = "123456789"
  script_name     = "my_worker"
  main_module     = "worker.mjs"
  content_file    = "worker.mjs"
  content_sha256  = filesha256("worker.mjs")
  assets = {
    config = {
      headers = file("_headers")
      redirects = file("_redirects")
    }
    # Completion jwt from:
    # https://developers.cloudflare.com/api/resources/workers/subresources/assets/subresources/upload/
    jwt = "jwt"
  }
}
```

Available in Cloudflare Terraform Provider 5.8.0.

#### Python Workers Support

Added support for uploading [Python Workers](https://developers.cloudflare.com/workers/languages/python/) (beta) in Terraform. You can now deploy Python Workers with:

```tf
resource "cloudflare_workers_script" "my_worker" {
  account_id       = "123456789"
  script_name      = "my_worker"
  content_file     = "worker.py"
  content_sha256   = filesha256("worker.py")
  content_type     = "text/x-python"
}
```

Available in Cloudflare Terraform Provider 5.8.0.

#### SDK Enhancements

#### Improved File Upload API

Fixed an issue where Workers script versions in the SDK did not allow uploading files. This now works, and also has an improved files upload interface:

```js
const scriptContent = `
  export default {
    async fetch(request, env, ctx) {
      return new Response('Hello World!', { status: 200 });
    }
  };
`;

client.workers.scripts.versions.create('my-worker', {
  account_id: '123456789',
  metadata: {
    main_module: 'my-worker.mjs',
  },
  files: [
    await toFile(
      Buffer.from(scriptContent),
      'my-worker.mjs',
      {
        type: "application/javascript+module",
      }
    )
  ]
});
```

Will be available in cloudflare-typescript 4.6.0. A similar change will be available in cloudflare-python 4.4.0.

#### Fixed updating KV values

Previously when creating a KV value like this:

```js
await cf.kv.namespaces.values.update("my-kv-namespace", "key1", {
  account_id: "123456789",
  metadata: "my metadata",
  value: JSON.stringify({
    hello: "world"
  })
});
```

...and recalling it in your Worker like this:

```ts
const value = await c.env.KV.get<{hello: string}>("key1", "json");
```

You'd get back this: `{metadata:'my metadata', value:"{'hello':'world'}"}` instead of the correct value of `{hello: 'world'}`

This is fixed in cloudflare-typescript 4.5.0 and will be fixed in cloudflare-python 4.4.0.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-14-workers-terraform-and-sdk-improvements/#page","headline":"Terraform provider improvements — Python Workers support, smaller plan diffs, and API SDK fixes","description":"Multiple improvements to the Workers Terraform resources and SDKs including fixes for plan diffs, file uploads, and Python Workers support.","url":"https://developers.cloudflare.com/changelog/post/2025-08-14-workers-terraform-and-sdk-improvements/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-14-workers-terraform-and-sdk-improvements/og.png?v=9b3787249cf3e4cc","dateModified":"2025-08-14","datePublished":"2025-08-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
