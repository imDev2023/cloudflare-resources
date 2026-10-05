---
title: RTKPip
image: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkpip/og.png?v=f93a8df6a8dab696
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RTKPip

Last updated Jul 22, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkpip/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Modules

<dl><dt><a href="#module_RTKPip">RTKPip</a></dt>
<dd></dd>
</dl>

## Functions

<dl><dt><a href="#getInitials">getInitials()</a></dt>
<dd>

Code from ui-kit. Same method used in the avatar component

</dd></dl>

- [RTKPip](#module_RTKPip)
  - [.disable](#module_RTKPip+disable)
  - [.init(\[options\])](#module_RTKPip+init)
  - [.disableSource(source)](#module_RTKPip+disableSource)
  - [.addSource(id, element, enabled, \[displayText\])](#module_RTKPip+addSource)
  - [.updateSource(id, source)](#module_RTKPip+updateSource)
  - [.removeSource(id)](#module_RTKPip+removeSource)
  - [.removePinnedSource(id)](#module_RTKPip+removePinnedSource)
  - [.removeAllSources()](#module_RTKPip+removeAllSources)
  - [.enable()](#module_RTKPip+enable)

### meeting.participants.pip.disable

Disable PiP

**Kind**: instance property of [`RTKPip`](#module_RTKPip)  

### meeting.participants.pip.init(\[options])

Initialize PiP and prepare sources

**Kind**: instance method of [`RTKPip`](#module_RTKPip)

| Param | Type |
| --- | --- |
| \[options] | `Object` |
| \[options.height] | `number` |
| \[options.width] | `number` |

### meeting.participants.pip.disableSource(source)

**Kind**: instance method of [`RTKPip`](#module_RTKPip)

| Param | Type |
| --- | --- |
| source | `string` |

### meeting.participants.pip.addSource(id, element, enabled, \[displayText])

Add a video source from the participant grid

**Kind**: instance method of [`RTKPip`](#module_RTKPip)

| Param | Type | Description |
| --- | --- | --- |
| id | `string` | id for the source (ex. participant id) |
| element | `HTMLVideoElement` | HTMLVideoElement for the video source |
| enabled | `boolean` | if source is enabled |
| \[displayText] | `string` | two character display text |

### meeting.participants.pip.updateSource(id, source)

Update a video source

**Kind**: instance method of [`RTKPip`](#module_RTKPip)

| Param | Type |
| --- | --- |
| id | `string` |
| source | `any` |

### meeting.participants.pip.removeSource(id)

Remove the video source for the participant

**Kind**: instance method of [`RTKPip`](#module_RTKPip)

| Param | Description |
| --- | --- |
| id | id for the source (ex. participant id) |

### meeting.participants.pip.removePinnedSource(id)

Remove the pinned source

**Kind**: instance method of [`RTKPip`](#module_RTKPip)

| Param | Description |
| --- | --- |
| id | id for the source (ex. participant id) |

### meeting.participants.pip.removeAllSources()

Remove all sources

**Kind**: instance method of [`RTKPip`](#module_RTKPip)  

### meeting.participants.pip.enable()

Enable PiP

**Kind**: instance method of [`RTKPip`](#module_RTKPip)  

Code from ui-kit. Same method used in the avatar component

**Kind**: global function
