---
description: Apply consistent behavior to requests made with service tokens across your Zero Trust organization.
title: New strict service token authentication setting for Access
image: https://developers.cloudflare.com/changelog/post/2026-10-02-strict-service-token-authentication/og.png?v=1567ce58fae60c3b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 2, 2026

## New strict service token authentication setting for Access

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-02-strict-service-token-authentication/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The strict service token authentication setting applies consistent behavior to requests made with service tokens. When the setting is on for a Zero Trust organization, Access handles requests with service token headers as follows:

- If authentication or authorization fails, Access always returns `401` or `403` instead of redirecting the client to the login page with `302`.
- Only Service Auth policies can authorize the request. Access ignores Allow policies and any `CF_Authorization` cookie sent with the request.
- Access does not return a `CF_Authorization` cookie to the client after successful authentication. Subsequent requests should continue to use service token headers.
- Failed requests for recognized service tokens appear in [Access authentication logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/#non-identity-authentication).

Zero Trust organizations created on or after October 5, 2026 have strict service token authentication turned on by default and cannot turn it off. Cloudflare recommends that existing organizations turn it on as well.

Organizations created before October 5, 2026 can configure the setting in the dashboard or through the API.

1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Access settings**. [Go to **Access settings** ↗](https://one.dash.cloudflare.com/?to=/:account/access-controls/settings)
2. Under **Manage service tokens**, turn on **Strict service token authentication**.
3. In the confirmation dialog, select **Enable**.

To turn off strict service token authentication, turn off the setting and select **Disable**.

```bash
curl "https://api.cloudflare.com/client/v4/accounts/%7Baccount_id%7D/access/organizations" \
	--request PATCH \
	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
	--json '{
		"strict_service_token_auth": true
	}'
```

To turn off strict service token authentication, set `strict_service_token_auth` to `false`.

For behavior and configuration details, refer to [Strict service token authentication](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#strict-service-token-authentication).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-10-02-strict-service-token-authentication/#page","headline":"New strict service token authentication setting for Access","description":"Apply consistent behavior to requests made with service tokens across your Zero Trust organization.","url":"https://developers.cloudflare.com/changelog/post/2026-10-02-strict-service-token-authentication/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-10-02-strict-service-token-authentication/og.png?v=1567ce58fae60c3b","dateModified":"2026-10-02","datePublished":"2026-10-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
