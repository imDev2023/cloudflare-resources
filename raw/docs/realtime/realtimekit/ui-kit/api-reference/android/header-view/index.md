---
description: API reference for RtkHeaderView component (Android Library)
title: RtkHeaderView
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/header-view/og.png?v=01c02c0fc87d80fb
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkHeaderView

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/header-view/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A base header view component. Provides background styling and design token support.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `activate` | `meeting: RealtimeKitClient` | Bind the header to the meeting state |
| `applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming |

## Usage Examples

### Basic Usage

```xml
<com.cloudflare.realtimekit.ui.view.headers.RtkHeaderView
    android:id="@+id/rtk_header"
    android:layout_width="match_parent"
    android:layout_height="wrap_content" />
```

### With Methods

```kotlin
val header = findViewById<RtkHeaderView>(R.id.rtk_header)
header.activate(meeting)
```
