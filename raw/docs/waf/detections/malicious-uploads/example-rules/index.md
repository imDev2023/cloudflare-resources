---
description: Example rules for handling detected malicious file uploads.
title: Example rules
image: https://developers.cloudflare.com/waf/detections/malicious-uploads/example-rules/og.png?v=4b3ad8e9c93eb313
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/waf/llms.txt  
> Use this file to discover all available pages before exploring further.

# Example rules

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/waf/detections/malicious-uploads/example-rules/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Log requests with an uploaded content object

This [custom rule](https://developers.cloudflare.com/waf/custom-rules/) example logs all requests with at least one uploaded content object:

- **When incoming requests match:**

  | Field | Operator | Value |
  | --- | --- | --- |
  | Has content object | equals | True |

  If you are using the Expression Editor:  
  `(cf.waf.content_scan.has_obj)`
- **Action:** *Log*

## Block requests to URI path with a malicious content object

This custom rule example blocks requests addressed at `/upload.php` that contain at least one uploaded content object considered malicious:

- **When incoming requests match:**

  | Field | Operator | Value |  |
  | --- | --- | --- | --- |
  | Has malicious content object | equals | True | And |
  | URI Path | equals | `/upload.php` |  |

  If you are using the Expression Editor:  
  `(cf.waf.content_scan.has_malicious_obj and http.request.uri.path eq "/upload.php")`
- **Action:** *Block*

## Block requests with non-PDF file uploads

This custom rule example blocks requests addressed at `/upload` with uploaded content objects that are not PDF files:

- **When incoming requests match:**  
  `any(cf.waf.content_scan.obj_types[*] != "application/pdf") and http.request.uri.path eq "/upload"`
- **Action:** *Block*

## Block requests with uploaded files over 500 KB

This custom rule example blocks requests addressed at `/upload` with uploaded content objects over 500 KB (512,000 bytes) in size:

- **When incoming requests match:**  
  `any(cf.waf.content_scan.obj_sizes[*] > 512000) and http.request.uri.path eq "/upload"`
- **Action:** *Block*

## Block requests with uploaded files over the content scanning limit (50 MB)

This custom rule example blocks requests with uploaded content objects over 50 MB in size (the current content scanning limit):

- **When incoming requests match:**  
  `any(cf.waf.content_scan.obj_sizes[*] >= 52428800)`
- **Action:** *Block*

In this example, you must also test for equality because currently any file over 50 MB will be handled internally as if it had a size of 50 MB (52,428,800 bytes). This means that using the `>` (greater than) [comparison operator](https://developers.cloudflare.com/ruleset-engine/rules-language/operators/#comparison-operators) would not work for this particular rule — you should use `>=` (greater than or equal) instead.
