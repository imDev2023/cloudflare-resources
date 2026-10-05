---
description: API reference for RtkSetupScreen component (React Native Library)
title: RtkSetupScreen
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksetupscreen/og.png?v=64ac08ff33da4268
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkSetupScreen

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksetupscreen/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Pre-join setup screen with video preview, mic/camera toggles, display name input, camera switch, and join button.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `config` | `UIConfig` | ❌ | `defaultConfig` | UI configuration object |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | `'sm'` | Size variant |
| `states` | `States` | ❌ | - | UI state object |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkSetupScreen } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkSetupScreen meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkSetupScreen } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return (
		<RtkSetupScreen
			meeting={meeting}
			config={customConfig}
			size="md"
			iconPack={customIconPack}
		/>
	);
}
```
