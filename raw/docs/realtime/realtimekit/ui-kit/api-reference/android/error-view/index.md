---
description: API reference for RtkErrorView component (Android Library)
title: RtkErrorView
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/error-view/og.png?v=200350d042bb7960
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkErrorView

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/error-view/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A full-screen error view that displays an error message and a retry button.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `refresh` | `errorMessage: String, onRetryClicked: () -> Unit` | Set the error message and retry button callback |

## Usage Examples

### Basic Usage

```xml
<com.cloudflare.realtimekit.ui.view.RtkErrorView
    android:id="@+id/rtk_error_view"
    android:layout_width="match_parent"
    android:layout_height="match_parent" />
```

### With Methods

```kotlin
val errorView = findViewById<RtkErrorView>(R.id.rtk_error_view)
errorView.refresh("Failed to connect") {
    // Retry connection
}
```
