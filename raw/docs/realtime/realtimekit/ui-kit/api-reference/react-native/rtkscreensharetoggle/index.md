---
description: API reference for RtkScreenShareToggle component (React Native Library)
title: RtkScreenShareToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkscreensharetoggle/og.png?v=03e5ddc07ba009fe
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkScreenShareToggle

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkscreensharetoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Toggle button to start or stop screen sharing. Automatically hides based on permissions and screenshare limits.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | `'sm'` | Icon size |
| `variant` | `'button' \| 'horizontal'` | ❌ | `'button'` | Layout variant |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkScreenShareToggle } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkScreenShareToggle meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkScreenShareToggle } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkScreenShareToggle meeting={meeting} size="md" variant="button" />;
}
```
