---
description: API reference for RtkLiveStreamIndicator component (React Native Library)
title: RtkLiveStreamIndicator
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtklivestreamindicator/og.png?v=9f246c738f80a6be
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkLiveStreamIndicator

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtklivestreamindicator/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Displays a "Live" indicator when a livestream is active. Only visible in livestream mode for off-stage viewers.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | `'sm'` | Size variant |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkLiveStreamIndicator } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkLiveStreamIndicator meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkLiveStreamIndicator } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkLiveStreamIndicator meeting={meeting} size="md" />;
}
```
