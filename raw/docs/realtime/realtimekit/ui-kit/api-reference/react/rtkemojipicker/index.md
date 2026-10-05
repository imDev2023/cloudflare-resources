---
description: API reference for RtkEmojiPicker component (React Library)
title: RtkEmojiPicker
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkemojipicker/og.png?v=a60bffbf6aec76b5
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkEmojiPicker

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkemojipicker/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A very simple emoji picker component.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `focusWhenOpened` | `boolean` | ✅ | - | Controls whether or not to focus on mount |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkEmojiPicker } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkEmojiPicker />;
}
```

### With Properties

```tsx
import { RtkEmojiPicker } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkEmojiPicker
      focusWhenOpened={true}
    />
  );
}
```
