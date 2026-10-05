---
description: API reference for RtkScreenshareView component (React Library)
title: RtkScreenshareView
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkscreenshareview/og.png?v=7e68049e577e8f34
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkScreenshareView

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkscreenshareview/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which plays a participant's screenshared video. It also allows for placement of other components similar to `rtk-participant-tile`. This component will not render anything if the participant hasn't start screensharing.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `hideFullScreenButton` | `boolean` | ✅ | - | Hide full screen button |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `nameTagPosition` | `\| 'bottom-left' \| 'bottom-right' \| 'bottom-center' \| 'top-left' \| 'top-right' \| 'top-center'` | ✅ | - | Position of name tag |
| `participant` | `Peer` | ✅ | - | Participant object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `'solid' \| 'gradient'` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkScreenshareView } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkScreenshareView />;
}
```

### With Properties

```tsx
import { RtkScreenshareView } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkScreenshareView
      hideFullScreenButton={true}
      meeting={meeting}
      nameTagPosition={| 'bottom-left'
    | 'bottom-right'
    | 'bottom-center'
    | 'top-left'
    | 'top-right'
    | 'top-center'}
    />
  );
}
```
