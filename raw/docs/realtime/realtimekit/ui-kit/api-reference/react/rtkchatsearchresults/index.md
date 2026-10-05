---
description: API reference for RtkChatSearchResults component (React Library)
title: RtkChatSearchResults
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatsearchresults/og.png?v=e550fd7eb1466b3a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkChatSearchResults

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatsearchresults/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

@deprecated `rtk-chat-search-results` is deprecated and will be removed soon. Use `rtk-chat-messages-ui-paginated` instead. -

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `channelId` | `string` | ✅ | - | Channel id |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `query` | `string` | ✅ | - | Search query |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkChatSearchResults } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkChatSearchResults />;
}
```

### With Properties

```tsx
import { RtkChatSearchResults } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkChatSearchResults
      channelId="example"
      meeting={meeting}
      query="example"
    />
  );
}
```
