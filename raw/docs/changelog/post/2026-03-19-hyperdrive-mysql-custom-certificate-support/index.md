---
description: Configure custom server certificates (VERIFY_CA, VERIFY_IDENTITY) and client certificates (mTLS) for MySQL connections through Hyperdrive.
title: Hyperdrive now supports custom TLS/SSL certificates for MySQL
image: https://developers.cloudflare.com/changelog/post/2026-03-19-hyperdrive-mysql-custom-certificate-support/og.png?v=a4d0b2ded3bc68eb
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 19, 2026

## Hyperdrive now supports custom TLS/SSL certificates for MySQL

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-19-hyperdrive-mysql-custom-certificate-support/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Hyperdrive now supports custom TLS/SSL certificates for MySQL databases, bringing the same certificate options previously available for PostgreSQL to MySQL connections.

You can now configure:

- **Server certificate verification** with `VERIFY_CA` or `VERIFY_IDENTITY` SSL modes to verify that your MySQL database server's certificate is signed by the expected certificate authority (CA).
- **Client certificates** (mTLS) for Hyperdrive to authenticate itself to your MySQL database with credentials beyond username and password.

Create a Hyperdrive configuration with custom certificates for MySQL:

```bash
# Upload a CA certificate
npx wrangler cert upload certificate-authority --ca-cert your-ca-cert.pem --name your-custom-ca-name

# Create a Hyperdrive with VERIFY_IDENTITY mode
npx wrangler hyperdrive create your-hyperdrive-config \
  --connection-string="mysql://user:password@hostname:port/database" \
  --ca-certificate-id <CA_CERT_ID> \
  --sslmode VERIFY_IDENTITY
```

For more information, refer to [SSL/TLS certificates for Hyperdrive](https://developers.cloudflare.com/hyperdrive/configuration/tls-ssl-certificates-for-hyperdrive/) and [MySQL TLS/SSL modes](https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-19-hyperdrive-mysql-custom-certificate-support/#page","headline":"Hyperdrive now supports custom TLS/SSL certificates for MySQL","description":"Configure custom server certificates (VERIFY_CA, VERIFY_IDENTITY) and client certificates (mTLS) for MySQL connections through Hyperdrive.","url":"https://developers.cloudflare.com/changelog/post/2026-03-19-hyperdrive-mysql-custom-certificate-support/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-19-hyperdrive-mysql-custom-certificate-support/og.png?v=a4d0b2ded3bc68eb","dateModified":"2026-03-19","datePublished":"2026-03-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
