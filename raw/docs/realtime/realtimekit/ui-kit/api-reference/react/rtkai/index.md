---
description: API reference for RtkAi component (React Library)
title: RtkAi
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkai/og.png?v=898652eb52cfec47
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkAi

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkai/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `view` | `AIView` | ✅ | - | View type |

## Usage Examples

### Basic Usage

```tsx
import { RtkAi } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkAi />;
}
```

### With Properties

```tsx
import { RtkAi } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkAi
      meeting={meeting}
      size="md"
      view={aiview}
    />
  );
}
```
