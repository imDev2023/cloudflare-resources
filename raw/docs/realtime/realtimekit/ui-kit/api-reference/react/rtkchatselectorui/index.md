---
description: API reference for RtkChatSelectorUi component (React Library)
title: RtkChatSelectorUi
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatselectorui/og.png?v=928ea86cd4f28236
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkChatSelectorUi

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatselectorui/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `groups` | `ChatGroup[]` | ✅ | - | Participants |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `selectedGroupId` | `string` | ✅ | - | Selected participant |
| `selfUserId` | `string` | ✅ | - | Self User ID |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `unreadCounts` | `Record<string, number>` | ✅ | - | Unread counts |

## Usage Examples

### Basic Usage

```tsx
import { RtkChatSelectorUi } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkChatSelectorUi />;
}
```

### With Properties

```tsx
import { RtkChatSelectorUi } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkChatSelectorUi
      groups={[]}
      selectedGroupId="example"
      selfUserId="example"
    />
  );
}
```
