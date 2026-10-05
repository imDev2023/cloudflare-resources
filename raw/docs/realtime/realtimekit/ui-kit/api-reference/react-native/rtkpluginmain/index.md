---
description: API reference for RtkPluginMain component (React Native Library)
title: RtkPluginMain
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpluginmain/og.png?v=ff915f2ce6db5965
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkPluginMain

Last updated Jul 9, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpluginmain/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Renders an active plugin by loading `plugin.component.src` in a `WebView`. Includes a header bar with the plugin name, a fullscreen toggle, and an optional close button (shown when `plugin.permissions.canDeactivate` is `true`). Pressing close calls `plugin.deactivate()`.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `plugin` | `RTKPlugin` | ✅ | - | The plugin to render |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |

## Usage Examples

### Basic Usage

```tsx
import { RtkPluginMain } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkPluginMain meeting={meeting} plugin={activePlugin} />;
}
```

### With Properties

```tsx
import { RtkPluginMain } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return (
		<RtkPluginMain
			meeting={meeting}
			plugin={activePlugin}
			iconPack={customIconPack}
		/>
	);
}
```
