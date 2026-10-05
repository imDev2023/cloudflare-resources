---
description: Learn about external evaluation rules in this guide.
title: External Evaluation rules
image: https://developers.cloudflare.com/learning-paths/clientless-access/advanced-workflows/external-evaluation/og.png?v=1c515fce6fa710e0
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/learning-paths/llms.txt  
> Use this file to discover all available pages before exploring further.

# External Evaluation rules

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/learning-paths/clientless-access/advanced-workflows/external-evaluation/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

With Cloudflare Access, you can build infinitely customizable policies using External Evaluation rules. External Evaluation rules allow you to call any API during the evaluation of an Access policy and authenticate users based on custom business logic. Example use cases include:

- Customize policies based on time of day.
- Check IP addresses against external threat feeds.
- Call industry-specific user registries.

The External Evaluation rule requires two values: an API endpoint to call and a key to verify that any request response is coming from a trusted source. After the user authenticates with your identity provider, all information about the user, device and location is passed to your external API. The API returns a pass or fail response to Access which will then either allow or deny access to the user.

## Set up External Evaluation rule

For detailed setup instructions, refer to [External Evaluation rules](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/external-evaluation/).

Example code for the API is available in our [open-source repository ↗︎](https://github.com/cloudflare/workers-access-external-auth-example).
