---
description: API reference for RtkTabBar component (React Library)
title: RtkTabBar
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktabbar/og.png?v=d2733c8d58ac85d4
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkTabBar

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktabbar/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `activeTab` | `Tab` | ✅ | - | Active tab |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | UI Config |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon Pack |
| `layout` | `GridLayout1` | ✅ | - | Grid Layout |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `tabs` | `Tab[]` | ✅ | - | Tabs |

## Usage Examples

### Basic Usage

```tsx
import { RtkTabBar } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkTabBar />;
}
```

### With Properties

```tsx
import { RtkTabBar } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkTabBar
      activeTab={tab}
      layout={gridlayout1}
      meeting={meeting}
    />
  );
}
```
