---
description: API reference for RtkPermissionsMessage component (React Native Library)
title: RtkPermissionsMessage
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpermissionsmessage/og.png?v=7f9328949d4dad39
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkPermissionsMessage

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpermissionsmessage/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Displays a message when device permissions (camera/microphone) are denied, with options to continue or open system settings.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkPermissionsMessage } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkPermissionsMessage meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkPermissionsMessage } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkPermissionsMessage meeting={meeting} iconPack={customIconPack} />;
}
```
