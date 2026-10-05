---
title: RTKRecording
image: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkrecording/og.png?v=63dc70c155af4902
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RTKRecording

Last updated Jul 22, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkrecording/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The RTKRecording module represents the state of the current recording, and allows to start/stop recordings and check if there's a recording in progress.

- [RTKRecording](#module_RTKRecording)
  - [.start()](#module_RTKRecording+start)
  - [.stop()](#module_RTKRecording+stop)
  - [.pause()](#module_RTKRecording+pause)
  - [.resume()](#module_RTKRecording+resume)

### meeting.recording.start()

Starts recording the meeting.

**Kind**: instance method of [`RTKRecording`](#module_RTKRecording)  

### meeting.recording.stop()

Stops all recording currently in 'RECORDING' state

**Kind**: instance method of [`RTKRecording`](#module_RTKRecording)  

### meeting.recording.pause()

Pauses all recording currently in 'RECORDING' state

**Kind**: instance method of [`RTKRecording`](#module_RTKRecording)  

### meeting.recording.resume()

Resumes all recording currently in 'PAUSED' state

**Kind**: instance method of [`RTKRecording`](#module_RTKRecording)
