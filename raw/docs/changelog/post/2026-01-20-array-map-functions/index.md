---
description: Rulesets now support split, join, has_key, and has_value functions for advanced expression logic.
title: New functions for array and map operations
image: https://developers.cloudflare.com/changelog/post/2026-01-20-array-map-functions/og.png?v=8953cde18c5746b7
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 20, 2026

## New functions for array and map operations

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-20-array-map-functions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

#### New functions for array and map operations

Cloudflare Rulesets now include new functions that enable advanced expression logic for evaluating arrays and maps. These functions allow you to build rules that match against lists of values in request or response headers, enabling use cases like country-based blocking using custom headers.

---

#### New functions

| Function | Description |
| --- | --- |
| `split(source, delimiter)` | Splits a string into an array of strings using the specified delimiter. |
| `join(array, delimiter)` | Joins an array of strings into a single string using the specified delimiter. |
| `has_key(map, key)` | Returns `true` if the specified key exists in the map. |
| `has_value(map, value)` | Returns `true` if the specified value exists in the map. |

---

#### Example use cases

**Check if a country code exists in a header list:**

```txt
has_value(split(http.response.headers["x-allow-country"][0], ","), ip.src.country)
```

**Check if a specific header key exists:**

```txt
has_key(http.request.headers, "x-custom-header")
```

**Join array values for logging or comparison:**

```txt
join(http.request.headers.names, ", ")
```

For more information, refer to the [Functions reference](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-20-array-map-functions/#page","headline":"New functions for array and map operations","description":"Rulesets now support split, join, has_key, and has_value functions for advanced expression logic.","url":"https://developers.cloudflare.com/changelog/post/2026-01-20-array-map-functions/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-20-array-map-functions/og.png?v=8953cde18c5746b7","dateModified":"2026-01-20","datePublished":"2026-01-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
