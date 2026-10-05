---
description: Advanced DLP settings can now be configured at the account level for consistent enforcement across all profiles.
title: DLP account-level settings
image: https://developers.cloudflare.com/changelog/post/2025-04-14-account-level-dlp-settings/og.png?v=567ac6e9d6f8e36a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 14, 2026

## DLP account-level settings

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-14-account-level-dlp-settings/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

**Account-level DLP settings are now available** in Cloudflare One. You can now configure advanced DLP settings at the account level, including OCR, AI context analysis, and payload masking. This provides consistent enforcement across all DLP profiles and simplifies configuration management.

Key changes:

- **Consistent enforcement**: Settings configured at the account level apply to all DLP profiles
- **Simplified migration**: Settings enabled on any profile are automatically migrated to account level
- **Deprecation notice**: Profile-level advanced settings will be deprecated in a future release

**Migration details:**

During the migration period, if a setting is enabled on any profile, it will automatically be enabled at the account level. This means profiles that previously had a setting disabled may now have it enabled if another profile in the account had it enabled.

Settings are evaluated using OR logic - a setting is enabled if it is turned on at either the account level or the profile level. However, profile-level settings cannot be enabled when the account-level setting is off.

For more details, refer to the [DLP settings documentation](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-settings/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-14-account-level-dlp-settings/#page","headline":"DLP account-level settings","description":"Advanced DLP settings can now be configured at the account level for consistent enforcement across all profiles.","url":"https://developers.cloudflare.com/changelog/post/2025-04-14-account-level-dlp-settings/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-14-account-level-dlp-settings/og.png?v=567ac6e9d6f8e36a","dateModified":"2026-04-14","datePublished":"2026-04-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
