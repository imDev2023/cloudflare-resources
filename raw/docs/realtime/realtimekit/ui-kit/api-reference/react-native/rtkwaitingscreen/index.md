---
description: API reference for RtkWaitingScreen component (React Native Library)
title: RtkWaitingScreen
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkwaitingscreen/og.png?v=cec1f6b517e3b05a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkWaitingScreen

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkwaitingscreen/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Screen displayed while waiting to join (waitlist, kicked, disconnected states).

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ❌ | - | UI configuration object |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkWaitingScreen } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkWaitingScreen />;
}
```

### With Properties

```tsx
import { RtkWaitingScreen } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkWaitingScreen config={customConfig} />;
}
```
