---
description: API reference for RtkUIProvider component (React Native Library)
title: RtkUIProvider
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkuiprovider/og.png?v=c471f3c953f56b03
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkUIProvider

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkuiprovider/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Context provider component that wraps the meeting UI. Provides SafeAreaView, state management, and back button handling. Must wrap all Rtk UI components.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | ✅ | - | Child components to wrap |

## Usage Examples

### Basic Usage

```tsx
import {
	RtkUIProvider,
	RtkMeeting,
} from "@cloudflare/realtimekit-react-native-ui";

function App() {
	return (
		<RtkUIProvider>
			<RtkMeeting meeting={meeting} />
		</RtkUIProvider>
	);
}
```

### With Properties

```tsx
import {
	RtkUIProvider,
	RtkGrid,
	RtkControlbar,
	RtkHeader,
} from "@cloudflare/realtimekit-react-native-ui";

function App() {
	return (
		<RtkUIProvider>
			<RtkHeader meeting={meeting} />
			<RtkGrid meeting={meeting} />
			<RtkControlbar meeting={meeting} />
		</RtkUIProvider>
	);
}
```
