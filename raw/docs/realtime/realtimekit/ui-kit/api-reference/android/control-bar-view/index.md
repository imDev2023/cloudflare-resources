---
description: API reference for RtkControlBarView component (Android Library)
title: RtkControlBarView
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/control-bar-view/og.png?v=64e0d37bcef5ef44
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkControlBarView

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/control-bar-view/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A base container for control bar buttons. Provides design token support and background styling.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming |

## Usage Examples

### Basic Usage

```xml
<com.cloudflare.realtimekit.ui.view.controlbars.RtkControlBarView
    android:id="@+id/rtk_control_bar"
    android:layout_width="match_parent"
    android:layout_height="wrap_content" />
```
