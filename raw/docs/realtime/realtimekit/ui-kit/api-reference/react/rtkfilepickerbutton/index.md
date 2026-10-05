---
description: API reference for RtkFilePickerButton component (React Library)
title: RtkFilePickerButton
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfilepickerbutton/og.png?v=05b99ef6819ef232
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkFilePickerButton

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfilepickerbutton/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `filter` | `string` | ✅ | - | File type filter to open file picker with |
| `icon` | `keyof IconPack1` | ✅ | - | Icon |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `label` | `string` | ✅ | - | Label for tooltip |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkFilePickerButton } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkFilePickerButton />;
}
```

### With Properties

```tsx
import { RtkFilePickerButton } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkFilePickerButton
      filter="example"
      icon={defaultIconPack}
      label="example"
    />
  );
}
```
