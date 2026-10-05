---
description: Download cloud onramp terraform
title: Generate customized terraform files for building cloud network on-ramps
image: https://developers.cloudflare.com/changelog/post/2024-12-05-cloud-onramp-terraform/og.png?v=4e6cae2fb46b0971
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 5, 2024

## Generate customized terraform files for building cloud network on-ramps

[Multi-Cloud Networking](https://developers.cloudflare.com/multi-cloud-networking/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2024-12-05-cloud-onramp-terraform/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now generate customized terraform files for building cloud network on-ramps to [Magic WAN](https://developers.cloudflare.com/cloudflare-wan/).

[Magic Cloud](https://developers.cloudflare.com/multi-cloud-networking/) can scan and discover existing network resources and generate the required terraform files to automate cloud resource deployment using their existing infrastructure-as-code workflows for cloud automation.

You might want to do this to:

- Review the proposed configuration for an on-ramp before deploying it with Cloudflare.
- Deploy the on-ramp using your own infrastructure-as-code pipeline instead of deploying it with Cloudflare.

For more details, refer to [Set up with Terraform](https://developers.cloudflare.com/multi-cloud-networking/cloud-on-ramps/#set-up-with-terraform).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2024-12-05-cloud-onramp-terraform/#page","headline":"Generate customized terraform files for building cloud network on-ramps","description":"Download cloud onramp terraform","url":"https://developers.cloudflare.com/changelog/post/2024-12-05-cloud-onramp-terraform/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2024-12-05-cloud-onramp-terraform/og.png?v=4e6cae2fb46b0971","dateModified":"2024-12-05","datePublished":"2024-12-05","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
