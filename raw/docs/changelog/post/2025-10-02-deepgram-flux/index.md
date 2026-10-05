---
description: Partner voice activity detection model
title: New Deepgram Flux model available on Workers AI
image: https://developers.cloudflare.com/changelog/post/2025-10-02-deepgram-flux/og.png?v=8b2721765816bcf8
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 2, 2025

## New Deepgram Flux model available on Workers AI

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-02-deepgram-flux/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Deepgram's newest Flux model [`@cf/deepgram/flux`](https://developers.cloudflare.com/workers-ai/models/flux/) is now available on Workers AI, hosted directly on Cloudflare's infrastructure. We're excited to be a launch partner with Deepgram and offer their new Speech Recognition model built specifically for enabling voice agents. Check out [Deepgram's blog ↗︎](https://deepgram.com/flux) for more details on the release.

The Flux model can be used in conjunction with Deepgram's speech-to-text model [`@cf/deepgram/nova-3`](https://developers.cloudflare.com/workers-ai/models/nova-3/) and text-to-speech model [`@cf/deepgram/aura-1`](https://developers.cloudflare.com/workers-ai/models/aura-1/) to build end-to-end voice agents. Having Deepgram on Workers AI takes advantage of our edge GPU infrastructure, for ultra low latency voice AI applications.

#### Promotional Pricing

For the month of October 2025, Deepgram's Flux model will be free to use on Workers AI. Official pricing will be announced soon and charged after the promotional pricing period ends on October 31, 2025. Check out the [model page](https://developers.cloudflare.com/workers-ai/models/flux/) for pricing details in the future.

#### Example Usage

The new Flux model is WebSocket only as it requires live bi-directional streaming in order to recognize speech activity.

1. Create a worker that establishes a websocket connection with `@cf/deepgram/flux`

```js
export default {
  async fetch(request, env, ctx): Promise<Response> {
    const resp = await env.AI.run("@cf/deepgram/flux", {
      encoding: "linear16",
      sample_rate: "16000"
    }, {
      websocket: true
    });
    return resp;
  },
} satisfies ExportedHandler<Env>;
```

2. Deploy your worker

```bash
npx wrangler deploy
```

3. Write a client script to connect to your worker and start sending random audio bytes to it

```js
const ws = new WebSocket('wss://<your-worker-url.com>');

ws.onopen = () => {
  console.log('Connected to WebSocket');

  // Generate and send random audio bytes
  // You can replace this part with a function
  // that reads from your mic or other audio source
  const audioData = generateRandomAudio();
  ws.send(audioData);
  console.log('Audio data sent');
};

ws.onmessage = (event) => {
  // Transcription will be received here
  // Add your custom logic to parse the data
  console.log('Received:', event.data);
};

ws.onerror = (error) => {
  console.error('WebSocket error:', error);
};

ws.onclose = () => {
  console.log('WebSocket closed');
};

// Generate random audio data (1 second of noise at 44.1kHz, mono)
function generateRandomAudio() {
  const sampleRate = 44100;
  const duration = 1;
  const numSamples = sampleRate * duration;
  const buffer = new ArrayBuffer(numSamples * 2);
  const view = new Int16Array(buffer);

  for (let i = 0; i < numSamples; i++) {
    view[i] = Math.floor(Math.random() * 65536 - 32768);
  }

  return buffer;
}
```

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-02-deepgram-flux/#page","headline":"New Deepgram Flux model available on Workers AI","description":"Partner voice activity detection model","url":"https://developers.cloudflare.com/changelog/post/2025-10-02-deepgram-flux/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-02-deepgram-flux/og.png?v=8b2721765816bcf8","dateModified":"2025-10-02","datePublished":"2025-10-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
