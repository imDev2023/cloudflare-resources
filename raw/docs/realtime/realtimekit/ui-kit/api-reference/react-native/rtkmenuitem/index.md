---
description: API reference for RtkMenuItem component (React Native Library)
title: RtkMenuItem
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmenuitem/og.png?v=bbbbd13997c73939
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkMenuItem

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmenuitem/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A pressable menu item within a menu.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | ✅ | - | Menu item content |
| `onClick` | `(ev) => {}` | ❌ | - | Press handler callback |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | - | Size variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkMenuItem } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return (
		<RtkMenuItem onClick={() => ({})}>
			<Text>Option 1</Text>
		</RtkMenuItem>
	);
}
```

### With Properties

```tsx
import { RtkMenuItem } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return (
		<RtkMenuItem onClick={(ev) => ({})} size="md">
			<Text>Option 1</Text>
		</RtkMenuItem>
	);
}
```
