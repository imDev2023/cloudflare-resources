---
description: API reference for RtkDialogManager component (React Native Library)
title: RtkDialogManager
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkdialogmanager/og.png?v=a714f26e27c5d207
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkDialogManager

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkdialogmanager/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Manages and renders modal dialogs for leave confirmation, settings, join stage confirmation, and permissions messages.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `config` | `UIConfig` | ❌ | `defaultConfig` | UI configuration object |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | - | Size variant |
| `states` | `States` | ❌ | - | UI state object |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |
| `onRtkStateUpdate` | `(e) => void` | ❌ | `() => \{\}` | Callback when UI state changes |

## Usage Examples

### Basic Usage

```tsx
import { RtkDialogManager } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkDialogManager meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkDialogManager } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return (
		<RtkDialogManager
			meeting={meeting}
			config={customConfig}
			size="md"
			onRtkStateUpdate={(e) => handleStateUpdate(e)}
		/>
	);
}
```
