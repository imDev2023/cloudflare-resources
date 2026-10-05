---
description: Automate Snippet deployments with Terraform.
title: Terraform Support for Snippets
image: https://developers.cloudflare.com/changelog/post/2024-12-11-terraform-snippets/og.png?v=0b586dece24bcf0b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 11, 2024

## Terraform Support for Snippets

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2024-12-11-terraform-snippets/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Now, you can manage [Cloudflare Snippets](https://developers.cloudflare.com/rules/snippets/) with [Terraform](https://developers.cloudflare.com/terraform/). Use infrastructure-as-code to deploy and update Snippet code and rules without manual changes in the dashboard.

Example Terraform configuration:

```tf
resource "cloudflare_snippet" "my_snippet" {
	zone_id  = "<ZONE_ID>"
	name = "my_test_snippet_1"
	main_module = "file1.js"
	files {
		name = "file1.js"
		content = file("file1.js")
	}
}

resource "cloudflare_snippet_rules" "cookie_snippet_rule" {
	zone_id  = "<ZONE_ID>"
	rules {
		enabled = true
		expression = "http.cookie eq \"a=b\""
		description = "Trigger snippet on specific cookie"
		snippet_name = "my_test_snippet_1"
	}
	depends_on = [cloudflare_snippet.my_snippet]
}
```

Learn more in the [Configure Snippets using Terraform](https://developers.cloudflare.com/rules/snippets/create-terraform/) documentation.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2024-12-11-terraform-snippets/#page","headline":"Terraform Support for Snippets","description":"Automate Snippet deployments with Terraform.","url":"https://developers.cloudflare.com/changelog/post/2024-12-11-terraform-snippets/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2024-12-11-terraform-snippets/og.png?v=0b586dece24bcf0b","dateModified":"2024-12-11","datePublished":"2024-12-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
