---
description: API reference for RtkLiveStreamViewerCount component (React Native Library)
title: RtkLiveStreamViewerCount
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtklivestreamviewercount/og.png?v=ca6a5850b0bf8265
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkLiveStreamViewerCount

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtklivestreamviewercount/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Displays the current livestream viewer count. Only visible in livestream mode.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `t` | `RtkI18n` | ✅ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import {
	RtkLiveStreamViewerCount,
	useLanguage,
} from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	const t = useLanguage();
	return <RtkLiveStreamViewerCount meeting={meeting} t={t} />;
}
```

### With Properties

```tsx
import {
	RtkLiveStreamViewerCount,
	useLanguage,
} from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	const t = useLanguage();
	return (
		<RtkLiveStreamViewerCount
			meeting={meeting}
			t={t}
			iconPack={customIconPack}
		/>
	);
}
```
