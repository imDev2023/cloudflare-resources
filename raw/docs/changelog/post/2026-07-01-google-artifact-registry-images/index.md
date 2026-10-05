---
description: Use private Google Artifact Registry images
title: Use Google Artifact Registry images with Containers
image: https://developers.cloudflare.com/changelog/post/2026-07-01-google-artifact-registry-images/og.png?v=426420897bde89d5
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 1, 2026

## Use Google Artifact Registry images with Containers

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-01-google-artifact-registry-images/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Containers now support [Google Artifact Registry ↗︎](https://cloud.google.com/artifact-registry) images. After you configure credentials, you can use a fully qualified Google Artifact Registry image reference in your [Wrangler configuration](https://developers.cloudflare.com/workers/wrangler/configuration/#containers) instead of first pushing the image to Cloudflare Registry.

Provide the service account email with `--gar-email` and pipe the service account JSON key through `stdin`:

```bash
cat <PATH_TO_KEY> | npx wrangler containers registries configure <REGION>-docker.pkg.dev --gar-email=<SERVICE_ACCOUNT_EMAIL> --secret-name=<SECRET_NAME>
```

```jsonc
{
  "$schema": "./node_modules/wrangler/config-schema.json",
  "containers": [
    {
      "image": "<REGION>-docker.pkg.dev/<PROJECT_ID>/<REPOSITORY>/<IMAGE>:<TAG>"
    }
  ]
}
```

```toml
# Example: us-central1-docker.pkg.dev/my-project/my-repo/my-image:latest
[[containers]]
image = "<REGION>-docker.pkg.dev/<PROJECT_ID>/<REPOSITORY>/<IMAGE>:<TAG>"
```

Only `*-docker.pkg.dev` hosts are supported. To configure credentials, refer to [Use private Google Artifact Registry images](https://developers.cloudflare.com/containers/guides/image-management/#use-private-google-artifact-registry-images).

For more information, refer to [Image management](https://developers.cloudflare.com/containers/guides/image-management/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-01-google-artifact-registry-images/#page","headline":"Use Google Artifact Registry images with Containers","description":"Use private Google Artifact Registry images","url":"https://developers.cloudflare.com/changelog/post/2026-07-01-google-artifact-registry-images/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-01-google-artifact-registry-images/og.png?v=426420897bde89d5","dateModified":"2026-07-01","datePublished":"2026-07-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
