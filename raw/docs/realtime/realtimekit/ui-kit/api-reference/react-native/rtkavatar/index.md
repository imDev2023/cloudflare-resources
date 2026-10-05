---
description: API reference for RtkAvatar component (React Native Library)
title: RtkAvatar
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkavatar/og.png?v=65aac5e4be798ad5
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkAvatar

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkavatar/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Displays a participant's avatar image or initials-based fallback avatar.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `participant` | `RTKParticipant \| RTKSelf` | ✅ | - | The participant whose avatar to display |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | `'sm'` | Size of the avatar |
| `variant` | `'circular' \| 'hexagon' \| 'square'` | ❌ | `'circular'` | Shape variant of the avatar |

## Usage Examples

### Basic Usage

```tsx
import { RtkAvatar } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkAvatar participant={participant} />;
}
```

### With Properties

```tsx
import { RtkAvatar } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkAvatar participant={participant} size="lg" variant="circular" />;
}
```
