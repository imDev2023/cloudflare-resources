---
description: The Workers runtime adds opt-in post-quantum algorithms and key encapsulation methods through a compatibility flag.
title: Web Crypto adds ML-KEM and ML-DSA support
image: https://developers.cloudflare.com/changelog/post/2026-09-28-webcrypto-modern-algorithms/og.png?v=2e8cda1d0804d920
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 1, 2026

## Web Crypto adds ML-KEM and ML-DSA support

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-28-webcrypto-modern-algorithms/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The Workers Web Crypto API now supports ML-KEM-768, ML-KEM-1024, ML-DSA-44, ML-DSA-65, and ML-DSA-87. ML-KEM establishes shared secrets, while ML-DSA signs and verifies data.

The opt-in API also adds key encapsulation and decapsulation methods, `getPublicKey()`, `SubtleCrypto.supports()`, and JSON Web Keys (JWKs) with the `AKP` key type.

Turn on the `webcrypto_modern_algorithms` compatibility flag to use these features:

```jsonc
{
  "$schema": "./node_modules/wrangler/config-schema.json",
  "compatibility_flags": [
    "webcrypto_modern_algorithms"
  ]
}
```

```toml
compatibility_flags = ["webcrypto_modern_algorithms"]
```

This example uses ML-KEM-768 to establish the same shared secret on both sides:

*src/index.jsjs*

```js
const keyPair = await crypto.subtle.generateKey("ML-KEM-768", false, [
	"encapsulateBits",
	"decapsulateBits",
]);

if (!("publicKey" in keyPair)) {
	throw new Error("Expected an ML-KEM key pair");
}

const { sharedKey, ciphertext } = await crypto.subtle.encapsulateBits(
	"ML-KEM-768",
	keyPair.publicKey,
);

const recoveredSharedKey = await crypto.subtle.decapsulateBits(
	"ML-KEM-768",
	keyPair.privateKey,
	ciphertext,
);
```

*src/index.tsts*

```ts
const keyPair = await crypto.subtle.generateKey("ML-KEM-768", false, [
	"encapsulateBits",
	"decapsulateBits",
]);

if (!("publicKey" in keyPair)) {
	throw new Error("Expected an ML-KEM key pair");
}

const { sharedKey, ciphertext } = await crypto.subtle.encapsulateBits(
	"ML-KEM-768",
	keyPair.publicKey,
);

const recoveredSharedKey = await crypto.subtle.decapsulateBits(
	"ML-KEM-768",
	keyPair.privateKey,
	ciphertext,
);
```

Workers implements a subset of the evolving [Modern Algorithms in the Web Cryptography API ↗︎](https://wicg.github.io/webcrypto-modern-algos/) draft. ML-KEM-512 and the draft's other algorithms are not supported. The API may change as the draft evolves.

For current algorithm and operation support, refer to [Web Crypto supported algorithms](https://developers.cloudflare.com/workers/runtime-apis/web-crypto/#supported-algorithms).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-28-webcrypto-modern-algorithms/#page","headline":"Web Crypto adds ML-KEM and ML-DSA support","description":"The Workers runtime adds opt-in post-quantum algorithms and key encapsulation methods through a compatibility flag.","url":"https://developers.cloudflare.com/changelog/post/2026-09-28-webcrypto-modern-algorithms/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-28-webcrypto-modern-algorithms/og.png?v=2e8cda1d0804d920","dateModified":"2026-10-01","datePublished":"2026-10-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
