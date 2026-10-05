---
description: Upload a document as a detection entry type to be identified in traffic utilizing Gateway or at rest with CASB.
title: "New detection entry type: Document Matching for DLP"
image: https://developers.cloudflare.com/changelog/post/2025-07-17-document-matching/og.png?v=4a8d9427f1d08a83
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 17, 2025

## New detection entry type: Document Matching for DLP

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-07-17-document-matching/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now create [document-based](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#document-entries) detection entries in DLP by uploading example documents. Cloudflare will encrypt your documents and create a unique fingerprint of the file. This fingerprint is then used to identify similar documents or snippets within your organization's traffic and stored files.

![DLP](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1356,height=839,format=webp/_astro/document-match.CcN8pGgR.png)

**Key features and benefits:**

- **Upload documents, forms, or templates:** Easily upload .docx and .txt files (up to 10 MB) that contain sensitive information you want to protect.
- **Granular control with similarity percentage:** Define a minimum similarity percentage (0-100%) that a document must meet to trigger a detection, reducing false positives.
- **Comprehensive coverage:** Apply these document-based detection entries in:
  - **Gateway policies:** To inspect network traffic for sensitive documents as they are uploaded or shared.
  - **CASB (Cloud Access Security Broker):** To scan files stored in cloud applications for sensitive documents at rest.
- **Identify sensitive data:** This new detection entry type is ideal for identifying sensitive data within completed forms, templates, or even small snippets of a larger document, helping you prevent data exfiltration and ensure compliance.

Once uploaded and processed, you can add this new document entry into a DLP profile and policies to enhance your data protection strategy.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-07-17-document-matching/#page","headline":"New detection entry type: Document Matching for DLP","description":"Upload a document as a detection entry type to be identified in traffic utilizing Gateway or at rest with CASB.","url":"https://developers.cloudflare.com/changelog/post/2025-07-17-document-matching/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-07-17-document-matching/og.png?v=4a8d9427f1d08a83","dateModified":"2025-07-17","datePublished":"2025-07-17","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
