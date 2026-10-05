---
description: CASB for Zero Trust.
title: CASB
image: https://developers.cloudflare.com/cloudflare-one/troubleshooting/casb/og.png?v=53701f47e3083dda
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-one/llms.txt  
> Use this file to discover all available pages before exploring further.

# CASB

Last updated Apr 17, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-one/troubleshooting/casb/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Use this guide to troubleshoot common issues with Cloud Access Security Broker (CASB).

## Security findings

### Findings not appearing

If you do not see findings for an integrated application:

- **Wait for scan**: Initial scans can take up to 24 hours depending on the size of the application.
- **Permissions**: Ensure the account used to integrate the application has the necessary administrative permissions.
- **Enabled status**: Verify that the integration is enabled in the Zero Trust dashboard.

### False positives

If CASB flags a configuration that is intended for your organization:

1. Go to **CASB** > **Findings**.
2. Select the finding and choose **Dismiss**.
3. Provide a reason for dismissal to help refine future scans.

---

## More CASB resources

For more information, refer to the full CASB documentation.

[CASB troubleshooting ❯](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/troubleshooting/)
