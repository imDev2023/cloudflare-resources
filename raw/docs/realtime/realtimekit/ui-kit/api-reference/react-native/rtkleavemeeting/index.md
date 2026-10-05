---
description: API reference for RtkLeaveMeeting component (React Native Library)
title: RtkLeaveMeeting
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkleavemeeting/og.png?v=137f2448c398f78a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkLeaveMeeting

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkleavemeeting/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Leave meeting confirmation dialog with options to leave or end the meeting for all (if host).

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `onClose` | `any` | ✅ | - | Callback to close the dialog |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `states` | `States` | ❌ | - | UI state object |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkLeaveMeeting } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkLeaveMeeting meeting={meeting} onClose={() => setOpen(false)} />;
}
```

### With Properties

```tsx
import { RtkLeaveMeeting } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return (
		<RtkLeaveMeeting
			meeting={meeting}
			onClose={() => setOpen(false)}
			states={states}
		/>
	);
}
```
