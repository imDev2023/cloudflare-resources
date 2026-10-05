---
description: Format paragraphs and line breaks correctly.
title: Paragraphs and line breaks
image: https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/structure/paragraphs-and-line-breaks/og.png?v=b1cfd5c51b9d6c27
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/style-guide/llms.txt  
> Use this file to discover all available pages before exploring further.

# Paragraphs and line breaks

Last updated Aug 20, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/structure/paragraphs-and-line-breaks/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Paragraphs in Markdown

To start a new paragraph, leave an empty line (with no spaces) before adding the new paragraph content.

```txt
This sentence is the first one in this paragraph.
This second sentence also belongs to the first paragraph.

This is the first sentence of the second paragraph.
```

## Line breaks in Markdown

Avoid line breaks when possible. Considering creating a separate paragraph, even inside numbered lists.

If you need to add a line break, use the `<br/>` HTML element.

Example inside a table:

```txt
| Feature                          | Enabled |
|----------------------------------|---------|
| Feature name<br/>Additional info | Yes     |
```

This is how the table looks:

| Feature | Enabled |
| --- | --- |
| Feature name<br>Additional info | Yes |

Caution

Do not use two spaces at the end of a sentence to create a forced line break. Although this Markdown syntax is supported, it is not immediately visible and can easily miss these line breaks during peer reviews.
