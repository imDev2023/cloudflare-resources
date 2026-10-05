---
description: Simplifying the management of users, groups, and permissions within Cloudflare.
title: Cloudflare User Groups &amp; Enhanced Permission Policies are now in Beta
image: https://developers.cloudflare.com/changelog/post/2025-06-02-user-groups-beta/og.png?v=444127fa36fcaf3d
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 2, 2025

## Cloudflare User Groups & Enhanced Permission Policies are now in Beta

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-02-user-groups-beta/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We're excited to announce the Public Beta launch of **User Groups for Cloudflare Dashboard** and **System for Cross Domain Identity Management (SCIM) User Groups**, expanding our RBAC capabilities to simplify user and group management at scale.

We've also visually overhauled the **Permission Policies UI** to make defining permissions more intuitive.

**What's New**

**User Groups \[BETA]**: [User Groups](https://developers.cloudflare.com/fundamentals/manage-members/user-groups/) are a new Cloudflare IAM primitive that enable administrators to create collections of account members that are treated equally from an access control perspective. User Groups can be assigned permission policies, with individual members in the group inheriting all permissions granted to the User Group. User Groups can be created manually or via our APIs.

**SCIM User Groups \[BETA]**: Centralize & simplify your user and group management at scale by syncing memberships directly from your upstream identity provider (like Okta or Entra ID) to the Cloudflare Platform. This ensures Cloudflare stays in sync with your identity provider, letting you apply Permission Policies to those synced groups directly within the Cloudflare Dashboard.

Note

SCIM Virtual Groups (identified by the pattern `CF-<accountID>-<Role Name>` in your IdP) are deprecated as of 06/02/25. We recommend migrating SCIM Virtual Groups implementations to use [SCIM User Groups](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/). If you did not use Virtual Groups, no action is needed.

**Revamped Permission Policies UI \[BETA]**: As Cloudflare's services have grown, so has the need for precise, role-based access control. We've given the Permission Policies builder a visual overhaul to make it much easier for administrators to find and define the exact permissions they want for specific principals.

![Updated Permissions Policy UX](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2872,height=1884,format=webp/_astro/2025-06-02-permissions-policy-ux.2wLEPgVX.png)

Note

When opting into the Beta for User Groups and Permission Policies, you'll be transitioning to a new experience. Please be aware that opting out isn't currently available.

For more info:

- [Get started with User Groups](https://developers.cloudflare.com/fundamentals/manage-members/user-groups/)
- [Explore our SCIM integration guide](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-02-user-groups-beta/#page","headline":"Cloudflare User Groups & Enhanced Permission Policies are now in Beta","description":"Simplifying the management of users, groups, and permissions within Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-06-02-user-groups-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-06-02-user-groups-beta/og.png?v=444127fa36fcaf3d","dateModified":"2025-06-02","datePublished":"2025-06-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
