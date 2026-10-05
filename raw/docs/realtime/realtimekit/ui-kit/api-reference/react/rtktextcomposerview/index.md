---
description: API reference for RtkTextComposerView component (React Library)
title: RtkTextComposerView
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktextcomposerview/og.png?v=a886214c6920957c
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkTextComposerView

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktextcomposerview/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which renders a text composer

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `disabled` | `boolean` | ✅ | - | Disable the text input (default = false) |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `keyDownHandler` | `(e: KeyboardEvent)` | ✅ | - | Keydown event handler function |
| `maxLength` | `number` | ✅ | - | Max length for text input |
| `placeholder` | `string` | ✅ | - | Placeholder text |
| `rateLimitBreached` | `boolean` | ✅ | - | Boolean to indicate if rate limit is breached |
| `setText` | `(text: string, focus?: boolean)` | ❌ | - | Sets value of the text input |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |
| `value` | `string` | ✅ | - | Default value for text input |

## Usage Examples

### Basic Usage

```tsx
import { RtkTextComposerView } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkTextComposerView />;
}
```

### With Properties

```tsx
import { RtkTextComposerView } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkTextComposerView
      disabled={true}
      keyDownHandler={(e: keyboardevent)}
      maxLength={42}
    />
  );
}
```
