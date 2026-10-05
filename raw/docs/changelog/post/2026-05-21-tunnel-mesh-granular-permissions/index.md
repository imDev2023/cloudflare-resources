---
description: New resource-scoped permissions allow administrators to grant access to specific Cloudflare Tunnel instances and Cloudflare Mesh nodes instead of all tunnels and nodes in an account.
title: Granular permissions for Cloudflare Tunnel and Cloudflare Mesh
image: https://developers.cloudflare.com/changelog/post/2026-05-21-tunnel-mesh-granular-permissions/og.png?v=f6421f8f6c8a3d62
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 21, 2026

## Granular permissions for Cloudflare Tunnel and Cloudflare Mesh

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Mesh](https://developers.cloudflare.com/mesh/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-21-tunnel-mesh-granular-permissions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now scope Cloudflare permissions to individual [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) instances and [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) nodes. Administrators can delegate access to specific Tunnels or Mesh nodes without granting account-wide control over private networking.

#### What is new

When you [add a member](https://developers.cloudflare.com/fundamentals/manage-members/manage/) or create a [permission policy](https://developers.cloudflare.com/fundamentals/manage-members/policies/), the resource picker now lists [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) instances and [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) nodes as scopable resource types. You can:

- Grant a read-only role on a single Cloudflare Tunnel instance to a support operator for log streaming and diagnostics — without exposing other Tunnels or destructive actions.
- Grant a write role on a specific Cloudflare Mesh node to an application team — without giving them access to the rest of your private network.
- Scope a single policy to one or many Tunnels and Mesh nodes at once.

#### How it works

Granular permissions are a parallel layer to existing account-level roles — they do not replace them.

- **Existing account-level roles continue to work.** A member with `Cloudflare Access` or `Cloudflare Zero Trust` retains write access to every Tunnel and Mesh node in the account. This ensures backward compatibility for existing automation and tokens.
- **Granular permissions are additive.** For any API request on a specific Tunnel or Mesh node, access is granted if the principal has **either** the account-level role **or** a granular permission for that resource.
- **Resource enumeration is authorization-aware.** Listing endpoints ( `GET /accounts/{id}/cfd_tunnel`, `GET /accounts/{id}/warp_connector`) return only the resources the principal has at least read access to.

#### Get started

- Configure [granular permissions for Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/guides/granular-permissions/).
- Configure [granular permissions for Cloudflare Tunnel and Cloudflare Mesh in Cloudflare One](https://developers.cloudflare.com/cloudflare-one/networks/connectors/granular-permissions/).
- Review the [resource-scoped roles](https://developers.cloudflare.com/fundamentals/manage-members/roles/#resource-scoped-roles) on the Cloudflare role reference.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-21-tunnel-mesh-granular-permissions/#page","headline":"Granular permissions for Cloudflare Tunnel and Cloudflare Mesh","description":"New resource-scoped permissions allow administrators to grant access to specific Cloudflare Tunnel instances and Cloudflare Mesh nodes instead of all tunnels and nodes in an account.","url":"https://developers.cloudflare.com/changelog/post/2026-05-21-tunnel-mesh-granular-permissions/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-21-tunnel-mesh-granular-permissions/og.png?v=f6421f8f6c8a3d62","dateModified":"2026-05-21","datePublished":"2026-05-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
