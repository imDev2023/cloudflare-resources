---
description: API reference for RtkPollForm component (React Library)
title: RtkPollForm
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpollform/og.png?v=be481439000ec138
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkPollForm

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpollform/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component that lets you create a poll.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkPollForm } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkPollForm />;
}
```

### With Properties

```tsx
import { RtkPollForm } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkPollForm
      iconPack={defaultIconPack}
      t={rtki18n}
    />
  );
}
```
