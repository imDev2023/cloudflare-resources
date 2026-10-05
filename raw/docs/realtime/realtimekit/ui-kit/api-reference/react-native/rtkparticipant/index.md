---
description: API reference for RtkParticipant component (React Native Library)
title: RtkParticipant
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkparticipant/og.png?v=02ad94acb9e49702
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkParticipant

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkparticipant/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A participant list item card showing avatar, name, audio/video status icons, and host control options (pin, kick, mute, stage management).

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `participant` | `Peer` | ✅ | - | The participant to display |
| `meeting` | `RealtimeKitClient` | ❌ | - | The RealtimeKit meeting instance |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkParticipant } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkParticipant participant={participant} />;
}
```

### With Properties

```tsx
import { RtkParticipant } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return (
		<RtkParticipant
			participant={participant}
			meeting={meeting}
			iconPack={customIconPack}
		/>
	);
}
```
