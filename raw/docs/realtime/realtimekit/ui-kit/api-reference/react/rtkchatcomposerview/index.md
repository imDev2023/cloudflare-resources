---
description: API reference for RtkChatComposerView component (React Library)
title: RtkChatComposerView
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatcomposerview/og.png?v=5c4c53c90d91328f
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkChatComposerView

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatcomposerview/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which renders a chat composer

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `canSendFiles` | `boolean` | ✅ | - | Whether user can send file messages |
| `canSendTextMessage` | `boolean` | ✅ | - | Whether user can send text messages |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `inputTextPlaceholder` | `string` | ✅ | - | Placeholder for text input |
| `isEditing` | `boolean` | ✅ | - | Sets composer to edit mode |
| `maxLength` | `number` | ✅ | - | Max length for text input |
| `message` | `string` | ✅ | - | Message to be pre-populated |
| `quotedMessage` | `string` | ✅ | - | Quote message to be displayed |
| `rateLimits` | `{ period: number; maxInvocations: number; }` | ✅ | - | Rate limits |
| `storageKey` | `string` | ✅ | - | Key for storing message in localStorage |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkChatComposerView } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkChatComposerView />;
}
```

### With Properties

```tsx
import { RtkChatComposerView } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkChatComposerView
      canSendFiles={true}
      canSendTextMessage={true}
      inputTextPlaceholder="example"
    />
  );
}
```
