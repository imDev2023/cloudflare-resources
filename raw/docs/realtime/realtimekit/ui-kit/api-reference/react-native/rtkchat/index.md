---
description: API reference for RtkChat component (React Native Library)
title: RtkChat
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkchat/og.png?v=2ebfb16bf4516e30
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkChat

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkchat/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Full chat interface with message list, text input, image/file upload support, and pinned messages.

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
import { RtkChat } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkChat meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkChat } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkChat meeting={meeting} size="md" config={customConfig} />;
}
```
