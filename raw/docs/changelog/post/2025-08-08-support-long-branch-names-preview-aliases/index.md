---
description: Branch names that create URLs longer than 63 characters now get hash-based preview URLs instead of failing, ensuring every pull request has a working preview link.
title: Workers per-branch preview URLs now support long branch names
image: https://developers.cloudflare.com/changelog/post/2025-08-08-support-long-branch-names-preview-aliases/og.png?v=ac290a0886e477cf
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 14, 2025

## Workers per-branch preview URLs now support long branch names

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-08-support-long-branch-names-preview-aliases/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We've updated [preview URLs](https://developers.cloudflare.com/workers/versions-and-deployments/preview-urls/) for Cloudflare Workers to support long branch names.

Previously, branch and Worker names exceeding the 63-character DNS limit would cause alias generation to fail, leaving pull requests without aliased preview URLs. This particularly impacted teams relying on descriptive branch naming.

Now, Cloudflare automatically truncates long branch names and appends a unique hash, ensuring every pull request gets a working preview link.

#### How it works

- **63 characters or less**: `<branch-name>-<worker-name>` → Uses actual branch name as is
- **64 characters or more**: `<truncated-branch-name>--<hash>-<worker-name>` → Uses truncated name with 4-character hash
- **Hash generation**: The hash is derived from the full branch name to ensure uniqueness
- **Stable URLs**: The same branch always generates the same hash across all commits

#### Requirements and compatibility

- **Wrangler 4.30.0 or later**: This feature requires updating to wrangler@4.30.0+
- **No configuration needed**: Works automatically with existing preview URL setups

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-08-support-long-branch-names-preview-aliases/#page","headline":"Workers per-branch preview URLs now support long branch names","description":"Branch names that create URLs longer than 63 characters now get hash-based preview URLs instead of failing, ensuring every pull request has a working preview link.","url":"https://developers.cloudflare.com/changelog/post/2025-08-08-support-long-branch-names-preview-aliases/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-08-support-long-branch-names-preview-aliases/og.png?v=ac290a0886e477cf","dateModified":"2025-08-14","datePublished":"2025-08-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
