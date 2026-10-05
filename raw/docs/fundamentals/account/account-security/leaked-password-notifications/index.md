---
description: Cloudflare checks your password against known data breaches at login and prompts you to reset it if a match is found.
title: Leaked Password Notifications
image: https://developers.cloudflare.com/fundamentals/account/account-security/leaked-password-notifications/og.png?v=cb32e6357254b506
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/fundamentals/llms.txt  
> Use this file to discover all available pages before exploring further.

# Leaked Password Notifications

Last updated Apr 20, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/fundamentals/account/account-security/leaked-password-notifications/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare automatically checks if your password has been compromised when you log in to the Cloudflare dashboard. Every time you log in to your account, we will securely verify through threat intelligence sources to confirm if your password has been leaked in a past data breach.

Refer to the [blog post ↗︎](https://blog.cloudflare.com/helping-keep-customers-safe-with-leaked-password-notification/) for more information on how Cloudflare checks for leaked credentials.

Note

Cloudflare does not have additional information about the specific breach or Internet service that potentially lost your password.

Popular online tools such as [Have I Been Pwned ↗︎](https://haveibeenpwned.com/) can help you better understand where your external accounts were attacked. If you reused this password in other systems, it is recommended that you reset it in those as well.

If your password is found in a data breach, we will email you information on how to reset your password and prompt you to do so in the Cloudflare dashboard.

Your first three login attempts will warn you of the need to reset your password. After three attempts, you will be required to reset your password to log in to Cloudflare.

Users leveraging [Single Sign-On (SSO)](https://developers.cloudflare.com/fundamentals/manage-members/dashboard-sso/) or [two-factor authentication (2FA)](https://developers.cloudflare.com/fundamentals/user-profiles/2fa/) will not be subject to these requirements given the higher level of security provided by those features.

We encourage you to enable two-factor authentication to secure your account.

Cloudflare account Super Administrators can also require that [all members enable 2FA](https://developers.cloudflare.com/fundamentals/user-profiles/2fa/). This functionality can be enabled by going to **Manage Account** > **Members** in the Cloudflare dashboard.
