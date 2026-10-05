---
description: API reference for RtkButton component (Android Library)
title: RtkButton
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/button/og.png?v=1f01e255896b340a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkButton

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/button/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button that follows the RealtimeKit design system.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `rtk_btn_variant` | `primary \| secondary \| danger` | ❌ | - | Button variant |

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming |
| `refresh` | `uiTokens: RtkDesignTokens` | Refresh the button with the provided tokens |

## Usage Examples

### Basic Usage

```xml
<com.cloudflare.realtimekit.ui.view.button.RtkButton
    android:id="@+id/btn_id"
    android:layout_width="200dp"
    android:layout_height="48dp"
    android:text="Text on Button"
    app:rtk_btn_variant="primary" />
```
