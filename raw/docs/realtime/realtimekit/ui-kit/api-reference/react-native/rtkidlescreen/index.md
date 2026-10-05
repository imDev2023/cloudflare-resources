---
description: API reference for RtkIdleScreen component (React Native Library)
title: RtkIdleScreen
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkidlescreen/og.png?v=0412da7e40a80fb5
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkIdleScreen

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkidlescreen/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Loading/idle screen displayed while the meeting is initializing, showing a logo and spinner.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ✅ | - | UI configuration object (used for logo URL) |

## Usage Examples

### Basic Usage

```tsx
import { RtkIdleScreen } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkIdleScreen config={config} />;
}
```

### With Properties

```tsx
import {
	RtkIdleScreen,
	defaultConfig,
} from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkIdleScreen config={defaultConfig} />;
}
```
