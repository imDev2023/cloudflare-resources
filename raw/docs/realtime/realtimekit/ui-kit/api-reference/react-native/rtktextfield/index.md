---
description: API reference for RtkTextField component (React Native Library)
title: RtkTextField
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtktextfield/og.png?v=deca92287f9541a9
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkTextField

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtktextfield/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A themed text input field component.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `disabled` | `boolean` | ❌ | `false` | Whether the input is disabled |
| `placeholder` | `string` | ❌ | `''` | Placeholder text |
| `type` | `string` | ❌ | `'text'` | Input type |
| `style` | `StyleProp<any>` | ❌ | - | Custom styles |
| `onChangeText` | `(s: string) => void` | ❌ | - | Callback when text changes |

## Usage Examples

### Basic Usage

```tsx
import { RtkTextField } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkTextField placeholder="Enter your name" />;
}
```

### With Properties

```tsx
import { RtkTextField } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return (
		<RtkTextField
			placeholder="Enter display name"
			onChangeText={(text) => setName(text)}
			disabled={false}
		/>
	);
}
```
