---
description: Create a transform rule to rewrite the URL format `/posts/<YYYY>-<MM>-<DD>-<TITLE>` to the new format `/posts/<YYYY>/<MM>/<DD>/<TITLE>`.
title: Rewrite blog archive URLs
image: https://developers.cloudflare.com/rules/transform/examples/rewrite-archive-urls-new-format/og.png?v=6ae81122ce561809
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Rewrite blog archive URLs

Create a transform rule to rewrite the URL format `/posts/<YYYY>-<MM>-<DD>-<TITLE>` to the new format `/posts/<YYYY>/<MM>/<DD>/<TITLE>`.

Last updated Oct 13, 2025|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/transform/examples/rewrite-archive-urls-new-format/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

To rewrite the URLs of a blog archive that follow the URL format `/posts/<YYYY>-<MM>-<DD>-<TITLE>` to the new format `/posts/<YYYY>/<MM>/<DD>/<TITLE>`, create the following URL rewrite rule:

Text in **Expression Editor**:

```txt
http.request.uri.path ~ "^/posts/[0-9]+-[0-9]+-[0-9]+-.*"
```

Text after **Path** > **Rewrite to** > *Dynamic*:

```txt
regex_replace(http.request.uri.path, "^/posts/([0-9]+)-([0-9]+)-([0-9]+)-(.*)$", "/posts/${1}/${2}/${3}/${4}")
```

The function `regex_replace()` also allows you to extract parts of the URL using regular expressions' capture groups. Create capture groups by putting part of the regular expression in parentheses. Then, reference a capture group using `${<NUMBER>}` in the replacement string, where `<NUMBER>` is the number of the capture group.
