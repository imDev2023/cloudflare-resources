---
description: API reference for RtkPollForm component (React Native Library)
title: RtkPollForm
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpollform/og.png?v=be481439000ec138
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkPollForm

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpollform/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Form for creating a new poll with question, dynamic options, anonymous voting, and hide results toggles.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |
| `onRtkCreatePoll` | `any` | ❌ | - | Callback when poll is created (receives question, options, anonymous, hideVotes) |

## Usage Examples

### Basic Usage

```tsx
import { RtkPollForm } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkPollForm onRtkCreatePoll={(data) => handleCreatePoll(data)} />;
}
```

### With Properties

```tsx
import { RtkPollForm } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return (
		<RtkPollForm
			onRtkCreatePoll={(data) => handleCreatePoll(data)}
			iconPack={customIconPack}
		/>
	);
}
```
