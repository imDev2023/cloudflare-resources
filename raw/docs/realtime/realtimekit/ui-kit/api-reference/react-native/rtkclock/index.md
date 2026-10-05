---
description: API reference for RtkClock component (React Native Library)
title: RtkClock
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkclock/og.png?v=ce627aae9380acca
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkClock

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkclock/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Displays elapsed meeting time as a running clock (HH:MM:SS or MM:SS).

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkClock } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkClock meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkClock } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkClock meeting={meeting} iconPack={customIconPack} />;
}
```
