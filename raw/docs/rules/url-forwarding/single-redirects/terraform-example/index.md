---
description: Create Single Redirect rules using the Terraform Cloudflare provider.
title: Create a redirect rule using Terraform
image: https://developers.cloudflare.com/rules/url-forwarding/single-redirects/terraform-example/og.png?v=28d23a7763d0f86b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Create a redirect rule using Terraform

Last updated Aug 25, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/terraform-example/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

Terraform code snippets below refer to the v4 SDK only.

The following example defines a single redirect rule for a zone using Terraform. The rule creates a static URL redirect for visitors requesting the contacts page using an old URL.

```tf
# Single Redirects resource
resource "cloudflare_ruleset" "single_redirects_example" {
  zone_id     = "<ZONE_ID>"
  name        = "redirects"
  description = "Redirects ruleset"
  kind        = "zone"
  phase       = "http_request_dynamic_redirect"

  rules {
    ref         = "redirect_old_url"
    description = "Redirect visitors still using old URL"
    expression  = "(http.request.uri.path matches \"^/contact-us/\")"
    action      = "redirect"
    action_parameters {
      from_value {
        status_code = 301
        target_url {
          value = "/contacts/"
        }
        preserve_query_string = false
      }
    }
  }
}
```

Use the `ref` field to get stable rule IDs across updates when using Terraform. Adding this field prevents Terraform from recreating the rule on changes. For more information, refer to [Troubleshooting](https://developers.cloudflare.com/terraform/troubleshooting/rule-id-changes/#how-to-keep-the-same-rule-id-between-modifications) in the Terraform documentation.

## Additional resources

For additional guidance on using Terraform with Cloudflare, refer to the following resources:

- [Terraform documentation](https://developers.cloudflare.com/terraform/)
- [Cloudflare Provider for Terraform ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) (reference documentation)
