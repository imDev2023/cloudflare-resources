---
description: Create a configuration rule using Terraform to turn off Email Obfuscation and Browser Integrity Check for API requests in a given zone.
title: Define a single configuration rule using Terraform
image: https://developers.cloudflare.com/rules/configuration-rules/examples/define-single-configuration-terraform/og.png?v=0acc4eaf324e5f0d
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/rules/llms.txt  
> Use this file to discover all available pages before exploring further.

# Define a single configuration rule using Terraform

Create a configuration rule using Terraform to turn off Email Obfuscation and Browser Integrity Check for API requests in a given zone.

Last updated Aug 25, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/rules/configuration-rules/examples/define-single-configuration-terraform/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

Terraform code snippets below refer to the v4 SDK only.

The following example defines a single configuration rule for a zone using Terraform. The rule disables Email Obfuscation and Browser Integrity Check for API requests.

```tf
# Disable a couple of Cloudflare settings for API requests
resource "cloudflare_ruleset" "http_config_rules_example" {
  zone_id     = "<ZONE_ID>"
  name        = "Config rules ruleset"
  description = "Set configuration rules for incoming requests"
  kind        = "zone"
  phase       = "http_config_settings"

  rules {
    ref         = "disable_obfuscation_bic"
    description = "Disable email obfuscation and BIC for API requests"
    expression  = "(http.request.uri.path matches \"^/api/\")"
    action      = "set_config"
    action_parameters {
      email_obfuscation = false
      bic               = false
    }
  }
}
```

Use the `ref` field to get stable rule IDs across updates when using Terraform. Adding this field prevents Terraform from recreating the rule on changes. For more information, refer to [Troubleshooting](https://developers.cloudflare.com/terraform/troubleshooting/rule-id-changes/#how-to-keep-the-same-rule-id-between-modifications) in the Terraform documentation.

## Additional resources

For additional guidance on using Terraform with Cloudflare, refer to the following resources:

- [Terraform documentation](https://developers.cloudflare.com/terraform/)
- [Cloudflare Provider for Terraform ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) (reference documentation)
