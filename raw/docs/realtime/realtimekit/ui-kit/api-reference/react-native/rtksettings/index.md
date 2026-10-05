---
description: API reference for RtkSettings component (React Native Library)
title: RtkSettings
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksettings/og.png?v=655bb2b8ef09f945
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkSettings

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksettings/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Settings dialog with audio device selection, video device selection, and network connection status.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | `'sm'` | Size variant |
| `states` | `States` | ❌ | - | UI state object |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |
| `onClose` | `any` | ❌ | - | Callback to close the settings dialog |

## Usage Examples

### Basic Usage

```tsx
import { RtkSettings } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkSettings meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkSettings } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return (
		<RtkSettings
			meeting={meeting}
			size="md"
			onClose={() => setSettingsOpen(false)}
		/>
	);
}
```
