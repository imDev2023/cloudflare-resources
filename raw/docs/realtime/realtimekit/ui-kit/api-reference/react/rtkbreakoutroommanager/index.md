---
description: API reference for RtkBreakoutRoomManager component (React Library)
title: RtkBreakoutRoomManager
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbreakoutroommanager/og.png?v=1940d935b1caeefb
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkBreakoutRoomManager

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbreakoutroommanager/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `allowDelete` | `boolean` | ✅ | - | allow room delete |
| `assigningParticipants` | `boolean` | ✅ | - | Enable updating participants |
| `defaultExpanded` | `boolean` | ✅ | - | display expanded card by default |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `isDragMode` | `boolean` | ✅ | - | Drag mode |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `mode` | `'edit' \| 'create'` | ✅ | - | Mode in which selector is used |
| `room` | `DraftMeeting` | ✅ | - | Connected Room Config Object |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkBreakoutRoomManager } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkBreakoutRoomManager />;
}
```

### With Properties

```tsx
import { RtkBreakoutRoomManager } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkBreakoutRoomManager
      allowDelete={true}
      assigningParticipants={true}
      defaultExpanded={true}
    />
  );
}
```
