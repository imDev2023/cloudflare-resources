---
description: API reference for RtkLiveStreamStageToggle component (React Native Library)
title: RtkLiveStreamStageToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtklivestreamstagetoggle/og.png?v=ee6bceb39b1f52e5
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkLiveStreamStageToggle

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtklivestreamstagetoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Toggle button for joining or leaving the livestream stage. Only visible in livestream mode.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | `'sm'` | Size variant |
| `variant` | `'button' \| 'horizontal'` | ❌ | `'button'` | Layout variant |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkLiveStreamStageToggle } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkLiveStreamStageToggle meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkLiveStreamStageToggle } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return (
		<RtkLiveStreamStageToggle meeting={meeting} size="md" variant="button" />
	);
}
```
