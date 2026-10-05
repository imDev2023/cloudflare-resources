---
description: API reference for RtkEmojiPickerButton component (React Library)
title: RtkEmojiPickerButton
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkemojipickerbutton/og.png?v=610473e23fbe7ccd
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkEmojiPickerButton

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkemojipickerbutton/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `isActive` | `boolean` | ✅ | - | Active state indicator |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkEmojiPickerButton } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkEmojiPickerButton />;
}
```

### With Properties

```tsx
import { RtkEmojiPickerButton } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkEmojiPickerButton
      isActive={true}
    />
  );
}
```
