---
description: Enable Zaraz debug mode to inspect events in the browser console.
title: Debug mode
image: https://developers.cloudflare.com/zaraz/web-api/debug-mode/og.png?v=42f7f1c2f0aed2de
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/zaraz/llms.txt  
> Use this file to discover all available pages before exploring further.

# Debug mode

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/zaraz/web-api/debug-mode/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Zaraz offers a debug mode to troubleshoot the events and triggers systems. To activate debug mode you need to create a special debug cookie (`zarazDebug`) containing your debug key. You can set this cookie manually or via the `zaraz.debug` helper function available in your console.

1. In the Cloudflare dashboard, go to the **Settings** page. [Go to **Settings** ↗](https://dash.cloudflare.com/?to=/:account/tag-management/settings)
2. Copy your **Debug Key**.
3. Open a web browser and access its Developer Tools. For example, to access Developer Tools in Google Chrome, select **View** > **Developer** > **Developer Tools**.
4. Select the **Console** pane and enter the following command to create a debug cookie:

   ```js
   zaraz.debug("YOUR_DEBUG_KEY")
   ```



Zaraz’s debug mode is now enabled. A pop-up window will show up with the debugger information. To exit debug mode, remove the cookie by typing `zaraz.debug()` in the console pane of the browser.
