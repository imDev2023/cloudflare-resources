---
description: Preserve credential boundaries, resource authorization, negotiation ordering, and cleanup when adapting Realtime SFU applications.
title: Best practices
image: https://developers.cloudflare.com/realtime/sfu/best-practices/og.png?v=9982b9e7b9639db8
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# Best practices

Last updated Sep 22, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/sfu/best-practices/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Your application owns identity, state, and lifecycle around the SFU's media transport. Preserve these boundaries when adapting an example.

## Keep credentials on the backend

Store the SFU App Secret on trusted server infrastructure. In Workers, use a Worker secret. Browsers and devices authenticate to your application backend using credentials scoped to their own responsibilities.

Expose application operations with validated inputs. Avoid an unrestricted SFU proxy that lets a browser select arbitrary sessions, publications, or destructive operations.

WebSocket endpoint credentials are separate from the SFU App Secret. Keep both out of public assets, URLs sent to viewers, and logs.

## Authorize resource operations

Check identity and resource ownership before creating, publishing, subscribing, updating permissions, or closing resources. A room name, session ID, track name, or adapter ID is a locator rather than proof of permission.

An operator role also needs application authorization. For device control, the backend can assign a short controller lease and grant `canReply` only to that selection. Handle lease expiry and revoked access in the application, not just the browser UI.

## Coordinate negotiation

Follow [per-session mutation ordering](https://developers.cloudflare.com/realtime/sfu/concepts/negotiation/#serialize-mutations-per-session). Retain work that arrives during an outstanding exchange, and check per-item results before advancing application state.

## Define recovery explicitly

Decide whether an application keeps its identity while replacing a media connection. Give each connection attempt an ID so old responses cannot alter replacement sessions. Follow the [replacement-connection sequence](https://developers.cloudflare.com/realtime/sfu/concepts/negotiation/#retry-and-reconnect).

Make reconnect visible to the user, bound retries, and provide a recovery action when automatic attempts fail. The correct choice depends on the application: a room can rebuild subscriptions, while a device listener might require an explicit rejoin.

For WebSocket adapters, implement recreation after terminal closure and respect the different ingest and stream reconnect behavior.

## Retain cleanup state

Remove unavailable or unauthorized publications from discovery. Retain their resource identifiers privately until required cleanup is complete. Check [individual close results](https://developers.cloudflare.com/realtime/sfu/observability/error-codes/#interpret-close-results) and keep unresolved items available for retry.

Decide whether replacement can proceed while old resources remain. Discarding an obsolete connection from application state does not stop SFU forwarding. When you need to stop access, close the affected SFU resources and confirm the result.

Use explicit leave/stop operations and application expiry for abandoned clients. A browser tab may close without sending cleanup. Keep the backend available while retries still need to run.

## Apply application limits

Set admission limits, operation rates, and resource lifetimes appropriate to your application. An example's room size or controller policy is an application decision. Refer to [SFU limits](https://developers.cloudflare.com/realtime/sfu/platform/limits/) for product constraints.

Use [observability](https://developers.cloudflare.com/realtime/sfu/observability/) to connect API results, endpoint state, and media delivery. Validate authorization and failure paths alongside the successful flow.

## Learn with an example

The [video-room production guide ↗︎](https://github.com/cloudflare/realtime-examples/blob/main/video-room/PRODUCTION.md) explains identity and room authorization. The [cloud-gaming architecture ↗︎](https://github.com/cloudflare/realtime-examples/blob/main/cloud-gaming/ARCHITECTURE.md) shows controller generations and input release. [Pocket Radio's architecture ↗︎](https://github.com/cloudflare/realtime-examples/blob/main/esp32-radio/ARCHITECTURE.md) explains device credentials, listener membership, and controller leases.
