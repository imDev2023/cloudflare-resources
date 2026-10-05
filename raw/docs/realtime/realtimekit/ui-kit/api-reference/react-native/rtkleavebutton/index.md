---
description: API reference for RtkLeaveButton component (React Native Library)
title: RtkLeaveButton
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkleavebutton/og.png?v=9585f0f5c7a51f16
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkLeaveButton

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkleavebutton/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Button to trigger the leave meeting confirmation dialog.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `variant` | `'button' \| 'horizontal'` | ❌ | - | Layout variant |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | - | Button size |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkLeaveButton } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkLeaveButton />;
}
```

### With Properties

```tsx
import { RtkLeaveButton } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkLeaveButton variant="button" size="md" />;
}
```
