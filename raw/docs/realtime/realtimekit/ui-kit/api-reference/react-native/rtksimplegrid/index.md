---
description: API reference for RtkSimpleGrid component (React Native Library)
title: RtkSimpleGrid
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksimplegrid/og.png?v=1de93f1c06d8f0ad
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkSimpleGrid

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksimplegrid/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A simple grid layout that arranges participant tiles in rows and columns with automatic sizing based on participant count.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `participants` | `Peer[]` | ✅ | - | Array of participants to display |
| `aspectRatio` | `string` | ❌ | `'3:4'` | Aspect ratio for grid tiles |
| `config` | `UIConfig` | ❌ | `defaultConfig` | UI configuration object |
| `gap` | `number` | ❌ | `8` | Gap between grid tiles in pixels |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | `'sm'` | Size variant |
| `states` | `States` | ❌ | - | UI state object |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |
| `style` | `StyleProp<any>` | ❌ | - | Custom styles for the grid container |

## Usage Examples

### Basic Usage

```tsx
import { RtkSimpleGrid } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkSimpleGrid meeting={meeting} participants={participants} />;
}
```

### With Properties

```tsx
import { RtkSimpleGrid } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return (
		<RtkSimpleGrid
			meeting={meeting}
			participants={participants}
			aspectRatio="16:9"
			gap={12}
			size="md"
		/>
	);
}
```
