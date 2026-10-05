---
description: Subscribe to Workers KV change events and process them with Cloudflare Queues.
title: Event subscriptions
image: https://developers.cloudflare.com/kv/platform/event-subscriptions/og.png?v=75ecaacb9dc79583
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/kv/llms.txt  
> Use this file to discover all available pages before exploring further.

# Event subscriptions

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/kv/platform/event-subscriptions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Event subscriptions](https://developers.cloudflare.com/queues/event-subscriptions/) allow you to receive messages when events occur across your Cloudflare account. Cloudflare products (e.g., [KV](https://developers.cloudflare.com/kv/), [Workers AI](https://developers.cloudflare.com/workers-ai/), [Workers](https://developers.cloudflare.com/workers/)) can publish structured events to a [queue](https://developers.cloudflare.com/queues/), which you can then consume with Workers or [HTTP pull consumers](https://developers.cloudflare.com/queues/configuration/pull-consumers/) to build custom workflows, integrations, or logic.

For more information on [Event Subscriptions](https://developers.cloudflare.com/queues/event-subscriptions/), refer to the [management guide](https://developers.cloudflare.com/queues/event-subscriptions/manage-event-subscriptions/).

## Available KV events

#### `namespace.created`

Triggered when a namespace is created.

**Example:**

```json
{
  "type": "cf.kv.namespace.created",
  "source": {
    "type": "kv"
  },
  "payload": {
    "id": "ns-12345678-90ab-cdef-1234-567890abcdef",
    "name": "my-kv-namespace"
  },
  "metadata": {
    "accountId": "f9f79265f388666de8122cfb508d7776",
    "eventSubscriptionId": "1830c4bb612e43c3af7f4cada31fbf3f",
    "eventSchemaVersion": 1,
    "eventTimestamp": "2025-05-01T02:48:57.132Z"
  }
}
```

#### `namespace.deleted`

Triggered when a namespace is deleted.

**Example:**

```json
{
  "type": "cf.kv.namespace.deleted",
  "source": {
    "type": "kv"
  },
  "payload": {
    "id": "ns-12345678-90ab-cdef-1234-567890abcdef",
    "name": "my-kv-namespace"
  },
  "metadata": {
    "accountId": "f9f79265f388666de8122cfb508d7776",
    "eventSubscriptionId": "1830c4bb612e43c3af7f4cada31fbf3f",
    "eventSchemaVersion": 1,
    "eventTimestamp": "2025-05-01T02:48:57.132Z"
  }
}
```
