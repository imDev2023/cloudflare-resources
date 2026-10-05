---
description: API reference for RtkLiveStreamToggle component (React Native Library)
title: RtkLiveStreamToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtklivestreamtoggle/og.png?v=63c8fb0e5cf4c79c
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkLiveStreamToggle

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtklivestreamtoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Toggle button to start or stop a livestream. Only visible for hosts with livestream permissions.

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
import { RtkLiveStreamToggle } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkLiveStreamToggle meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkLiveStreamToggle } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkLiveStreamToggle meeting={meeting} size="md" variant="button" />;
}
```
