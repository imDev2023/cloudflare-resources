---
description: API reference for RtkImageViewer component (React Native Library)
title: RtkImageViewer
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkimageviewer/og.png?v=4aa4d9a6eb8410b0
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkImageViewer

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkimageviewer/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Image viewer with fullscreen toggle and download functionality for chat images.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `image` | `any` | ✅ | - | The image message object |
| `size` | `'lg' \| 'md' \| 'sm' \| 'xl'` | ❌ | - | Size variant |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |
| `isContinued` | `boolean` | ❌ | `false` | Whether this message continues from the same sender |
| `_id` | `string \| number` | ❌ | - | Unique identifier for fullscreen tracking |

## Usage Examples

### Basic Usage

```tsx
import { RtkImageViewer } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkImageViewer image={imageMessage} />;
}
```

### With Properties

```tsx
import { RtkImageViewer } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkImageViewer image={imageMessage} size="md" _id="viewer-1" />;
}
```
