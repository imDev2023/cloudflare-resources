---
description: API reference for RtkPollsToggle component (React Native Library)
title: RtkPollsToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpollstoggle/og.png?v=0cc4ab9e48fe46a2
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkPollsToggle

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpollstoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Toggle button to open the polls sidebar panel. Hides if poll permissions are not available.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `states` | `States` | ✅ | - | UI state object |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | - | Icon size |
| `variant` | `'button' \| 'horizontal'` | ❌ | - | Layout variant |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkPollsToggle } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkPollsToggle meeting={meeting} states={states} />;
}
```

### With Properties

```tsx
import { RtkPollsToggle } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return (
		<RtkPollsToggle
			meeting={meeting}
			states={states}
			size="md"
			variant="button"
		/>
	);
}
```
