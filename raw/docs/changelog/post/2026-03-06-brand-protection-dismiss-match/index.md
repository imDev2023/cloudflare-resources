---
description: Streamline your workflow by dismissing benign matches and toggling visibility of past reviews
title: Dismiss and filter matches in Brand Protection
image: https://developers.cloudflare.com/changelog/post/2026-03-06-brand-protection-dismiss-match/og.png?v=46ba81c1aa2d2f0b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 6, 2026

## Dismiss and filter matches in Brand Protection

[Security Center](https://developers.cloudflare.com/security-center/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-06-brand-protection-dismiss-match/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We have introduced new triage controls to help you manage your Brand Protection results more efficiently. You can now clear out the noise by dismissing matches while maintaining full visibility into your historical decisions.

#### What's new

- **Dismiss matches**: Users can now mark specific results as dismissed if they are determined to be benign or false positives, removing them from the primary triage view.
- **Show/Hide toggle**: A new visibility control allows you to instantly switch between viewing only active matches and including previously dismissed ones.
- **Persistent review states**: Dismissed status is saved across sessions, ensuring that your workspace remains organized and focused on new or high-priority threats.

#### Key benefits of the dismiss match functionality:

- Reduce alert fatigue by hiding known-safe results, allowing your team to focus exclusively on unreviewed or high-risk infringements.
- Auditability and recovery through the visibility toggle, ensuring that no match is ever truly "lost" and can be re-evaluated if a site's content changes.
- Improved collaboration as your team members can see which matches have already been vetted and dismissed by others.

Ready to clean up your match queue? Learn more in our [Brand Protection documentation](https://developers.cloudflare.com/security-center/brand-protection/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-06-brand-protection-dismiss-match/#page","headline":"Dismiss and filter matches in Brand Protection","description":"Streamline your workflow by dismissing benign matches and toggling visibility of past reviews","url":"https://developers.cloudflare.com/changelog/post/2026-03-06-brand-protection-dismiss-match/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-06-brand-protection-dismiss-match/og.png?v=46ba81c1aa2d2f0b","dateModified":"2026-03-06","datePublished":"2026-03-06","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
