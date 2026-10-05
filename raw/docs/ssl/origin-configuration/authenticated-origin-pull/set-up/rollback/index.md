---
description: Roll back per-hostname Authenticated Origin Pulls to zone-level settings.
title: Roll back per-hostname AOP
image: https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/rollback/og.png?v=0a12558534de95b6
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ssl/llms.txt  
> Use this file to discover all available pages before exploring further.

# Roll back per-hostname AOP

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/rollback/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

If you need to disable or remove your [per-hostname](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/) Authenticated Origin Pulls configuration, follow these steps.

Note

[Global AOP](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/global/), [zone-level AOP](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/zone-level/), and [per-hostname AOP](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/) are three independent configurations. Enabling or disabling one does not affect the others.

1. Use a [`PUT` request](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/hostnames/methods/update/) to disable Authenticated Origin Pulls on the hostname.<details><summary>

   Required API token permissions</summary>

At least one of the following <a href="https://developers.cloudflare.com/fundamentals/api/reference/permissions/">token permissions</a> is required:
   - <code>SSL and Certificates Write</code></details>

   *Enable or Disable a Hostname for Client Authenticationbash*

   

   ```bash
   curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/origin_tls_client_auth/hostnames" \
   	--request PUT \
   	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
   	--json '{
   		"config": [
   				{
   						"enabled": false,
   						"cert_id": "<CERT_ID>",
   						"hostname": "<YOUR_HOSTNAME>"
   				}
   		]
   	}'
   ```


2. (Optional) Use a [`GET` request](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/hostname_certificates/methods/list/) to obtain a list of the client certificate IDs. You will need the ID of the certificate you want to remove for the following step.<details><summary>

   Required API token permissions</summary>

At least one of the following <a href="https://developers.cloudflare.com/fundamentals/api/reference/permissions/">token permissions</a> is required:
   - <code>SSL and Certificates Write</code>
   - <code>SSL and Certificates Read</code></details>

   *List Certificatesbash*

   

   ```bash
   curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/origin_tls_client_auth/hostnames/certificates" \
   	--request GET \
   	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
   ```


3. Use the [Delete hostname client certificate](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/hostname_certificates/methods/delete/) endpoint to remove the certificate you had uploaded.<details><summary>

   Required API token permissions</summary>

At least one of the following <a href="https://developers.cloudflare.com/fundamentals/api/reference/permissions/">token permissions</a> is required:
   - <code>SSL and Certificates Write</code></details>

   *Delete Hostname Client Certificatebash*

   

   ```bash
   curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/origin_tls_client_auth/hostnames/certificates/$CERTIFICATE_ID" \
   	--request DELETE \
   	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
   ```
