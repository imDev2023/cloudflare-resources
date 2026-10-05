---
description: Cloudflare CASB adds two new granular roles, CASB Read and CASB, for more precise user access control.
title: CASB introduces new granular roles
image: https://developers.cloudflare.com/changelog/post/2025-10-28-casb-roles/og.png?v=4d77008b07947267
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 28, 2025

## CASB introduces new granular roles

[CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-28-casb-roles/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare CASB (Cloud Access Security Broker) now supports two new granular roles to provide more precise access control for your security teams:

- **Cloudflare CASB Read:** Provides read-only access to view CASB findings and dashboards. This role is ideal for security analysts, compliance auditors, or team members who need visibility without modification rights.
- **Cloudflare CASB:** Provides full administrative access to configure and manage all aspects of the CASB product.

These new roles help you better enforce the principle of least privilege. You can now grant specific members access to CASB security findings without assigning them broader permissions, such as the **Super Administrator** or **Administrator** roles.

To enable [Data Loss Prevention (DLP)](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/), scans in CASB, account members will need the **Cloudflare Zero Trust** role.

You can find these new roles when inviting members or creating API tokens in the Cloudflare dashboard under **Manage Account** > **Members**.

To learn more about managing roles and permissions, refer to the [Manage account members and roles documentation](https://developers.cloudflare.com/fundamentals/manage-members/roles/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-28-casb-roles/#page","headline":"CASB introduces new granular roles","description":"Cloudflare CASB adds two new granular roles, CASB Read and CASB, for more precise user access control.","url":"https://developers.cloudflare.com/changelog/post/2025-10-28-casb-roles/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-28-casb-roles/og.png?v=4d77008b07947267","dateModified":"2025-10-28","datePublished":"2025-10-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
