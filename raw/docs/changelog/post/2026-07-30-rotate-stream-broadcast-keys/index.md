---
description: Rotate credentials for a Stream live input without changing the live input ID or its other configuration.
title: Rotate Stream broadcast keys for live inputs
image: https://developers.cloudflare.com/changelog/post/2026-07-30-rotate-stream-broadcast-keys/og.png?v=081db3d3840b83cc
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 31, 2026

## Rotate Stream broadcast keys for live inputs

[Stream](https://developers.cloudflare.com/stream/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-30-rotate-stream-broadcast-keys/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now rotate the broadcast credentials for a Stream live input without changing the live input identifier.

Use key rotation when live input credentials may have been shared with the wrong audience, exposed in client code or a screenshare, or need to be refreshed as part of your security process. Rotating keys revokes the old credentials, disconnects broadcasts using stale credentials, and returns refreshed credentials in the API response.

To rotate keys for a live input, make a `POST` request to the `rotate_keys` endpoint:

```bash
curl --request POST \
https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/rotate_keys \
--header "Authorization: Bearer <API_TOKEN>"
```

Live input responses now also include `keysRotatedAt`, which indicates when the live input keys were last rotated. This field is omitted for live inputs whose keys have never been rotated.

For endpoint details, refer to [Rotate keys for a live input](https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/methods/rotate_keys/). For usage guidance, refer to [Manage live inputs](https://developers.cloudflare.com/stream/stream-live/start-stream-live/#manage-live-inputs).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-30-rotate-stream-broadcast-keys/#page","headline":"Rotate Stream broadcast keys for live inputs","description":"Rotate credentials for a Stream live input without changing the live input ID or its other configuration.","url":"https://developers.cloudflare.com/changelog/post/2026-07-30-rotate-stream-broadcast-keys/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-30-rotate-stream-broadcast-keys/og.png?v=081db3d3840b83cc","dateModified":"2026-07-31","datePublished":"2026-07-31","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
