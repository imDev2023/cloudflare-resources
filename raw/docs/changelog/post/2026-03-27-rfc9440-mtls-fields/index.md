---
description: Four new fields in request.cf.tlsClientAuth expose client certificate data in RFC 9440 format, making it simpler to forward mTLS certificate information to your origin.
title: New RFC 9440 mTLS certificate fields in Workers
image: https://developers.cloudflare.com/changelog/post/2026-03-27-rfc9440-mtls-fields/og.png?v=0034b5b37c87b549
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 27, 2026

## New RFC 9440 mTLS certificate fields in Workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-27-rfc9440-mtls-fields/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Four new fields are now available on `request.cf.tlsClientAuth` in Workers for requests that include a mutual TLS (mTLS) client certificate. These fields encode the client certificate and its intermediate chain in [RFC 9440 ↗︎](https://www.rfc-editor.org/rfc/rfc9440) format — the same standard format used by the `Client-Cert` and `Client-Cert-Chain` HTTP headers — so your Worker can forward them directly to your origin without any custom parsing or encoding logic.

#### New fields

| Field | Type | Description |
| --- | --- | --- |
| `certRFC9440` | String | The client leaf certificate in RFC 9440 format (`:base64-DER:`). Empty if no client certificate was presented. |
| `certRFC9440TooLarge` | Boolean | `true` if the leaf certificate exceeded 10 KB and was omitted from `certRFC9440`. |
| `certChainRFC9440` | String | The intermediate certificate chain in RFC 9440 format as a comma-separated list. Empty if no intermediates were sent or if the chain exceeded 16 KB. |
| `certChainRFC9440TooLarge` | Boolean | `true` if the intermediate chain exceeded 16 KB and was omitted from `certChainRFC9440`. |

#### Example: forwarding client certificate headers to your origin

```js
export default {
  async fetch(request) {
    const tls = request.cf.tlsClientAuth;

    // Only forward if cert was verified and chain is complete
    if (!tls || !tls.certVerified || tls.certRevoked || tls.certChainRFC9440TooLarge) {
      return new Response("Unauthorized", { status: 401 });
    }

    const headers = new Headers(request.headers);
    headers.set("Client-Cert", tls.certRFC9440);
    headers.set("Client-Cert-Chain", tls.certChainRFC9440);

    return fetch(new Request(request, { headers }));
  },
};
```

For more information, refer to [Client certificate variables](https://developers.cloudflare.com/ssl/client-certificates/client-certificate-variables/#workers-variables) and [Mutual TLS authentication](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-27-rfc9440-mtls-fields/#page","headline":"New RFC 9440 mTLS certificate fields in Workers","description":"Four new fields in request.cf.tlsClientAuth expose client certificate data in RFC 9440 format, making it simpler to forward mTLS certificate information to your origin.","url":"https://developers.cloudflare.com/changelog/post/2026-03-27-rfc9440-mtls-fields/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-27-rfc9440-mtls-fields/og.png?v=0034b5b37c87b549","dateModified":"2026-03-27","datePublished":"2026-03-27","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
