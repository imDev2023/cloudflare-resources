---
description: API reference for RtkMeetingTitle component (React Native Library)
title: RtkMeetingTitle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmeetingtitle/og.png?v=1d8678b25a56f256
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkMeetingTitle

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmeetingtitle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Displays the meeting title from meeting metadata.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |

## Usage Examples

### Basic Usage

```tsx
import { RtkMeetingTitle } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkMeetingTitle meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkMeetingTitle } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkMeetingTitle meeting={meeting} />;
}
```
