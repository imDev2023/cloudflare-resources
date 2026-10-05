---
description: API reference for RtkMarkdownView component (React Library)
title: RtkMarkdownView
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmarkdownview/og.png?v=f9a1bd9b43e39373
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkMarkdownView

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmarkdownview/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `maxLength` | `number` | ✅ | - | max length of text to render as markdown |
| `text` | `string` | ✅ | - | raw text to render as markdown |

## Usage Examples

### Basic Usage

```tsx
import { RtkMarkdownView } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkMarkdownView />;
}
```

### With Properties

```tsx
import { RtkMarkdownView } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkMarkdownView
      maxLength={42}
      text="example"
    />
  );
}
```
