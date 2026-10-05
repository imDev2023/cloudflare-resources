---
description: Browser Run Session Recordings now include an Inspect panel for debugging console output, network activity, and page structure after a session ends.
title: Inspect logs, network requests, and DOM in Session Recordings
image: https://developers.cloudflare.com/changelog/post/2026-09-18-browser-run-session-recording-inspect/og.png?v=6981a58816a495a3
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 18, 2026

## Inspect logs, network requests, and DOM in Session Recordings

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-18-browser-run-session-recording-inspect/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Browser Run Session Recordings](https://developers.cloudflare.com/browser-run/features/session-recording/) now include an **Inspect** panel, giving you more context to understand what happened during a browser session without having to reproduce it.

![Inspecting logs, network requests, and the DOM in a Browser Run Session Recording](https://developers.cloudflare.com/images/browser-run/session-recording-inspect.gif)

The **Logs** tab lets you search captured console output and filter messages by level. The **Network** tab shows each request's method, status, headers, payload, response, and timing waterfall, with the option to download the session's network activity as a HAR file.

You can also [retrieve recorded network activity via API](https://developers.cloudflare.com/browser-run/features/session-recording/#retrieve-network-activity-via-api) as raw JSON or a HAR file for use in your own debugging and analysis workflows.

The **DOM** tab provides an expandable view of the page structure at the end of the recording and lets you copy the reconstructed HTML. For sessions with multiple browser tabs, the Inspect panel updates to show data for the tab selected in the recording viewer.

To get started, enable recording when launching a browser session. After the session closes, open **Browser Run** > **Runs** in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers/browser-run/runs) and select the recording icon next to the session.

Refer to the [Session recording documentation](https://developers.cloudflare.com/browser-run/features/session-recording/) for setup instructions and current limits.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-18-browser-run-session-recording-inspect/#page","headline":"Inspect logs, network requests, and DOM in Session Recordings","description":"Browser Run Session Recordings now include an Inspect panel for debugging console output, network activity, and page structure after a session ends.","url":"https://developers.cloudflare.com/changelog/post/2026-09-18-browser-run-session-recording-inspect/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-18-browser-run-session-recording-inspect/og.png?v=6981a58816a495a3","dateModified":"2026-09-18","datePublished":"2026-09-18","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
