---
description: API reference for RtkBreakoutRoomParticipants component (React Library)
title: RtkBreakoutRoomParticipants
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbreakoutroomparticipants/og.png?v=e2c93a0143de4533
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkBreakoutRoomParticipants

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbreakoutroomparticipants/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which lists all participants, with ability to run privileged actions on each participant according to your permissions.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `participantIds` | `string[]` | ✅ | - | Participant ids |
| `selectedParticipantIds` | `string[]` | ✅ | - | selected participants |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkBreakoutRoomParticipants } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkBreakoutRoomParticipants />;
}
```

### With Properties

```tsx
import { RtkBreakoutRoomParticipants } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkBreakoutRoomParticipants
      meeting={meeting}
      participantIds="example"
      selectedParticipantIds="example"
    />
  );
}
```
