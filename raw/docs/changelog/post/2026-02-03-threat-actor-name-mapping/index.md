---
description: Threat events now include aliases and common names for threat actors to help teams correlate intelligence across different platforms
title: Threat actor identification with &quot;also known as&quot; aliases
image: https://developers.cloudflare.com/changelog/post/2026-02-03-threat-actor-name-mapping/og.png?v=f7a921263fe71484
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 3, 2026

## Threat actor identification with "also known as" aliases

[Security Center](https://developers.cloudflare.com/security-center/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-03-threat-actor-name-mapping/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Identifying threat actors can be challenging, because naming conventions often vary across the security industry. To simplify your research, **Cloudflare Threat Events** now include an **Also known as** field, providing a list of common aliases and industry-standard names for the groups we track.

This new field is available in both the Cloudflare dashboard and via the API. In the dashboard, you can view these aliases by expanding the event details side panel (under the **Attacker** field) or by adding it as a column in your configurable table view.

#### Key benefits

- Easily map Cloudflare-tracked actors to the naming conventions used by other vendors without manual cross-referencing.
- Quickly identify if a detected threat actor matches a group your team is already monitoring via other intelligence feeds.

For more information on how to access this data, refer to the [Threat Events API documentation ↗︎](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-03-threat-actor-name-mapping/#page","headline":"Threat actor identification with \"also known as\" aliases","description":"Threat events now include aliases and common names for threat actors to help teams correlate intelligence across different platforms","url":"https://developers.cloudflare.com/changelog/post/2026-02-03-threat-actor-name-mapping/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-03-threat-actor-name-mapping/og.png?v=f7a921263fe71484","dateModified":"2026-02-03","datePublished":"2026-02-03","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
