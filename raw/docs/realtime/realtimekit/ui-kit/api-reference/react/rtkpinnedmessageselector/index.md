---
description: API reference for RtkPinnedMessageSelector component (React Library)
title: RtkPinnedMessageSelector
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpinnedmessageselector/og.png?v=0bdb7840695d5f18
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkPinnedMessageSelector

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpinnedmessageselector/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkPinnedMessageSelector } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkPinnedMessageSelector />;
}
```

### With Properties

```tsx
import { RtkPinnedMessageSelector } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkPinnedMessageSelector
      meeting={meeting}
    />
  );
}
```
