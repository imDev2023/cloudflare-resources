---
description: You can now use a predefined DLP profile to detect, block, or redirect unsanitized HAR files in HTTP traffic, preventing sensitive data like session cookies and authentication tokens from being exfiltrated.
title: Detect and sanitize HAR files
image: https://developers.cloudflare.com/changelog/post/2026-03-25-har-file-detection-and-sanitization/og.png?v=0cfcc25874ee42b2
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 25, 2026

## Detect and sanitize HAR files

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-25-har-file-detection-and-sanitization/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

HTTP Archive (HAR) files are used by engineering and support teams to capture and share web traffic logs for troubleshooting. However, these files routinely contain highly sensitive data — including session cookies, authorization headers, and other credentials — that can pose a significant risk if uploaded to third-party services without being reviewed or cleaned first.

Gateway now includes a predefined DLP profile called **Unsanitized HAR** that detects HAR files in HTTP traffic. You can use this profile in a Gateway HTTP policy to either block HAR file uploads entirely or redirect users to a sanitization tool before allowing the upload to proceed.

#### How to configure a HAR file policy

In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Traffic policies** > **Firewall Policies** > **HTTP** and create a new HTTP policy using the **DLP Profile** selector:

| Selector | Operator | Value | Action |
| --- | --- | --- | --- |
| DLP Profile | in | *Unsanitized HAR* | |

Then choose one of the following actions:

- **Block**: Prevents the upload of any HAR file that has not been sanitized by Cloudflare's sanitizer. Use this for strict environments where HAR file sharing must be disallowed entirely.
- **Block** with **Gateway Redirect**: Intercepts the upload and redirects the user to `https://har-sanitizer.pages.dev/`, where they can sanitize the file. Once sanitized, the user can re-upload the clean file and proceed with their workflow.

#### Sanitized HAR recognition

HAR files processed by the Cloudflare HAR sanitizer receive a tamper-evident sanitized marker. DLP recognizes this marker and will not re-trigger the policy on a file that has already been sanitized and has not been modified since. If a previously sanitized file is edited, it will be treated as unsanitized and flagged again.

#### Visibility in Gateway logs

Gateway logs will reflect whether a detected HAR file was classified as **Unsanitized** or **Sanitized**, giving your security team full visibility into HAR file activity across your organization.

For more information, refer to [predefined DLP profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-25-har-file-detection-and-sanitization/#page","headline":"Detect and sanitize HAR files","description":"You can now use a predefined DLP profile to detect, block, or redirect unsanitized HAR files in HTTP traffic, preventing sensitive data like session cookies and authentication tokens from being exfiltrated.","url":"https://developers.cloudflare.com/changelog/post/2026-03-25-har-file-detection-and-sanitization/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-25-har-file-detection-and-sanitization/og.png?v=0cfcc25874ee42b2","dateModified":"2026-03-25","datePublished":"2026-03-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
