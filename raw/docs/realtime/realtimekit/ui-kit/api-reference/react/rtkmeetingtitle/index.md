---
description: API reference for RtkMeetingTitle component (React Library)
title: RtkMeetingTitle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmeetingtitle/og.png?v=1d8678b25a56f256
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkMeetingTitle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmeetingtitle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Displays the title of the meeting.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkMeetingTitle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkMeetingTitle />;
}
```

### With Properties

```tsx
import { RtkMeetingTitle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkMeetingTitle
      meeting={meeting}
    />
  );
}
```
