---
description: Recommended cipher suite security levels for different use cases.
title: Security levels
image: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/recommendations/og.png?v=faaf5a97cda95eb1
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ssl/llms.txt  
> Use this file to discover all available pages before exploring further.

# Security levels

Last updated Apr 17, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/recommendations/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Refer to the sections below for three different security levels and how Cloudflare recommends that you set them up if you need to restrict the [cipher suites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/) used between Cloudflare and clients that access your website or application.

Refer to [Customize cipher suites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/) to learn how to specify cipher suites at zone level or per hostname.

Caution

Before opting for [compatible](#compatible) or [modern](#modern), review the [related SSL/TLS settings](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/#related-ssltls-settings)<sup>[1](#user-content-fn-4)</sup>.

## Modern

Offers the best security and performance, limiting your range of clients to modern devices and browsers. Supports TLS 1.2-1.3 cipher suites. All suites are forward-secret and support authenticated encryption (AEAD).

<details>

<summary>

Cipher suites list

</summary>

<code>AEAD-AES128-GCM-SHA256</code><sup><a href="#user-content-fn-1">2</a></sup>, <code>AEAD-AES256-GCM-SHA384</code><sup><a href="#user-content-fn-2">3</a></sup>, <code>AEAD-CHACHA20-POLY1305-SHA256</code><sup><a href="#user-content-fn-3">4</a></sup>,<code>ECDHE-ECDSA-AES128-GCM-SHA256</code>, <code>ECDHE-ECDSA-CHACHA20-POLY1305</code>, <code>ECDHE-RSA-AES128-GCM-SHA256</code>, <code>ECDHE-RSA-CHACHA20-POLY1305</code>, <code>ECDHE-ECDSA-AES256-GCM-SHA384</code>, <code>ECDHE-RSA-AES256-GCM-SHA384</code>

</details>

If you are customizing cipher suites via API, refer to [Steps and API examples](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/api/#steps-and-api-examples) for a snippet you can copy with the formatted array.

## Compatible

Provides broader compatibility with somewhat weaker security. Supports TLS 1.2-1.3 cipher suites. All suites are forward-secret.

<details>

<summary>

Cipher suites list

</summary>

<code>AEAD-AES128-GCM-SHA256</code><sup><a href="#user-content-fn-1">2</a></sup>, <code>AEAD-AES256-GCM-SHA384</code><sup><a href="#user-content-fn-2">3</a></sup>, <code>AEAD-CHACHA20-POLY1305-SHA256</code><sup><a href="#user-content-fn-3">4</a></sup>, <code>ECDHE-ECDSA-AES128-GCM-SHA256</code>, <code>ECDHE-ECDSA-CHACHA20-POLY1305</code>, <code>ECDHE-RSA-AES128-GCM-SHA256</code>, <code>ECDHE-RSA-CHACHA20-POLY1305</code>, <code>ECDHE-ECDSA-AES256-GCM-SHA384</code>, <code>ECDHE-RSA-AES256-GCM-SHA384</code>, <code>ECDHE-ECDSA-AES128-SHA256</code>, <code>ECDHE-RSA-AES128-SHA256</code>, <code>ECDHE-ECDSA-AES256-SHA384</code>, <code>ECDHE-RSA-AES256-SHA384</code>

</details>

If you are customizing cipher suites via API, refer to [Steps and API examples](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/api/#steps-and-api-examples) for a snippet you can copy with the formatted array.

## Legacy (default)

Includes all cipher suites that Cloudflare supports today. Broadest compatibility with the weakest security. Supports TLS 1.0-1.3 cipher suites.

<details>

<summary>

Cipher suites list

</summary>

<code>AEAD-AES128-GCM-SHA256</code><sup><a href="#user-content-fn-1">2</a></sup>, <code>AEAD-AES256-GCM-SHA384</code><sup><a href="#user-content-fn-2">3</a></sup>, <code>AEAD-CHACHA20-POLY1305-SHA256</code><sup><a href="#user-content-fn-3">4</a></sup>, <code>ECDHE-ECDSA-AES128-GCM-SHA256</code>, <code>ECDHE-ECDSA-CHACHA20-POLY1305</code>, <code>ECDHE-RSA-AES128-GCM-SHA256</code>, <code>ECDHE-RSA-CHACHA20-POLY1305</code>, <code>ECDHE-ECDSA-AES256-GCM-SHA384</code>, <code>ECDHE-RSA-AES256-GCM-SHA384</code>, <code>ECDHE-ECDSA-AES128-SHA256</code>, <code>ECDHE-RSA-AES128-SHA256</code>, <code>ECDHE-ECDSA-AES256-SHA384</code>, <code>ECDHE-RSA-AES256-SHA384</code>, <code>ECDHE-ECDSA-AES128-SHA</code>, <code>ECDHE-RSA-AES128-SHA</code>, <code>AES128-GCM-SHA256</code>, <code>AES128-SHA256</code>, <code>AES128-SHA</code>, <code>ECDHE-RSA-AES256-SHA</code>, <code>AES256-GCM-SHA384</code>, <code>AES256-SHA256</code>, <code>AES256-SHA</code>, <code>DES-CBC3-SHA</code>

</details>

To reset your option to the default, [use an empty array](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/#reset-to-default-values).

## Footnotes

1. Although configured independently, cipher suites interact with **Minimum TLS version** and **TLS 1.3**. [↩](#user-content-fnref-4)
2. Same as `TLS_AES_128_GCM_SHA256`. Refer to [TLS 1.3 cipher suites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/#tls-13) for details. [↩](#user-content-fnref-1) [↩<sup>2</sup>](#user-content-fnref-1-2) [↩<sup>3</sup>](#user-content-fnref-1-3)
3. Same as `TLS_AES_256_GCM_SHA384`. Refer to [TLS 1.3 cipher suites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/#tls-13) for details. [↩](#user-content-fnref-2) [↩<sup>2</sup>](#user-content-fnref-2-2) [↩<sup>3</sup>](#user-content-fnref-2-3)
4. Same as `TLS_CHACHA20_POLY1305_SHA256`. Refer to [TLS 1.3 cipher suites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/#tls-13) for details. [↩](#user-content-fnref-3) [↩<sup>2</sup>](#user-content-fnref-3-2) [↩<sup>3</sup>](#user-content-fnref-3-3)
