---
description: API reference for RtkSpotlightIndicator component (React Library)
title: RtkSpotlightIndicator
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkspotlightindicator/og.png?v=02e6c1322e11a332
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkSpotlightIndicator

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkspotlightindicator/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkSpotlightIndicator } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkSpotlightIndicator />;
}
```

### With Properties

```tsx
import { RtkSpotlightIndicator } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkSpotlightIndicator
      meeting={meeting}
      size="md"
    />
  );
}
```
