---
description: API reference for RtkDraftAttachmentView component (React Library)
title: RtkDraftAttachmentView
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdraftattachmentview/og.png?v=9a5c68a35b9a82b9
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkDraftAttachmentView

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdraftattachmentview/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which renders the draft attachment to send

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `attachment` | `{ type: 'image' \| 'file'; file: File; }` | ✅ | - | Attachment to display |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkDraftAttachmentView } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkDraftAttachmentView />;
}
```

### With Properties

```tsx
import { RtkDraftAttachmentView } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkDraftAttachmentView
      attachment={{}}
    />
  );
}
```
