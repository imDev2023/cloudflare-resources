---
description: API reference for RtkLiveStreamPlayer component (React Native Library)
title: RtkLiveStreamPlayer
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtklivestreamplayer/og.png?v=7cc34a2379595bfd
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkLiveStreamPlayer

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtklivestreamplayer/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

IVS (Amazon Interactive Video Service) player for viewing livestream playback. Requires `amazon-ivs-react-native-player` peer dependency.

## Properties

This component does not accept any props. It reads the livestream URL from the meeting context.

## Usage Examples

### Basic Usage

```tsx
import { RtkLiveStreamPlayer } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkLiveStreamPlayer />;
}
```
