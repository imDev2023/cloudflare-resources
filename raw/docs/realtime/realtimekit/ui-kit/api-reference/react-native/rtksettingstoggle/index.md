---
description: API reference for RtkSettingsToggle component (React Native Library)
title: RtkSettingsToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksettingstoggle/og.png?v=601c3aff145dc1e3
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkSettingsToggle

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksettingstoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Toggle button to open the settings dialog. Hides if no audio or video permissions are available.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | - | Icon size |
| `states` | `States` | ❌ | - | UI state object |
| `variant` | `'button' \| 'horizontal'` | ❌ | - | Layout variant |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkSettingsToggle } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkSettingsToggle />;
}
```

### With Properties

```tsx
import { RtkSettingsToggle } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkSettingsToggle size="md" variant="button" states={states} />;
}
```
