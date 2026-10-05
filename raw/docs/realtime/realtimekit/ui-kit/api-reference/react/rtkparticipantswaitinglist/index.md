---
description: API reference for RtkParticipantsWaitingList component (React Library)
title: RtkParticipantsWaitingList
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantswaitinglist/og.png?v=fa417c43838fa16f
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkParticipantsWaitingList

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantswaitinglist/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |
| `view` | `ParticipantsViewMode` | ✅ | - | View mode for participants list |

## Usage Examples

### Basic Usage

```tsx
import { RtkParticipantsWaitingList } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkParticipantsWaitingList />;
}
```

### With Properties

```tsx
import { RtkParticipantsWaitingList } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkParticipantsWaitingList
      meeting={meeting}
      size="md"
      view={participantsviewmode}
    />
  );
}
```
