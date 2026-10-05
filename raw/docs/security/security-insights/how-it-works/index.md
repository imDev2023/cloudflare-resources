---
description: How Security Insights scans your account and produces security findings.
title: How it works
image: https://developers.cloudflare.com/security/security-insights/how-it-works/og.png?v=462a8fa79eefbebc
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/security/llms.txt  
> Use this file to discover all available pages before exploring further.

# How it works

Last updated Aug 26, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/security/security-insights/how-it-works/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare runs regular security scans on your account. These scans check your Cloudflare account settings, DNS record configurations, and product configurations — such as SSL/TLS, WAF, and Access — across all domains in your account.

Each scan compares your current configuration against a set of ideal product configurations that indicate a strong security posture. When your configuration does not match an ideal configuration for one or more checks, the scan produces a **Security Insight** — a finding that represents a potential risk.

The [list of insights](https://developers.cloudflare.com/security/security-insights/) may include potential security threats, vulnerabilities, compliance risks, insecure configurations, or any other identified risks.

Note

Security Insights also checks [non-proxied (DNS-only) hostnames](https://developers.cloudflare.com/dns/proxy-status/#dns-only-records). Because these records are not routed through Cloudflare, they do not benefit from Cloudflare's application security features.

## Scan properties

Each insight has the following properties:

- **Severity**: The security risk of the insight. The severity values are: *Low*, *Moderate*, and *Critical*. The higher the severity level, the higher the risk of threat to your environment.
- **Insight**: The insight description detailing the current configuration that is causing the risk or vulnerability.
- **Risk**: A description of the risk associated with not addressing the issue.
- **Type**: The insight category.

For a full list of insight types and their descriptions, refer to [Security Insights](https://developers.cloudflare.com/security/security-insights/).

## Scan frequency

Cloudflare performs scans automatically for all accounts and zones by default. On-demand scans are available on all plans:

| Plan | Scan Frequency | On-Demand |
| --- | --- | --- |
| Free | Every 7 days | Yes |
| Pro and Business | Every 3 days | Yes |
| Enterprise | Daily | Yes |

Caution

Automated scans for Free accounts may be paused due to account inactivity. To ensure scans continue to run, regularly review Security Insights in the Cloudflare dashboard or through the [API](https://developers.cloudflare.com/api/resources/security_center/).

All accounts can also manually start a scan from the **Security Insights** page in the Cloudflare dashboard.

[Go to **Security insights** ↗](https://dash.cloudflare.com/?to=/:account/security-center)
