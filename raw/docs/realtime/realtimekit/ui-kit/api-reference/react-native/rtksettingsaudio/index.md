---
description: API reference for RtkSettingsAudio component (React Native Library)
title: RtkSettingsAudio
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksettingsaudio/og.png?v=49cab8353221259b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkSettingsAudio

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksettingsaudio/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Audio settings panel with device selection dropdown, audio visualizer preview, and notification sound toggle.

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
import { RtkSettingsAudio } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkSettingsAudio meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkSettingsAudio } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkSettingsAudio meeting={meeting} size="md" states={states} />;
}
```
