---
description: Edit existing Zaraz variables.
title: Edit variables
image: https://developers.cloudflare.com/zaraz/variables/edit-variables/og.png?v=d3479ead9ddeda6e
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/zaraz/llms.txt  
> Use this file to discover all available pages before exploring further.

# Edit variables

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/zaraz/variables/edit-variables/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

1. In the Cloudflare dashboard, go to the **Tag setup** page. [Go to **Tag setup** ↗](https://dash.cloudflare.com/?to=/:account/tag-management/zaraz)
2. Go to **Tools Configuration** > **Variables**.
3. Locate the variable you want to edit, and select **Edit** to make your changes.
4. Select **Save** to save your edits.

## Delete a variable

Important

You cannot delete a variable being used in tools or triggers.

1. In the Cloudflare dashboard, go to the **Tag setup** page. [Go to **Tag setup** ↗](https://dash.cloudflare.com/?to=/:account/tag-management/zaraz)
2. Go to **Tools Configuration** > **Third-party tools**.
3. Locate any tools using the variable, and delete the variable from those tools.
4. Select **Zaraz** > **Tools Configuration** > **Triggers**.
5. Locate all the triggers using the variable, and delete the variable from those triggers.
6. Navigate to **Zaraz** > **Tools Configuration** > **Variables**.
7. Locate the variable you want to delete, and select **Delete**.
