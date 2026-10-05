---
description: API reference for RtkParticipantsToggle component (React Library)
title: RtkParticipantsToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantstoggle/og.png?v=63c68c3f13abad03
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkParticipantsToggle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantstoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button which toggles visibility of participants. When clicked it emits a `rtkStateUpdate` event with the data:

```ts
{ activeSidebar: boolean; sidebar: 'participants' }
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
import { RtkParticipantsToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkParticipantsToggle />;
}
```

### With Properties

```tsx
import { RtkParticipantsToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkParticipantsToggle
      meeting={meeting}
      size="md"
      variant="button"
    />
  );
}
```
