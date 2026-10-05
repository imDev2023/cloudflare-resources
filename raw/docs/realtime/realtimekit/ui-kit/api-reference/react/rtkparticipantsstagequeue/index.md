---
description: API reference for RtkParticipantsStageQueue component (React Library)
title: RtkParticipantsStageQueue
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsstagequeue/og.png?v=dec330cab4f04eac
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkParticipantsStageQueue

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsstagequeue/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

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
import { RtkParticipantsStageQueue } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkParticipantsStageQueue />;
}
```

### With Properties

```tsx
import { RtkParticipantsStageQueue } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkParticipantsStageQueue
      meeting={meeting}
      size="md"
      view={participantsviewmode}
    />
  );
}
```
