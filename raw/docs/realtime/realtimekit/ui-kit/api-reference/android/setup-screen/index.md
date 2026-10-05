---
description: API reference for RtkSetupFragment component (Android Library)
title: RtkSetupFragment
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/setup-screen/og.png?v=a8b107a5832f7d84
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkSetupFragment

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/setup-screen/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A screen shown before joining the meeting, where you can edit your display name and media settings.

## Usage Examples

### Basic Usage

```kotlin
val rtkSetupFragment = RtkSetupFragment()
supportFragmentManager.beginTransaction()
    .add(R.id.fragmentContainer, rtkSetupFragment)
    .commit()
```
