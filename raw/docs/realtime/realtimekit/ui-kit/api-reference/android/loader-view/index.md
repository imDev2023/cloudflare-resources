---
description: API reference for RtkLoaderView component (Android Library)
title: RtkLoaderView
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/loader-view/og.png?v=5a02bd79315a6e25
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkLoaderView

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/loader-view/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A full-screen loader component that can be displayed while a connection is being established with the RealtimeKit server. You must manually control the visibility of this view based on your application's connection state.

## Usage Examples

### Basic Usage

```xml
<com.cloudflare.realtimekit.ui.view.RtkLoaderView
    android:id="@+id/clLoader"
    android:layout_width="match_parent"
    android:layout_height="match_parent" />
```
