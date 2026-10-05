---
description: Look up threat intelligence for IPs, domains, URLs, and AS numbers.
title: Investigate
image: https://developers.cloudflare.com/security-center/investigate/og.png?v=5a23cb16dfa7404e
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/security-center/llms.txt  
> Use this file to discover all available pages before exploring further.

# Investigate

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/security-center/investigate/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

User permission

Investigate is available to all users. Every user can view existing URL scanner reports and initiate new URL scans.

However, advanced intelligence features, including searching for IP and domain intelligence and passive DNS records, are restricted to users with the following roles: Super Admin, Administrator, Brand Protection, Cloudforce One Admin.

Investigate allows you to view a domain’s category, the IP it belongs to, and whether the category has changed before. You can also see which records it points to, including the country of origin and passive DNS records. After searching with Investigate, you will get an API curl to retrieve the same search results.

You can learn more about the IP addresses in your logs by searching via the IP address to view its category and threat data. Enter any IP address, domain name, and hostname to see how it has been categorized from a threat perspective.

Investigate also shows [Web Application Firewall ↗︎](https://developers.cloudflare.com/waf/) analytics for your websites behind Cloudflare to help you discover what your vulnerabilities are, where attacks come from, and what to do about it.
