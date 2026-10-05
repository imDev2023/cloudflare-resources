---
description: Configure malicious upload detection using Terraform.
title: Terraform configuration examples
image: https://developers.cloudflare.com/waf/detections/malicious-uploads/terraform-examples/og.png?v=0a6682a5c188692b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/waf/llms.txt  
> Use this file to discover all available pages before exploring further.

# Terraform configuration examples

Last updated May 6, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/waf/detections/malicious-uploads/terraform-examples/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The following Terraform configuration examples address common scenarios for managing, configuring, and using WAF content scanning.

For more information, refer to the [Terraform Cloudflare provider documentation ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs).

If you are using the Cloudflare API, refer to [Common API calls](https://developers.cloudflare.com/waf/detections/malicious-uploads/api-calls/).

## Enable WAF content scanning

Use the `cloudflare_content_scanning` resource to enable content scanning for a zone. For example:

```terraform
resource "cloudflare_content_scanning" "zone_content_scanning_example" {
	zone_id = var.cloudflare_zone_id
	enabled = true
}
```

## Configure a custom scan expression

Use the `cloudflare_content_scanning_expression` resource to add a custom scan expression. For example:

```terraform
resource "cloudflare_content_scanning_expression" "my_custom_scan_expression" {
  zone_id = var.cloudflare_zone_id
  payload = "lookup_json_string(http.request.body.raw, \"file\")"
}
```

For more information, refer to [Custom scan expressions](https://developers.cloudflare.com/waf/detections/malicious-uploads/#custom-scan-expressions).

## Add a custom rule to block malicious uploads

This example adds a [custom rule](https://developers.cloudflare.com/waf/custom-rules/) that blocks requests with one or more content objects considered malicious by using one of the [content scanning fields](https://developers.cloudflare.com/waf/detections/malicious-uploads/#content-scanning-fields) in the rule expression.

To use the [`cf.waf.content_scan.has_malicious_obj`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.has_malicious_obj/) field you must [enable content scanning](#enable-waf-content-scanning).

<details>

<summary>

Required API token permissions

</summary>

At least one of the following <a href="https://developers.cloudflare.com/fundamentals/api/reference/permissions/">token permissions</a> is required:

- <code>Zone WAF Write</code>

</details>

Configure the [`cloudflare_ruleset` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/ruleset) resource:

```tf
resource "cloudflare_ruleset" "zone_custom_firewall_malicious_uploads" {
  zone_id     = var.cloudflare_zone_id
  name        = "Phase entry point ruleset for custom rules in my zone"
  description = ""
  kind        = "zone"
  phase       = "http_request_firewall_custom"

  rules = [{
    ref         = "block_malicious_uploads"
    description = "Block requests uploading malicious content objects"
    expression  = "(cf.waf.content_scan.has_malicious_obj and http.request.uri.path eq \"/upload.php\")"
    action      = "block"
  }]
}
```

```tf
resource "cloudflare_ruleset" "zone_custom_firewall_malicious_uploads" {
  zone_id     = var.cloudflare_zone_id
  name        = "Phase entry point ruleset for custom rules in my zone"
  description = ""
  kind        = "zone"
  phase       = "http_request_firewall_custom"

  rules {
    ref         = "block_malicious_uploads"
    description = "Block requests uploading malicious content objects"
    expression  = "(cf.waf.content_scan.has_malicious_obj and http.request.uri.path eq \"/upload.php\")"
    action      = "block"
  }
}
```

## More resources

For additional Terraform configuration examples, refer to [WAF custom rules configuration using Terraform](https://developers.cloudflare.com/terraform/additional-configurations/waf-custom-rules/).
