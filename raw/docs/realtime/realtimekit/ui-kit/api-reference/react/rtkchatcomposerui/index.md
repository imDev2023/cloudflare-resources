---
description: API reference for RtkChatComposerUi component (React Library)
title: RtkChatComposerUi
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatcomposerui/og.png?v=b30579d7e9b64684
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkChatComposerUi

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatcomposerui/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

@deprecated . This component is deprecated, please use rtk-chat-composer-view instead.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `canSendFiles` | `boolean` | ✅ | - | Whether user can send file messages |
| `canSendTextMessage` | `boolean` | ✅ | - | Whether user can send text messages |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `prefill` | `{ suggestedReplies?: string[]; editMessage?: TextMessage; replyMessage?: TextMessage; }` | ❌ | - | prefill the composer |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkChatComposerUi } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkChatComposerUi />;
}
```

### With Properties

```tsx
import { RtkChatComposerUi } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkChatComposerUi
      canSendFiles={true}
      canSendTextMessage={true}
      size="md"
    />
  );
}
```
