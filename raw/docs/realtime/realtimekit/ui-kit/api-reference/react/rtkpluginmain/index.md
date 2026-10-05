---
description: API reference for RtkPluginMain component (React Library)
title: RtkPluginMain
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpluginmain/og.png?v=ff915f2ce6db5965
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkPluginMain

Last updated Jun 18, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpluginmain/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which renders a plugin's UI.

The plugin's `component` (an HTMLElement) is placed into this element's light DOM and projected into the shadow DOM layout via a `<slot>`. This ensures external CSS from the consuming application continues to apply to the plugin content.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting |
| `plugin` | `RTKPlugin` | ✅ | - | Plugin |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkPluginMain } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkPluginMain />;
}
```

### With Properties

```tsx
import { RtkPluginMain } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkPluginMain
      meeting={meeting}
      plugin={rtkplugin}
    />
  );
}
```
