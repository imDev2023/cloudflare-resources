---
title: RTKPolls
image: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkpolls/og.png?v=a61501c560f8eb70
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RTKPolls

Last updated Jul 20, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkpolls/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The RTKPolls module consists of the polls that have been created in the meeting.

- [RTKPolls](#module_RTKPolls)
  - [.items](#module_RTKPolls+items)
  - [.create(question, options, anonymous, hideVotes)](#module_RTKPolls+create)
  - [.vote(pollId, index)](#module_RTKPolls+vote)

### meeting.polls.items

An array of poll items.

**Kind**: instance property of [`RTKPolls`](#module_RTKPolls)  

### meeting.polls.create(question, options, anonymous, hideVotes)

Creates a poll in the meeting.

**Kind**: instance method of [`RTKPolls`](#module_RTKPolls)

| Param | Default | Description |
| --- | --- | --- |
| question |  | The question that is to be voted for. |
| options |  | The options of the poll. |
| anonymous | `false` | If true, the poll votes are anonymous. |
| hideVotes | `false` | If true, the votes on the poll are hidden. |

### meeting.polls.vote(pollId, index)

Casts a vote on an existing poll.

**Kind**: instance method of [`RTKPolls`](#module_RTKPolls)

| Param | Description |
| --- | --- |
| pollId | The ID of the poll that is to be voted on. |
| index | The index of the option. |
