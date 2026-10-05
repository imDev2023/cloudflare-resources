---
description: API reference for RtkChatToggle component (React Native Library)
title: RtkChatToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkchattoggle/og.png?v=52a6799656a647a7
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkChatToggle

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkchattoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Toggle button to open the chat sidebar panel. Hides if chat permissions are not available.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | - | Icon size |
| `states` | `States` | ❌ | - | UI state object |
| `variant` | `'button' \| 'horizontal'` | ❌ | - | Layout variant |
| `iconPack` | `IconPack` | ❌ | - | Custom icon pack |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkChatToggle } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkChatToggle meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkChatToggle } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkChatToggle meeting={meeting} size="md" variant="button" />;
}
```
