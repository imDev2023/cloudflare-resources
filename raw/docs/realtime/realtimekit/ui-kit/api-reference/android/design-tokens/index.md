---
description: API reference for RtkDesignTokens component (Android Library)
title: RtkDesignTokens
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/design-tokens/og.png?v=e03f88d3c9e5e4b1
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkDesignTokens

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/design-tokens/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The top-level design token container for customizing the look and feel of all UI Kit components.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `colors` | `RtkColorTokens` | ❌ | - | Color theme tokens |
| `borderWidth` | `RtkBorderWidthToken` | ❌ | - | Border width token |
| `borderRadius` | `RtkBorderRadiusToken` | ❌ | - | Border radius token |

## Usage Examples

### Basic Usage

```kotlin
val designTokens = RtkDesignTokens(
    colors = RtkColorTokens(
        brand = BrandColor(
            shade300 = Color.parseColor("#497CFD"),
            shade400 = Color.parseColor("#356EFD"),
            shade500 = Color.parseColor("#2160FD"),
            shade600 = Color.parseColor("#0D52FD"),
            shade700 = Color.parseColor("#0046E5")
        ),
        background = BackgroundColor(
            shade600 = Color.parseColor("#2C2C2C"),
            shade700 = Color.parseColor("#242424"),
            shade800 = Color.parseColor("#1C1C1C"),
            shade900 = Color.parseColor("#141414"),
            shade1000 = Color.parseColor("#0C0C0C")
        )
    ),
    borderRadius = RtkBorderRadiusToken.Rounded,
    borderWidth = RtkBorderWidthToken.Thin
)
```
