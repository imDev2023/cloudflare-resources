---
description: Permanently delete account and zone Log Explorer datasets from the Cloudflare dashboard or API.
title: Delete Log Explorer datasets
image: https://developers.cloudflare.com/changelog/post/2026-08-26-dataset-deletion/og.png?v=57cf9d8ea3f0bf6a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 26, 2026

## Delete Log Explorer datasets

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-26-dataset-deletion/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Log Explorer customers can now permanently delete account and zone datasets from the Cloudflare dashboard or API.

Deletion protection is enabled by default to prevent accidental data loss. In the dashboard, go to [Manage datasets](https://developers.cloudflare.com/log-explorer/manage-datasets/), disable deletion protection for the dataset, select **Delete**, and enter the dataset name to confirm.

To delete a dataset through the API, first set `deletion_protection` to `false` with the [Update an account or zone dataset](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/update/) method. Then use the [Delete an account or zone dataset](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/delete/) method.

Dataset deletion is irreversible and runs asynchronously. You cannot recreate the same dataset while deletion is in progress.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-26-dataset-deletion/#page","headline":"Delete Log Explorer datasets","description":"Permanently delete account and zone Log Explorer datasets from the Cloudflare dashboard or API.","url":"https://developers.cloudflare.com/changelog/post/2026-08-26-dataset-deletion/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-26-dataset-deletion/og.png?v=57cf9d8ea3f0bf6a","dateModified":"2026-08-26","datePublished":"2026-08-26","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
