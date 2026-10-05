---
description: Troubleshoot Cloudflare 1023 error code.
title: Error 1023
image: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1023/og.png?v=1c45d387268410bb
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/support/llms.txt  
> Use this file to discover all available pages before exploring further.

# Error 1023

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1023/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Error 1023: Could not find host

This error indicates that the host could not be found due to a configuration issue or propagation delay.

### Common causes

- If the owner just signed up for Cloudflare it can take a few minutes for the website's information to be distributed to our global network. Something is wrong with the site's configuration.
- Usually, this happens when accounts have been signed up with a partner organization (for example, hosting provider) and the provider's DNS fails.

Note

Error `1023` is returned via a HTTP `503` response code.

### Resolution

Contact [Cloudflare Support](https://developers.cloudflare.com/support/contacting-cloudflare-support/) with the following details:

- Your domain name.
- A screenshot of the `1023` error including the [**Ray ID**](https://developers.cloudflare.com/fundamentals/reference/cloudflare-ray-id/) mentioned in the error message.
- A [HAR file](https://developers.cloudflare.com/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/) captured while duplicating the error.
