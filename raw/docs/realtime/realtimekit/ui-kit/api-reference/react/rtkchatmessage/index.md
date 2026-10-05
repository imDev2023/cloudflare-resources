---
description: API reference for RtkChatMessage component (React Library)
title: RtkChatMessage
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessage/og.png?v=7b264f59acb0ac78
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkChatMessage

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessage/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

@deprecated `rtk-chat-message` is deprecated and will be removed soon. Use `rtk-message-view` instead.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `alignRight` | `boolean` | ✅ | - | aligns message to right |
| `canDelete` | `boolean` | ✅ | - | can delete message |
| `canEdit` | `boolean` | ✅ | - | can edit message |
| `canPin` | `boolean` | ✅ | - | can pin this message |
| `canReply` | `boolean` | ✅ | - | can quote reply this message |
| `child` | `HTMLElement` | ✅ | - | Child |
| `disableControls` | `boolean` | ✅ | - | disables controls |
| `hideAvatar` | `boolean` | ✅ | - | hides avatar |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `isContinued` | `boolean` | ✅ | - | is continued |
| `isSelf` | `boolean` | ✅ | - | if sender is self |
| `isUnread` | `boolean` | ✅ | - | is unread |
| `leftAlign` | `boolean` | ✅ | - | Whether to left align the chat bubbles |
| `message` | `Message` | ✅ | - | message item |
| `senderDisplayPicture` | `string` | ✅ | - | sender display picture url |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkChatMessage } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkChatMessage />;
}
```

### With Properties

```tsx
import { RtkChatMessage } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkChatMessage
      alignRight={true}
      canDelete={true}
      canEdit={true}
    />
  );
}
```
