---
description: API reference for RtkRecordingIndicator component (React Native Library)
title: RtkRecordingIndicator
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkrecordingindicator/og.png?v=eadcdc862010b323
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkRecordingIndicator

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkrecordingindicator/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Displays a blinking recording indicator when the meeting is being recorded.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | `'sm'` | Size variant |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkRecordingIndicator } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkRecordingIndicator meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkRecordingIndicator } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkRecordingIndicator meeting={meeting} size="md" />;
}
```
