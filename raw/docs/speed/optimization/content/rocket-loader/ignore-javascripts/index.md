---
description: Exclude specific scripts from Rocket Loader optimization.
title: Ignore JavaScripts
image: https://developers.cloudflare.com/speed/optimization/content/rocket-loader/ignore-javascripts/og.png?v=8a1f4f6a456a1fff
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/speed/llms.txt  
> Use this file to discover all available pages before exploring further.

# Ignore JavaScripts

Last updated Apr 17, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/speed/optimization/content/rocket-loader/ignore-javascripts/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can have Rocket Loader ignore individual scripts by adding the `data-cfasync="false"` attribute to the relevant script tag:

```html
<script data-cfasync="false" src="/javascript.js"></script>
```

Rocket Loader will still optimize the loading of all other scripts on the page.

Note

If Rocket Loader is only impacting a specific page, use a [Configuration Rule](https://developers.cloudflare.com/rules/configuration-rules/) to exclude that page by URL.

## Limitations

- Adding this attribute within JavaScript will not work if you wish to exclude the script from Rocket Loader.
- If the script you want Rocket Loader to ignore has dependency on other JavaScript(s) on the page, those dependencies must also have the `data-cfasync="false"` attribute.
- The `data-cfasync` attribute must be added before the `src` attribute.
- Rocket Loader will recognize the tag when either single or double quotes are placed around the attribute value.
