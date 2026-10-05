---
description: API reference for RtkFileMessage component (React Library)
title: RtkFileMessage
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfilemessage/og.png?v=e4fd0b82e91cab25
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkFileMessage

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfilemessage/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

@deprecated `rtk-file-message` is deprecated and will be removed soon. Use `rtk-file-message-view` instead. A component which renders a file message from chat.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `isContinued` | `boolean` | ✅ | - | Whether the message is continued by same user |
| `message` | `FileMessage` | ✅ | - | Text message object |
| `now` | `Date` | ✅ | - | Date object of now, to calculate distance between dates |
| `showBubble` | `boolean` | ✅ | - | show message in bubble |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkFileMessage } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkFileMessage />;
}
```

### With Properties

```tsx
import { RtkFileMessage } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkFileMessage
      isContinued={true}
      message={filemessage}
      now={date}
    />
  );
}
```
