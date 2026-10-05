---
description: Restrict which WebAuthn authenticators users can enroll and allow users to skip redundant MFA prompts when they have already performed MFA using their IdP.
title: AAGUID restrictions and AMR matching for Access independent MFA
image: https://developers.cloudflare.com/changelog/post/2026-04-23-independent-mfa-aaguid-amr/og.png?v=a666c2c5f7f1632b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 23, 2026

## AAGUID restrictions and AMR matching for Access independent MFA

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-23-independent-mfa-aaguid-amr/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Independent MFA](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/independent-mfa/) in Cloudflare Access now supports two additional organization-level controls:

- **[Restrict authenticators by AAGUID](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/independent-mfa/#restrict-authenticators-by-aaguid)** — Limit enrollment to a specific set of WebAuthn authenticators using their [AAGUID ↗︎](https://fidoalliance.org/specs/fido-v2.0-id-20180227/fido-registry-v2.0-id-20180227.html#authenticator-attestation-guid). This is useful for organizations that require FIPS-validated security keys or company-issued hardware. AAGUIDs are managed through a new [List](https://developers.cloudflare.com/cloudflare-one/reusable-components/lists/) type.
- **[AMR matching](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/independent-mfa/#use-identity-provider-mfa)** — Skip the independent MFA prompt when the identity provider has already performed an equivalent MFA. Access reads the `amr` claim defined in [RFC 8176 ↗︎](https://datatracker.ietf.org/doc/html/rfc8176) and matches supported values such as `hwk`, `otp`, and `fpt` to the authenticator types allowed on the application or policy. This prevents users from having to complete MFA twice when their identity provider already enforces it.

To get started, refer to [Independent MFA](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/independent-mfa/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-23-independent-mfa-aaguid-amr/#page","headline":"AAGUID restrictions and AMR matching for Access independent MFA","description":"Restrict which WebAuthn authenticators users can enroll and allow users to skip redundant MFA prompts when they have already performed MFA using their IdP.","url":"https://developers.cloudflare.com/changelog/post/2026-04-23-independent-mfa-aaguid-amr/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-23-independent-mfa-aaguid-amr/og.png?v=a666c2c5f7f1632b","dateModified":"2026-04-23","datePublished":"2026-04-23","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
