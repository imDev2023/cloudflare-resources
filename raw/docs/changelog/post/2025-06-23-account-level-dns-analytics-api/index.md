---
description: Authoritative DNS analytics can now be accessed on the account level via the GraphQL Analytics API.
title: Account-level DNS analytics now available via GraphQL Analytics API
image: https://developers.cloudflare.com/changelog/post/2025-06-23-account-level-dns-analytics-api/og.png?v=a0c410ea74bff7ae
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 19, 2025

## Account-level DNS analytics now available via GraphQL Analytics API

[DNS](https://developers.cloudflare.com/dns/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-23-account-level-dns-analytics-api/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Authoritative DNS analytics are now available on the **account level** via the [Cloudflare GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/).

This allows users to query DNS analytics across multiple zones in their account, by using the `accounts` filter.

Here is an example to retrieve the most recent DNS queries across all zones in your account that resulted in an `NXDOMAIN` response over a given time frame. Please replace `a30f822fcd7c401984bf85d8f2a5111c` with your actual account ID.

*GraphQL example for account-level DNS analyticsgraphql*

```graphql
query GetLatestNXDOMAINResponses {
	viewer {
		accounts(filter: { accountTag: "a30f822fcd7c401984bf85d8f2a5111c" }) {
			dnsAnalyticsAdaptive(
				filter: {
					date_geq: "2025-06-16"
					date_leq: "2025-06-18"
					responseCode: "NXDOMAIN"
				}
				limit: 10000
				orderBy: [datetime_DESC]
			) {
				zoneTag
				queryName
				responseCode
				queryType
				datetime
			}
		}
	}
}
```

To learn more and get started, refer to the [DNS Analytics documentation](https://developers.cloudflare.com/dns/additional-options/analytics/#analytics).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-23-account-level-dns-analytics-api/#page","headline":"Account-level DNS analytics now available via GraphQL Analytics API","description":"Authoritative DNS analytics can now be accessed on the account level via the GraphQL Analytics API.","url":"https://developers.cloudflare.com/changelog/post/2025-06-23-account-level-dns-analytics-api/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-06-23-account-level-dns-analytics-api/og.png?v=a0c410ea74bff7ae","dateModified":"2025-06-19","datePublished":"2025-06-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
