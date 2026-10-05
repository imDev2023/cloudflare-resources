---
description: API reference for RtkParticipant component (React Library)
title: RtkParticipant
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipant/og.png?v=02ad94acb9e49702
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkParticipant

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipant/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A participant entry component used inside `rtk-participants` which shows data like: name, picture and media device status. You can perform privileged actions on the participant too.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config object |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `participant` | `Peer` | ✅ | - | Participant object |
| `states` | `States1` | ✅ | - | States |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `view` | `ParticipantViewMode` | ✅ | - | Show participant summary |

## Usage Examples

### Basic Usage

```tsx
import { RtkParticipant } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkParticipant />;
}
```

### With Properties

```tsx
import { RtkParticipant } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkParticipant
      meeting={meeting}
      participant={participant}
      view={participantviewmode}
    />
  );
}
```
