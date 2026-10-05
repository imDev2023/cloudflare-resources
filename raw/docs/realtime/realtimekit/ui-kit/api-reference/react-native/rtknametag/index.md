---
description: API reference for RtkNameTag component (React Native Library)
title: RtkNameTag
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtknametag/og.png?v=2ea405d9650023aa
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkNameTag

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtknametag/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Displays a participant's name with optional child content (such as an audio visualizer icon). Used as an overlay on participant tiles.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `participant` | `Peer` | ✅ | - | The participant to display the name for |
| `meeting` | `RealtimeKitClient` | ❌ | - | The RealtimeKit meeting instance (used to identify self) |
| `isScreenshare` | `boolean` | ❌ | `false` | Whether this is a screenshare name tag |
| `maxLength` | `number` | ❌ | `20` | Maximum width offset for the name tag |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | `'sm'` | Text size |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |
| `children` | `ReactNode` | ❌ | - | Content to render before the name |

## Usage Examples

### Basic Usage

```tsx
import { RtkNameTag } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkNameTag participant={participant} />;
}
```

### With Properties

```tsx
import { RtkNameTag } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return (
		<RtkNameTag
			participant={participant}
			meeting={meeting}
			size="md"
			maxLength={25}
		/>
	);
}
```
