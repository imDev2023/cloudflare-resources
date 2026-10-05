---
description: Create a request header transform rule to add an HTTP header when the Workers subrequest comes from a different zone.
title: Add a request header for subrequests from other zones
image: https://developers.cloudflare.com/rules/transform/examples/add-request-header-subrequest-other-zone/og.png?v=9ed90226281aaafe
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Add a request header for subrequests from other zones

Create a request header transform rule to add an HTTP header when the Workers subrequest comes from a different zone.

Last updated Oct 13, 2025|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/transform/examples/add-request-header-subrequest-other-zone/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The following request header transform rule adds an HTTP header to Workers subrequests coming from a different zone:

Text in **Expression Editor** (replace `myappexample.com` with your domain):

```txt
(cf.worker.upstream_zone != "" and cf.worker.upstream_zone != "myappexample.com")
```

Selected operation under **Modify request header**: *Set static*

**Header name**: `X-External-Workers-Subrequest`

**Value**: `1`

The [`cf.worker.upstream_zone`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.worker.upstream_zone/) field used in the rule expression is set to empty if the current request is not a Workers subrequest.
