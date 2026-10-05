---
description: Render RealtimeKit participant video as a floating Picture-in-Picture tile in the browser.
title: Picture in Picture
image: https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/pip/og.png?v=d37018f536cfe11e
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# Picture in Picture

Last updated Aug 24, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/pip/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Picture-in-Picture API allows you to render `meeting.participants.active` participant's video as a floating tile outside of the current webpage's context.

Note

Supported in Chrome, Edge, and Chromium-based browsers only.

WebMobile

ReactWeb ComponentsAngular

Picture-in-Picture is not available on this platform.

## Check support

Picture-in-Picture API might not be supported in your browser. Always check for support before using the API.

```js
const isSupported = meeting.participants.pip.isSupported();
```

## Enable Picture-in-Picture

```js
await meeting.participants.pip.enable();
```

## Disable Picture-in-Picture

```js
await meeting.participants.pip.disable();
```

## Check support

Picture-in-Picture API might not be supported in your browser. Always check for support before using the API.

```jsx
const isSupported = meeting.participants.pip.isSupported();
```

## Enable Picture-in-Picture

```jsx
await meeting.participants.pip.enable();
```

## Disable Picture-in-Picture

```jsx
await meeting.participants.pip.disable();
```
