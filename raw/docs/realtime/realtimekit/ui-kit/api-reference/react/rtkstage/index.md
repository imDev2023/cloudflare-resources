---
description: API reference for RtkStage component (React Library)
title: RtkStage
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkstage/og.png?v=91a29548bbb0da98
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkStage

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkstage/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component used as a stage that commonly houses the `grid` and `sidebar` components.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkStage } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkStage />;
}
```

### With Properties

```tsx
import { RtkStage } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkStage
      iconPack={defaultIconPack}
      t={rtki18n}
    />
  );
}
```
