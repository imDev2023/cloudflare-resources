---
description: Analyze and secure user prompts to popular generative AI services with new, DLP topic classifications.
title: New DLP topic based detection entries for AI prompt protection
image: https://developers.cloudflare.com/changelog/post/2025-08-25-ai-prompt-protection/og.png?v=181b0b18ec7d4d64
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 25, 2025

## New DLP topic based detection entries for AI prompt protection

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-25-ai-prompt-protection/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You now have access to a comprehensive suite of capabilities to secure your organization's use of generative AI. AI prompt protection introduces four key features that work together to provide deep visibility and granular control.

1. **Prompt Detection for AI Applications**

DLP can now natively detect and inspect user prompts submitted to popular AI applications, including **Google Gemini**, **ChatGPT**, **Claude**, and **Perplexity**.

2. **Prompt Analysis and Topic Classification**

Our DLP engine performs deep analysis on each prompt, applying [topic classification](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics). These topics are grouped into two evaluation categories:

- **Content:** PII, Source Code, Credentials and Secrets, Financial Information, and Customer Data.
- **Intent:** Jailbreak attempts, requests for malicious code, or attempts to extract PII.

To help you apply these topics quickly, we have also released five new predefined profiles (for example, AI Prompt: AI Security, AI Prompt: PII) that bundle these new topics.

![DLP](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=728,height=439,format=webp/_astro/ai-prompt-detection-entry.4QmdkAuv.png)

3. **Granular Guardrails**

   You can now build guardrails using Gateway HTTP policies with [application granular controls](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#granular-controls). Apply a DLP profile containing an [AI prompt topic detection](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics) to individual AI applications (for example, `ChatGPT`) and specific user actions (for example, `SendPrompt`) to block sensitive prompts.![DLP](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=731,height=511,format=webp/_astro/ai-prompt-policy.CF3H2rbK.png)
4. **Full Prompt Logging**

   To aid in incident investigation, an optional setting in your Gateway policy allows you to [capture prompt logs](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#log-generative-ai-prompt-content) to store the full interaction of prompts that trigger a policy match. To make investigations easier, logs can be filtered by `conversation_id`, allowing you to reconstruct the full context of an interaction that led to a policy violation.![DLP](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=728,height=444,format=webp/_astro/ai-prompt-log.ywQDc5qN.png)

AI prompt protection is now available in open beta. To learn more about it, read the [blog ↗︎](https://blog.cloudflare.com/ai-prompt-protection/#closing-the-loop-logging) or refer to [AI prompt topics](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-25-ai-prompt-protection/#page","headline":"New DLP topic based detection entries for AI prompt protection","description":"Analyze and secure user prompts to popular generative AI services with new, DLP topic classifications.","url":"https://developers.cloudflare.com/changelog/post/2025-08-25-ai-prompt-protection/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-25-ai-prompt-protection/og.png?v=181b0b18ec7d4d64","dateModified":"2025-08-25","datePublished":"2025-08-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
