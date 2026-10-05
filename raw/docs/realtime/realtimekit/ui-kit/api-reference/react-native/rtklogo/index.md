---
description: API reference for RtkLogo component (React Native Library)
title: RtkLogo
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtklogo/og.png?v=9290dbb1f04a0c9e
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkLogo

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtklogo/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Displays a logo from a URL (SVG format) in the meeting header.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `any` | ❌ | - | The RealtimeKit meeting instance |
| `config` | `UIConfig` | ❌ | - | UI configuration object |
| `logoUrl` | `string` | ❌ | - | URL of the logo SVG to display |
| `style` | `StyleProps` | ❌ | - | Style object with width/height for the logo |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkLogo } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkLogo logoUrl="https://example.com/logo.svg" />;
}
```

### With Properties

```tsx
import { RtkLogo } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return (
		<RtkLogo
			logoUrl="https://example.com/logo.svg"
			style={{ width: 120, height: 40 }}
			config={customConfig}
		/>
	);
}
```
