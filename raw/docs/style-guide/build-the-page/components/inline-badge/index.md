---
description: Display inline status badges like Beta or New.
title: Inline badge
image: https://developers.cloudflare.com/style-guide/build-the-page/components/inline-badge/og.png?v=66332ac6a41842d0
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/style-guide/llms.txt  
> Use this file to discover all available pages before exploring further.

# Inline badge

Last updated Aug 20, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/style-guide/build-the-page/components/inline-badge/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The `InlineBadge` component is used `10` times on `10` pages.

<details>

<summary>

See all examples of pages that use InlineBadge

</summary>

Used **10** times.

**Pages**

- <a href="https://developers.cloudflare.com/agents/communication-channels/voice/">/agents/communication-channels/voice/</a>-<a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/agents/communication-channels/voice.mdx">Source</a>
- <a href="https://developers.cloudflare.com/agents/examples/browser-agent/">/agents/examples/browser-agent/</a>-<a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/agents/examples/browser-agent.mdx">Source</a>
- <a href="https://developers.cloudflare.com/agents/examples/voice-agent/">/agents/examples/voice-agent/</a>-<a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/agents/examples/voice-agent.mdx">Source</a>
- <a href="https://developers.cloudflare.com/agents/tools/browser/">/agents/tools/browser/</a>-<a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/agents/tools/browser.mdx">Source</a>
- <a href="https://developers.cloudflare.com/browser-run/features/session-recording/">/browser-run/features/session-recording/</a>-<a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/browser-run/features/session-recording.mdx">Source</a>
- <a href="https://developers.cloudflare.com/ddos-protection/about/attack-coverage/">/ddos-protection/about/attack-coverage/</a>-<a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/ddos-protection/about/attack-coverage.mdx">Source</a>
- <a href="https://developers.cloudflare.com/ssl/edge-certificates/geokey-manager/setup/">/ssl/edge-certificates/geokey-manager/setup/</a>-<a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/ssl/edge-certificates/geokey-manager/setup.mdx">Source</a>
- <a href="https://developers.cloudflare.com/stream/stream-live/start-stream-live/">/stream/stream-live/start-stream-live/</a>-<a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/stream/stream-live/start-stream-live.mdx">Source</a>
- <a href="https://developers.cloudflare.com/stream/viewing-videos/using-the-stream-player/">/stream/viewing-videos/using-the-stream-player/</a>-<a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/stream/viewing-videos/using-the-stream-player/index.mdx">Source</a>
- <a href="https://developers.cloudflare.com/workers/wrangler/commands/artifacts/">/workers/wrangler/commands/artifacts/</a>-<a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/workers/wrangler/commands/artifacts.mdx">Source</a>

**Partials**

</details>

Recommendation: Avoid inline badges

Our current recommendation is to avoid inline badges, since they may hurt readability.

Guidelines:

- Mention beta/alpha/early access in the feature's main documentation page (use the [`<Badge>`](https://developers.cloudflare.com/style-guide/build-the-page/components/badges/) component for this purpose).
- If an additional reference is needed in the middle of the text, use "(beta)", with no special formatting, after the feature name.
- For instructions related to the feature (such as instructions on turning the feature on or off), you may mention again it's in beta, and also include "(beta)" in the side nav.

## Component

To adopt this styling in a React component, apply the `sl-badge` class to a `span` element.

```mdx
import { InlineBadge } from '~/components';

### Alpha <InlineBadge preset="alpha" />

### Beta <InlineBadge preset="beta" />

### Deprecated <InlineBadge preset="deprecated" />

### Early Access <InlineBadge preset="early-access" />

### Legacy <InlineBadge preset="legacy" />

### Default <InlineBadge text="Default" />
```

## Inputs

Either `preset` or `text` and `variant` must be specified.

### Presets

- `alpha`
  - **Text**: `Alpha`
  - **Variant** `success`
- `beta`
  - **Text**: `Beta`
  - **Variant** `caution`
- `deprecated`
  - **Text**: `Deprecated`
  - **Variant** `danger`
- `early-access`
  - **Text**: `Early Access`
  - **Variant** `note`
- `legacy`
  - **Text**: `Legacy`
  - **Variant** `danger`

### Text

Any string.

### Variant

- `note`
  - **Color**: Blue
- `tip`
  - **Color**: Purple
- `danger`
  - **Color**: Red
- `caution`
  - **Color**: Orange
- `success`
  - **Color**: Green
