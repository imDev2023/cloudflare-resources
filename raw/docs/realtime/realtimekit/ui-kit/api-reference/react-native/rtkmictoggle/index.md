---
description: API reference for RtkMicToggle component (React Native Library)
title: RtkMicToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmictoggle/og.png?v=30b7996cf191a5cb
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkMicToggle

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmictoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Toggle button to enable or disable the local participant's microphone. Automatically hides if the participant lacks audio production permissions.

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
import { RtkMicToggle } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkMicToggle meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkMicToggle } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkMicToggle meeting={meeting} size="md" variant="button" />;
}
```
