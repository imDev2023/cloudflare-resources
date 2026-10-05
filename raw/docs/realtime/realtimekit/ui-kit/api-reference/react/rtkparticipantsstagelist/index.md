---
description: API reference for RtkParticipantsStageList component (React Library)
title: RtkParticipantsStageList
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsstagelist/og.png?v=b3b3c0090e0f1b59
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkParticipantsStageList

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsstagelist/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which lists all participants, with ability to run privileged actions on each participant according to your permissions.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config |
| `hideHeader` | `boolean` | ✅ | - | Hide Stage Participants Count Header |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `search` | `string` | ✅ | - | Search |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States1` | ✅ | - | Meeting object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `view` | `ParticipantsViewMode` | ✅ | - | View mode for participants list |

## Usage Examples

### Basic Usage

```tsx
import { RtkParticipantsStageList } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkParticipantsStageList />;
}
```

### With Properties

```tsx
import { RtkParticipantsStageList } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkParticipantsStageList
      hideHeader={true}
      meeting={meeting}
      search="example"
    />
  );
}
```
