---
description: Cloudflare API 403 responses now include a documentation_url that points directly to the denied endpoint's API documentation, where you can review the roles required for access.
title: Enriched 403 responses for the Cloudflare API
image: https://developers.cloudflare.com/changelog/post/2026-08-20-contextual-403s/og.png?v=3ffd9d81d7a4f513
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 21, 2026

## Enriched 403 responses for the Cloudflare API

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-20-contextual-403s/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare API `403 Forbidden` responses now include a `documentation_url` field that links directly to the API documentation for the endpoint that was denied. This gives developers, administrators, and agents an immediate path to the relevant docs with role information instead of guessing at which role or permission they are missing for that endpoint.

**What's New**

**Enriched 403 error responses**: When a Cloudflare API request is denied, the error response now includes a `documentation_url` field that points to the documentation for that specific endpoint. Contextual 403 responses are now available across nearly all Cloudflare product APIs.

**Faster troubleshooting**: The linked API docs surface the roles required for each endpoint, making it easier to self-serve access issues.

**Better support for tools and agents**: Agents can use the \\documentation\_url\` field to immediately fetch the endpoint's documentation from the 403 error response, identify the accepted permissions for the denied action, and use that context to drive third-party approval workflows.\`

Example 403 response:

```json
{
  "success": false,
  "errors": [
    {
      "code": 10000,
      "message": "Forbidden",
      "documentation_url": "https://developers.cloudflare.com/api/resources/workers/subresources/beta/subresources/workers/methods/list"
    }
  ],
  "messages": [],
  "result": null
}
```

For more info:

- [Browse the Cloudflare API documentation](https://developers.cloudflare.com/api/)
- [Review Cloudflare roles](https://developers.cloudflare.com/fundamentals/manage-members/roles/)
- [Review API token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-20-contextual-403s/#page","headline":"Enriched 403 responses for the Cloudflare API","description":"Cloudflare API 403 responses now include a documentation_url that points directly to the denied endpoint's API documentation, where you can review the roles required for access.","url":"https://developers.cloudflare.com/changelog/post/2026-08-20-contextual-403s/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-20-contextual-403s/og.png?v=3ffd9d81d7a4f513","dateModified":"2026-08-21","datePublished":"2026-08-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
