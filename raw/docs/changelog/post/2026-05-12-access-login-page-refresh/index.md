---
description: The Access login and one-time password pages now feature a modernized design with a unified authentication card and better mobile responsiveness.
title: Refreshed Access login page
image: https://developers.cloudflare.com/changelog/post/2026-05-12-access-login-page-refresh/og.png?v=5d0366de64f15f71
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 12, 2026

## Refreshed Access login page

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-12-access-login-page-refresh/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Access login page](https://developers.cloudflare.com/cloudflare-one/reusable-components/custom-pages/access-login-page/) and [one-time password (OTP)](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/one-time-pin/) page now feature a refreshed design that improves visual consistency, user trust, and mobile responsiveness.

**Before:**

![Screenshot of the previous Access login page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=532,height=906,format=webp/_astro/access-login-old.CwNVkCQH.png)

**After:**

![Screenshot of the updated Access login page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=541,height=722,format=webp/_astro/access-login-new.Y7WUfg9G.png)

The updated login experience includes:

- **Unified authentication card** - All sign-in options (identity provider buttons, email input, OTP) now appear in a single card with consistent styling, replacing the previous multi-section layout.
- **Consistent button styling** - Identity provider buttons use a uniform size and layout for easier scanning and selection.
- **Better mobile experience** - Responsive layout improvements ensure the login page renders correctly on phones and tablets.
- **Dark mode support** - The login page now supports dark mode.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-12-access-login-page-refresh/#page","headline":"Refreshed Access login page","description":"The Access login and one-time password pages now feature a modernized design with a unified authentication card and better mobile responsiveness.","url":"https://developers.cloudflare.com/changelog/post/2026-05-12-access-login-page-refresh/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-12-access-login-page-refresh/og.png?v=5d0366de64f15f71","dateModified":"2026-05-12","datePublished":"2026-05-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
