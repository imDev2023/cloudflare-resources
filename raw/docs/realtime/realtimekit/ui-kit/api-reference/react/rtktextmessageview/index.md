---
description: API reference for RtkTextMessageView component (React Library)
title: RtkTextMessageView
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktextmessageview/og.png?v=72e84a4079acb674
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkTextMessageView

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktextmessageview/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which renders a text message from chat.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `isMarkdown` | `boolean` | ✅ | - | Renders text as markdown (default = true) |
| `text` | `string` | ✅ | - | Text message |

## Usage Examples

### Basic Usage

```tsx
import { RtkTextMessageView } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkTextMessageView />;
}
```

### With Properties

```tsx
import { RtkTextMessageView } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkTextMessageView
      isMarkdown={true}
      text="example"
    />
  );
}
```
