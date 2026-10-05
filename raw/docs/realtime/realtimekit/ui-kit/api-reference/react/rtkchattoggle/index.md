---
description: API reference for RtkChatToggle component (React Library)
title: RtkChatToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchattoggle/og.png?v=52a6799656a647a7
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkChatToggle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchattoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button which toggles visibility of chat. You need to pass the `meeting` object to it to see the unread messages count badge. When clicked it emits a `rtkStateUpdate` event with the data:

```ts
{ activeSidebar: boolean; sidebar: 'chat' }
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
import { RtkChatToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkChatToggle />;
}
```

### With Properties

```tsx
import { RtkChatToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkChatToggle
      meeting={meeting}
      size="md"
      variant="button"
    />
  );
}
```
