---
description: Register a virtual appliance, generate its license key, and rotate the key directly from the Connectors page.
title: Self-serve registration of Cloudflare One Virtual Appliance in the dashboard
image: https://developers.cloudflare.com/changelog/post/2026-07-06-virtual-appliance-self-serve-ui/og.png?v=2dd5e511f81d6908
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 6, 2026

## Self-serve registration of Cloudflare One Virtual Appliance in the dashboard

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-06-virtual-appliance-self-serve-ui/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now register a [Cloudflare One Virtual Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) and generate its license key directly from the dashboard, without contacting your account team.

![Registering a Cloudflare One Virtual Appliance and generating its authentication key from the Connectors page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=988,format=webp/_astro/2026-07-06-virtual-appliance-self-serve-ui.Dn2NC_ql.gif)

- On the **Connectors** page, select **Add an appliance** and choose **Virtual appliance** to register a virtual appliance and generate its authentication key.
- Use **Regenerate authentication key** from a virtual appliance connector's menu to rotate its key. The previous key is immediately and irrevocably revoked.
- The authentication key is shown only once — copy and store it securely.

This complements the existing [API and Terraform self-serve workflow](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#register-a-virtual-appliance-and-generate-a-license-key) for provisioning virtual appliances. Hardware appliances continue to use the existing account-team fulfillment workflow.

For details, refer to [Configure a Cloudflare One Virtual Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-06-virtual-appliance-self-serve-ui/#page","headline":"Self-serve registration of Cloudflare One Virtual Appliance in the dashboard","description":"Register a virtual appliance, generate its license key, and rotate the key directly from the Connectors page.","url":"https://developers.cloudflare.com/changelog/post/2026-07-06-virtual-appliance-self-serve-ui/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-06-virtual-appliance-self-serve-ui/og.png?v=2dd5e511f81d6908","dateModified":"2026-07-06","datePublished":"2026-07-06","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
