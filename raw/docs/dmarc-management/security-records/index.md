---
description: Learn how to configure SPF records, DKIM records, and DMARC records in your Cloudflare account to help improve email security.
title: Security records
image: https://developers.cloudflare.com/dmarc-management/security-records/og.png?v=9cbcb64541d8ff83
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/dmarc-management/llms.txt  
> Use this file to discover all available pages before exploring further.

# Security records

Last updated May 5, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/dmarc-management/security-records/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Without email authentication records, anyone can send email that appears to come from your domain — a technique known as domain spoofing. To prevent this, you add DNS TXT records (text-based entries in your domain's DNS settings) that allow receiving mail servers to verify whether an email actually came from you:

- [Sender Policy Framework (SPF) ↗︎](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/): Lists the IP addresses and domains authorized to send email on behalf of your domain.
- [DomainKeys Identified Mail (DKIM) ↗︎](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/): Authenticates the sender's domain and verifies that email content was not altered in transit, using a cryptographic signature.
- [Domain-based Message Authentication Reporting and Conformance (DMARC) ↗︎](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/): Tells receiving servers what to do when SPF or DKIM checks fail (for example, reject or quarantine the email), and sends you aggregate reports about your email traffic.

Note

For additional background on email security records, refer to the [introductory blog post ↗︎](https://blog.cloudflare.com/tackling-email-spoofing/).

## Create security records

To set up email security records:

1. Log in to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), and select your account and domain.
2. Go to **Email** > **DMARC Management**.
3. In **Email record overview**, select **View records**.
4. Use the available options to set up [SPF ↗︎](https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-spf-record/), [DKIM ↗︎](https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dkim-record/), and [DMARC records ↗︎](https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dmarc-record/). This page will also list any previous records you might already have in your account.

## Edit or delete records

Refer to [Manage DNS records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) for more information.
