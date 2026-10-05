---
description: API reference for RtkGridPagination component (React Native Library)
title: RtkGridPagination
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkgridpagination/og.png?v=e5272e9f91aade2a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkGridPagination

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkgridpagination/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Pagination controls for navigating between pages of participants in the grid. Shows page numbers and navigation arrows.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack |
| `states` | `States` | ❌ | - | UI state object |
| `t` | `RtkI18n` | ❌ | - | i18n translation function |

## Usage Examples

### Basic Usage

```tsx
import { RtkGridPagination } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return <RtkGridPagination meeting={meeting} />;
}
```

### With Properties

```tsx
import { RtkGridPagination } from "@cloudflare/realtimekit-react-native-ui";

function MyComponent() {
	return (
		<RtkGridPagination
			meeting={meeting}
			iconPack={customIconPack}
			states={states}
		/>
	);
}
```
