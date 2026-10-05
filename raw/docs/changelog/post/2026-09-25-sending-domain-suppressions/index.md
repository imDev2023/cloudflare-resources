---
description: Email Sending suppressions can now apply to one sending domain instead of every sending domain in your account.
title: Suppress recipients for one sending domain
image: https://developers.cloudflare.com/changelog/post/2026-09-25-sending-domain-suppressions/og.png?v=80666514790e2e1b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 25, 2026

## Suppress recipients for one sending domain

[Email Service](https://developers.cloudflare.com/email-service/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-25-sending-domain-suppressions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Email Sending suppressions](https://developers.cloudflare.com/email-service/concepts/suppressions/) now have a **scope**:

- **`account`**: The suppression applies to every sending domain and subdomain in your account. This is the default.
- **`sending_domain`**: The suppression applies to one sending domain only. A suppression for `mail.myappexample.com` does not block mail from `myappexample.com`.

Most importantly, Email Sending now automatically creates bounce and complaint suppressions at the sending-domain level. This provides greater granularity by preventing an issue with one sending domain from suppressing the recipient across your entire account.

To add a suppression for one sending domain in the dashboard, go to **Email Sending** > **Suppressions** and select **Sending domain** in **Scope**. Imports can also set a scope for each row or a default scope.

In the API, pass `scope` when you create the suppression:

```bash
curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/email/sending/suppressions \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "email": "user@example.net",
    "scope": { "type": "sending_domain", "value": "mail.myappexample.com" }
  }'
```

The [suppressions API](https://developers.cloudflare.com/api/resources/email_sending/subresources/suppressions/) returns `scope` on every suppression. To list the suppressions for one domain, use `scope_type=sending_domain&scope_value=mail.myappexample.com`. If you omit `scope`, the API creates an `account` suppression, so existing integrations continue to work.

Refer to [Suppression lists](https://developers.cloudflare.com/email-service/concepts/suppressions/#suppression-scope) and [Manage suppressions](https://developers.cloudflare.com/email-service/configuration/suppressions/) for details.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-25-sending-domain-suppressions/#page","headline":"Suppress recipients for one sending domain","description":"Email Sending suppressions can now apply to one sending domain instead of every sending domain in your account.","url":"https://developers.cloudflare.com/changelog/post/2026-09-25-sending-domain-suppressions/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-25-sending-domain-suppressions/og.png?v=80666514790e2e1b","dateModified":"2026-09-25","datePublished":"2026-09-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
