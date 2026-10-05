---
description: API reference for rtk-participant component (Web Components (HTML) Library)
title: rtk-participant
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participant/og.png?v=dd34515efeb9bd02
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-participant

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participant/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A participant entry component used inside `rtk-participants` which shows data like: name, picture and media device status. You can perform privileged actions on the participant too.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config object |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `participant` | `Peer` | ✅ | - | Participant object |
| `states` | `States1` | ✅ | - | States |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `view` | `ParticipantViewMode` | ✅ | - | Show participant summary |

## Usage Examples

### Basic Usage

```html
<rtk-participant></rtk-participant>
```

### With Properties

```html
<rtk-participant>
</rtk-participant>
```

```html
<script>
  const el = document.querySelector("rtk-participant");

  el.meeting= meeting
  el.participant= participant
</script>
```
