---
description: Use D1 Sessions API to leverage read replication.
title: D1 Read Replication Public Beta
image: https://developers.cloudflare.com/changelog/post/2025-04-10-d1-read-replication-beta/og.png?v=998401636412dfea
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 10, 2025

## D1 Read Replication Public Beta

[D1](https://developers.cloudflare.com/d1/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-10-d1-read-replication-beta/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

D1 read replication is available in public beta to help lower average latency and increase overall throughput for read-heavy applications like e-commerce websites or content management tools.

Workers can leverage read-only database copies, called read replicas, by using D1 [Sessions API](https://developers.cloudflare.com/d1/best-practices/read-replication). A session encapsulates all the queries from one logical session for your application. For example, a session may correspond to all queries coming from a particular web browser session. With Sessions API, D1 queries in a session are guaranteed to be [sequentially consistent](https://developers.cloudflare.com/d1/best-practices/read-replication/#replica-lag-and-consistency-model) to avoid data consistency pitfalls. D1 [bookmarks](https://developers.cloudflare.com/d1/reference/time-travel/#bookmarks) can be used from a previous session to ensure logical consistency between sessions.

```ts
// retrieve bookmark from previous session stored in HTTP header
const bookmark = request.headers.get("x-d1-bookmark") ?? "first-unconstrained";

const session = env.DB.withSession(bookmark);
const result = await session
	.prepare(`SELECT * FROM Customers WHERE CompanyName = 'Bs Beverages'`)
	.run();
// store bookmark for a future session
response.headers.set("x-d1-bookmark", session.getBookmark() ?? "");
```

Read replicas are automatically created by Cloudflare (currently one in each supported [D1 region](https://developers.cloudflare.com/d1/best-practices/read-replication/#read-replica-locations)), are active/inactive based on query traffic, and are transparently routed to by Cloudflare at no additional cost.

To checkout D1 read replication, deploy the following Worker code using Sessions API, which will prompt you to create a D1 database and enable read replication on said database.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/d1-starter-sessions-api)

To learn more about how read replication was implemented, go to our [blog post ↗︎](https://blog.cloudflare.com/d1-read-replication-beta).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-10-d1-read-replication-beta/#page","headline":"D1 Read Replication Public Beta","description":"Use D1 Sessions API to leverage read replication.","url":"https://developers.cloudflare.com/changelog/post/2025-04-10-d1-read-replication-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-10-d1-read-replication-beta/og.png?v=998401636412dfea","dateModified":"2025-04-10","datePublished":"2025-04-10","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
