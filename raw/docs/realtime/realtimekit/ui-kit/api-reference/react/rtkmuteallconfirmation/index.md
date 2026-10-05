---
description: API reference for RtkMuteAllConfirmation component (React Library)
title: RtkMuteAllConfirmation
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmuteallconfirmation/og.png?v=8cec89538767df37
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkMuteAllConfirmation

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmuteallconfirmation/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkMuteAllConfirmation } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkMuteAllConfirmation />;
}
```

### With Properties

```tsx
import { RtkMuteAllConfirmation } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkMuteAllConfirmation
      meeting={meeting}
    />
  );
}
```
