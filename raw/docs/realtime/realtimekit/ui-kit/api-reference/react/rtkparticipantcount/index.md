---
description: API reference for RtkParticipantCount component (React Library)
title: RtkParticipantCount
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantcount/og.png?v=9a4eeae27730b734
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkParticipantCount

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantcount/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which shows count of total joined participants in a meeting.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkParticipantCount } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkParticipantCount />;
}
```

### With Properties

```tsx
import { RtkParticipantCount } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkParticipantCount
      meeting={meeting}
      size="md"
    />
  );
}
```
