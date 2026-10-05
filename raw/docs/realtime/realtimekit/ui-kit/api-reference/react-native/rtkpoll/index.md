---
description: API reference for RtkPoll component (React Native Library)
title: RtkPoll
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpoll/og.png?v=54810cd33a95719e
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkPoll

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpoll/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Renders a single poll with question, votable options, vote counts, and voter avatars.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `poll` | `Poll` | ✅ | - | The poll object to display |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `onRtkVotePoll` | `any` | ❌ | - | Callback when a vote is cast (receives option index) |
| `self` | `string` | ❌ | - | Self user ID |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkPoll } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkPoll poll={poll} meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkPoll } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return (
		<RtkPoll
			poll={poll}
			meeting={meeting}
			onRtkVotePoll={(index) => handleVote(index)}
			self={selfUserId}
		/>
	);
}
```
