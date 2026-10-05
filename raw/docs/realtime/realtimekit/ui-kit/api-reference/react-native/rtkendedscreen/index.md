---
description: API reference for RtkEndedScreen component (React Native Library)
title: RtkEndedScreen
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkendedscreen/og.png?v=81f563531e50240c
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkEndedScreen

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkendedscreen/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Screen displayed when the meeting has ended.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ❌ | - | The RealtimeKit meeting instance |
| `config` | `UIConfig` | ❌ | `defaultConfig` | UI configuration object |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | - | Size variant |
| `states` | `States` | ❌ | - | UI state object |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkEndedScreen } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkEndedScreen />;
}
```

### With Properties

```tsx
import { RtkEndedScreen } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkEndedScreen meeting={meeting} config={customConfig} size="md" />;
}
```
