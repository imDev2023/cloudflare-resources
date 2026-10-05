---
description: API reference for RtkFileMessage component (React Native Library)
title: RtkFileMessage
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkfilemessage/og.png?v=e4fd0b82e91cab25
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkFileMessage

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkfilemessage/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Renders a file message in chat with file name, size, extension, and download button.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `message` | `Message` | ✅ | - | The chat message object |
| `isContinued` | `boolean` | ❌ | `false` | Whether this message continues from the same sender |
| `now` | `Date` | ❌ | `new Date()` | Current time for relative timestamps |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |

## Usage Examples

### Basic Usage

```tsx
import { RtkFileMessage } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkFileMessage message={message} />;
}
```

### With Properties

```tsx
import { RtkFileMessage } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return (
		<RtkFileMessage message={message} isContinued={true} now={new Date()} />
	);
}
```
