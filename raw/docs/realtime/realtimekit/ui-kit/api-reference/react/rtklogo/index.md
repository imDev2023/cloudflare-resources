---
description: API reference for RtkLogo component (React Library)
title: RtkLogo
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklogo/og.png?v=9290dbb1f04a0c9e
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkLogo

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklogo/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which loads the logo from your config, or via the `logo-url` attribute.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object |
| `logoUrl` | `string` | ✅ | - | Logo URL |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkLogo } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkLogo />;
}
```

### With Properties

```tsx
import { RtkLogo } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkLogo
      logoUrl="example"
      meeting={meeting}
    />
  );
}
```
