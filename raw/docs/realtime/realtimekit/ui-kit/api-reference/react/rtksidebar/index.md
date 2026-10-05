---
description: API reference for RtkSidebar component (React Library)
title: RtkSidebar
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksidebar/og.png?v=e0ecf141c81f4e77
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkSidebar

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksidebar/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which handles the sidebar and you can customize which sections you want, and which section you want as the default.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config |
| `defaultSection` | `RtkSidebarSection` | ✅ | - | Default section |
| `enabledSections` | `RtkSidebarTab[]` | ✅ | - | Enabled sections in sidebar |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `view` | `RtkSidebarView` | ✅ | - | View type |

## Usage Examples

### Basic Usage

```tsx
import { RtkSidebar } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkSidebar />;
}
```

### With Properties

```tsx
import { RtkSidebar } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkSidebar
      defaultSection={rtksidebarsection}
      enabledSections={[]}
      meeting={meeting}
    />
  );
}
```
