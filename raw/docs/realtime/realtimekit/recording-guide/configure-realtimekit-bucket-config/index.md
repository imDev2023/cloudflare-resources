---
description: Disable automatic recording uploads to the RealtimeKit R2 bucket using the realtimekit_bucket_config parameter.
title: Disable Upload to RealtimeKit Bucket
image: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-realtimekit-bucket-config/og.png?v=4df89f53b418f527
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# Disable Upload to RealtimeKit Bucket

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-realtimekit-bucket-config/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Once the recording is complete, by default, RealtimeKit uploads all recordings to RealtimeKit's Cloudflare R2 bucket. Additionally, a presigned URL is generated with a 7-day expiry. The recording can be accessed using the `downloadUrl` associated with each recording.

However, RealtimeKit provides users with the flexibility to choose whether or not to upload their recordings to RealtimeKit's R2 bucket. If you wish to disable uploads to RealtimeKit's bucket, you can set the `realtimekit_bucket_config` parameter to false in the [Start Recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/).

For example:

```json
{
	"realtimekit_bucket_config": {
		"enabled": false
	}
}
```

Note

If you haven't specified an external storage configuration and also disabled uploads to RealtimeKit's bucket, then the recording will not be uploaded to any location. It is considered as an invalid recording.

For more information on how to set your external storage configuration, see [Publish Recorded File to Your Cloud Provider](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/custom-cloud-storage/).
