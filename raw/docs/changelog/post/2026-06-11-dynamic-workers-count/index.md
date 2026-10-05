---
description: View the number of billable Dynamic Workers invoked during your billing period from the dashboard or GraphQL Analytics API.
title: Track Dynamic Workers usage from the dashboard and GraphQL API
image: https://developers.cloudflare.com/changelog/post/2026-06-11-dynamic-workers-count/og.png?v=4716e320dee4cdcb
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 11, 2026

## Track Dynamic Workers usage from the dashboard and GraphQL API

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-11-dynamic-workers-count/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

![Dynamic Workers usage on the Workers overview page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1476,height=1102,format=webp/_astro/dynamic-workers-count.BcGsgQ0m.png)

Customers can now view the number of [Dynamic Workers](https://developers.cloudflare.com/dynamic-workers/) invoked during their billing period from the Workers overview page in the Cloudflare dashboard.

This count reflects the number of Dynamic Workers that Cloudflare would bill for during the selected billing period. Dynamic Workers usage data only goes back to June 1, 2026.

You can also query this count through the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/) by using `workersInvocationsByOwnerAndScriptGroups` and selecting `distinctDynamicWorkerCount`:

```graphql
query getDynamicWorkersCount(
	$accountTag: string!
	$filter: AccountWorkersInvocationsByOwnerAndScriptGroupsFilter_InputObject
) {
	viewer {
		accounts(filter: { accountTag: $accountTag }) {
			workersInvocationsByOwnerAndScriptGroups(limit: 10000, filter: $filter) {
				uniq {
					distinctDynamicWorkerCount
				}
			}
		}
	}
}
```

Use variables to set the account and billing-period date range:

```json
{
	"accountTag": "<ACCOUNT_ID>",
	"filter": {
		"date_geq": "2026-06-01",
		"date_leq": "2026-06-30"
	}
}
```

For more information, refer to [Dynamic Workers pricing](https://developers.cloudflare.com/dynamic-workers/pricing/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-11-dynamic-workers-count/#page","headline":"Track Dynamic Workers usage from the dashboard and GraphQL API","description":"View the number of billable Dynamic Workers invoked during your billing period from the dashboard or GraphQL Analytics API.","url":"https://developers.cloudflare.com/changelog/post/2026-06-11-dynamic-workers-count/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-11-dynamic-workers-count/og.png?v=4716e320dee4cdcb","dateModified":"2026-06-11","datePublished":"2026-06-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
