---
description: Scan and review aggregated security risks.
title: Security Insights
image: https://developers.cloudflare.com/learning-paths/application-security/security-center/insights/og.png?v=944da72726f1af15
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/learning-paths/llms.txt  
> Use this file to discover all available pages before exploring further.

# Security Insights

Last updated May 5, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/learning-paths/application-security/security-center/insights/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Security Insights provides you with a list of insights, covering different areas of your Cloudflare environment, such as: Cloudflare account settings, DNS record configurations, SSL/TLS certificates configurations, Cloudflare Access configurations and Cloudflare WAF configurations.

## Dashboard analytics

Security Insights focuses on your Cloudflare environment by running [security scans](https://developers.cloudflare.com/security/security-insights/how-it-works/#scan-frequency) at regular intervals. Instead of navigating through each of your domains to review their security issues, the Security Center aggregates all of them into a single dashboard.

![Security Insights Overview](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1007,height=595,format=webp/_astro/security-insights-overview.lQDBpBkp.png)

The list of insights may include potential security threats, vulnerabilities, compliance risks, insecure configurations, or any other identified risks.

## Severity properties

Each insight that is discovered by the Security Insights scan will have the following properties assigned to them:

- **Severity**: The security risk of the insight. The severity values are: *Low*, *Moderate*, and *Critical*. The higher the severity level, the higher the risk of threat to your environment.
- **Insight**: The insight description detailing the current configuration that is causing the risk or vulnerability.
- **Risk**: A description of the risk associated with not addressing the issue.
- **Type**: The insight category.
