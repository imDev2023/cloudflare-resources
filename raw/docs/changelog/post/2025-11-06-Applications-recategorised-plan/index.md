---
description: We are preparing to remap some existing applications to better reflect their category
title: Applications to be remapped to the new categories
image: https://developers.cloudflare.com/changelog/post/2025-11-06-Applications-recategorised-plan/og.png?v=899fe890f8f1cb95
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 6, 2025

## Applications to be remapped to the new categories

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-06-Applications-recategorised-plan/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We have previously added new application categories to better reflect their content and improve HTTP traffic management: refer to [Changelog](https://developers.cloudflare.com/cloudflare-one/changelog/gateway/#2025-10-28). While the new categories are live now, we want to ensure you have ample time to review and adjust any existing rules you have configured against old categories. The remapping of existing applications into these new categories will be completed by January 30, 2026. This timeline allows you a dedicated period to:

- Review the new category structure.
- Identify any policies you have that target the older categories.
- Adjust your rules to reference the new, more precise categories before the old mappings change. Once the applications have been fully remapped by January 30, 2026, you might observe some changes in the traffic being mitigated or allowed by your existing policies. We encourage you to use the intervening time to prepare for a smooth transition.

**Applications being remappedd**

| Application Name | Existing Category | New Category |
| --- | --- | --- |
| Google Photos | File Sharing | Photography & Graphic Design |
| Flickr | File Sharing | Photography & Graphic Design |
| ADP | Human Resources | Business |
| Greenhouse | Human Resources | Business |
| myCigna | Human Resources | Health & Fitness |
| UnitedHealthcare | Human Resources | Health & Fitness |
| ZipRecruiter | Human Resources | Business |
| Amazon Business | Human Resources | Business |
| Jobcenter | Human Resources | Business |
| Jobsuche | Human Resources | Business |
| Zenjob | Human Resources | Business |
| DocuSign | Legal | Business |
| Postident | Legal | Business |
| Adobe Creative Cloud | Productivity | Photography & Graphic Design |
| Airtable | Productivity | Development |
| Autodesk Fusion360 | Productivity | IT Management |
| Coursera | Productivity | Education |
| Microsoft Power BI | Productivity | Business |
| Tableau | Productivity | Business |
| Duolingo | Productivity | Education |
| Adobe Reader | Productivity | Business |
| AnpiReport | Productivity | Travel |
| ビズリーチ | Productivity | Business |
| doda (デューダ) | Productivity | Business |
| 求人ボックス | Productivity | Business |
| マイナビ2026 | Productivity | Business |
| Power Apps | Productivity | Business |
| RECRUIT AGENT | Productivity | Business |
| シフトボード | Productivity | Business |
| スタンバイ | Productivity | Business |
| Doctolib | Productivity | Health & Fitness |
| Miro | Productivity | Photography & Graphic Design |
| MyFitnessPal | Productivity | Health & Fitness |
| Sentry Mobile | Productivity | Travel |
| Slido | Productivity | Photography & Graphic Design |
| Arista Networks | Productivity | IT Management |
| Atlassian | Productivity | Business |
| CoderPad | Productivity | Business |
| eAgreements | Productivity | Business |
| Vmware | Productivity | IT Management |
| Vmware Vcenter | Productivity | IT Management |
| AWS Skill Builder | Productivity | Education |
| Microsoft Office 365 (GCC) | Productivity | Business |
| Microsoft Exchange Online (GCC) | Productivity | Business |
| Canva | Sales & Marketing | Photography & Graphic Design |
| Instacart | Shopping | Food & Drink |
| Wawa | Shopping | Food & Drink |
| McDonald's | Shopping | Food & Drink |
| Vrbo | Shopping | Travel |
| American Airlines | Shopping | Travel |
| Booking.com | Shopping | Travel |
| Ticketmaster | Shopping | Entertainment & Events |
| Airbnb | Shopping | Travel |
| DoorDash | Shopping | Food & Drink |
| Expedia | Shopping | Travel |
| EasyPark | Shopping | Travel |
| UEFA Tickets | Shopping | Entertainment & Events |
| DHL Express | Shopping | Business |
| UPS | Shopping | Business |

For more information on creating HTTP policies, refer to [Applications and app types](https://developers.cloudflare.com/cloudflare-one/traffic-policies/application-app-types/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-06-Applications-recategorised-plan/#page","headline":"Applications to be remapped to the new categories","description":"We are preparing to remap some existing applications to better reflect their category","url":"https://developers.cloudflare.com/changelog/post/2025-11-06-Applications-recategorised-plan/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-06-Applications-recategorised-plan/og.png?v=899fe890f8f1cb95","dateModified":"2025-11-06","datePublished":"2025-11-06","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
