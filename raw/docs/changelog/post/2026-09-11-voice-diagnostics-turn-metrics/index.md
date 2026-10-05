---
description: "@cloudflare/voice v0.4.0 adds per-turn metrics and browser diagnostics for Voice Agents."
title: Inspect Voice Agent turn latency and outcomes
image: https://developers.cloudflare.com/changelog/post/2026-09-11-voice-diagnostics-turn-metrics/og.png?v=a4bb563d234b1bbe
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 11, 2026

## Inspect Voice Agent turn latency and outcomes

[Agents](https://developers.cloudflare.com/agents/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-11-voice-diagnostics-turn-metrics/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cloudflare/voice` v0.4.0 now lets you inspect where each Voice Agent turn spends time and how it ends.

```ts
client.addEventListener("turnmetrics", (turn) => {
	console.log(turn.outcome, turn.turnTotalMs);
});
```

#### About the Voice package

The `@cloudflare/voice` package lets you build real-time voice agents with Cloudflare Agents. It streams microphone audio to an Agent over WebSocket, transcribes speech, runs your model through `onTurn()`, converts the response to speech, and streams audio back to the caller.

A turn moves through several stages:

```txt
User speaks -> speech-to-text -> model -> text-to-speech -> audio
```

Previously, the package's four aggregate metrics covered successful, non-empty speech turns. They did not show how failed, aborted, empty, or text turns ended.

#### Turn metrics

Each speech or text turn now produces a typed `VoiceTurnMetrics` summary with:

- A `turnId` for correlating events from the same turn.
- A terminal outcome such as `completed`, `no_output`, `output_limit`, `content_filtered`, `model_error`, `tts_error`, or `aborted`.
- Timings for important stages, including speech-to-final-transcript, model-to-first-text, TTS-to-first-audio, and total turn duration.

These timings can overlap and are not additive. Timings for stages that a turn did not reach are omitted.

The latest summary is available through `VoiceClient`, `useVoiceAgent()`, and `useVoiceInput()`. Voice input includes only the speech and transcription timings it can measure.

If an agent produces no audio, you can now distinguish between the model returning no output, reaching an output limit, encountering content filtering, or failing.

#### Additional diagnostics

For local debugging, you can forward server lifecycle events to the browser console:

```js
import { Agent } from "agents";
import { withVoice } from "@cloudflare/voice";

const VoiceAgent = withVoice(Agent, {
	diagnostics: {
		browserConsole: true,
	},
});
```

```ts
import { Agent } from "agents";
import { withVoice } from "@cloudflare/voice";

const VoiceAgent = withVoice(Agent, {
	diagnostics: {
		browserConsole: true,
	},
});
```

The browser console combines server lifecycle events with local microphone, connection, and playback events, including model start, first model text, first audio, and playback start. Diagnostics are off by default, and their event names and fields can change.

`VoiceClient` also exposes typed events for speech-to-text failures, connection errors, and model outcomes. The SDK removes known content fields and does not read arbitrary provider responses, but custom error messages must not contain sensitive data.

Install the release with a compatible Agents SDK version:

npmyarnpnpmbun

```
npm i @cloudflare/voice@^0.4.0 agents@^0.22.0
```

```
yarn add @cloudflare/voice@^0.4.0 agents@^0.22.0
```

```
pnpm add @cloudflare/voice@^0.4.0 agents@^0.22.0
```

```
bun add @cloudflare/voice@^0.4.0 agents@^0.22.0
```

Refer to the [Voice pipeline metrics](https://developers.cloudflare.com/agents/communication-channels/voice/#pipeline-metrics) and [Voice Agent example ↗︎](https://github.com/cloudflare/agents/tree/main/examples/voice-agent) to get started.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-11-voice-diagnostics-turn-metrics/#page","headline":"Inspect Voice Agent turn latency and outcomes","description":"@cloudflare/voice v0.4.0 adds per-turn metrics and browser diagnostics for Voice Agents.","url":"https://developers.cloudflare.com/changelog/post/2026-09-11-voice-diagnostics-turn-metrics/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-11-voice-diagnostics-turn-metrics/og.png?v=a4bb563d234b1bbe","dateModified":"2026-09-11","datePublished":"2026-09-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
