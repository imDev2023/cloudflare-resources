---
description: Fix content encoding mismatches with compression settings.
title: Content encoding issues
image: https://developers.cloudflare.com/speed/optimization/content/troubleshooting/content-encoding-issues/og.png?v=2424d2463e6a4f85
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/speed/llms.txt  
> Use this file to discover all available pages before exploring further.

# Content encoding issues

Last updated Apr 17, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/speed/optimization/content/troubleshooting/content-encoding-issues/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

If you are noticing any encoding errors with your HTML pages, we recommend verifying that the impacted pages are explicitly setting the correct charset in the `Content-Type` header from your origin for all text/html pages, for example `Content-Type: text/html; charset=utf-8`. This is particularly important if you are not using [UTF-8 encoding standard ↗︎](https://en.wikipedia.org/wiki/UTF-8) for characters. Alternatively you can set the correct charset within the HTML.

If you believe these settings are correct, please inform us. You can find more information in [setting the HTTP charset parameter ↗︎](https://www.w3.org/International/articles/http-charset/index) and in [HTML charset attribute ↗︎](https://www.w3schools.com/tags/att_meta_charset.asp).

Alternatively, you can use a [Configuration Rule](https://developers.cloudflare.com/rules/configuration-rules/) to disable features that rewrite HTML. This will send the content as-is to the browser.

You also have the option to turn off these features site-wide within the dashboard:

- [Email Obfuscation](https://developers.cloudflare.com/waf/tools/scrape-shield/email-address-obfuscation/), located in the **Security** > **Settings** section.
- [Rocket Loader](https://developers.cloudflare.com/speed/optimization/content/rocket-loader/), located in **Speed** > **Settings** > **Content Optimization** section.
- [Automatic HTTPS Rewrites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/automatic-https-rewrites/), located in the **SSL/TLS** > **Edge Certificates** section.

Misconfiguring the `Content-Type` or charset within HTML, or leaving them unspecified can lead to unintended consequences. This can disrupt the intended content presentation, resulting in disorganized rendering and potentially unclear characters. Properly configuring these elements ensures consistent and accurate interpretation, correct HTML modifications, and accurate rendering for browsers. This creates a seamless user experience and aligns with best practices in web development.
