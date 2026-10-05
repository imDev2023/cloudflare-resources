---
description: API reference for RtkFullscreenToggle component (React Library)
title: RtkFullscreenToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfullscreentoggle/og.png?v=a5e29226252e7f01
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkFullscreenToggle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfullscreentoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button which toggles full screen mode for any existing `rtk-meeting` component in the DOM.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `targetElement` | `HTMLElement` | ✅ | - | Target Element to fullscreen |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkFullscreenToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkFullscreenToggle />;
}
```

### With Properties

```tsx
import { RtkFullscreenToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkFullscreenToggle
      size="md"
      targetElement={htmlelement}
      variant="button"
    />
  );
}
```
