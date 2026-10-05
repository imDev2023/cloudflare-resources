---
description: API reference for RtkHeader component (React Native Library)
title: RtkHeader
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkheader/og.png?v=0ef2644f1553b7f8
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkHeader

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkheader/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The meeting header bar that renders logo, title, participant count, clock, and other header elements using the declarative UI config system.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `config` | `UIConfig` | ❌ | `defaultConfig` | UI configuration object |
| `iconPack` | `IconPack` | ❌ | - | Custom icon pack |
| `states` | `States` | ❌ | - | UI state object |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkHeader } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkHeader meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkHeader } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkHeader meeting={meeting} config={customConfig} states={states} />;
}
```
