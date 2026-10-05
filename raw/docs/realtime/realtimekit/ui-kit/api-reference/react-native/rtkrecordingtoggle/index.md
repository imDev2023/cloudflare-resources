---
description: API reference for RtkRecordingToggle component (React Native Library)
title: RtkRecordingToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkrecordingtoggle/og.png?v=262c9bf0f1e54224
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkRecordingToggle

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkrecordingtoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Toggle button to start or stop meeting recording. Only visible for participants with recording permissions who are on stage.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | - | Icon size |
| `variant` | `'button' \| 'horizontal'` | ❌ | - | Layout variant |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkRecordingToggle } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkRecordingToggle meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkRecordingToggle } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkRecordingToggle meeting={meeting} size="md" variant="button" />;
}
```
