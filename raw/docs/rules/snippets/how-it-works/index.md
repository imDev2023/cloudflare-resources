---
description: How Snippets execute JavaScript at the edge for matching requests.
title: How Snippets work
image: https://developers.cloudflare.com/rules/snippets/how-it-works/og.png?v=f018bf2c62451e77
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# How Snippets work

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/snippets/how-it-works/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Snippets are executed based on rules defined within your zone. Here is how the process works:

![Diagram of the snippets execution workflow](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1546,height=491,format=webp/_astro/snippets-execution.Cb6ZLHBP.png)

## 1. Evaluate snippet rules

For each incoming request, Cloudflare evaluates the expression of every snippet rule defined in the zone. The evaluation checks for a match based on various request properties (such as bot score, WAF attack score, country of origin, and cookies).

## 2. Build Snippets table

For every snippet rule in a zone that matches an incoming request, Cloudflare adds the corresponding unique snippet ID to a Snippets table.

## 3. Execute snippets code

Once all the rules have been evaluated and the full table has been compiled, Cloudflare starts processing all the snippet IDs in the table.

The snippets are executed sequentially. Each snippet receives the modified request from the previous snippet and applies new modifications to it.

## 4. Continue with the request execution workflow

After executing the final snippet IDs, the resulting modified request is passed back to the request execution workflow. Refer to [Execution order](https://developers.cloudflare.com/rules/snippets/#execution-order) for more information on the Rules features evaluated before and after Cloudflare Snippets.
