---
description: API reference for RtkParticipantCount component (React Native Library)
title: RtkParticipantCount
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkparticipantcount/og.png?v=9a4eeae27730b734
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkParticipantCount

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkparticipantcount/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Displays the total participant count and opens the participants sidebar when tapped.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkParticipantCount } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkParticipantCount meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkParticipantCount } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkParticipantCount meeting={meeting} iconPack={customIconPack} />;
}
```
