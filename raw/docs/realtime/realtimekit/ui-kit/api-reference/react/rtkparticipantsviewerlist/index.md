---
description: API reference for RtkParticipantsViewerList component (React Library)
title: RtkParticipantsViewerList
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsviewerlist/og.png?v=907f96eb49be35ad
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkParticipantsViewerList

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsviewerlist/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config |
| `hideHeader` | `boolean` | ✅ | - | Hide Viewer Count Header |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `search` | `string` | ✅ | - | Search |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |
| `view` | `ParticipantsViewMode` | ✅ | - | View mode for participants list |

## Usage Examples

### Basic Usage

```tsx
import { RtkParticipantsViewerList } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkParticipantsViewerList />;
}
```

### With Properties

```tsx
import { RtkParticipantsViewerList } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkParticipantsViewerList
      hideHeader={true}
      meeting={meeting}
      search="example"
    />
  );
}
```
