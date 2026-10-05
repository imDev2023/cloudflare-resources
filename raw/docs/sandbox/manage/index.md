---
description: List the sandboxes that belong to a user, and record when and why each one stops.
title: Manage sandboxes
image: https://developers.cloudflare.com/sandbox/manage/og.png?v=a318273d37327390
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/sandbox/llms.txt  
> Use this file to discover all available pages before exploring further.

# Manage sandboxes

Last updated Sep 30, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/sandbox/manage/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Your Worker reaches each sandbox by name. The runtime does not record which names belong to which user, and it does not wake a Durable Object when its container stops. To list a user's sandboxes or act when a sandbox stops, your Worker keeps its own records.

- [List a user's sandboxes](https://developers.cloudflare.com/sandbox/manage/list-sandboxes/): Record each user's sandboxes in a Durable Object, and report which ones are running.
- [Run code when a sandbox stops](https://developers.cloudflare.com/sandbox/manage/run-code-when-a-sandbox-stops/): Record when and why a sandbox stops, including stops that happen while no requests arrive.
