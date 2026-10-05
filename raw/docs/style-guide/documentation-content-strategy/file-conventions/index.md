---
description: Follow file naming and organization conventions.
title: File conventions
image: https://developers.cloudflare.com/style-guide/documentation-content-strategy/file-conventions/og.png?v=b4b4fcb459e9bda4
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/style-guide/llms.txt  
> Use this file to discover all available pages before exploring further.

# File conventions

Last updated Aug 20, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/style-guide/documentation-content-strategy/file-conventions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Our docs have a few conventions around files.

## Naming

When creating new files, follow specific conventions for your naming.

Filenames should:

- Semantically communicate the purpose of the file
- Be lowercased
- Use dashes between words

*Acceptable file namestxt*

```txt
/src/content/docs/fundamentals/concepts/what-is-cloudflare.mdx
/src/assets/images/api-shield/api-shield-call-sequence.png
```

*Unacceptable file namestxt*

```txt
/src/content/docs/fundamentals/concepts/What is Cloudflare.mdx
/src/content/docs/fundamentals/concepts/What-is-Cloudflare.mdx
/src/assets/images/api-shield/API_Image_1.png
```

These conventions are important for user readability, SEO conventions, and making sure our GitHub actions do not break.

## Folders

Each folder should have a file named `index.mdx`.

```txt
/src/content/docs/fundamentals/concepts/index.mdx
```

The content at `/src/content/docs/fundamentals/concepts/index.mdx` will be rendered at `https://developers.cloudflare.com/fundamentals/concepts/`.

## Content files

Add regular content files to the `/src/content/docs/{product_folder}/` directory.

```txt
/src/content/docs/fundamentals/concepts/what-is-cloudflare.mdx
```

## Image files

Add image files to the `/src/assets/images/{product_folder}/` directory.

```txt
/src/assets/images/api-shield/api-shield-call-sequence.png
```
