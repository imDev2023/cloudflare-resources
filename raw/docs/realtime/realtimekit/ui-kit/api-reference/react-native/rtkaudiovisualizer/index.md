---
description: API reference for RtkAudioVisualizer component (React Native Library)
title: RtkAudioVisualizer
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkaudiovisualizer/og.png?v=13f4bf266aaa5158
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkAudioVisualizer

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkaudiovisualizer/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Displays an audio visualizer with animated bars representing a participant's audio levels.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `participant` | `Peer \| RTKParticipant` | ✅ | - | The participant whose audio to visualize |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack for icons |
| `isScreenshare` | `boolean` | ❌ | `false` | Whether this is a screenshare audio visualizer |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | `'sm'` | Size of the visualizer |
| `variant` | `'bar'` | ❌ | `'bar'` | Visual variant of the visualizer |

## Usage Examples

### Basic Usage

```tsx
import { RtkAudioVisualizer } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkAudioVisualizer participant={participant} />;
}
```

### With Properties

```tsx
import { RtkAudioVisualizer } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return (
		<RtkAudioVisualizer participant={participant} size="md" variant="bar" />
	);
}
```
