---
description: API reference for RtkWebinarStageToggle component (React Native Library)
title: RtkWebinarStageToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkwebinarstagetoggle/og.png?v=7577be92a6ae638f
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkWebinarStageToggle

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkwebinarstagetoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Toggle button for requesting to join or leave the webinar stage. Only visible in webinar mode for participants with stage access permissions.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `iconPack` | `IconPack` | ❌ | - | Custom icon pack |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | `'sm'` | Size variant |
| `variant` | `'button' \| 'horizontal'` | ❌ | `'button'` | Layout variant |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkWebinarStageToggle } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkWebinarStageToggle meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkWebinarStageToggle } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkWebinarStageToggle meeting={meeting} size="md" variant="button" />;
}
```
