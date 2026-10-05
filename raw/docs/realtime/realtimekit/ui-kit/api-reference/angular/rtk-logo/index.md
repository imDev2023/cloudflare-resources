---
description: API reference for rtk-logo component (Angular Library)
title: rtk-logo
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-logo/og.png?v=f2e032250683d8eb
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-logo

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-logo/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

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

```html
<!-- component.html -->
<rtk-logo></rtk-logo>
```

### With Properties

```html
<!-- component.html -->
<rtk-logo
 logoUrl="example"
 [meeting]="meeting">
</rtk-logo>
```
