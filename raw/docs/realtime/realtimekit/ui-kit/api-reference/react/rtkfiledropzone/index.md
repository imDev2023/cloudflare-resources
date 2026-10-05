---
description: API reference for RtkFileDropzone component (React Library)
title: RtkFileDropzone
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfiledropzone/og.png?v=a3c5d3e2b2a892fb
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkFileDropzone

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfiledropzone/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `hostEl` | `HTMLElement` | ✅ | - | Host element on which drop events to attach |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkFileDropzone } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkFileDropzone />;
}
```

### With Properties

```tsx
import { RtkFileDropzone } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkFileDropzone
      hostEl={htmlelement}
    />
  );
}
```
