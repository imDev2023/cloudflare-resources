---
description: API reference for RtkLivestreamPlayer component (React Library)
title: RtkLivestreamPlayer
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklivestreamplayer/og.png?v=4620273d83ea0a43
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkLivestreamPlayer

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklivestreamplayer/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkLivestreamPlayer } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkLivestreamPlayer />;
}
```

### With Properties

```tsx
import { RtkLivestreamPlayer } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkLivestreamPlayer
      meeting={meeting}
      size="md"
    />
  );
}
```
