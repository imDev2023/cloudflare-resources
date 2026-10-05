---
description: Status classifications for scripts and connections detected by client-side security.
title: Script and connection statuses
image: https://developers.cloudflare.com/client-side-security/reference/script-statuses/og.png?v=0baa84e08069fbd5
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/client-side-security/llms.txt  
> Use this file to discover all available pages before exploring further.

# Script and connection statuses

Last updated Apr 15, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/client-side-security/reference/script-statuses/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare classifies scripts and connections (also known as resources) according to the following:

- The number of times a script/connection was reported.
- Whether the script/connection is considered malicious or not.

Use client-side security's dashboards to review the scripts loaded in your domain and the connections they make. For more information, refer to [Monitor resources and cookies](https://developers.cloudflare.com/client-side-security/detection/monitor-connections-scripts/).

## Available statuses

- **Infrequent**: There are less than three reports for the script/connection. If there are no reports for a script/connection with *Infrequent* status for five days, then Cloudflare will delete all the information about the script/connection. Scripts with *Infrequent* status appear only in the All Reported Scripts dashboard, and connections with *Infrequent* status appear only in the All Reported Connections dashboard.
- **Active**: There are more than three reports for the script/connection.
- **Inactive**: A previously active script/connection was not reported in the last seven days. If the script/connection is reported again later, its status will change back to *Active*. If the script/connection is not reported for 30 days, Cloudflare will delete all the information about it. Scripts with *Inactive* status appear only in the All Reported Scripts dashboard, and connections with *Inactive* status appear only in the All Reported Connections dashboard.

Note

All scripts and connections considered malicious will appear in the Monitors dashboard, regardless of their status.

Malicious script detection is only available to customers with Client-Side Security Advanced.
