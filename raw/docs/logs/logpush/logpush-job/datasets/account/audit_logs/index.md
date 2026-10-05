---
description: The descriptions below detail the fields available for audit_logs.
title: Audit Logs
image: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/audit_logs/og.png?v=ab9933ef89f0b369
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/logs/llms.txt  
> Use this file to discover all available pages before exploring further.

# Audit Logs

Last updated Sep 14, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/audit_logs/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The descriptions below detail the fields available for `audit_logs`.

## ActionResult

Type: `bool`

Whether the action was successful.

## ActionType

Type: `string`

Type of action taken.

## ActorEmail

Type: `string`

Email of the actor.

## ActorID

Type: `string`

Unique identifier of the actor in Cloudflare's system.

## ActorIP

Type: `string`

Physical network address of the actor.

## ActorType

Type: `string`

Type of user that started the audit trail.

## ID

Type: `string`

Unique identifier of an audit log.

## Interface

Type: `string`

Entry point or interface of the audit log.

## Metadata

Type: `object`

Additional audit log-specific information. Metadata is organized in key:value pairs. Key and Value formats can vary by ResourceType.

## NewValue

Type: `object`

Contains the new value for the audited item.

## OldValue

Type: `object`

Contains the old value for the audited item.

## OwnerID

Type: `string`

The identifier of the user that was acting or was acted on behalf of. If a user did the action themselves, this value will be the same as the ActorID.

## ResourceID

Type: `string`

Unique identifier of the resource within Cloudflare's system.

## ResourceType

Type: `string`

The type of resource that was changed.

## When

Type: `int or string`

When the change happened.
