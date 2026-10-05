---
description: API reference for RtkSpotlightGrid component (React Native Library)
title: RtkSpotlightGrid
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkspotlightgrid/og.png?v=3225ff86894c8ce5
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkSpotlightGrid

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkspotlightgrid/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A grid layout that highlights pinned participants in a larger view with other participants in a smaller strip. Handles livestream player display for off-stage viewers.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `participants` | `Peer[]` | ✅ | - | Array of active participants |
| `pinnedParticipants` | `Peer[]` | ✅ | - | Array of pinned participants to spotlight |
| `aspectRatio` | `string` | ❌ | `'3:4'` | Aspect ratio for grid tiles |
| `config` | `UIConfig` | ❌ | `defaultConfig` | UI configuration object |
| `gap` | `number` | ❌ | `4` | Gap between grid tiles in pixels |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | `'sm'` | Size variant |
| `states` | `States` | ❌ | - | UI state object |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkSpotlightGrid } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return (
		<RtkSpotlightGrid
			meeting={meeting}
			participants={participants}
			pinnedParticipants={pinned}
		/>
	);
}
```

### With Properties

```tsx
import { RtkSpotlightGrid } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return (
		<RtkSpotlightGrid
			meeting={meeting}
			participants={participants}
			pinnedParticipants={pinned}
			aspectRatio="16:9"
			gap={8}
			size="md"
		/>
	);
}
```
