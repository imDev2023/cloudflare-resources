---
description: API reference for RtkSettingsVideo component (React Native Library)
title: RtkSettingsVideo
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksettingsvideo/og.png?v=9df3ccedda570a34
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkSettingsVideo

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksettingsvideo/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Video settings panel with camera selection dropdown and live video preview.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | `'sm'` | Size variant |
| `states` | `States` | ❌ | - | UI state object |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkSettingsVideo } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkSettingsVideo meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkSettingsVideo } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkSettingsVideo meeting={meeting} size="md" states={states} />;
}
```
