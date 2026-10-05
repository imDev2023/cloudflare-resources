---
description: API reference for RtkParticipantsAudio component (React Library)
title: RtkParticipantsAudio
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsaudio/og.png?v=9340f1c1eeb897a3
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkParticipantsAudio

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsaudio/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which plays all the audio from participants and screenshares.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `preloadedAudioElem` | `HTMLAudioElement` | ✅ | - | Pass existing audio element |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkParticipantsAudio } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkParticipantsAudio />;
}
```

### With Properties

```tsx
import { RtkParticipantsAudio } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkParticipantsAudio
      meeting={meeting}
      preloadedAudioElem={htmlaudioelement}
    />
  );
}
```
