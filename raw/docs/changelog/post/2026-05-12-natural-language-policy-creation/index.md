---
description: Cloudflare Gateway now supports AI-powered policy creation, allowing administrators to describe a desired policy in plain language and receive a fully populated rule in the policy builder.
title: Create Gateway firewall policies with natural language
image: https://developers.cloudflare.com/changelog/post/2026-05-12-natural-language-policy-creation/og.png?v=dd47107dd6b38de1
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 12, 2026

## Create Gateway firewall policies with natural language

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-12-natural-language-policy-creation/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Gateway now supports natural language policy creation for [DNS](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/), [HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/), and [Network](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) firewall policies. Administrators can describe the outcome they want in plain language, and Cloudflare will generate a complete policy rule that populates the policy builder form.

![Create with AI button on the Gateway firewall policies page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2360,height=1088,format=webp/_astro/gateway-create-with-ai.BYG07coh.png)

To create a policy with natural language, select **Create with AI** on any Gateway firewall policy tab. Choose a policy type, describe what the policy should do, and a fully configured rule will appear in the policy builder for review. You can edit any field before saving, or re-generate with a different prompt.

The generated policy incorporates your account context - including lists, DLP profiles, applications, and device posture checks - so that references to your existing resources resolve automatically.

A built-in feedback mechanism allows you to rate each generated policy and provide optional comments, which Cloudflare uses to improve output quality over time.

For more information, refer to [Gateway firewall policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-12-natural-language-policy-creation/#page","headline":"Create Gateway firewall policies with natural language","description":"Cloudflare Gateway now supports AI-powered policy creation, allowing administrators to describe a desired policy in plain language and receive a fully populated rule in the policy builder.","url":"https://developers.cloudflare.com/changelog/post/2026-05-12-natural-language-policy-creation/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-12-natural-language-policy-creation/og.png?v=dd47107dd6b38de1","dateModified":"2026-05-12","datePublished":"2026-05-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
