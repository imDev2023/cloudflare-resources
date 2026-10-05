---
description: Delegate certificate signing to downstream key servers.
title: Keyless delegation
image: https://developers.cloudflare.com/ssl/keyless-ssl/reference/keyless-delegation/og.png?v=a7a8b2d8571e0654
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ssl/llms.txt  
> Use this file to discover all available pages before exploring further.

# Keyless delegation

Last updated May 5, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ssl/keyless-ssl/reference/keyless-delegation/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Keyless Delegation is Cloudflare's implementation of the emerging delegated credentials standard ([RFC 9345 ↗︎](https://www.rfc-editor.org/rfc/rfc9345.html)). When you upload a certificate for use with Keyless that has the special extension permitting the use of delegated credentials, Cloudflare will automatically produce a delegated credential and use it at the edge with clients that support this feature. The handshakes will complete without the extra latency induced by reaching back to the Keyless Server, and there are [additional advantages to flexibility in algorithm choice ↗︎](https://blog.cloudflare.com/keyless-delegation/).

Behind the scenes we periodically create delegated credentials and sign them via Keyless, through the same mechanism used to sign the Certificate Verify messages our servers send when using Keyless. These credentials have a short lifetime, ensuring that if you disable Keyless the credentials created will become invalid within 24 hours. Supporting clients validate the credential, and the server can use the key it generated to sign the response to the TLS handshake without the round trip.

For security reasons certificates must contain a special identifier for use with delegated credentials. This takes the form of an optional X509 extension with NULL contents and the OID 1.3.6.1.4.1.44363.44. Your CA may need to make code changes to support delegated credentials.

Currently very few clients support delegated credentials, and only a handful of certificate authorities will issue certificates with the extension. We have had success with DigiCert. Firefox 77 and later support delegated credentials.
