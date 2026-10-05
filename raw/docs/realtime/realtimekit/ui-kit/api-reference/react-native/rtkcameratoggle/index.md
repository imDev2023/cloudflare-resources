---
description: API reference for RtkCameraToggle component (React Native Library)
title: RtkCameraToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkcameratoggle/og.png?v=3665c032712ae2ae
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkCameraToggle

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkcameratoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Toggle button to enable or disable the local participant's camera. Automatically hides if the participant lacks video production permissions.

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
import { RtkCameraToggle } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkCameraToggle meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkCameraToggle } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkCameraToggle meeting={meeting} size="md" variant="button" />;
}
```
