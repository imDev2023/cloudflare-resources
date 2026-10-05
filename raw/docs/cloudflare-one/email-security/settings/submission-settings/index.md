---
description: Phish submissions in Email Security.
title: Submission settings
image: https://developers.cloudflare.com/cloudflare-one/email-security/settings/submission-settings/og.png?v=b6ea5b50cfe80997
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-one/llms.txt  
> Use this file to discover all available pages before exploring further.

# Submission settings

Last updated Sep 22, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-one/email-security/settings/submission-settings/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

As part of your continuous email security posture, administrators and security analysts need to submit missed phishing samples to Email security, so Cloudflare can process them and take necessary action.

Submitting missed phish samples to Cloudflare is of paramount importance and necessary for continuous protection. Submitting missed phish samples helps Cloudflare improve our machine learning (ML) models, and alerts us of new attack vectors before they become prevalent.

There are three routes you can use to report an email as a phish:

- Via Investigation, by [reclassifying an email](https://developers.cloudflare.com/cloudflare-one/email-security/settings/submission-settings/#reclassify-an-email).
- Via [PhishNet 365](https://developers.cloudflare.com/cloudflare-one/email-security/settings/submission-settings/phishnet-365/).
- Via [Submission addresses](https://developers.cloudflare.com/cloudflare-one/email-security/settings/submission-settings/submission-addresses/).

## Reclassify an email

1. Log in to [Cloudflare One ↗︎](https://one.dash.cloudflare.com/).
2. Select **Email security** > **Investigation**.
3. On the **Investigation** page, under **Your matching messages**, select the message you want to reclassify. Select the three dots, then select **Submit for review**. By selecting **Submit for review**, you are requesting a new disposition for the message.
4. Select the new disposition, then select **Save**.

When you report an email as phish, this email will be displayed under [User submissions](https://developers.cloudflare.com/cloudflare-one/email-security/submissions/user-submissions/).
