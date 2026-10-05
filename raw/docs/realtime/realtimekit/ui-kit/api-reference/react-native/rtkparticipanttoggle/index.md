---
description: API reference for RtkParticipantToggle component (React Native Library)
title: RtkParticipantToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkparticipanttoggle/og.png?v=03dd58ff2b0e1971
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkParticipantToggle

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkparticipanttoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Toggle button to open the participants sidebar panel. Shows a badge with pending request count.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | - | Icon size |
| `variant` | `'button' \| 'horizontal'` | ❌ | - | Layout variant |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `states` | `States` | ❌ | - | UI state object |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkParticipantToggle } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkParticipantToggle meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkParticipantToggle } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkParticipantToggle meeting={meeting} size="md" variant="button" />;
}
```
