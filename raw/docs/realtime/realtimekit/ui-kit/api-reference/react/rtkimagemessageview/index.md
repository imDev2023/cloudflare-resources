---
description: API reference for RtkImageMessageView component (React Library)
title: RtkImageMessageView
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkimagemessageview/og.png?v=70dff6521261fecf
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkImageMessageView

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkimagemessageview/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which renders an image message.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |
| `url` | `string` | ✅ | - | Url of the image |

## Usage Examples

### Basic Usage

```tsx
import { RtkImageMessageView } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkImageMessageView />;
}
```

### With Properties

```tsx
import { RtkImageMessageView } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkImageMessageView
      url="example"
    />
  );
}
```
