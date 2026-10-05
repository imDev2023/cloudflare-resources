---
description: CASB remediation policies automatically fix Microsoft 365 and Google Workspace file-sharing findings and send webhooks, without manual intervention.
title: Automatically remediate Microsoft 365 and Google Workspace findings with API-based CASB remediation policies
image: https://developers.cloudflare.com/changelog/post/2026-08-21-casb-policies/og.png?v=1f62a80a0e6e5fa1
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 21, 2026

## Automatically remediate Microsoft 365 and Google Workspace findings with API-based CASB remediation policies

[CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-21-casb-policies/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/) is an API-based (agentless) tool that continuously scans your SaaS and cloud applications for security misconfigurations and data exposure. You can now use **CASB remediation policies** to automatically fix a finding or send a webhook the moment CASB detects it, without manual triage.

#### Remediate Microsoft 365 and Google Workspace findings

A policy can perform a first-party remediation action directly against the SaaS integration API. When a policy triggers, Cloudflare revokes the external sharing configuration without human intervention.

Remediation is currently supported for file-sharing findings in Microsoft 365 and Google Workspace. Support for additional finding types and integrations is coming soon. For the full list of supported finding types, refer to [Run remediations](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/policies/#run-remediations) in the CASB remediation policies documentation.

#### Send webhooks

A policy can send posture finding data to Slack, ServiceNow, or any other webhook destination. Webhook actions are supported for all posture finding types across CASB integrations.

A single policy can perform both actions: remediate a finding and send a webhook.

#### Get started

1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com), go to **Cloud & SaaS findings** > **Policies**.
2. Select **Create a policy**.
3. Under **Basic information**, enter a **Policy name** and, optionally, a **Description**.
4. Under **Choose how you want to trigger the policy**, select a **Vendor**, **Integration**, and **Finding type**.
5. Under **Define what to do with findings that match your trigger**, choose **Run Remediation**, **Send webhooks**, or both.
6. Under **Status**, turn on **Enable policy**.
7. Select **Create policy**.

#### Learn more

- Learn how to [create and manage CASB remediation policies](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/policies/) in Cloudflare One.
- Configure [CASB webhooks](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/webhooks/) as a policy destination.
- Learn how to [manage findings](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/manage-findings/) in Cloudflare One.

CASB remediation policies are now available in Cloudflare One.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-21-casb-policies/#page","headline":"Automatically remediate Microsoft 365 and Google Workspace findings with API-based CASB remediation policies","description":"CASB remediation policies automatically fix Microsoft 365 and Google Workspace file-sharing findings and send webhooks, without manual intervention.","url":"https://developers.cloudflare.com/changelog/post/2026-08-21-casb-policies/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-21-casb-policies/og.png?v=1f62a80a0e6e5fa1","dateModified":"2026-08-21","datePublished":"2026-08-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
