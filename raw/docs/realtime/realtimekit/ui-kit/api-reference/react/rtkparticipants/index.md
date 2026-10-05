---
description: API reference for RtkParticipants component (React Library)
title: RtkParticipants
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipants/og.png?v=7a62784ddf7c5df2
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkParticipants

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipants/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which lists all participants, with ability to run privileged actions on each participant according to your permissions.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config |
| `defaultParticipantsTabId` | `ParticipantsTabId` | ✅ | - | Default section |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkParticipants } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkParticipants />;
}
```

### With Properties

```tsx
import { RtkParticipants } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkParticipants
      defaultParticipantsTabId={participantstabid}
      meeting={meeting}
      size="md"
    />
  );
}
```
