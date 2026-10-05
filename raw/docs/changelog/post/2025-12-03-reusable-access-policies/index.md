---
description: Workers now use reusable Access policies to reduce duplication and make it easier to manage access across multiple Workers.
title: One-click Access protection for Workers now creates reusable Cloudflare Access policies
image: https://developers.cloudflare.com/changelog/post/2025-12-03-reusable-access-policies/og.png?v=dbb0a9181c6e432b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 4, 2025

## One-click Access protection for Workers now creates reusable Cloudflare Access policies

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-03-reusable-access-policies/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers applications now use reusable [Cloudflare Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) to reduce duplication and simplify access management across multiple Workers.

Previously, enabling Cloudflare Access on a Worker created per-application policies, unique to each application. Now, we create reusable policies that can be shared across applications:

- **Preview URLs**: All Workers preview URLs share a single "Cloudflare Workers Preview URLs" policy across your account. This policy is automatically created the first time you enable Access on any preview URL. By sharing a single policy across all preview URLs, you can configure access rules once and have them apply company-wide to all Workers which protect preview URLs. This makes it much easier to manage who can access preview environments without having to update individual policies for each Worker.
- **Production workers.dev URLs**: When enabled, each Worker gets its own reusable policy (named `<worker-name> - Production`) by default. We recognize production services often have different access requirements and having individual policies here makes it easier to configure service-to-service authentication or protect internal dashboards or applications with specific user groups. Keeping these policies separate gives you the flexibility to configure exactly the right access rules for each production service. When you disable Access on a production Worker, the associated policy is automatically cleaned up if it's not being used by other applications.

This change reduces policy duplication, simplifies cross-company access management for preview environments, and provides the flexibility needed for production services. You can still customize access rules by editing the reusable policies in the Zero Trust dashboard.

To enable Cloudflare Access on your Worker:

1. In the Cloudflare dashboard, go to **Workers & Pages**.
2. Select your Worker.
3. Go to **Settings** > **Domains & Routes**.
4. For `workers.dev` or Preview URLs, click **Enable Cloudflare Access**.
5. Optionally, click **Manage Cloudflare Access** to customize the policy.

For more information on configuring Cloudflare Access for Workers, refer to the [Workers Access documentation](https://developers.cloudflare.com/workers/configuration/routing/workers-dev/#manage-access-to-workersdev).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-03-reusable-access-policies/#page","headline":"One-click Access protection for Workers now creates reusable Cloudflare Access policies","description":"Workers now use reusable Access policies to reduce duplication and make it easier to manage access across multiple Workers.","url":"https://developers.cloudflare.com/changelog/post/2025-12-03-reusable-access-policies/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-12-03-reusable-access-policies/og.png?v=dbb0a9181c6e432b","dateModified":"2025-12-04","datePublished":"2025-12-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
