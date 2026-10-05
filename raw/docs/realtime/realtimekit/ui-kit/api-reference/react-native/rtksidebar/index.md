---
description: API reference for RtkSidebar component (React Native Library)
title: RtkSidebar
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksidebar/og.png?v=e0ecf141c81f4e77
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkSidebar

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksidebar/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Full-screen sidebar modal with tabbed navigation for chat, participants, polls, and plugins panels.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `config` | `UIConfig` | ❌ | `defaultConfig` | UI configuration object |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | `'sm'` | Size variant |
| `states` | `States` | ❌ | - | UI state object |
| `defaultSection` | `'chat' \| 'none' \| 'participants' \| 'plugins' \| 'polls'` | ❌ | `'chat'` | Default active tab |
| `enabledSections` | `SidebarSection[]` | ❌ | `['chat', 'polls', 'participants', 'plugins']` | Which sidebar sections to display |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkSidebar } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkSidebar meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkSidebar } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return (
		<RtkSidebar
			meeting={meeting}
			defaultSection="chat"
			enabledSections={["chat", "participants", "polls"]}
			size="md"
		/>
	);
}
```
