---
description: Migrate from hCaptcha to Cloudflare Turnstile.
title: Migrate from hCaptcha
image: https://developers.cloudflare.com/turnstile/migration/hcaptcha/og.png?v=8d9bc87ea0591429
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/turnstile/llms.txt  
> Use this file to discover all available pages before exploring further.

# Migrate from hCaptcha

Last updated May 5, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/turnstile/migration/hcaptcha/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

If you are using hCaptcha today, you can switch seamlessly to Cloudflare Turnstile by following the step-by-step guide below to assist with the upgrade process.

To complete the migration, you must obtain the [sitekey and secret key](https://developers.cloudflare.com/turnstile/get-started/widget-management/).

## Client-side integration

1. Update the client-side integration by inserting the Turnstile script snippet in your HTML's `<head>` element:

   *Turnstile script snippethtml*

   

   ```html
   <script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>
   ```


2. Locate the `hcaptcha.render()` calls and replace the sitekey with your Turnstile sitekey and the API.

   *Renderjs*

   

   ```js
    // before
     hcaptcha.render(element, {
         sitekey: "00000000-0000-0000-0000-000000000000"
     })
     // after
     turnstile.render(element, {
         sitekey: "1x00000000000000000000AA"
     })
   ```



Note

Turnstile supports:

- the `render()` call
- hCaptcha invisible mode with the `execute()` call

## Server-side integration

1. Update the server-side integration by replacing the Siteverify URL.

   Replace: `https://hcaptcha.com/siteverify` with the following:

   ```txt
   https://challenges.cloudflare.com/turnstile/v0/siteverify
   ```


2. Replace the `h-captcha-response` input name with the following:

   ```txt
   cf-turnstile-response
   ```
