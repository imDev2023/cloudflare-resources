---
description: API reference for RtkMixedGrid component (React Native Library)
title: RtkMixedGrid
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmixedgrid/og.png?v=f2c4fa362ea19c25
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkMixedGrid

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmixedgrid/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A grid layout that handles mixed content: participants, screenshares, plugins, and pinned participants. Automatically switches between simple, spotlight, and highlighted grid layouts.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `participants` | `Peer[]` | ✅ | `[]` | Array of active participants |
| `pinnedParticipants` | `Peer[]` | ✅ | `[]` | Array of pinned participants |
| `screenShareParticipants` | `Peer[]` | ✅ | `[]` | Array of participants sharing their screen |
| `plugins` | `RTKPlugin[]` | ✅ | `[]` | Array of active plugins |
| `aspectRatio` | `string` | ❌ | `'16:9'` | Aspect ratio for grid tiles |
| `config` | `UIConfig` | ❌ | `defaultConfig` | UI configuration object |
| `gap` | `number` | ❌ | `8` | Gap between grid tiles in pixels |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | `'sm'` | Size variant |
| `variant` | `'boxed' \| 'solid'` | ❌ | `'solid'` | Visual style variant |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `states` | `States` | ❌ | - | UI state object |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkMixedGrid } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return (
		<RtkMixedGrid
			meeting={meeting}
			participants={participants}
			pinnedParticipants={[]}
			screenShareParticipants={[]}
			plugins={[]}
		/>
	);
}
```

### With Properties

```tsx
import { RtkMixedGrid } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return (
		<RtkMixedGrid
			meeting={meeting}
			participants={participants}
			pinnedParticipants={pinned}
			screenShareParticipants={screenshares}
			plugins={activePlugins}
			aspectRatio="16:9"
			gap={12}
			size="md"
		/>
	);
}
```
