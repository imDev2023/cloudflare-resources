---
description: CASB and DLP with Cloud Data Extraction for AWS cloud environments
title: Find security misconfigurations in your AWS cloud environment
image: https://developers.cloudflare.com/changelog/post/2024-11-22-cloud-data-extraction-aws/og.png?v=9ff88f44d8c06704
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 22, 2024

## Find security misconfigurations in your AWS cloud environment

[CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2024-11-22-cloud-data-extraction-aws/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now use CASB to find security misconfigurations in your AWS cloud environment using [Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/).

You can also [connect your AWS compute account](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/aws-s3/#compute-account) to extract and scan your S3 buckets for sensitive data while avoiding egress fees. CASB will scan any objects that exist in the bucket at the time of configuration.

To connect a compute account to your AWS integration:

1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com), go to **Cloud & SaaS findings** > **Integrations**.
2. Find and select your AWS integration.
3. Select **Open connection instructions**.
4. Follow the instructions provided to connect a new compute account.
5. Select **Refresh**.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2024-11-22-cloud-data-extraction-aws/#page","headline":"Find security misconfigurations in your AWS cloud environment","description":"CASB and DLP with Cloud Data Extraction for AWS cloud environments","url":"https://developers.cloudflare.com/changelog/post/2024-11-22-cloud-data-extraction-aws/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2024-11-22-cloud-data-extraction-aws/og.png?v=9ff88f44d8c06704","dateModified":"2024-11-22","datePublished":"2024-11-22","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
