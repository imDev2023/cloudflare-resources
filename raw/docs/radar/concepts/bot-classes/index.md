---
description: Cloudflare Radar classifies traffic as likely automated or likely human based on bot score ranges.
title: Bot classes
image: https://developers.cloudflare.com/radar/concepts/bot-classes/og.png?v=9345bf05b18f61cf
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/radar/llms.txt  
> Use this file to discover all available pages before exploring further.

# Bot classes

Last updated Apr 20, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/radar/concepts/bot-classes/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A bot class in Radar is a grouping of [bot scores](https://developers.cloudflare.com/bots/concepts/bot-score).

Scores between 1 and 29 are classified as bot traffic. Scores equal or above 30 are classified as non-bot/human traffic.

| Class | Description |
| --- | --- |
| **Likely automated** | Bot scores of 1 through 29. |
| **Likely human** | Bot scores of 30 through 99. |
