---
description: API reference for RtkLivestreamIndicator component (React Library)
title: RtkLivestreamIndicator
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklivestreamindicator/og.png?v=1c8ce3f4ff7fc1f9
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkLivestreamIndicator

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklivestreamindicator/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

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
import { RtkLivestreamIndicator } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkLivestreamIndicator />;
}
```

### With Properties

```tsx
import { RtkLivestreamIndicator } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkLivestreamIndicator
      meeting={meeting}
      size="md"
    />
  );
}
```
