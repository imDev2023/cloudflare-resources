---
description: API reference for rtk-avatar component (Web Components (HTML) Library)
title: rtk-avatar
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-avatar/og.png?v=de0a682a094a4763
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-avatar

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-avatar/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Avatar component which renders a participant's image or their initials.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `participant` | `Peer \| WaitlistedParticipant \| { name: string; picture: string }` | ✅ | - | Participant object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `AvatarVariant` | ✅ | - | Avatar type |

## Usage Examples

### Basic Usage

```html
<rtk-avatar></rtk-avatar>
```

### With Properties

```html
<rtk-avatar
 participant="example"
 size="md"
 variant="circular">
</rtk-avatar>
```

```html
<script>
  const el = document.querySelector("rtk-avatar");

  el.participant= {};
</script>
```
