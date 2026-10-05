---
description: API reference for RtkGridView component (Android Library)
title: RtkGridView
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/grid-view/og.png?v=ce270aa7a4b0abff
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkGridView

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/grid-view/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The main grid component which handles the participant grid layout, pagination, and focus modes.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `activate` | `meeting: RealtimeKitClient` | Bind the grid to the meeting state |
| `refresh` | `force: Boolean` | Force a refresh of the grid layout and participants |
| `enableFocusMode` | - | Enable focus mode, which hides the horizontal peer strip and full-screen toggle to keep attention on the primary speaker or shared content |
| `applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming |

## Usage Examples

### Basic Usage

```xml
<com.cloudflare.realtimekit.ui.view.grid.RtkGridView
    android:id="@+id/rtk_grid"
    android:layout_width="match_parent"
    android:layout_height="match_parent" />
```

### With Methods

```kotlin
val grid = findViewById<RtkGridView>(R.id.rtk_grid)
grid.activate(meeting)
```
