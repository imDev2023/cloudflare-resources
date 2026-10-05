---
description: Emails will need to be authenticated either via SPF or DKIM in order to be forwarded.
title: Mail authentication requirements for Email Routing
image: https://developers.cloudflare.com/changelog/post/2025-06-30-mail-authentication/og.png?v=72095ea402efa1c2
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 30, 2025

## Mail authentication requirements for Email Routing

[Email Service](https://developers.cloudflare.com/email-service/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-30-mail-authentication/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The Email Routing platform supports [SPF ↗︎](https://datatracker.ietf.org/doc/html/rfc7208) records and [DKIM (DomainKeys Identified Mail) ↗︎](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail) signatures and honors these protocols when the sending domain has them configured. However, if the sending domain doesn't implement them, we still forward the emails to upstream mailbox providers.

Starting on July 3, 2025, we will require all emails to be authenticated using at least one of the protocols, SPF or DKIM, to forward them. We also strongly recommend that all senders implement the DMARC protocol.

If you are using a Worker with an Email trigger to receive email messages and forward them upstream, you will need to handle the case where the forward action may fail due to missing authentication on the incoming email.

SPAM has been a long-standing issue with email. By enforcing mail authentication, we will increase the efficiency of identifying abusive senders and blocking bad emails. If you're an email server delivering emails to large mailbox providers, it's likely you already use these protocols; otherwise, please ensure you have them properly configured.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-30-mail-authentication/#page","headline":"Mail authentication requirements for Email Routing","description":"Emails will need to be authenticated either via SPF or DKIM in order to be forwarded.","url":"https://developers.cloudflare.com/changelog/post/2025-06-30-mail-authentication/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-06-30-mail-authentication/og.png?v=72095ea402efa1c2","dateModified":"2025-06-30","datePublished":"2025-06-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
