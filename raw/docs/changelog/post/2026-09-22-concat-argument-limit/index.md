---
description: Build richer dynamic values in Rules expressions by combining up to 32 values with concat().
title: concat() now supports up to 32 arguments
image: https://developers.cloudflare.com/changelog/post/2026-09-22-concat-argument-limit/og.png?v=12b2312bd69f0db1
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 22, 2026

## concat() now supports up to 32 arguments

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-22-concat-argument-limit/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The `concat()` function in Cloudflare Rules now accepts up to 32 arguments, increased from 16. This allows you to build richer dynamic values directly in Rules expressions and simplify configurations that combine request data.

A common use case is adding a request header that sends context to your origin. The following Rulesets API request adds a Request Header Transform Rule to an existing `http_request_late_transform` phase ruleset. Its 18-argument expression combines request and network information into one header value:

```bash
curl --request POST \
  "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/rulesets/$RULESET_ID/rules" \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "ref": "add_request_context_header",
    "description": "Add request context for the origin",
    "expression": "true",
    "action": "rewrite",
    "action_parameters": {
      "headers": {
        "X-Request-Context": {
          "operation": "set",
          "expression": "concat(\"ip=\", to_string(ip.src), \";country=\", ip.src.country, \";host=\", http.host, \";method=\", http.request.method, \";path=\", http.request.uri.path, \";query=\", http.request.uri.query, \";ray-id=\", cf.ray_id, \";asn=\", to_string(ip.src.asnum), \";user-agent=\", http.user_agent)"
        }
      }
    }
  }'
```

For more information, refer to the [`concat()` function reference](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#concat) and [HTTP request header modification](https://developers.cloudflare.com/rules/transform/request-header-modification/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-22-concat-argument-limit/#page","headline":"concat() now supports up to 32 arguments","description":"Build richer dynamic values in Rules expressions by combining up to 32 values with concat().","url":"https://developers.cloudflare.com/changelog/post/2026-09-22-concat-argument-limit/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-22-concat-argument-limit/og.png?v=12b2312bd69f0db1","dateModified":"2026-09-22","datePublished":"2026-09-22","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
