---
description: Gain more control over your DLP detections and reduce false positives by specifying whether to scan the HTTP request or response body.
title: Refine DLP Scans with New Body Phase Selector
image: https://developers.cloudflare.com/changelog/post/2025-09-25-body-phase-selector/og.png?v=a90b8518c3ecfe72
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 25, 2025

## Refine DLP Scans with New Body Phase Selector

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-25-body-phase-selector/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now more precisely control your HTTP DLP policies by specifying whether to scan the request or response body, helping to reduce false positives and target specific data flows.

In the Gateway HTTP policy builder, you will find a new selector called *Body Phase*. This allows you to define the direction of traffic the DLP engine will inspect:

- *Request Body*: Scans data sent from a user's machine to an upstream service. This is ideal for monitoring data uploads, form submissions, or other user-initiated data exfiltration attempts.
- *Response Body*: Scans data sent to a user's machine from an upstream service. Use this to inspect file downloads and website content for sensitive data.

For example, consider a policy that blocks Social Security Numbers (SSNs). Previously, this policy might trigger when a user visits a website that contains example SSNs in its content (the response body). Now, by setting the **Body Phase** to *Request Body*, the policy will only trigger if the user attempts to upload or submit an SSN, ignoring the content of the web page itself.

All policies without this selector will continue to scan both request and response bodies to ensure continued protection.

For more information, refer to [Gateway HTTP policy selectors](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#body-phase).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-25-body-phase-selector/#page","headline":"Refine DLP Scans with New Body Phase Selector","description":"Gain more control over your DLP detections and reduce false positives by specifying whether to scan the HTTP request or response body.","url":"https://developers.cloudflare.com/changelog/post/2025-09-25-body-phase-selector/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-25-body-phase-selector/og.png?v=a90b8518c3ecfe72","dateModified":"2025-09-25","datePublished":"2025-09-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
