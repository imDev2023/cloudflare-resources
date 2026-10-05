---
description: Protect environments from accidental changes.
title: Read-only environments
image: https://developers.cloudflare.com/version-management/reference/read-only-environments/og.png?v=2bc87e7f8f67b0e4
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/version-management/llms.txt  
> Use this file to discover all available pages before exploring further.

# Read-only environments

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/version-management/reference/read-only-environments/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

When an environment is read-only, versions deployed to this environment will permanently become read-only. This configuration protects sensitive environments from accidental changes.

**Version Zero** is an exception to this rule and is always editable.

**Production** is a read-only environment by default. This means that any version associated with **Production** also becomes read-only. This configuration prevents another member of your account from accidentally editing the version associated with your live traffic. You can change this configuration by editing the environment.

  

For similar reasons, some organizations may make **Staging** a read-only environment. Otherwise, another member of your account could make changes to a version in **Staging** *after* your organization has performed the validation tests prior to promoting to **Production**. Without having a read-only **Staging** environment, this change could be released into **Production** without testing and might cause an issue with live traffic.

To change the read-only status of an environment, [edit the environment](https://developers.cloudflare.com/version-management/how-to/environments/#edit-environment).
