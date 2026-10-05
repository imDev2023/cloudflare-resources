---
description: Test your exposed credentials check configuration.
title: Test your exposed credentials checks configuration
image: https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/test-configuration/og.png?v=90231d470ae49de3
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/waf/llms.txt  
> Use this file to discover all available pages before exploring further.

# Test your exposed credentials checks configuration

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/test-configuration/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Deprecation notice

Exposed credentials check has been deprecated.

Switch from exposed credentials check to [leaked credentials detection](https://developers.cloudflare.com/waf/detections/leaked-credentials/) for improved security. To upgrade your current configuration, refer to the [upgrade guide](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/upgrade-to-leaked-credentials-detection/).

After enabling and configuring exposed credentials checks, you may want to test if the checks are working properly.

Cloudflare provides a special set of case-sensitive credentials for this purpose:

- Login: `CF_EXPOSED_USERNAME` or `CF_EXPOSED_USERNAME@example.com`
- Password: `CF_EXPOSED_PASSWORD`

The WAF always considers these specific credentials as having been previously exposed. Use them to force an "exposed credentials" event, which allows you to check the behavior of your current configuration.
