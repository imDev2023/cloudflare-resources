---
description: Run a Cloudflare Mesh node as a Docker container for Docker Compose, Kubernetes, and CI/CD environments.
title: Container image for Cloudflare Mesh
image: https://developers.cloudflare.com/changelog/post/2026-08-07-mesh-container-image/og.png?v=588b366cb89cd3ce
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 7, 2026

## Container image for Cloudflare Mesh

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-07-mesh-container-image/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/) nodes can now run as Docker containers. The [`cloudflare/mesh` ↗︎](https://hub.docker.com/r/cloudflare/mesh) image is available on Docker Hub for Docker Compose, Kubernetes, and any OCI-compatible runtime — no host-level package installation required.

The image supports `amd64` and `arm64` architectures and includes built-in [source NAT](https://developers.cloudflare.com/mesh/guides/run-mesh-in-containers/#source-nat) so return traffic routes correctly without VPC route table changes.

#### Deployment patterns

- **Docker Compose** — add a `cloudflare-mesh` service to your `compose.yaml` and connect your entire stack to a private network.
- **Kubernetes StatefulSet** — deploy a standalone Mesh node with persistent registration state.
- **Kubernetes sidecar** — add the Mesh image as a sidecar container in a Pod to connect an application to Cloudflare without application changes.
- **CI/CD** — pull the image in a pipeline step, join the Mesh, run integration tests against private infrastructure, and tear down. The node disappears when the container exits.

For [high availability](https://developers.cloudflare.com/mesh/features/high-availability/), run multiple replicas with the same Mesh node token. Cloudflare operates replicas in active-passive mode with automatic failover.

[Go to **Mesh** ↗](https://dash.cloudflare.com/?to=/:account/mesh)

For setup steps, runtime configuration, and deployment examples, refer to [Run Mesh in Docker / Kubernetes](https://developers.cloudflare.com/mesh/guides/run-mesh-in-containers/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-07-mesh-container-image/#page","headline":"Container image for Cloudflare Mesh","description":"Run a Cloudflare Mesh node as a Docker container for Docker Compose, Kubernetes, and CI/CD environments.","url":"https://developers.cloudflare.com/changelog/post/2026-08-07-mesh-container-image/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-07-mesh-container-image/og.png?v=588b366cb89cd3ce","dateModified":"2026-08-07","datePublished":"2026-08-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
