---
description: API reference for RtkControlBarButton component (Android Library)
title: RtkControlBarButton
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/control-bar-button/og.png?v=1fd291aff9381827
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkControlBarButton

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/control-bar-button/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A skeleton component used for composing custom controlbar buttons.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `rtk_cbb_icon` | `reference` | ❌ | - | Drawable resource for the button icon |
| `rtk_cbb_variant` | `button \| horizontal` | ❌ | `button` | Layout variant |
| `rtk_cbb_showText` | `boolean` | ❌ | `true` | Whether to show the label text |
| `rtk_cbb_iconSize` | `dimension` | ❌ | - | Size of the icon |
| `rtk_cbb_iconPadding` | `dimension` | ❌ | - | Padding between icon and label |

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming |
| `setIconDrawable` | `drawable: Drawable?` | Set the button icon |
| `setIconTint` | `color: Int` | Set the icon tint color |
| `setText` | `text: String?` | Set the button label text |
| `setProcessingState` | `processing: Boolean` | Show or hide a loading spinner |

## Usage Examples

### Basic Usage

```xml
<com.cloudflare.realtimekit.ui.view.controlbarbuttons.RtkControlBarButton
    android:id="@+id/rtk_control_bar_button"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    app:rtk_cbb_showText="true"
    app:rtk_cbb_variant="button" />
```

### With Methods

```kotlin
val buttonView = findViewById<RtkControlBarButton>(R.id.rtk_control_bar_button)
buttonView.setOnClickListener { }
```
