---
description: API reference for RtkPollsToggle component (React Library)
title: RtkPollsToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpollstoggle/og.png?v=0cc4ab9e48fe46a2
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkPollsToggle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpollstoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button which toggles visibility of polls. You need to pass the `meeting` object to it to see the unread polls count badge. When clicked it emits a `rtkStateUpdate` event with the data:

```ts
{ activeSidebar: boolean; sidebar: 'polls' }
```

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkPollsToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkPollsToggle />;
}
```

### With Properties

```tsx
import { RtkPollsToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkPollsToggle
      meeting={meeting}
      size="md"
      variant="button"
    />
  );
}
```
