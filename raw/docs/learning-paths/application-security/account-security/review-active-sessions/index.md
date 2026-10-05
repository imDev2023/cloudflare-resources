---
description: View and revoke active account sessions.
title: Review active sessions
image: https://developers.cloudflare.com/learning-paths/application-security/account-security/review-active-sessions/og.png?v=fcb7f0776274a5b2
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/learning-paths/llms.txt  
> Use this file to discover all available pages before exploring further.

# Review active sessions

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/learning-paths/application-security/account-security/review-active-sessions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

In the Cloudflare dashboard, you can view a list of active sessions associated with your email address.

Each time your email is used to log in to your Cloudflare account, a session begins. The Cloudflare dashboard provides session information including if the device is currently viewing the dashboard, the IP address, location, device type, browser type, and last active login.

If you notice any suspicious activity, you can also revoke any active sessions.

Note

By default, the session timeout for the Cloudflare dashboard is 72 hours without any activity.

Some customers can also enforce single-sign on (SSO) by [adding a Dashboard SSO application](https://developers.cloudflare.com/fundamentals/manage-members/dashboard-sso/).

If you navigate to **My Profile** > **Sessions**, you can view active sessions and revoke any session that you do not recognize.
