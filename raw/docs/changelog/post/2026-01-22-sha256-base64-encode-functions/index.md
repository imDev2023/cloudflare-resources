---
description: Rulesets now support encode_base64() and sha256() functions for generating signed request headers directly in expressions.
title: New cryptographic functions — encode_base64() and sha256()
image: https://developers.cloudflare.com/changelog/post/2026-01-22-sha256-base64-encode-functions/og.png?v=0f6b7225ae576e18
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 22, 2026

## New cryptographic functions — encode\_base64() and sha256()

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-22-sha256-base64-encode-functions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Rulesets now includes `encode_base64()` and `sha256()` functions, enabling you to generate signed request headers directly in rule expressions. These functions support common patterns like constructing a canonical string from request attributes, computing a SHA256 digest, and Base64-encoding the result.

---

#### New functions

| Function | Description | Availability |
| --- | --- | --- |
| `encode_base64(input, flags)` | Encodes a string to Base64 format. Optional `flags` parameter: `u` for URL-safe encoding, `p` for padding (adds `=` characters to make the output length a multiple of 4, as required by some systems). By default, output is standard Base64 without padding. | All plans (in header transform rules) |
| `sha256(input)` | Computes a SHA256 hash of the input string. | Requires enablement |

Note

The `sha256()` function is available as an Enterprise add-on and requires a specific entitlement. Contact your account team to enable it.

---

#### Examples

**Encode a string to Base64 format:**

```txt
encode_base64("hello world")
```

Returns: `aGVsbG8gd29ybGQ`

**Encode a string to Base64 format with padding:**

```txt
encode_base64("hello world", "p")
```

Returns: `aGVsbG8gd29ybGQ=`

**Perform a URL-safe Base64 encoding of a string:**

```txt
encode_base64("hello world", "u")
```

Returns: `aGVsbG8gd29ybGQ`

**Compute the SHA256 hash of a secret token:**

```txt
sha256("my-token")
```

Returns a hash that your origin can validate to authenticate requests.

**Compute the SHA256 hash of a string and encode the result to Base64 format:**

```txt
encode_base64(sha256("my-token"))
```

Combines hashing and encoding for systems that expect Base64-encoded signatures.

For more information, refer to the [Functions reference](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-22-sha256-base64-encode-functions/#page","headline":"New cryptographic functions — encode_base64() and sha256()","description":"Rulesets now support encode_base64() and sha256() functions for generating signed request headers directly in expressions.","url":"https://developers.cloudflare.com/changelog/post/2026-01-22-sha256-base64-encode-functions/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-22-sha256-base64-encode-functions/og.png?v=0f6b7225ae576e18","dateModified":"2026-01-22","datePublished":"2026-01-22","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
