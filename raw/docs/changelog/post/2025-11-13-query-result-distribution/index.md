---
description: Visualize your Log Explorer query results with a graphical distribution chart over time.
title: Log Explorer now shows query result distribution
image: https://developers.cloudflare.com/changelog/post/2025-11-13-query-result-distribution/og.png?v=7cfd3845b3635ad0
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 4, 2025

## Log Explorer now shows query result distribution

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-13-query-result-distribution/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We're excited to announce a new feature in Log Explorer that significantly enhances how you analyze query results: the Query results distribution chart.

This new chart provides a graphical distribution of your results over the time window of the query. Immediately after running a query, you will see the distribution chart above your result table. This visualization allows Log Explorer users to quickly spot trends, identify anomalies, and understand the temporal concentration of log events that match their criteria. For example, you can visually confirm if a spike in traffic or errors occurred at a specific time, allowing you to focus your investigation efforts more effectively. This feature makes it faster and easier to extract meaningful insights from your vast log data.

The chart will dynamically update to reflect the logs matching your current query.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-13-query-result-distribution/#page","headline":"Log Explorer now shows query result distribution","description":"Visualize your Log Explorer query results with a graphical distribution chart over time.","url":"https://developers.cloudflare.com/changelog/post/2025-11-13-query-result-distribution/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-13-query-result-distribution/og.png?v=7cfd3845b3635ad0","dateModified":"2025-11-04","datePublished":"2025-11-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
