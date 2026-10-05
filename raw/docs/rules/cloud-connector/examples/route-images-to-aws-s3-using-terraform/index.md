---
description: Route requests with a URI path starting with `/images` to a specific AWS S3 bucket with Cloud Connector using Terraform.
title: Route /images to an S3 Bucket using Terraform
image: https://developers.cloudflare.com/rules/cloud-connector/examples/route-images-to-aws-s3-using-terraform/og.png?v=25f0cbad093e2ef5
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Route /images to an S3 Bucket using Terraform

Route requests with a URI path starting with `/images` to a specific AWS S3 bucket with Cloud Connector using Terraform.

Last updated May 5, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/cloud-connector/examples/route-images-to-aws-s3-using-terraform/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

Terraform code snippets below refer to the v4 SDK only.

The following example defines a single Cloud Connector rule for a zone using Terraform. The rule routes requests to `/images` on your domain to an AWS S3 bucket.

```tf
resource "cloudflare_cloud_connector_rules" "serve_images_in_aws" {
  zone_id = "<ZONE_ID>"
  rules {
    description = "Route images to AWS S3 bucket"
    enabled     = true
    expression  = "http.request.full_uri wildcard \"https://<YOUR_HOSTNAME>/images/*\""
    provider    = "aws_s3"
    parameters {
      host = "<BUCKET_NAME>.s3.amazonaws.com"
    }
  }
}
```

## Additional resources

For additional guidance on using Terraform with Cloudflare, refer to the following resources:

- [Terraform documentation](https://developers.cloudflare.com/terraform/)
- [Cloudflare Provider for Terraform ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) (reference documentation)
