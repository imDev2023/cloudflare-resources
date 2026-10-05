---
description: API reference for RtkPolls component (React Native Library)
title: RtkPolls
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpolls/og.png?v=14c04eab217bec0d
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkPolls

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpolls/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Full polls panel showing all polls with voting and a create poll form for hosts.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `config` | `UIConfig` | ❌ | `defaultConfig` | UI configuration object |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | `'sm'` | Size variant |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkPolls } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkPolls meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkPolls } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkPolls meeting={meeting} size="md" config={customConfig} />;
}
```
