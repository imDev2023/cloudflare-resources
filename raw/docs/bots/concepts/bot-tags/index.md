---
description: Tags that explain why Cloudflare assigned a specific bot score to a request.
title: Bot tags
image: https://developers.cloudflare.com/bots/concepts/bot-tags/og.png?v=c59ecf6bde20df78
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/bots/llms.txt  
> Use this file to discover all available pages before exploring further.

# Bot tags

Last updated Sep 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/bots/concepts/bot-tags/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Bot tags provide more detail about *why* Cloudflare assigned a [bot score](https://developers.cloudflare.com/bots/concepts/bot-score/) to a request.

Use these tags to learn more about your bot traffic and better inform security settings.

Note

Bot tags are only available to Enterprise customers who have purchased Bot Management.

## Potential values

Once you [enable bot tags](#enable-bot-tags), you can see more information about bot requests, such as whether a request came from a verified bot (like Bing) or a category of verified bot (like SearchEngine).

The following values are **examples** of what may be present in the `BotTags` log field, but not an exhaustive list:

- api
- google
- bing
- googleAds
- googleMedia
- googleImageProxy
- pinterest
- newRelic
- baidu
- apple
- yandex

When matching the Ruleset Engine field, use uppercase tag values such as `API`, `GOOGLE`, or `BING`.

## Use bot tags

To include bot tags in logs, add the `BotTags` field when using [Logpush](https://developers.cloudflare.com/logs/logpush/).

To match bot tags in Ruleset Engine expressions, use the [`cf.bot_management.tags`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.bot_management.tags/) field. For example:

```txt
any(cf.bot_management.tags[*] eq "API")
```
