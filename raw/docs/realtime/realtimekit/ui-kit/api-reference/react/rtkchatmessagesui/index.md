---
description: API reference for RtkChatMessagesUi component (React Library)
title: RtkChatMessagesUi
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessagesui/og.png?v=e7821db333e861a6
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkChatMessagesUi

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessagesui/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

@deprecated Use `rtk-chat-messages-ui-paginated` instead.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `canPinMessages` | `boolean` | ✅ | - | Can current user pin/unpin messages |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `messages` | `Chat[]` | ✅ | - | Chat Messages |
| `selectedGroup` | `string` | ✅ | - | Selected group key |
| `selfUserId` | `string` | ✅ | - | User ID of self user |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkChatMessagesUi } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkChatMessagesUi />;
}
```

### With Properties

```tsx
import { RtkChatMessagesUi } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkChatMessagesUi
      canPinMessages={true}
      messages={[]}
      selectedGroup="example"
    />
  );
}
```
