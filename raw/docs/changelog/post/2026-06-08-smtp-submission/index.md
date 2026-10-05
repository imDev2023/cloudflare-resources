---
description: Send transactional emails through Cloudflare Email Service from any SMTP-capable application or mail client using authenticated SMTP submission on smtp.mx.cloudflare.net.
title: Authenticated SMTP submission now available in beta
image: https://developers.cloudflare.com/changelog/post/2026-06-08-smtp-submission/og.png?v=7fbf2b3fb0b5cdee
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 8, 2026

## Authenticated SMTP submission now available in beta

[Email Service](https://developers.cloudflare.com/email-service/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-08-smtp-submission/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now send emails through **Cloudflare Email Service** using authenticated [SMTP submission](https://developers.cloudflare.com/email-service/api/send-emails/smtp/) on `smtp.mx.cloudflare.net:465`. SMTP joins the [REST API](https://developers.cloudflare.com/email-service/api/send-emails/rest-api/) and the [Workers binding](https://developers.cloudflare.com/email-service/api/send-emails/workers-api/) as a third way to send transactional email — useful for existing applications that already speak SMTP and language-native SMTP libraries (Nodemailer, `smtplib`, PHPMailer, JavaMail).

| Setting | Value |
| --- | --- |
| Host | `smtp.mx.cloudflare.net` |
| Port | `465` (implicit TLS) |
| AUTH | `PLAIN` or `LOGIN` |
| Username | `api_token` |
| Password | A Cloudflare API token (account-owned or user-owned) with **Email Sending: Edit** |

Submissions enter the same delivery pipeline as the REST API and Workers binding: identical [limits](https://developers.cloudflare.com/email-service/platform/limits/), automatic DKIM and ARC signing, and shared dashboard logs.

Send your first email with a single command:

```sh
curl --ssl-reqd \
  --url "smtps://smtp.mx.cloudflare.net:465" \
  --user "api_token:<API_TOKEN>" \
  --mail-from "welcome@yourdomain.com" \
  --mail-rcpt "user@example.com" \
  --upload-file mail.txt
```

Refer to the [SMTP reference](https://developers.cloudflare.com/email-service/api/send-emails/smtp/) for authentication details, response codes, and language-specific examples.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-08-smtp-submission/#page","headline":"Authenticated SMTP submission now available in beta","description":"Send transactional emails through Cloudflare Email Service from any SMTP-capable application or mail client using authenticated SMTP submission on smtp.mx.cloudflare.net.","url":"https://developers.cloudflare.com/changelog/post/2026-06-08-smtp-submission/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-08-smtp-submission/og.png?v=7fbf2b3fb0b5cdee","dateModified":"2026-06-08","datePublished":"2026-06-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
