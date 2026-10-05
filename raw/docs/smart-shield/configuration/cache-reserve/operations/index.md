---
description: How Cache Reserve read, write, and delete operations work with R2 storage.
title: Cache Reserve operations
image: https://developers.cloudflare.com/smart-shield/configuration/cache-reserve/operations/og.png?v=fd4dbd973e1bafa6
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/smart-shield/llms.txt  
> Use this file to discover all available pages before exploring further.

# Cache Reserve operations

Last updated Apr 17, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/smart-shield/configuration/cache-reserve/operations/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Operations are performed by Cache Reserve on behalf of the user to write data from the origin to Cache Reserve and to pass that data downstream to other parts of Cloudflare’s network. These operations are managed internally by Cloudflare.

#### Class A operations (writes)

Class A operations are performed based on cache misses from Cloudflare’s CDN. When a request cannot be served from cache, it will be fetched from the origin and written to cache reserve as well as our edge caches on the way back to the visitor.

#### Class B operations (reads)

Class B operations are performed when data needs to be fetched from Cache Reserve to respond to a miss in the edge cache.

#### Purge and invalidation

Purge requests are free operations. Invalidation requests can result in Class A operations.

[Purging](https://developers.cloudflare.com/cache/how-to/purge-cache/) content forces a cache miss in both Cache Reserve and the edge cache, regardless of purge type. The next request for that content is fetched from your origin and written to Cache Reserve again, which is a Class A operation.

Purging by URL deletes content from Cache Reserve. Purging by tag, hostname, prefix, or everything does not delete it right away. Matching content stays stored and continues to incur storage costs until a later request replaces it or its retention period ends.

[Invalidating](https://developers.cloudflare.com/cache/guides/invalidate-cache/) content keeps it in Cache Reserve and marks it for revalidation. If your origin responds with `304 Not Modified`, Cloudflare reuses the stored content instead of fetching it from your origin. Updating the stored content after the `304` response is a Class A operation. Invalidating by URL also updates the stored content when you send the request, which is a Class A operation. Invalidated content remains stored and continues to incur storage costs.
