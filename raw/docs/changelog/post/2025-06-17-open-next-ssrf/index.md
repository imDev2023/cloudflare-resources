---
description: Mitigations have been put in place for all existing and future deployments of sites with the Cloudflare adapter for Open Next in response to an identified Server-Side Request Forgery (SSRF) vulnerability in the @opennextjs/cloudflare package
title: SSRF vulnerability in @opennextjs/cloudflare proactively mitigated for all Cloudflare customers
image: https://developers.cloudflare.com/changelog/post/2025-06-17-open-next-ssrf/og.png?v=b043d7d9fd051300
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 17, 2025

## SSRF vulnerability in @opennextjs/cloudflare proactively mitigated for all Cloudflare customers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-17-open-next-ssrf/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Mitigations have been put in place for all existing and future deployments of sites with the Cloudflare adapter for Open Next in response to an identified Server-Side Request Forgery (SSRF) vulnerability in the `@opennextjs/cloudflare` package.

The vulnerability stemmed from an unimplemented feature in the Cloudflare adapter for Open Next, which allowed users to proxy arbitrary remote content via the `/_next/image` endpoint.

This issue allowed attackers to load remote resources from arbitrary hosts under the victim site's domain for any site deployed using the Cloudflare adapter for Open Next. For example: `https://victim-site.com/_next/image?url=https://attacker.com`. In this example, attacker-controlled content from `attacker.com` is served through the victim site's domain (`victim-site.com`), violating the same-origin policy and potentially misleading users or other services.

References: [https://www.cve.org/cverecord?id=CVE-2025-6087 ↗︎](https://www.cve.org/cverecord?id=CVE-2025-6087), [https://github.com/opennextjs/opennextjs-cloudflare/security/advisories/GHSA-rvpw-p7vw-wj3m ↗︎](https://github.com/opennextjs/opennextjs-cloudflare/security/advisories/GHSA-rvpw-p7vw-wj3m)

#### Impact

- SSRF via unrestricted remote URL loading
- Arbitrary remote content loading
- Potential internal service exposure or phishing risks through domain abuse

#### Mitigation

The following mitigations have been put in place:

**Server side updates** to Cloudflare's platform to restrict the content loaded via the `/_next/image` endpoint to images. The update automatically mitigates the issue for all existing and any future sites deployed to Cloudflare using the affected version of the Cloudflare adapter for Open Next

**Root cause fix:** Pull request [#727 ↗︎](https://github.com/opennextjs/opennextjs-cloudflare/pull/727) to the Cloudflare adapter for Open Next. The patched version of the adapter has been released as `@opennextjs/cloudflare@1.3.0`

**Package dependency update:** Pull request [cloudflare/workers-sdk#9608 ↗︎](https://github.com/cloudflare/workers-sdk/pull/9608) to create-cloudflare (c3) to use the fixed version of the Cloudflare adapter for Open Next. The patched version of create-cloudflare has been published as `create-cloudflare@2.49.3`.

In addition to the automatic mitigation deployed on Cloudflare's platform, we encourage affected users to upgrade to `@opennext/cloudflare` v1.3.0 and use the [`remotePatterns` ↗︎](https://nextjs.org/docs/pages/api-reference/components/image#remotepatterns) filter in Next config if they need to allow-list external urls with images assets.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-17-open-next-ssrf/#page","headline":"SSRF vulnerability in @opennextjs/cloudflare proactively mitigated for all Cloudflare customers","description":"Mitigations have been put in place for all existing and future deployments of sites with the Cloudflare adapter for Open Next in response to an identified Server-Side Request Forgery (SSRF) vulnerability in the @opennextjs/cloudflare package","url":"https://developers.cloudflare.com/changelog/post/2025-06-17-open-next-ssrf/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-06-17-open-next-ssrf/og.png?v=b043d7d9fd051300","dateModified":"2025-06-17","datePublished":"2025-06-17","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
