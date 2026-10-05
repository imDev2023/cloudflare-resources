---
description: API reference for RtkJoinStage component (React Native Library)
title: RtkJoinStage
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkjoinstage/og.png?v=1ea61132cd822779
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkJoinStage

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkjoinstage/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Join stage confirmation dialog with video preview and mic/camera toggles for webinar/livestream participants.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `states` | `States` | ❌ | - | UI state object |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkJoinStage } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkJoinStage meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkJoinStage } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return (
		<RtkJoinStage meeting={meeting} iconPack={customIconPack} states={states} />
	);
}
```
