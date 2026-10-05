---
description: "Cloudflare-generated 1xxx errors now return structured Markdown when requested with Accept: text/markdown."
title: Markdown responses for Cloudflare 1xxx errors
image: https://developers.cloudflare.com/changelog/post/2026-02-26-markdown-responses-for-1xxx-errors/og.png?v=4ee7b18625cd3fe8
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 26, 2026

## Markdown responses for Cloudflare 1xxx errors

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-26-markdown-responses-for-1xxx-errors/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare now returns structured Markdown responses for Cloudflare-generated 1xxx errors when clients send `Accept: text/markdown`.

Each response includes YAML frontmatter plus guidance sections (`What happened` / `What you should do`) so agents can make deterministic retry and escalation decisions without parsing HTML.

In measured 1,015 comparisons, Markdown reduced payload size and token footprint by over 98% versus HTML.

Included frontmatter fields:

- `error_code`, `error_name`, `error_category`, `http_status`
- `ray_id`, `timestamp`, `zone`
- `cloudflare_error`, `retryable`, `retry_after` (when applicable), `owner_action_required`

Default behavior is unchanged: clients that do not explicitly request Markdown continue to receive HTML error pages.

#### Negotiation behavior

Cloudflare uses standard HTTP content negotiation on the `Accept` header.

- `Accept: text/markdown` -> Markdown
- `Accept: text/markdown, text/html;q=0.9` -> Markdown
- `Accept: text/*` -> Markdown
- `Accept: */*` -> HTML (default browser behavior)

When multiple values are present, Cloudflare selects the highest-priority supported media type using `q` values. If Markdown is not explicitly preferred, HTML is returned.

#### Availability

Available now for Cloudflare-generated 1xxx errors.

#### Get started

```bash
curl -H "Accept: text/markdown" https://<your-domain>/cdn-cgi/error/1015
```

Reference: [Cloudflare 1xxx error documentation](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-26-markdown-responses-for-1xxx-errors/#page","headline":"Markdown responses for Cloudflare 1xxx errors","description":"Cloudflare-generated 1xxx errors now return structured Markdown when requested with Accept: text/markdown.","url":"https://developers.cloudflare.com/changelog/post/2026-02-26-markdown-responses-for-1xxx-errors/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-26-markdown-responses-for-1xxx-errors/og.png?v=4ee7b18625cd3fe8","dateModified":"2026-02-26","datePublished":"2026-02-26","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
