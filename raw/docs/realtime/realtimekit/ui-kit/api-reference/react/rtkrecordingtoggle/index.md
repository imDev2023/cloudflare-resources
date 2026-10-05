---
description: API reference for RtkRecordingToggle component (React Library)
title: RtkRecordingToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkrecordingtoggle/og.png?v=262c9bf0f1e54224
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkRecordingToggle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkrecordingtoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button which toggles recording state of a meeting. Only a privileged user can perform this action, thus the button will not be visible for participants who don't have the permission to record a meeting.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `disabled` | `boolean` | ✅ | - | Disable the button |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkRecordingToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkRecordingToggle />;
}
```

### With Properties

```tsx
import { RtkRecordingToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkRecordingToggle
      disabled={true}
      meeting={meeting}
      size="md"
    />
  );
}
```
