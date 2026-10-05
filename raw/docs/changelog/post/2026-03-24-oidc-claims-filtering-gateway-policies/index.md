---
description: Cloudflare Gateway now supports OIDC Claims as a selector in Firewall, Resolver, and Egress policies, enabling fine-grained identity-based traffic filtering using custom OIDC claims from your identity provider.
title: OIDC Claims filtering now available in Gateway Firewall, Resolver, and Egress policies
image: https://developers.cloudflare.com/changelog/post/2026-03-24-oidc-claims-filtering-gateway-policies/og.png?v=b49d7108f5244462
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 24, 2026

## OIDC Claims filtering now available in Gateway Firewall, Resolver, and Egress policies

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-24-oidc-claims-filtering-gateway-policies/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Gateway now supports [OIDC Claims](https://developers.cloudflare.com/cloudflare-one/traffic-policies/identity-selectors/#oidc-claims) as a selector in Firewall, Resolver, and Egress policies. Administrators can use custom OIDC claims from their identity provider to build fine-grained, identity-based traffic policies across all Gateway policy types.

With this update, you can:

- Filter traffic in [DNS](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/), [HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/), and [Network](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) firewall policies based on OIDC claim values.
- Apply custom [resolver policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/resolver-policies/) to route DNS queries to specific resolvers depending on a user's OIDC claims.
- Control [egress policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/) to assign dedicated egress IPs based on OIDC claim attributes.

For example, you can create a policy that routes traffic differently for users with `department=engineering` in their OIDC claims, or restrict access to certain destinations based on a user's role claim.

To get started, configure [custom OIDC claims](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-oidc/#custom-oidc-claims) on your identity provider and use the **OIDC Claims** selector in the Gateway policy builder.

For more information, refer to [Identity-based policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/identity-selectors/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-24-oidc-claims-filtering-gateway-policies/#page","headline":"OIDC Claims filtering now available in Gateway Firewall, Resolver, and Egress policies","description":"Cloudflare Gateway now supports OIDC Claims as a selector in Firewall, Resolver, and Egress policies, enabling fine-grained identity-based traffic filtering using custom OIDC claims from your identity provider.","url":"https://developers.cloudflare.com/changelog/post/2026-03-24-oidc-claims-filtering-gateway-policies/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-24-oidc-claims-filtering-gateway-policies/og.png?v=b49d7108f5244462","dateModified":"2026-03-24","datePublished":"2026-03-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
