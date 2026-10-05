---
description: API reference for RtkSpinner component (React Native Library)
title: RtkSpinner
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkspinner/og.png?v=8739ee4d74485a8e
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkSpinner

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkspinner/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

An animated loading spinner component.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `style` | `object` | ❌ | - | Custom styles to override spinner appearance |

## Usage Examples

### Basic Usage

```tsx
import { RtkSpinner } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkSpinner />;
}
```

### With Properties

```tsx
import { RtkSpinner } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkSpinner style={{ width: 48, height: 48 }} />;
}
```
