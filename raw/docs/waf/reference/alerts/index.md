---
description: Set up alerts for WAF security events.
title: Alerts for security events
image: https://developers.cloudflare.com/waf/reference/alerts/og.png?v=df98be93362e0892
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/waf/llms.txt  
> Use this file to discover all available pages before exploring further.

# Alerts for security events

Last updated Oct 2, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/waf/reference/alerts/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare provides two types of security alerts that inform you of any spikes in security events:

- **Security Events Alert**: Alerts about spikes across all services that generate log entries in Security Events.
- **Advanced Security Events Alert**: Similar to Security Events Alert with support for additional filtering options.

For details on alert types and their availability, refer to [Alert types](#alert-types).

To receive security alerts, you must configure a [notification](https://developers.cloudflare.com/notifications/). All plans can receive notifications through email or webhooks. Business and higher plans can also use PagerDuty.

## Set up a notification for security alerts

For instructions on how to set up a notification for a security alert, refer to [Create a Notification](https://developers.cloudflare.com/notifications/get-started/#create-an-alert).

---

## Alert logic

Security alerts use a static threshold together with a [z-score ↗︎](https://en.wikipedia.org/wiki/Standard_score) calculation over the last six hours and five-minute buckets of events. An alert is triggered whenever the z-score value is above 3.5 and the spike crosses a threshold of 200 security events. You will not receive duplicate alerts within the same two-hour time frame.

## Alert types

<details>

<summary>

Advanced Security Events Alert

</summary>

**Who is it for?**

Enterprise customers who want to receive alerts about spikes in specific services that generate log entries in <a href="https://developers.cloudflare.com/waf/analytics/security-events/">Security Events</a>. For more information, refer to <a href="https://developers.cloudflare.com/waf/reference/alerts/">WAF alerts</a>.

**Other options / filters**

A mandatory <a href="https://developers.cloudflare.com/api/resources/alerting/subresources/policies/methods/create/"><code>filters</code></a> selection is needed when you create a notification policy which includes the list of services and zones that you want to be alerted on.

- You can search for and add domains from your list of Enterprise zones.
- You can choose which services the alert should monitor (Managed Firewall, Rate Limiting, etc.).
- You can filter events by a targeted action.

**Included with**

Enterprise plans.

**What should you do if you receive one?**

Review the information in <a href="https://developers.cloudflare.com/waf/analytics/security-events/">Security Events</a> to identify any possible attack or misconfiguration.

**Additional information**

The mean time to detection is five minutes.

When setting up this alert, you can select the services that will be monitored. Each selected service is monitored separately and can be selected as a filter.

**Limitations**

Security Events (WAF) alerts are not sent for each individual events, but only when a spike in traffic reaches the threshold for an alert to be sent.

These thresholds cannot be configured. Z-score is used to determine the threshold.

</details>

<details>

<summary>

Security Events Alert

</summary>

**Who is it for?**

Business and Enterprise customers who want to receive alerts about spikes across all services that generate log entries in <a href="https://developers.cloudflare.com/waf/analytics/security-events/">Security Events</a>. For more information, refer to <a href="https://developers.cloudflare.com/waf/reference/alerts/">WAF alerts</a>.

**Other options / filters**

A mandatory <a href="https://developers.cloudflare.com/api/resources/alerting/subresources/policies/methods/create/"><code>filters</code></a> selection is needed when you create a notification policy which includes the list of zones that you want to be alerted on.

- You can also search for and add domains from your list of business or enterprise zones. The notification will be sent for the domains chosen.
- You can filter events by a targeted action.

**Included with**

Business and Enterprise plans.

**What should you do if you receive one?**

Review the information in <a href="https://developers.cloudflare.com/waf/analytics/security-events/">Security Events</a> to identify any possible attack or misconfiguration.

**Additional information**

The mean time to detection is five minutes.

When setting up this alert, you can select the services that will be monitored. Each selected service is monitored separately.

**Limitations**

Security Events (WAF) alerts are not sent for each individual events, but only when a spike in traffic reaches the threshold for an alert to be sent.

These thresholds cannot be configured. Z-score is used to determine the threshold.

</details>
