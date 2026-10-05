---
description: You can now configure custom certificates for secure database connections with Hyperdrive, including both server certificate verification and client certificates
title: Hyperdrive now supports custom TLS/SSL certificates
image: https://developers.cloudflare.com/changelog/post/2025-04-09-hyperdrive-custom-certificate-support/og.png?v=e96a305fd4d5314e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 9, 2025

## Hyperdrive now supports custom TLS/SSL certificates

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-09-hyperdrive-custom-certificate-support/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Hyperdrive now supports more SSL/TLS security options for your database connections:

- Configure Hyperdrive to verify server certificates with `verify-ca` or `verify-full` SSL modes and protect against man-in-the-middle attacks
- Configure Hyperdrive to provide client certificates to the database server to authenticate itself (mTLS) for stronger security beyond username and password

Use the new `wrangler cert` commands to create certificate authority (CA) certificate bundles or client certificate pairs:

```bash
# Create CA certificate bundle
npx wrangler cert upload certificate-authority --ca-cert your-ca-cert.pem --name your-custom-ca-name

# Create client certificate pair
npx wrangler cert upload mtls-certificate --cert client-cert.pem --key client-key.pem --name your-client-cert-name
```

Then create a Hyperdrive configuration with the certificates and desired SSL mode:

```bash
npx wrangler hyperdrive create your-hyperdrive-config \
  --connection-string="postgres://user:password@hostname:port/database" \
  --ca-certificate-id <CA_CERT_ID> \
  --mtls-certificate-id <CLIENT_CERT_ID>
  --sslmode verify-full
```

Learn more about [configuring SSL/TLS certificates for Hyperdrive](https://developers.cloudflare.com/hyperdrive/configuration/tls-ssl-certificates-for-hyperdrive/) to enhance your database security posture.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-09-hyperdrive-custom-certificate-support/#page","headline":"Hyperdrive now supports custom TLS/SSL certificates","description":"You can now configure custom certificates for secure database connections with Hyperdrive, including both server certificate verification and client certificates","url":"https://developers.cloudflare.com/changelog/post/2025-04-09-hyperdrive-custom-certificate-support/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-09-hyperdrive-custom-certificate-support/og.png?v=e96a305fd4d5314e","dateModified":"2025-04-09","datePublished":"2025-04-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
