---
description: Pivot from raw telemetry to rich strategic context with Threat Actor Profiles.
title: Introducing Threat Actor Profiles in Threat Events
image: https://developers.cloudflare.com/changelog/post/2026-06-08-threat-actor-profiles/og.png?v=e3f9f3618a766196
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 8, 2026

## Introducing Threat Actor Profiles in Threat Events

[Security Center](https://developers.cloudflare.com/security-center/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-08-threat-actor-profiles/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

**TL;DR:** We’ve launched **Threat Actor Profiles** directly inside the Threat Events dashboard. You can now immediately pivot from a generic alert or blocked event to a profile that unmasks the "Who, Why, and How" behind a threat event.

#### Why this matters

Security teams often suffer from a visibility gap. When an attack is blocked, it's difficult to know if it was a random automated bot or a sophisticated advanced persistent threat (APT) campaign specifically targeting your industry. Finding out usually means leaving your security dashboard to hunt through external OSINT feeds or static, out-of-date threat reports. Threat Actor Profiles solve this by sharing Cloudforce One’s deep adversary research directly inside your workflow:

- Cloudflare sees the traffic in real-time across approximately 20% of the web. This means actor profiles display active malicious infrastructure the moment it touches our global edge.
- Every profile provides clear strategic and tactical modules including alternative aliases, origin tracking, historical threat event volume, and MITRE ATT&CK mapping detailing the adversary's technical methods.
- You can search the dedicated threat actor directory or click an actor's name inside any threat event to view all details and related events to the specific threat actor.

#### How to use it

Adversary tracking is now available in the Cloudflare Dashbboard and ready to be included in your daily investigation workflow:

- Click on the **Threat Actor** name in the Threat Events table to open their full identity profile and review their aliases and attack stats.
- Navigate to **Cloudflare Dashboard > Application Security > Threat Intelligence** to explore the new **Threat Actors** tab. Here, you can browse a card-based directory of all established entities tracked by Cloudforce One.

Learn more in the [Cloudforce One documentation ↗︎](https://developers.cloudflare.com/security-center/cloudforce-one/#identify-the-adversary).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-08-threat-actor-profiles/#page","headline":"Introducing Threat Actor Profiles in Threat Events","description":"Pivot from raw telemetry to rich strategic context with Threat Actor Profiles.","url":"https://developers.cloudflare.com/changelog/post/2026-06-08-threat-actor-profiles/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-08-threat-actor-profiles/og.png?v=e3f9f3618a766196","dateModified":"2026-06-08","datePublished":"2026-06-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
