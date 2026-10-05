---
description: Delete one or up to 100 Workflow instances and their stored state using a binding or Wrangler.
title: Delete Workflow instances individually or in batches
image: https://developers.cloudflare.com/changelog/post/2026-09-17-instance-delete/og.png?v=666dba06a016be28
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 17, 2026

## Delete Workflow instances individually or in batches

[Workflows](https://developers.cloudflare.com/workflows/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-17-instance-delete/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now delete one or up to 100 Workflow instances and their stored state via the [Workflows API](https://developers.cloudflare.com/workflows/build/workers-api/) or Wrangler 4.125.0 and later. Deleting an instance frees its stored state and stops its current execution. [Storage billing](https://developers.cloudflare.com/workflows/reference/pricing/#storage-usage) is based on the average daily peak.

Delete one instance by calling [`delete()`](https://developers.cloudflare.com/workflows/build/workers-api/#delete) on its handle:

```ts
const instance = await env.MY_WORKFLOW.get("instance-abc");
await instance.delete();
```

If a Workflow deletes its own instance, execution stops during `await instance.delete()`. Code after the call does not run.

Delete multiple instances by calling [`deleteBatch()`](https://developers.cloudflare.com/workflows/build/workers-api/#deletebatch) on the Workflow binding:

```ts
const result = await env.MY_WORKFLOW.deleteBatch([
	"instance-abc",
	"instance-def",
]);

console.log(result.deleted);
console.log(result.errors);
```

The batch result contains `{ id }` entries for successful deletions and per-instance errors. IDs that do not exist are returned as errors. Duplicate IDs count toward the limit and are deleted once, with the result repeated for each input position.

Wrangler accepts positional instance IDs, a file containing a top-level JSON array of strings, or both, up to 100 IDs total. Use `latest` to delete the most recently created instance. Use `--local` against a local `wrangler dev` session:

*instance-ids.jsonjson*

```json
["instance-abc", "instance-def"]
```

```sh
npx wrangler workflows instances delete my-workflow <INSTANCE_ID>
npx wrangler workflows instances delete my-workflow <INSTANCE_ID> <INSTANCE_ID>
npx wrangler workflows instances delete my-workflow latest
npx wrangler workflows instances delete my-workflow --filename ./instance-ids.json
npx wrangler workflows instances delete my-workflow <INSTANCE_ID> --local
```

For more information, refer to [Delete Workflow instances](https://developers.cloudflare.com/workflows/build/trigger-workflows/#delete-workflow-instances), [`delete`](https://developers.cloudflare.com/workflows/build/workers-api/#delete), and [`deleteBatch`](https://developers.cloudflare.com/workflows/build/workers-api/#deletebatch).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-17-instance-delete/#page","headline":"Delete Workflow instances individually or in batches","description":"Delete one or up to 100 Workflow instances and their stored state using a binding or Wrangler.","url":"https://developers.cloudflare.com/changelog/post/2026-09-17-instance-delete/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-17-instance-delete/og.png?v=666dba06a016be28","dateModified":"2026-09-17","datePublished":"2026-09-17","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
