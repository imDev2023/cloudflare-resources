---
description: API reference for RtkGrid component (React Native Library)
title: RtkGrid
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkgrid/og.png?v=515ca2287a49b4e3
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkGrid

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkgrid/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The main participant grid that automatically switches between simple, mixed, spotlight, and livestream layouts based on meeting state.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `config` | `UIConfig` | ❌ | `defaultConfig` | UI configuration object |
| `states` | `States` | ❌ | - | UI state object |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |
| `aspectRatio` | `string` | ❌ | `'3:4'` | Aspect ratio for grid tiles |
| `gap` | `number` | ❌ | `8` | Gap between grid tiles in pixels |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | `'sm'` | Size variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkGrid } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkGrid meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkGrid } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkGrid meeting={meeting} aspectRatio="16:9" gap={12} size="md" />;
}
```
