---
description: Directories in Email Security.
title: Directories
image: https://developers.cloudflare.com/cloudflare-one/email-security/settings/domains-and-directories/directories/og.png?v=316e8d06f53780a4
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-one/llms.txt  
> Use this file to discover all available pages before exploring further.

# Directories

Last updated Sep 22, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-one/email-security/settings/domains-and-directories/directories/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Directories are folders to store user data. Email security allows you to manage directories from the Cloudflare dashboard.

To add a directory:

1. Log in to [Cloudflare One ↗︎](https://one.dash.cloudflare.com/) > **Email security**.
2. Select **Settings** > **Domains & directories**.
3. Select **View** on the **Directories** card.
4. On the **Domains & directories** page, select **Add a directory** > **Connect an integration**.
5. Select either **Google Workspace CASB + EMAIL** or **Microsoft CASB + EMAIL**.
6. Refer to [Enable Gmail BCC integration](https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/enable-gmail-integration/#enable-gmail-bcc-integration) if you choose **Google Workspace CASB + EMAIL**. Refer to [Enable Microsoft integration](https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/api/m365-api/#enable-microsoft-integration) if you choose **Microsoft CASB + EMAIL**.

To sync a directory:

1. Locate the directory you want to sync.
2. Select the three dots, then select **Sync now**.

Note

The **Auto sync** option is on by default. It is recommended to keep this option on at all times to ensure directories are always synchronized.
