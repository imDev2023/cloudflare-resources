---
description: API reference for RtkMoreToggle component (React Native Library)
title: RtkMoreToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmoretoggle/og.png?v=983e772d9a46ec41
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkMoreToggle

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmoretoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Toggle button for the "more options" overflow menu in the control bar. Shows a notification badge for pending requests.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | - | Icon size |
| `variant` | `'button' \| 'horizontal'` | ❌ | - | Layout variant |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `states` | `States` | ❌ | - | UI state object |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |
| `children` | `ReactNode` | ❌ | - | Additional content to render |

## Usage Examples

### Basic Usage

```tsx
import { RtkMoreToggle } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkMoreToggle meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkMoreToggle } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return (
		<RtkMoreToggle
			meeting={meeting}
			size="md"
			variant="button"
			states={states}
		/>
	);
}
```
