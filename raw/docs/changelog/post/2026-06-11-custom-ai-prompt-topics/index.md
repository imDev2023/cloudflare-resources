---
description: Cloudflare DLP now supports custom AI prompt protection topics. Define concepts in natural language to detect content unique to your organization.
title: Define custom topics for AI prompt protection
image: https://developers.cloudflare.com/changelog/post/2026-06-11-custom-ai-prompt-topics/og.png?v=9c83e23ace59cc54
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 11, 2026

## Define custom topics for AI prompt protection

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-11-custom-ai-prompt-topics/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now define custom topics for AI prompt protection. Predefined [AI prompt topics](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics) cover common content and intent categories such as PII, source code, and jailbreak attempts. Custom topics let you detect unique or proprietary concepts that are not included in predefined categories.

You describe a custom topic in natural language, and Cloudflare DLP detects whether a prompt matches that topic based on context rather than specific keywords. For example, a topic that describes confidential merger discussions matches a prompt that paraphrases the deal, even when the prompt never uses the word merger or names the companies involved. To detect literal values such as internal codenames or product identifiers, use a [custom wordlist or pattern entry](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#custom-wordlist-datasets) instead.

Custom topics run through the same [application granular controls](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#granular-controls) path as predefined AI prompt topics. Custom topics are available for ChatGPT, Google Gemini, Perplexity, and Claude.

#### Create a custom AI prompt topic

1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Data loss prevention** > **Detection entries**.
2. Select **AI prompt topics**, then select **Custom Prompt Topic**.
3. Describe the topic in natural language. Be specific about the concept you want to detect. For example, describe unreleased product roadmap details or confidential customer contract terms.
4. Add this detection entry to an existing DLP profile, or [create a new DLP profile](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/#build-a-custom-profile).
5. Use the profile in a Gateway HTTP policy to log or block prompts that match the topic.

Note

Write the description as a concept to classify, not a list of keywords. For example, describe "internal financial forecasts and unreleased revenue figures" rather than listing specific document names.

For more information, refer to [AI prompt topics](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-11-custom-ai-prompt-topics/#page","headline":"Define custom topics for AI prompt protection","description":"Cloudflare DLP now supports custom AI prompt protection topics. Define concepts in natural language to detect content unique to your organization.","url":"https://developers.cloudflare.com/changelog/post/2026-06-11-custom-ai-prompt-topics/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-11-custom-ai-prompt-topics/og.png?v=9c83e23ace59cc54","dateModified":"2026-06-11","datePublished":"2026-06-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
