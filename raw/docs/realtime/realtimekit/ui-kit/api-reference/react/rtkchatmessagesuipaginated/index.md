---
description: API reference for RtkChatMessagesUiPaginated component (React Library)
title: RtkChatMessagesUiPaginated
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessagesuipaginated/og.png?v=a26537ec4f51a646
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkChatMessagesUiPaginated

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessagesuipaginated/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `privateChatRecipient` | `Participant \| null` | ✅ | - | Selected recipient for private chat; when unset, messages are loaded for public chat (Everyone). |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkChatMessagesUiPaginated } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkChatMessagesUiPaginated />;
}
```

### With Properties

```tsx
import { RtkChatMessagesUiPaginated } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkChatMessagesUiPaginated
      meeting={meeting}
      privateChatRecipient={participant | null}
      size="md"
    />
  );
}
```
