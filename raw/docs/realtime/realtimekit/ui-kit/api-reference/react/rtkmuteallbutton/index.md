---
description: API reference for RtkMuteAllButton component (React Library)
title: RtkMuteAllButton
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmuteallbutton/og.png?v=7f931671203606fc
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkMuteAllButton

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmuteallbutton/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkMuteAllButton } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkMuteAllButton />;
}
```

### With Properties

```tsx
import { RtkMuteAllButton } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkMuteAllButton
      meeting={meeting}
      size="md"
      variant="button"
    />
  );
}
```
