---
description: Download a report in Email Security.
title: Download a report
image: https://developers.cloudflare.com/cloudflare-one/email-security/monitoring/download-report/og.png?v=6c9b7d9f9c18fb95
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-one/llms.txt  
> Use this file to discover all available pages before exploring further.

# Download a report

Last updated Apr 17, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-one/email-security/monitoring/download-report/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Email security allows you to download three types of reports:

- Disposition report
- Retro scan report
- Security report

## Download a disposition report

A disposition report shows you all the email messages based on the type of disposition you selected.

1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com/), select **Email security**.
2. Select **Monitoring** > **Download report**.
3. In **Report type**, select **Email disposition report**.
4. Under **Email disposition report**, select the **Date Range** (required), and the **Disposition**.
5. Select **Export to CSV**.

Refer to [Dispositions and attributes](https://developers.cloudflare.com/cloudflare-one/email-security/reference/dispositions-and-attributes/) to learn more.

## Download a retro scan report

Retro scan scans the last 14 days of your emails, and gives you a report on bulk, spam, spoof, suspicious and malicious emails.

1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com/), select **Email security**.
2. Select **Monitoring** > **Download report**.
3. In **Report type**, select **Retro Scan report**.
4. Select **View report** to view a report of your last 14 days of emails.

Refer to [Retro Scan](https://developers.cloudflare.com/cloudflare-one/email-security/retro-scan/) to learn more.

## Download a security report

A security report provides an overview of your email traffic. The report can be generated on the last 30, 60, 90 days, or a timeframe of your choice.

The reports contains:

- An executive summary: A summary of the threats detected in your organization's email traffic in the last 30 days.
- Threat detection: Review metrics regarding dispositions, policy detection, and impersonation attempts.
- Submissions: Review the metrics of emails your security team or users have requested to reclassify.

To download a security report:

1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com/), select **Email security**.
2. Select **Monitoring** > **Download report**.
3. In **Report type**, select **Security report** and the **Date range**.
4. Select **Generate report**.
5. Your security report is being generated. You will receive an email with the security report attached once it is ready.
