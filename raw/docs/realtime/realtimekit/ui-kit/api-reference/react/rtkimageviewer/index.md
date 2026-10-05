---
description: API reference for RtkImageViewer component (React Library)
title: RtkImageViewer
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkimageviewer/og.png?v=4aa4d9a6eb8410b0
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkImageViewer

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkimageviewer/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which shows an image sent via chat.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `image` | `ImageMessage` | ✅ | - | Image message |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkImageViewer } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkImageViewer />;
}
```

### With Properties

```tsx
import { RtkImageViewer } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkImageViewer
      image={imagemessage}
      size="md"
    />
  );
}
```
