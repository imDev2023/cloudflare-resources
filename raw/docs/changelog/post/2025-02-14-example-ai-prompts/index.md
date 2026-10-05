---
description: Build applications on Workers with our prompt examples.
title: Build AI Agents with Example Prompts
image: https://developers.cloudflare.com/changelog/post/2025-02-14-example-ai-prompts/og.png?v=0588dca76544a62f
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 14, 2025

## Build AI Agents with Example Prompts

[Agents](https://developers.cloudflare.com/agents/) [Workers](https://developers.cloudflare.com/workers/) [Workflows](https://developers.cloudflare.com/workflows/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-14-example-ai-prompts/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We've added an [example prompt](https://developers.cloudflare.com/workers/get-started/prompting/) to help you get started with building AI agents and applications on Cloudflare [Workers](https://developers.cloudflare.com/workers/), including [Workflows](https://developers.cloudflare.com/workflows/), [Durable Objects](https://developers.cloudflare.com/durable-objects/), and [Workers KV](https://developers.cloudflare.com/kv/).

You can use this prompt with your favorite AI model, including Claude 3.5 Sonnet, OpenAI's o3-mini, Gemini 2.0 Flash, or Llama 3.3 on Workers AI. Models with large context windows will allow you to paste the prompt directly: provide your own prompt within the `<user_prompt></user_prompt>` tags.

```sh
{paste_prompt_here}
<user_prompt>
user: Build an AI agent using Cloudflare Workflows. The Workflow should run when a new GitHub issue is opened on a specific project with the label 'help' or 'bug', and attempt to help the user troubleshoot the issue by calling the OpenAI API with the issue title and description, and a clear, structured prompt that asks the model to suggest 1-3 possible solutions to the issue. Any code snippets should be formatted in Markdown code blocks. Documentation and sources should be referenced at the bottom of the response. The agent should then post the response to the GitHub issue. The agent should run as the provided GitHub bot account.
</user_prompt>
```

This prompt is still experimental, but we encourage you to try it out and [provide feedback ↗︎](https://github.com/cloudflare/cloudflare-docs/issues/new?template=content.edit.yml).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-14-example-ai-prompts/#page","headline":"Build AI Agents with Example Prompts","description":"Build applications on Workers with our prompt examples.","url":"https://developers.cloudflare.com/changelog/post/2025-02-14-example-ai-prompts/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-02-14-example-ai-prompts/og.png?v=0588dca76544a62f","dateModified":"2025-02-14","datePublished":"2025-02-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
