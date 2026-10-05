---
description: Bulk import images from Amazon S3 into Cloudflare Images.
title: Import from S3
image: https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/og.png?v=efe9cbf2c40b3ea3
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/images/llms.txt  
> Use this file to discover all available pages before exploring further.

# Import from S3

Last updated Sep 10, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Import from S3 lets you define one or more sources of images to bulk import from Amazon S3. You can reuse a source to import only new images into your Cloudflare Images account.

Imports skip unsupported objects and files in the source. You can also target paths, define image prefixes, and view error logs.

## Check storage class support

Use Import from S3 for buckets that contain images in non-archival storage classes. Import from S3 skips images in [archival storage classes ↗︎](https://aws.amazon.com/s3/storage-classes/#Archive), which require a separate import.

Import from S3 skips images stored using S3 Glacier tiers (not including Glacier Instant Retrieval) and logs them in the migration log. It also skips and logs images stored using S3 Intelligent Tiering in the Deep Archive tier.
