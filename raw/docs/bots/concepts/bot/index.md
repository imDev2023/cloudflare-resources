---
description: Automated software programs that interact with websites and APIs.
title: Bots
image: https://developers.cloudflare.com/bots/concepts/bot/og.png?v=b3fa9e233f54a697
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/bots/llms.txt  
> Use this file to discover all available pages before exploring further.

# Bots

Last updated Jul 1, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/bots/concepts/bot/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A **bot** is a software application programmed to do certain tasks.

Bots can be used for good (chatbots, search engine crawlers) or for evil (inventory hoarding, credential stuffing).

More information

For more background, refer to [What is a bot? ↗︎](https://www.cloudflare.com/learning/bots/what-is-a-bot/).

## AI bots

AI crawlers and agents interact with your site for very different reasons, and you may want to treat those reasons differently. Rather than relying on a single "AI bot" label, Cloudflare classifies bots by **behavior** — what a bot does on your site — so you can allow the behavior that helps your business and block the behavior that harms it. A single bot can have more than one behavior.

### Classification

Cloudflare lets all customers manage three AI-related use cases directly:

| Behavior | What it does |
| --- | --- |
| **Search** | Collects or indexes your content so it can answer questions about it later. |
| **Agent** | Automated activity acting in real time on a person's behalf to get something done, such as chat fetch bots and browser-use agents. |
| **Training** | Crawls your content to train or fine-tune a model, permanently absorbing your data into the model. |

Cloudflare classifies other behaviors, too — refer to [Verified bots](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/).
