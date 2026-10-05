---
description: FLUX 3 Video is Black Forest Labs' video generation model. It generates video from a text prompt (t2v), animates one or more reference images (i2v), or continues an existing clip (v2v), with synchronized audio, up to fhd resolution, and 5-20 second durations.
title: FLUX 3 Video
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/llms.txt  
> Use this file to discover all available pages before exploring further.

![Black Forest Labs logo](https://developers.cloudflare.com/_astro/blackforestlabs.Ccs-Y4-D.svg)

# FLUX 3 Video

Text-to-Video • Black Forest Labs

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-3-video/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

`black-forest-labs/flux-3-video`

- Third-party

FLUX 3 Video is Black Forest Labs' video generation model. It generates video from a text prompt (t2v), animates one or more reference images (i2v), or continues an existing clip (v2v), with synchronized audio, up to fhd resolution, and 5-20 second durations.

| Model Info | |
| --- | --- |
| Terms and License | [link ↗](https://blackforestlabs.ai/terms-of-service/) |
| More information | [link ↗](https://blackforestlabs.ai/) |
| Pricing | <ul><li>hd$0.17</li><li>fhd$0.29</li><li>v2v hd$0.41</li><li>v2v fhd$0.53</li><li>hd draft$0.06</li><li>v2v hd draft$0.12</li></ul> |

## Usage

```ts
const response = await env.AI.run(
  'black-forest-labs/flux-3-video',
  {
    mode: 't2v',
    prompt:
      'A cozy ramen shop on a rainy Tokyo night, steam rising from the broth. Rain patter and quiet kitchen sounds.',
    resolution: 'hd',
    duration: 5,
    generate_audio: true,
  },
)
console.log(response)
```

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "model": "black-forest-labs/flux-3-video",
  "input": {
    "mode": "t2v",
    "prompt": "A cozy ramen shop on a rainy Tokyo night, steam rising from the broth. Rain patter and quiet kitchen sounds.",
    "resolution": "hd",
    "duration": 5,
    "generate_audio": true
  }
}'
```

```json
{
  "state": "Completed",
  "result": {
    "video": "https://examples.aig.cloudflare.com/black-forest-labs/flux-3-video/text-to-video.mp4"
  },
  "gatewayMetadata": {
    "keySource": "Unified"
  }
}
```

## Parameters

▶Option 1{}

object

▶Option 2{}

object

▶Option 3{}

object

video

`string`format: uriSigned URL to the generated mp4 (24fps, with audio by default). Expires \~2 hours after ready — download promptly.

draft\_cache

`string`Draft-mode cache bundle URL, only present for draft: true requests.

## API Schemas (Raw)

Input [Open](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-3-video/schema-input.json) [Download](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-3-video/schema-input.json)

Output [Open](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-3-video/schema-output.json) [Download](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-3-video/schema-output.json)
