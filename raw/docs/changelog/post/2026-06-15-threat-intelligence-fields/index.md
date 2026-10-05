---
description: New cf.intel.ip fields available in custom rules and rate limiting rules for threat intelligence matching.
title: Use Cloudforce One threat intelligence in WAF rules
image: https://developers.cloudflare.com/changelog/post/2026-06-15-threat-intelligence-fields/og.png?v=d264f37f93436b8b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 15, 2026

## Use Cloudforce One threat intelligence in WAF rules

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-15-threat-intelligence-fields/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now match incoming requests against Cloudforce One threat intelligence in your WAF rules. A new detection looks up the client IP address of each request against the threat intelligence database. If the IP was involved in threat activity in the past seven days, Cloudflare populates `cf.intel.ip.*` fields that you can use in [custom rules](https://developers.cloudflare.com/waf/custom-rules/) and [rate limiting rules](https://developers.cloudflare.com/waf/rate-limiting-rules/).

The detection populates the following fields. Use the [`any()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#any) function with the `[*]` wildcard to match array values:

- `cf.intel.ip.datasets` — the dataset that flagged the IP address ( `ddos` or `waf`).
- `cf.intel.ip.target_industries` — industries the IP address has targeted.
- `cf.intel.ip.attacker_names` — known threat actors associated with the IP address.
- `cf.intel.ip.attacker_countries` — source countries of the threat activity.
- `cf.intel.ip.target_countries` — countries the IP address has targeted.

For example, the following custom rule expression blocks requests from IP addresses associated with DDoS activity that have targeted France:

```txt
any(cf.intel.ip.target_countries[*] == "FR") and any(cf.intel.ip.datasets[*] == "ddos")
```

These fields work with the Cloudflare API and Terraform. Matches are logged in [Security Analytics](https://developers.cloudflare.com/waf/analytics/security-analytics/).

The threat intelligence detection is available to customers with an active [Cloudforce One](https://developers.cloudflare.com/security-center/cloudforce-one/) subscription. For more information, refer to [Threat intelligence](https://developers.cloudflare.com/waf/detections/threat-intelligence/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-15-threat-intelligence-fields/#page","headline":"Use Cloudforce One threat intelligence in WAF rules","description":"New cf.intel.ip fields available in custom rules and rate limiting rules for threat intelligence matching.","url":"https://developers.cloudflare.com/changelog/post/2026-06-15-threat-intelligence-fields/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-15-threat-intelligence-fields/og.png?v=d264f37f93436b8b","dateModified":"2026-06-15","datePublished":"2026-06-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
