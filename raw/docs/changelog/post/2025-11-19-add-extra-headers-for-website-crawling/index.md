---
description: Index websites behind login walls by adding custom authentication headers to AI Search's website crawler.
title: AI Search support for crawling login protected website content
image: https://developers.cloudflare.com/changelog/post/2025-11-19-add-extra-headers-for-website-crawling/og.png?v=32e2e730c495f302
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 19, 2025

## AI Search support for crawling login protected website content

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-19-add-extra-headers-for-website-crawling/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports [custom HTTP headers](https://developers.cloudflare.com/ai-search/configuration/data-source/website/authentication-headers/) for website crawling, solving a common problem where valuable content behind authentication or access controls could not be indexed.

Previously, AI Search could only crawl publicly accessible pages, leaving knowledge bases, documentation, and other protected content out of your search results. With custom headers support, you can now include authentication credentials that allow the crawler to access this protected content.

This is particularly useful for indexing content like:

- **Internal documentation** behind corporate login systems
- **Premium content** that requires users to provide access to unlock
- **Sites protected by Cloudflare Access** using service tokens

To add custom headers when creating an AI Search instance, select **Parse options**. In the **Extra headers** section, you can add up to five custom headers per Website data source.

![Custom headers configuration in AI Search](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1098,height=287,format=webp/_astro/ai-search-extra-headers.B7A2spby.png)

For example, to crawl a site protected by [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/), you can add service token credentials as custom headers:

```plaintext
CF-Access-Client-Id: your-token-id.access
CF-Access-Client-Secret: your-token-secret
```

The crawler will automatically include these headers in all requests, allowing it to access protected pages that would otherwise be blocked.

Learn more about [configuring custom headers for website crawling](https://developers.cloudflare.com/ai-search/configuration/data-source/website/authentication-headers/) in AI Search.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-19-add-extra-headers-for-website-crawling/#page","headline":"AI Search support for crawling login protected website content","description":"Index websites behind login walls by adding custom authentication headers to AI Search's website crawler.","url":"https://developers.cloudflare.com/changelog/post/2025-11-19-add-extra-headers-for-website-crawling/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-19-add-extra-headers-for-website-crawling/og.png?v=32e2e730c495f302","dateModified":"2025-11-19","datePublished":"2025-11-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
