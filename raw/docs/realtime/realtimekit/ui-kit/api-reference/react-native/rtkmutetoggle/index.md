---
description: API reference for RtkMuteToggle component (React Native Library)
title: RtkMuteToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmutetoggle/og.png?v=fcdd36c8a701211f
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkMuteToggle

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmutetoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Button to mute all participants' audio. Only visible for hosts with mute-all permissions.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | - | Icon size |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkMuteToggle } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkMuteToggle meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkMuteToggle } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkMuteToggle meeting={meeting} size="md" />;
}
```
