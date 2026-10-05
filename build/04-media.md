# Build > Media: Images, Stream, Realtime and MoQ

The developer-docs sidebar's Build > Media dropdown lists three products, as of 2026-10-05: Images (store, transform and deliver images), Stream (upload, encode, store and deliver on-demand and live video, plus Media Transformations for video kept outside Stream) and Realtime (WebRTC infrastructure made of RealtimeKit meeting SDKs, the Realtime SFU and a managed TURN service).
This file also covers MoQ (Media over QUIC relays), which has its own docs section at `/moq/` but is not listed in the sidebar.
Images bills per unique transformation (5,000 free per month, then $0.50 per 1,000) and, for hosted storage, per 100,000 images stored and delivered.
Stream bills only on minutes stored ($5 per 1,000 prepaid) and minutes delivered ($1 per 1,000), with free ingest and encoding.
RealtimeKit bills per participant-minute, while the SFU and TURN bill $0.05 per GB of egress after a shared 1,000 GB monthly free tier.
MoQ relays are free during their beta.
Everything below is taken from the mirrored docs in `raw/docs/` (fetched 2026-10-05) and cites the live URL of each page.
The two large reference surfaces (Realtime's 715 pages and the REST API) are summarised by structure rather than page by page.

## Table of contents

1. [Sidebar map and status at a glance](#1-sidebar-map-and-status-at-a-glance)
2. [Images](#2-images)
3. [Stream](#3-stream)
4. [Realtime (RealtimeKit, SFU, TURN)](#4-realtime-realtimekit-sfu-turn)
5. [MoQ (Media over QUIC)](#5-moq-media-over-quic)
6. [Choosing a live-media product](#6-choosing-a-live-media-product)
7. [REST API surface and GitHub repos](#7-rest-api-surface-and-github-repos)
8. [Build hooks for Web3 projects](#8-build-hooks-for-web3-projects)
9. [Gaps and contradictions](#9-gaps-and-contradictions)

---

## 1. Sidebar map and status at a glance

Source: `raw/nav/home-sidebar.md` (Build > Media lists Images, Stream, Realtime only).

| Product | Docs root | What it is | Status (as of 2026-10-05) | Headline pricing (as of 2026-10-05) | Worker binding |
| --- | --- | --- | --- | --- | --- |
| Images | https://developers.cloudflare.com/images/ | Image transformation of any origin, plus optional managed storage and delivery | Available on Free and Paid plans; no beta label on core features | 5,000 unique transformations free, then $0.50 / 1,000; storage $5 / 100,000 images; delivery $1 / 100,000 images | `images` (`env.IMAGES`) |
| Stream | https://developers.cloudflare.com/stream/ | Video upload, encoding, storage, VOD and live delivery, Media Transformations | GA; LL-HLS is beta; WebRTC (WHIP/WHEP) "going GA" with billing from 2026-10-15; Media Transformations binding is open beta | $5 / 1,000 minutes stored (prepaid), $1 / 1,000 minutes delivered | `stream` (`env.STREAM`), `media` (`env.MEDIA`) |
| Realtime: RealtimeKit | https://developers.cloudflare.com/realtime/realtimekit/ | Meeting SDKs (Core + UI Kit) for web and mobile, recording, transcription | No product-level beta label; breakout rooms (connected meetings) and the Livestream meeting type are beta | $0.002 / A/V participant-minute, $0.0005 / audio-only participant-minute | None (REST + client SDKs) |
| Realtime: SFU | https://developers.cloudflare.com/realtime/sfu/ | Managed anycast Selective Forwarding Unit with an HTTPS Connection API | Changelog records open beta (2024-04-04) and no GA entry; WebSocket adapter is beta | $0.05 / GB egress, first 1,000 GB / month free (shared with TURN) | None (HTTPS API) |
| Realtime: TURN | https://developers.cloudflare.com/realtime/turn/ | Managed anycast TURN/STUN relay | GA since 2024-09-25 | $0.05 / GB egress, shared 1,000 GB free; STUN free | None (HTTPS credential API) |
| MoQ (not in sidebar) | https://developers.cloudflare.com/moq/ | Media over QUIC relays (IETF draft-14 and draft-16) | Beta | Free during beta | None (REST relay API) |

---

## 2. Images

### 2.1 What it is

Images is "a platform for creating scalable and reliable image pipelines" that resizes, optimizes and manipulates images at Cloudflare's edge so you do not store multiple copies per breakpoint or browser ([overview](https://developers.cloudflare.com/images/)).
It is available on Free and Paid plans ([overview](https://developers.cloudflare.com/images/)).
There are two integration paths ([introduction](https://developers.cloudflare.com/images/get-started/introduction/)):

- **Transform remote images** ("bring your own storage"): Cloudflare pulls the original from your origin, R2 or any provider, optimizes it at the edge and caches the result.
- **Hosted images**: upload into Images storage for a fully managed store, optimize and deliver pipeline (Paid plan only).

The introduction page says storing in R2 and using Images only for transformations "is typically the most cost-effective approach", while storing in Images gives a shared delivery domain, predefined variants and automatic cache invalidation on update ([introduction](https://developers.cloudflare.com/images/get-started/introduction/)).
Images and Images Resizing were merged into one product on 2024-01-15 ([changelog](https://developers.cloudflare.com/images/platform/changelog/)).

### 2.2 Key concepts

From [Key concepts](https://developers.cloudflare.com/images/get-started/key-concepts/):

| Term | Meaning |
| --- | --- |
| Remote image | Stored outside Images storage, including in R2 |
| Transformation | A request to optimize a remote image |
| Origin | Where the original lives; Cloudflare caches the original on a miss |
| Hosted image | Stored in Images; copies are generated dynamically |
| Parameter / option | An optimization (for example `width`) and its value (for example `100`) |
| Variant | A named, predefined resize for hosted images (only `width`, `height`, `fit`, `blur`) |

Up to 100 variants can be created; images are served with a `public` variant by default ([create variants](https://developers.cloudflare.com/images/optimization/hosted-images/create-variants/)).
Flexible variants allow arbitrary parameters on hosted-image URLs once enabled ([enable flexible variants](https://developers.cloudflare.com/images/optimization/hosted-images/enable-flexible-variants/)).

### 2.3 The four ways to request an optimization

1. **URL interface on your zone**: `https://<ZONE>/cdn-cgi/image/<OPTIONS>/<SOURCE-IMAGE>` after enabling transformations on the zone under Images > Transformations ([features](https://developers.cloudflare.com/images/optimization/features/), [transformations overview](https://developers.cloudflare.com/images/optimization/transformations/overview/)).
2. **Hosted-image delivery URL**: `https://imagedelivery.net/<ACCOUNT_HASH>/<IMAGE_ID>/<VARIANT_NAME>` on the shared Cloudflare-owned domain, or your own domain via the `/cdn-cgi/imagedelivery/` path ([serve uploaded images](https://developers.cloudflare.com/images/optimization/hosted-images/serve-uploaded-images/), [custom domains](https://developers.cloudflare.com/images/optimization/hosted-images/serve-from-custom-domains/)).
3. **`cf.image` on a Worker `fetch()` subrequest**, which is the same mechanism as the URL interface with programmatic control, available on any zone that hosts a Worker including `*.workers.dev`, billed to the Worker's account ([transform via fetch](https://developers.cloudflare.com/images/optimization/transformations/transform-via-workers/)):

```js
fetch(imageURL, { cf: { image: { fit: "scale-down", width: 800, height: 600 } } });
```

4. **Images binding**, which works on raw bytes from any source (Images, R2, a `fetch()` body, a request body) and lets you control the order of operations ([optimize with Workers](https://developers.cloudflare.com/images/optimization/binding/)).

By default Cloudflare only accepts source images from the same zone; other origins must be allowlisted ([sources](https://developers.cloudflare.com/images/optimization/transformations/sources/)).
Transform Rules can hide the `/cdn-cgi/image/` prefix behind custom paths ([rewrite rules](https://developers.cloudflare.com/images/optimization/transformations/rewrite-rules/)).

### 2.4 Images binding (Workers)

Configuration ([optimize with Workers](https://developers.cloudflare.com/images/optimization/binding/)):

```jsonc
{ "images": { "binding": "IMAGES" } }
```

Optimization methods: an operation starts with `.input(stream)` (image bytes up to 20 MB) or `.text(content, options)`, chains `.transform()` and `.draw()`, and ends with `.output({ format, quality, anim })`, whose result exposes `.response({ headers })`; `.info(stream)` returns `format`, `fileSize`, `width`, `height` and is free ([optimize with Workers](https://developers.cloudflare.com/images/optimization/binding/)).

```js
return (
  await env.IMAGES.input(stream)
    .transform({ width: 800 })
    .output({ format: "image/webp" })
).response({ headers: { "Cache-Control": "public, max-age=3600, stale-while-revalidate=86400" } });
```

- `.output()` requires `format`; there is no default output format.
- `.text()` rasterizes up to 1,000 characters into at most 4096 x 4096 pixels, with a custom `.ttf`, `.otf`, `.woff` or `.woff2` font up to 20 MB.
- Binding responses are not cached automatically, and the docs "strongly recommend" enabling Workers Cache (`"cache": { "enabled": true }`) and setting `Cache-Control`.
- `wrangler dev` uses a low-fidelity offline implementation that supports only `width`, `height`, `rotate` and `format`; `wrangler dev --remote` uses the production implementation; local use is not billed.

Hosted-image management lives under `env.IMAGES.hosted` ([manage hosted images with Workers](https://developers.cloudflare.com/images/storage/binding/)):

| Method | Notes |
| --- | --- |
| `hosted.upload(image, { id, filename, requireSignedURLs, metadata, creator, encoding: 'base64' })` | Returns `ImageMetadata` |
| `hosted.createDirectUpload({ id, metadata, requireSignedURLs, creator, expiresIn })` | `expiresIn` 120 to 21,600 seconds, default 1,800 |
| `hosted.list({ limit, cursor, sortOrder, creator, filter: { metadata } })` | Metadata filter supports `eq`, `in` (up to 10 values), `gt`, `gte`, `lt`, `lte`; at most five conditions per call; dotted paths up to five levels |
| `hosted.image(id).details()`, `.bytes()`, `.update()`, `.delete()` | `update` replaces metadata rather than merging |
| `hosted.image(id).signedUrl({ variant, expiresIn, keyName })` | Signed on Cloudflare's side, so the Worker never handles the signing key |

Hosted operations require a paid Images plan with storage ([manage hosted images with Workers](https://developers.cloudflare.com/images/storage/binding/)).

### 2.5 Optimization parameters

The [features](https://developers.cloudflare.com/images/optimization/features/) page documents these parameters: `anim`, `background`, `blur`, `border`, `brightness`, `compression`, `contrast`, `dpr`, `fit` (`scale-down`, `contain`, `cover`, `crop`, `aspect-crop`, `pad`, `squeeze`, `scale-up`), `flip`, `format`/`f`, `gamma`, `gravity`/`g` (`auto`, `face`, sides, `XxY`), `height`/`h`, `metadata`, `onerror`, `quality`/`q`, `rotate`, `saturation`, `segment`, `sharpen`, `slow-connection-quality`/`scq`, `trim`, `upscale`, `width`/`w` (including `width=auto`) and `zoom`/`face-zoom`.
`segment=foreground` removes the background using the open-source BiRefNet model through Workers AI ([features](https://developers.cloudflare.com/images/optimization/features/#segment)).
Overlays and watermarks use `draw` (URL/fetch) or `.draw()` (binding) with `opacity`, `repeat`, sides and `composite` ([draw overlays](https://developers.cloudflare.com/images/optimization/draw-overlays/)).
C2PA Content Credentials can be preserved for both hosted and remote images ([hosted](https://developers.cloudflare.com/images/optimization/hosted-images/preserve-content-credentials/), [remote](https://developers.cloudflare.com/images/optimization/transformations/preserve-content-credentials/)).
Recommended maximum sizes are 1920 px for desktop, 960 px for tablets and 640 px for phones ([features](https://developers.cloudflare.com/images/optimization/features/#recommended-image-sizes)).

### 2.6 Flows, Polish and framework integration

- **Transformation flows** apply optimization to matching requests without URL or code changes; a provider flow translates Fastly Image Optimizer parameters, and custom flows match on conditions such as file type or path ([flows](https://developers.cloudflare.com/images/optimization/transformations/flows/)).
- Flows are evaluated top to bottom, only the first match runs, they run after redirect rules, and they include loop prevention ([flows](https://developers.cloudflare.com/images/optimization/transformations/flows/)).
- **Polish** is a separate one-click optimizer that keeps the same URLs, strips metadata and applies lossless, lossy or WebP compression; it is not available on the Free plan ([Polish](https://developers.cloudflare.com/images/polish/)).
- Next.js and Nuxt image components can use transformations as a loader ([integrate with frameworks](https://developers.cloudflare.com/images/optimization/transformations/integrate-with-frameworks/)).

### 2.7 Uploads and access control (hosted images)

- Upload methods are the dashboard, the REST API (`/accounts/<ACCOUNT_ID>/images/v1`, by file or [by URL](https://developers.cloudflare.com/images/storage/upload-images/upload-url/)), the Worker binding, and bulk import from Amazon S3 ([methods](https://developers.cloudflare.com/images/storage/upload-images/methods/), [import from S3](https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/)).
- Custom IDs replace the generated UUID in the path ([custom path](https://developers.cloudflare.com/images/storage/upload-images/upload-custom-path/)), but private images do not support custom paths ([serve private images](https://developers.cloudflare.com/images/optimization/hosted-images/serve-private-images/)).
- **Direct Creator Upload** gives end users a one-time `uploadURL` from `POST /accounts/{account_id}/images/v2/direct_upload` without exposing your token; the URL expires after 30 minutes by default and the expiry can be set from two minutes to six hours ahead ([direct creator upload](https://developers.cloudflare.com/images/storage/upload-images/direct-creator-upload/)).
- Webhooks report Direct Creator Upload success or failure ([configure webhooks](https://developers.cloudflare.com/images/storage/upload-images/configure-webhooks/)).
- The batch API uses a batch token on a separate endpoint that does not count toward the global API rate limit, with 200 requests per second per token ([batch API](https://developers.cloudflare.com/images/storage/upload-images/images-batch/)).
- Private images need signed URL tokens generated server-side with a key from Hosted Images > Keys, and the docs say to keep the key in a Worker secret ([serve private images](https://developers.cloudflare.com/images/optimization/hosted-images/serve-private-images/)).
- WAF, Bot Management and Rate Limiting are the recommended protections against abuse of optimization endpoints ([security](https://developers.cloudflare.com/images/reference/security/)).

### 2.8 Caching

Optimized images follow the original's caching rules with a minimum cache time of one hour, and `must-revalidate` plus `Etag` are recommended for frequent updates ([features: caching](https://developers.cloudflare.com/images/optimization/features/#caching)).
Optimized variants cannot be purged individually and `/cdn-cgi/` URLs cannot be purged, but purging the original URL purges all its optimized versions ([features: caching](https://developers.cloudflare.com/images/optimization/features/#caching)).

### 2.9 Limits and formats (as of 2026-10-05)

From [Limits and formats](https://developers.cloudflare.com/images/get-started/limits/):

| Attribute | Remote (transformed) | Hosted (uploaded) |
| --- | --- | --- |
| File size | 100 MB | 10 MB |
| Area (non-animated) | 100 MP | 100 MP |
| Area (animated GIF/WebP, sum of all frames) | 100 MP; above 50 MP delivered untransformed | 100 MP; above 50 MP delivered untransformed |
| Max dimension (non-WebP/AVIF) | 12,000 px | 12,000 px |
| Max dimension (AVIF) | 1,200 px | 1,200 px |
| Metadata | n/a | 1,024 bytes |
| Binding `.input()` | 20 MB | 20 MB |

- Input formats are PNG, JPEG, GIF, WebP (including animations), SVG, HEIC and AVIF, with AVIF input only on Enterprise.
- Output formats are PNG, JPEG, GIF, WebP, SVG and AVIF, and AVIF falls back to WebP or JPEG when encoding would be too slow.
- SVGs are never resized and are sanitized with the open-source `svg-hush`, which strips scripting, hyperlinks and cross-origin references.
- Progressive JPEG falls back to baseline below 50x50 or above 3000x3000 output.

### 2.10 Pricing (as of 2026-10-05)

From [Pricing](https://developers.cloudflare.com/images/pricing/):

| Metric | Free plan | Paid plan |
| --- | --- | --- |
| Images Transformed (unique per calendar month) | 5,000; new transformations beyond that return error `9422`, no charge | First 5,000 included, then $0.50 / 1,000 |
| Images Stored | Not available | $5 / 100,000 images / month (prepaid increments) |
| Images Delivered | Not available | $1 / 100,000 images / month |

- A unique transformation is one source image plus one parameter set per calendar month; repeats in the same month are not billed again, and `format=auto` serving AVIF to some users and WebP to others counts once.
- Hosted images optimized via the delivery URL count as Images Delivered, but hosted images optimized via the binding count as Images Transformed.
- Variants do not count toward Images Stored.
- The pricing page's worked example (5,000 images of 5 MB in R2 served in five sizes) totals $2.72 per month, using R2 at $0.015 / GB-month, which matches the [R2 pricing page](https://developers.cloudflare.com/r2/pricing/).
- Media Transformations (video) share the same subscription and the same $0.50 / 1,000 rate ([Stream pricing](https://developers.cloudflare.com/stream/pricing/)).

### 2.11 Most useful Images pages

- Overview: https://developers.cloudflare.com/images/
- Introduction (Images vs R2): https://developers.cloudflare.com/images/get-started/introduction/
- Limits and formats: https://developers.cloudflare.com/images/get-started/limits/
- Pricing: https://developers.cloudflare.com/images/pricing/
- Features (all parameters): https://developers.cloudflare.com/images/optimization/features/
- Binding (optimize): https://developers.cloudflare.com/images/optimization/binding/
- Binding (hosted storage): https://developers.cloudflare.com/images/storage/binding/
- Direct Creator Upload: https://developers.cloudflare.com/images/storage/upload-images/direct-creator-upload/
- Tutorial, transform user uploads before R2: https://developers.cloudflare.com/images/tutorials/optimize-user-uploaded-image/
- Example, watermark from KV on an R2 image: https://developers.cloudflare.com/images/examples/watermark-from-kv/
- REST API: https://developers.cloudflare.com/api/resources/images/subresources/v1/methods/list/

The Images llms.txt lists 64 pages, grouped as overview, demos, pricing, Polish (5), examples (3), get-started (3), optimization (23), platform changelog, reference (security, troubleshooting), storage (15) and tutorials (2).

---

## 3. Stream

### 3.1 What it is

Stream is "serverless live and on-demand video streaming" that lets you or your users upload, store, encode and deliver video with one API ([overview](https://developers.cloudflare.com/stream/)).
It encodes to H.264 with adaptive bitrate from 360p to 1080p ([overview](https://developers.cloudflare.com/stream/)).
HDR uploads are re-encoded and delivered as SDR ([FAQ](https://developers.cloudflare.com/stream/faq/)).
Videos can be embedded on any domain, including domains not on Cloudflare ([FAQ](https://developers.cloudflare.com/stream/faq/)).
Since 2026-04-13 on-demand HLS manifests reference fragmented MP4 segments instead of MPEG-TS, and old segment references may 404 after 2026-05-13 ([changelog](https://developers.cloudflare.com/stream/changelog/)).

### 3.2 Uploading

From [Upload videos](https://developers.cloudflare.com/stream/uploading-videos/) and [Get started](https://developers.cloudflare.com/stream/get-started/):

- Methods are the dashboard, upload from a link (`POST /accounts/<ACCOUNT_ID>/stream/copy`), basic file upload (under 200 MB), resumable tus uploads for large files, and Direct Creator Uploads.
- Files must be under 30 GB.
- Accepted containers include MP4, MKV, MOV, AVI, FLV, MPEG-2 TS/PS, MXF, LXF, GXF, 3GP, WebM, MPG and QuickTime.
- Stream re-encodes for a maximum of 90 FPS playback.
- tus chunks can be at most 209,715,200 bytes ([resumable uploads](https://developers.cloudflare.com/stream/uploading-videos/resumable-uploads/)).
- Direct Creator Uploads require a `maxDurationSeconds` reservation that is deducted from storage until the upload is processed, and basic (non-tus) creator uploads are limited to 200 MB ([direct creator uploads](https://developers.cloudflare.com/stream/uploading-videos/direct-creator-uploads/)).
- Up to 120 videos can be queued or encoding at once by default ([FAQ](https://developers.cloudflare.com/stream/faq/)).
- Poll until `readyToStream` is `true`, or use webhooks ([get started](https://developers.cloudflare.com/stream/get-started/)).
- Only one webhook subscription is allowed per account, and webhooks cannot target localhost ([webhooks](https://developers.cloudflare.com/stream/manage-video-library/using-webhooks/)).
- The original input file cannot be downloaded, but encoded MP4 or M4A downloads can be generated ([FAQ](https://developers.cloudflare.com/stream/faq/), [download videos](https://developers.cloudflare.com/stream/viewing-videos/download-videos/)).

### 3.3 Playback

- The Stream Player is an iframe at `https://customer-<CODE>.cloudflarestream.com/<VIDEO_UID>/iframe` with a JavaScript Player API ([Stream Player](https://developers.cloudflare.com/stream/viewing-videos/using-the-stream-player/)).
- Any HLS or DASH player works, with documented examples for hls.js, dash.js, Shaka, Video.js, Vidstack, AVPlayer and ExoPlayer ([use your own player](https://developers.cloudflare.com/stream/viewing-videos/using-own-player/), [examples](https://developers.cloudflare.com/stream/examples/)).
- Thumbnails, including animated GIF thumbnails, are generated from the video ([thumbnails](https://developers.cloudflare.com/stream/viewing-videos/displaying-thumbnails/)).
- For a strict CSP, add `videodelivery.net` and `*.cloudflarestream.com`, or your `customer-<CODE>` subdomain ([FAQ](https://developers.cloudflare.com/stream/faq/)).

### 3.4 Access control

- Videos are public by video ID unless `requireSignedURLs` is set ([secure your Stream](https://developers.cloudflare.com/stream/viewing-videos/securing-your-stream/)).
- Tokens can come from the `/token` endpoint (for under 1,000 tokens per day; valid one hour; rate-limited; not for Live WebRTC), from your own signing key (recommended for volume and required for Live WebRTC), or from the Workers binding's `generateToken()` ([secure your Stream](https://developers.cloudflare.com/stream/viewing-videos/securing-your-stream/)).
- `allowedOrigins` restricts which sites can embed a video ([Workers binding](https://developers.cloudflare.com/stream/manage-video-library/bindings/)).

### 3.5 Live streaming

From [Stream live video](https://developers.cloudflare.com/stream/stream-live/) and [Start a live stream](https://developers.cloudflare.com/stream/stream-live/start-stream-live/):

- Create a live input (`POST /accounts/<ACCOUNT_ID>/stream/live_inputs`) and broadcast to it with RTMPS (`rtmps://live.cloudflare.com:443/live/` plus stream key) or SRT (caller mode only).
- Stream encodes the live feed at multiple resolutions and adapts its bitrate ladder to the bitrate it actually receives.
- Inputs require H.264 video, AAC audio and closed GOPs; a GOP of 2 to 8 seconds and a bitrate well under 12 Mbps are recommended.
- Recordings are available within 60 seconds after a broadcast ends, and recordings longer than seven days are truncated to seven days.
- Watermarks cannot be used with live video.
- Live inputs can be disabled to reject or terminate broadcasts, and custom RTMPS ingest domains are supported ([custom ingest domains](https://developers.cloudflare.com/stream/stream-live/custom-domains/)).
- **Low-Latency HLS** is beta (`preferLowLatency: true`); B-frames must be 0 and a GOP of 2 to 4 seconds is advised.
- **DVR** lets viewers rewind live broadcasts; manifests cap at 7,200 segments and performance may degrade past three hours ([DVR](https://developers.cloudflare.com/stream/stream-live/dvr-for-live/)).
- **Live Instant Clipping** makes shareable clips of up to 60 seconds, with previews up to 5 minutes, and charges no extra storage ([live instant clipping](https://developers.cloudflare.com/stream/stream-live/live-instant-clipping/)).
- **Simulcast** forwards a live input to up to 50 concurrent destinations such as YouTube, Twitch or X ([simulcast](https://developers.cloudflare.com/stream/stream-live/simulcasting/)).
- Live webhooks cover connect, disconnect and error events ([live webhooks](https://developers.cloudflare.com/stream/stream-live/webhooks/)).
- Live viewer counts are available from a views endpoint ([live viewer counts](https://developers.cloudflare.com/stream/getting-analytics/live-viewer-count/)).
- Unlimited live inputs have been allowed since 2022-11-01 ([changelog](https://developers.cloudflare.com/stream/changelog/)).

### 3.6 Ultra-low-latency WebRTC (WHIP/WHEP)

From [Ultra-low Latency with WebRTC](https://developers.cloudflare.com/stream/webrtc-beta/):

- Each live input exposes `webRTC.url` (WHIP publish URL, which is a credential) and `webRTCPlayback.url` (WHEP play URL).
- Viewers see under 500 ms of latency, and there are "no fixed limits on the number of concurrent viewers".
- Tested publishers are OBS 31.0+, Larix Broadcaster and FFmpeg 8.1+, plus the `whip-whep` and `@eyevinn/whip-web-client` libraries.
- Tested players are the Stream Player, `whip-whep`, `@eyevinn/webrtc-player` and `react-native-whip-whep`.
- Broadcast codecs are VP9, VP8 and H.264 Constrained Baseline 3.1 (`42e01f`).
- WHIP and WHEP must be used together, and recording, live HLS playback, simulcast, viewer counts and broadcast metrics are not supported.
- The banner reads "Stream Live WebRTC is going GA: Billing for WebRTC delivery will begin on October 15th, 2026", and pricing is $1 per 1,000 minutes delivered with no storage consumed.
- Since 2025-03-13 Stream WHIP/WHEP has been migrated to an implementation powered by Cloudflare Realtime ([changelog](https://developers.cloudflare.com/stream/changelog/)).
- A no-dependency browser tutorial covers both broadcast and playback ([first WebRTC broadcast](https://developers.cloudflare.com/stream/examples/browser-based-webrtc/)).

### 3.7 Editing and enrichment

- Captions can be AI-generated or uploaded as WebVTT, with one file per language and 10 MB per file ([captions](https://developers.cloudflare.com/stream/edit-videos/adding-captions/)).
- Generated captions moved to open beta on 2024-06-20 ([changelog](https://developers.cloudflare.com/stream/changelog/)).
- Other editing features are additional audio tracks, watermark profiles, player enhancements (logo, share link) and clipping by start and end time ([edit videos](https://developers.cloudflare.com/stream/edit-videos/video-clipping/)).
- Creator IDs associate videos with your own user accounts ([manage creators](https://developers.cloudflare.com/stream/manage-video-library/creator-id/)).
- Scheduled deletion is supported ([changelog](https://developers.cloudflare.com/stream/changelog/)).
- Server-side analytics are available through the dashboard and the GraphQL Analytics API ([analytics](https://developers.cloudflare.com/stream/getting-analytics/)).

### 3.8 Stream Workers binding

Configuration and use ([bind to Workers API](https://developers.cloudflare.com/stream/manage-video-library/bindings/)):

```jsonc
{ "stream": { "binding": "STREAM" } }
```

```ts
const video = await env.STREAM.upload("https://example.com/video.mp4", { meta: { name: "Launch trailer" } });
```

- Binding-level methods are `upload(url, params)`, `createDirectUpload({ maxDurationSeconds, expiry, creator, meta, allowedOrigins, requireSignedURLs, ... })` (up to 200 MB), and `videos.list({ limit, before, after, ... })`.
- `env.STREAM.video(id)` methods are `details()`, `update()`, `delete()`, `generateToken()`, `downloads.generate|get|delete`, and `captions.upload|generate`.
- Watermark profiles can also be managed from the binding.
- Errors are typed: `BadRequestError`, `QuotaReachedError`, `MaxFileSizeError`, `RateLimitedError`, `AlreadyUploadedError`, `InternalError`.

### 3.9 Media Transformations (video outside Stream)

From [Transform videos](https://developers.cloudflare.com/stream/transform-videos/) and [Bind to Workers API](https://developers.cloudflare.com/stream/transform-videos/bindings/):

- The URL form is `https://<zone>/cdn-cgi/media/<OPTIONS>/<SOURCE-VIDEO>`, and zones with Image Transformations enabled can also use it.
- `mode` is `video` (H.264/AAC MP4), `frame` (JPG or PNG), `spritesheet` (JPEG) or `audio` (M4A).
- `time` ranges from 0 to 10 minutes and `duration` from 1 to 60 seconds; `width` and `height` range from 10 to 2,000 px; `fit` is `contain`, `scale-down` or `cover`; other options are `audio` and `filename`.
- Inputs must be under 100 MB and 10 minutes, and should be MP4 (H.264 with AAC or MP3) or animated GIF; the origin must support HEAD and range requests.
- Media Transformations are incompatible with BYOIP.
- The `media` binding (`env.MEDIA.input(stream).transform({...}).output({ mode })`) is in public open beta and is not billed during the beta; after the beta, binding calls will be billed per operation rather than per unique transformation.
- URL-based billing counts a frame as 1 transformation and video or audio output as 1 transformation per output second, at $0.50 / 1,000 with 5,000 free per month shared with Images.

```ts
const out = await env.MEDIA.input(r2Object.body).transform({ width: 480, height: 480, fit: "cover" }).output({ mode: "frame", time: "2s" });
```

### 3.10 Pricing (as of 2026-10-05)

From [Stream pricing](https://developers.cloudflare.com/stream/pricing/):

| Dimension | Price | Notes |
| --- | --- | --- |
| Minutes stored | $5 / 1,000 minutes / month, prepaid | Rounded up to the second of duration regardless of file size; includes live recordings and outstanding `maxDurationSeconds` reservations |
| Minutes delivered | $1 / 1,000 minutes, postpaid | Counts Stream Player, HLS/DASH, WHEP, MP4 downloads and simulcast outputs; counted per segment request, so preloading is billable |
| Ingest, encoding, egress bandwidth | Free | Encoded quality levels and MP4 downloads do not consume storage |

- When storage runs out, new uploads and new live streams are blocked; Enterprise customers may continue uploading.
- Videos are removed if a lapsed subscription is not renewed within 30 days ([FAQ](https://developers.cloudflare.com/stream/faq/)).
- Example from the page: two viewers each watching 30 minutes cost 60 minutes delivered ($0.06).

### 3.11 Most useful Stream pages

- Overview: https://developers.cloudflare.com/stream/
- Get started: https://developers.cloudflare.com/stream/get-started/
- Pricing: https://developers.cloudflare.com/stream/pricing/
- FAQ (limits): https://developers.cloudflare.com/stream/faq/
- Direct creator uploads: https://developers.cloudflare.com/stream/uploading-videos/direct-creator-uploads/
- Start a live stream: https://developers.cloudflare.com/stream/stream-live/start-stream-live/
- WebRTC WHIP/WHEP: https://developers.cloudflare.com/stream/webrtc-beta/
- Secure your Stream: https://developers.cloudflare.com/stream/viewing-videos/securing-your-stream/
- Workers binding: https://developers.cloudflare.com/stream/manage-video-library/bindings/
- Media Transformations: https://developers.cloudflare.com/stream/transform-videos/
- REST API: https://developers.cloudflare.com/api/resources/stream/methods/list/

The Stream llms.txt lists 65 pages: overview, get started, upload (6), live (12, including the live API link), transform (4), manage (5), analytics (3), WebRTC (1), examples (14), API reference, changelog, FAQ, pricing, edit-videos (5) and viewing-videos (9).

---

## 4. Realtime (RealtimeKit, SFU, TURN)

### 4.1 What it is and how the pieces relate

Realtime is for "live applications where people, AI systems, and devices communicate in real time over Cloudflare's global network" ([Realtime overview](https://developers.cloudflare.com/realtime/)).
It has three parts ([Realtime overview](https://developers.cloudflare.com/realtime/)):

- **RealtimeKit**: prebuilt meeting UI and SDKs for web and mobile in which Cloudflare handles signaling and media routing, with managed recording and transcription.
- **Realtime SFU**: a managed Selective Forwarding Unit driven by an HTTPS API, where your app handles signaling, permissions, session state and track discovery.
- **TURN**: a managed anycast relay for when NATs or firewalls block a direct WebRTC path; RealtimeKit configures it for you, the SFU includes access to it, and it can also be used with your own SFU or peer-to-peer app.

The overview's guidance for webinars is to use RealtimeKit when attendees join as participants (speak, appear on camera, move to breakout rooms), and Stream Live when a few presenters broadcast to a large watch-only audience ([Realtime overview](https://developers.cloudflare.com/realtime/)).
RealtimeKit's Core SDK is "built on top of Realtime SFU" ([SDK selection](https://developers.cloudflare.com/realtime/realtimekit/sdk-selection/)).
The product was formerly called Calls, and the account API still uses `calls` paths (for example `/accounts/{account_id}/calls/apps` and `/calls/turn_keys` in `raw/api/endpoints.tsv`).

### 4.2 How the 715 pages are organised (as of 2026-10-05)

Page counts come from `raw/docs/realtime/**/index.md`; `realtime/llms.txt` has four sections (Overview, RealtimeKit, Realtime SFU, TURN Service).

| Subtree | Pages | What is in it |
| --- | --- | --- |
| `/realtime/` (overview) | 1 | Product chooser and FAQ |
| `/realtime/realtimekit/ui-kit/api-reference/` | 577 | Generated component reference: Web Components 137 (`rtk-*` elements), React 137 (`Rtk*`), Angular 137, React Native 76, Android 50, iOS 39, plus 1 index |
| `/realtime/realtimekit/ui-kit/` (guides) | 11 | Component library, branding and design system, custom header and control bar, state management, locale, add-ons, breakout rooms, build-your-own-UI |
| `/realtime/realtimekit/core/api-reference/` | 20 | Index plus 19 Core SDK classes: `RealtimeKitClient`, `RTKSelf`, `RTKSelfMedia`, `RTKParticipant(s)`, `RTKChat`, `RTKPolls`, `RTKPlugin(s)`, `RTKRecording`, `RTKLivestream`, `RTKStage`, `RTKStore`, `RTKAi`, `RTKConnectedMeetings`, `RTKMeta`, `RTKPip`, `RTKPermissionsPreset`, `RTKThemePreset` |
| `/realtime/realtimekit/core/` (guides) | 20 | Index, meeting object, local and remote participants, events, PiP, chat, polls, plugins, stage management, waiting room, breakout rooms, active speakers, video effects, iOS screen share, media acquisition, error codes, end a session |
| `/realtime/realtimekit/recording-guide/` | 13 | Start, stop, monitor, codecs, audio, watermark, own-cloud upload, track recording, recording SDK apps, interactive recording, config precedence |
| `/realtime/realtimekit/release-notes/` | 13 | Per-SDK release notes and a notice board |
| `/realtime/realtimekit/` (other) | 27 | Index, quickstart, concepts (5), SDK selection, pricing, limits, FAQ, data retention, webhooks, webinar, audio calls, broadcast APIs, collaborative stores, AI (3), custom plugins (2), best practices (2), network allowlist, legal (2) |
| `/realtime/sfu/` | 25 | Overview, get started (2), concepts (4), API, features (5), examples (5), observability (2), platform (limits, pricing, changelog), best practices |
| `/realtime/turn/` | 8 | Overview, what is TURN, generate credentials, FAQ, custom domains, replacing existing, analytics, RFC matrix |
| **Total** | **715** | |

In practice the 577 UI Kit reference pages describe the same roughly 137 components once per framework, so a builder needs one framework's set.

### 4.3 RealtimeKit

**Concepts** ([concepts](https://developers.cloudflare.com/realtime/realtimekit/concepts/), [meeting](https://developers.cloudflare.com/realtime/realtimekit/concepts/meeting/), [participant](https://developers.cloudflare.com/realtime/realtimekit/concepts/participant/), [preset](https://developers.cloudflare.com/realtime/realtimekit/concepts/preset/)):

| Concept | Meaning |
| --- | --- |
| App | Workspace or namespace for meetings, participants, presets and recordings; the docs suggest one App per environment |
| Meeting | A reusable virtual room with no start or end time |
| Session | A live instance of a meeting, created when the first participant joins and ended shortly after the last leaves; one active session per meeting; billing applies only during active sessions |
| Participant | A user added to a meeting via the Add Participant API, which returns an `authToken` |
| Preset | App-level reusable role: meeting type (Video, Audio/Voice, Webinar, Livestream beta), permissions and UI theme |
| Peer | One connection of a participant; each rejoin or reload creates a new peer ID ([FAQ](https://developers.cloudflare.com/realtime/realtimekit/faq/)) |

**Auth model** ([participant](https://developers.cloudflare.com/realtime/realtimekit/concepts/participant/), [FAQ](https://developers.cloudflare.com/realtime/realtimekit/faq/)):

- Participant tokens are JWTs scoped by `meetingId` and `participantId`, valid for 100 days, and their lifetime cannot be configured.
- Refreshing a token does not invalidate older tokens.
- Revocation is done by kicking the participant from the active session and then deleting the participant.
- Setting a meeting to `INACTIVE` blocks joins, even with valid tokens.
- `custom_participant_id` maps to your own user ID, and the docs say it should not contain PII.
- Scheduling is your backend's job, because meetings have no start or end time.
- The Cloudflare API token (permission Realtime > Realtime Admin) stays on the backend.

**Server flow** ([meeting](https://developers.cloudflare.com/realtime/realtimekit/concepts/meeting/)):

```bash
curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/realtime/kit/{APP_ID}/meetings \
  --request POST --header "Authorization: Bearer <CLOUDFLARE_API_TOKEN>" \
  --header "Content-Type: application/json" --data '{ "title": "My meeting" }'
```

Then call Add Participant with a preset name and pass the returned token to the client.

**Client SDKs** ([SDK selection](https://developers.cloudflare.com/realtime/realtimekit/sdk-selection/)):

| Platform | Core SDK | UI Kit |
| --- | --- | --- |
| Web Components (HTML, Vue, Svelte) | `@cloudflare/realtimekit` | `@cloudflare/realtimekit-ui` |
| React | `@cloudflare/realtimekit-react` | `@cloudflare/realtimekit-react-ui` |
| Angular | `@cloudflare/realtimekit` | `@cloudflare/realtimekit-angular-ui` |
| Android | `com.cloudflare.realtimekit:core` | `com.cloudflare.realtimekit:ui-android` |
| iOS | `RealtimeKit` (github.com/dyte-in/RealtimeKitCoreiOS) | `RealtimeKitUI` (github.com/dyte-in/RealtimeKitUI) |
| React Native | `@cloudflare/realtimekit-react-native` | `@cloudflare/realtimekit-react-native-ui` |

The UI Kit includes the Core SDK, and the SDK selection page estimates under 2 hours to ship with the UI Kit versus 5 to 6 days with the Core SDK alone.
Core SDK initialisation in plain JavaScript ([Core SDK](https://developers.cloudflare.com/realtime/realtimekit/core/)):

```js
const meeting = await RealtimeKitClient.init({ authToken, defaults: { audio: true, video: true } });
await meeting.join();
```

Latest SDK releases, as of 2026-10-05 ([release notes](https://developers.cloudflare.com/realtime/realtimekit/release-notes/)): Web Core and Web UI Kit 2.0.2 (2026-08-24), Android and iOS Core and UI Kit 3.2.0 (2026-09-16), React Native Core and UI Kit 2.0.0 (2026-07-08), Recording SDK 0.0.3 (2026-07-28), and Flutter Core and UI Kit (2026-08-07).
The notice board says Web Core 1.2.0+ removed the legacy media engine, so organisations created before 2025-03-01 may need a migration to keep recording working, and Web Core below 1.2.0 cannot join in Firefox 144+ ([notice board](https://developers.cloudflare.com/realtime/realtimekit/release-notes/notice-board/)).

**Features**:

- Stage management lets on-stage participants publish while off-stage participants use chat, polls and plugins and can request the stage ([meeting](https://developers.cloudflare.com/realtime/realtimekit/concepts/meeting/#stage)).
- Waiting rooms support admit-by-host, auto-admit when a privileged user joins, and bulk admit ([meeting](https://developers.cloudflare.com/realtime/realtimekit/concepts/meeting/#waiting-room)).
- Breakout rooms (connected meetings) are beta ([UI Kit breakout rooms](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/breakout-rooms/)).
- Webinars use the default `webinar_presenter` and `webinar_viewer` presets, with `stage_access` set to `ALLOWED`, `CAN_REQUEST` or `NOT_ALLOWED` ([webinar](https://developers.cloudflare.com/realtime/realtimekit/webinar/)).
- Audio calls use a `Voice` preset, and those participants bill at the audio-only rate ([audio calls](https://developers.cloudflare.com/realtime/realtimekit/audio-calls/)).
- `participants.broadcastMessage(type, payload, target?)` sends custom signaling messages to everyone, to chosen participant IDs, to preset names or to other meetings ([broadcast APIs](https://developers.cloudflare.com/realtime/realtimekit/broadcast-apis/)).
- Collaborative stores are realtime key-value stores (`meeting.stores.create('name')`, then `set`, `update`, `delete`) that last for the session ([collaborative stores](https://developers.cloudflare.com/realtime/realtimekit/collaborative-stores/)).
- Plugins are browser-based in-meeting apps, with built-in Whiteboard and Document Sharing ([custom plugins](https://developers.cloudflare.com/realtime/realtimekit/custom-plugins/)).
- Recording comes in two modes, composite (a bot joins, records in H.264 or VP8, and keeps the file in RealtimeKit's R2 bucket for 7 days) and per-participant track recording ([recording guide](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/)).
- Recordings can be uploaded to your own R2, S3, Azure, DigitalOcean or GCS bucket ([custom cloud storage](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/custom-cloud-storage/)).
- Custom recording layouts can be deployed as an app on Workers ([recording SDK apps](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/create-record-app-using-sdks/)).
- Real-time transcription runs Deepgram Nova-3 and post-meeting transcription runs Whisper Large v3 Turbo, both on Workers AI, enabled per preset with `permissions.transcription_enabled` and configured with `ai_config.transcription` (`language`, `keywords`, `profanity_filter`) ([transcription](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/)).
- Summaries are enabled with `summarize_on_end: true`, take a 150 to 1,000 word limit, and accept types `general`, `team_meeting`, `daily_standup`, `one_on_one_meeting`, `sales_call`, `client_check_in`, `interview`, `lecture` and `code_review` ([summary](https://developers.cloudflare.com/realtime/realtimekit/ai/summary/)).
- Webhooks are signed with the `rtk-signature` header and are subscription-only, with events such as `meeting.participantJoined`, `recording.statusUpdate` and `meeting.summary` ([webhooks](https://developers.cloudflare.com/realtime/realtimekit/webhooks/)).

**Limits** (as of 2026-10-05, [limits](https://developers.cloudflare.com/realtime/realtimekit/limits/)):

| Scope | Limit |
| --- | --- |
| All RealtimeKit REST APIs | 3,500 requests per 5 minutes (counts toward the global Cloudflare API limit) |
| Recording APIs | 1,000 requests per 50 seconds |
| Collaborative store writes, `broadcastMessage()` | 5 per second per participant |
| `sendTextMessage()`, `sendMessage()` | 180 per minute per participant |
| `sendImageMessage()`, `sendFileMessage()` | 20 per minute per participant |
| `getConnectedMeetings()` | 60 per minute |
| `getAllJoinedPeers()` | 10 per minute |
| `updatePermissions()` | 1,000 per minute |

The limits page gives no maximum participants per meeting.

**Data retention** (as of 2026-10-05, [data retention](https://developers.cloudflare.com/realtime/realtimekit/data-retention/)): meeting and participant records and `persist_chat` chat are kept indefinitely; other chat, composite recordings, track recordings and transcripts are kept 7 days; call analytics 6 months; webhook logs 1 month.

**Pricing** (as of 2026-10-05, [pricing](https://developers.cloudflare.com/realtime/realtimekit/pricing/)):

| Item | Price |
| --- | --- |
| Audio/video participant | $0.002 / minute |
| Audio-only participant | $0.0005 / minute |
| Export (recording, RTMP or HLS streaming) | $0.010 / minute |
| Export, audio only | $0.003 / minute |
| Export (raw RTP) into R2 | $0.0005 / minute |
| Real-time transcription | Standard Workers AI model pricing |

Participants rejected for invalid tokens are not billed ([participant](https://developers.cloudflare.com/realtime/realtimekit/concepts/participant/)).

### 4.4 Realtime SFU

**Model** ([sessions and tracks](https://developers.cloudflare.com/realtime/sfu/concepts/sessions-tracks/), [architecture](https://developers.cloudflare.com/realtime/sfu/concepts/architecture/)):

- An SFU **application** has an App ID and an App Secret, and the secret stays on the backend (in Workers, as a secret).
- A **session** is one WebRTC PeerConnection to the SFU; `POST /sessions/new` returns a `sessionId` but does not connect, and an unconnected session can expire and later return HTTP `410`.
- **Tracks** are published with `tracks/new` and `location: "local"` plus a `trackName`, and subscribed with `location: "remote"` plus the publisher's `sessionId` and `trackName`.
- **DataChannels** carry messages; one subscriber can get reply access (`canReply`), and channels support `ordered`, `maxRetransmits`, `maxPacketLifeTime` and `waitForAck` ([DataChannels](https://developers.cloudflare.com/realtime/sfu/features/datachannels/), [changelog](https://developers.cloudflare.com/realtime/sfu/platform/changelog/)).
- Rooms, presence and discovery are application state, and the SFU "does not supply a room-presence protocol"; the quickstart keeps room state in one Durable Object per room.
- There are no SFU regions to choose; the SFU runs on Cloudflare's anycast network.

**Connection API** ([API](https://developers.cloudflare.com/realtime/sfu/api/)): the base URL is `https://rtc.live.cloudflare.com/v1`, requests send `Authorization: Bearer <APP_SECRET>`, and the OpenAPI schema is `realtime-api-2024-05-21.yaml`.

| Operation | Method and path |
| --- | --- |
| Create session | `POST /apps/{appId}/sessions/new` |
| Publish or subscribe tracks | `POST /apps/{appId}/sessions/{sessionId}/tracks/new` |
| Update tracks | `PUT .../tracks/update` |
| Renegotiate | `PUT .../renegotiate` |
| Close tracks | `PUT .../tracks/close` |
| Inspect session | `GET /apps/{appId}/sessions/{sessionId}` |
| DataChannels | `POST .../datachannels/establish`, `POST .../datachannels/new`, `PUT .../datachannels/update`, `PUT .../datachannels/close` |
| WebSocket adapters | `POST /apps/{appId}/adapters/websocket/new`, `POST .../adapters/websocket/close` |

Responses can partially succeed, so check every per-track result, and serialize mutations per session ([API](https://developers.cloudflare.com/realtime/sfu/api/)).

**Features**:

- Simulcast lets subscribers pick a quality layer ([simulcast](https://developers.cloudflare.com/realtime/sfu/features/simulcast/)).
- The **WebSocket adapter** (beta) moves 48 kHz stereo PCM audio into the SFU (published as Opus), and moves PCM audio or JPEG video (1 FPS by default) out to a public `wss://` endpoint; each adapter is one-directional and video ingest is not supported ([WebSocket adapter](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/)).
- Worked examples cover an ESP32 device ("Pocket Radio"), cloud gaming from a Container, AI audio with Workers AI, and a custom video room ([examples](https://developers.cloudflare.com/realtime/sfu/examples/)).
- The quickstart clones `cloudflare/realtime-examples/video-room` (Worker plus Durable Object), says the example is experimental, and requires Cloudflare Access when deployed ([get started](https://developers.cloudflare.com/realtime/sfu/get-started/)).

**Limits** (as of 2026-10-05, [limits](https://developers.cloudflare.com/realtime/sfu/platform/limits/)):

- API requests are limited to 50 per second per session (not per app).
- One request can add up to 64 tracks, and there is no fixed per-session track cap.
- One request can create or close 1 to 4 WebSocket adapters, and WebSocket audio ingest messages are limited to 32 KB.
- A track with no incoming packets for 30 seconds is garbage-collected.
- A disconnected session has a 30-second reuse window.
- Operations wait up to 5 seconds for transport connectivity.
- Video codecs are H.264, H.265, VP8, VP9 and AV1; audio codecs are Opus and G.711 A-law and µ-law.

**Pricing** (as of 2026-10-05, [pricing](https://developers.cloudflare.com/realtime/sfu/platform/pricing/)):

- Egress from Cloudflare costs $0.05 per GB, and the first 1,000 GB per month is free and shared with TURN.
- Ingress is free, even when nothing subscribes to a publication.
- Traffic sent to WebSocket adapters bills as egress, while audio ingested from WebSocket is free.

### 4.5 TURN

From [TURN](https://developers.cloudflare.com/realtime/turn/), [generate credentials](https://developers.cloudflare.com/realtime/turn/generate-credentials/), [FAQ](https://developers.cloudflare.com/realtime/turn/faq/):

| Protocol | Address | Primary port | Alternate port |
| --- | --- | --- | --- |
| STUN/UDP | `stun.cloudflare.com` | 3478/udp | |
| TURN/UDP | `turn.cloudflare.com` | 3478/udp | 443/udp |
| TURN/TCP | `turn.cloudflare.com` | 3478/tcp | 80/tcp |
| TURN/TLS | `turn.cloudflare.com` | 5349/tcp | 443/tcp |

- Create a TURN key in the dashboard or API, and keep it server-side; you can create up to 1,000 TURN keys ([replacing existing](https://developers.cloudflare.com/realtime/turn/replacing-existing/)).
- Generate short-lived ICE servers per user with `POST https://rtc.live.cloudflare.com/v1/turn/keys/$TURN_KEY_ID/credentials/generate-ice-servers` and a body such as `{"ttl": 86400}`, then pass the returned `iceServers` to `RTCPeerConnection`.
- A `customIdentifier` can be attached to credentials for per-user usage accounting through the GraphQL dataset `callsTurnUsageAdaptiveGroups`, which is adaptively sampled, so query one customer per query when billing ([replacing existing](https://developers.cloudflare.com/realtime/turn/replacing-existing/), [analytics](https://developers.cloudflare.com/realtime/turn/analytics/)).
- Per-allocation limits are more than 5 new IPs per second, more than 5 to 10 kpps and more than 50 to 100 Mbps, and exceeding them drops packets.
- There is no MTU limit, and TLS 1.1, 1.2 and 1.3 are supported.
- TURN runs everywhere except the China Network.
- Custom domains work for STUN, TURN/UDP and TURN/TCP but not TLS, via a DNS-only CNAME to `turn.cloudflare.com` ([custom domains](https://developers.cloudflare.com/realtime/turn/custom-domains/)).
- Billing counts bytes from Cloudflare to the TURN client at $0.05 per GB, with a 1,000 GB free tier shared with the SFU; STUN is free and unlimited; traffic between TURN and the SFU or Stream WHIP/WHEP is not charged.
- Supported RFCs are RFC 5766 over UDP, TCP and TLS, the TURN REST API draft, the STUN origin draft and ALPN (RFC 7443); DTLS, RFC 6062 TCP relaying, RFC 6156 IPv6 and RFC 7635 OAuth are not supported ([RFC matrix](https://developers.cloudflare.com/realtime/turn/rfc-matrix/)).
- The FAQ says to use TURN alone for one-to-one links and the SFU for fan-out or groups, and that the two share the same fleet and data path.

### 4.6 Most useful Realtime pages

- Realtime overview: https://developers.cloudflare.com/realtime/
- RealtimeKit overview: https://developers.cloudflare.com/realtime/realtimekit/
- RealtimeKit quickstart: https://developers.cloudflare.com/realtime/realtimekit/quickstart/
- Concepts: https://developers.cloudflare.com/realtime/realtimekit/concepts/
- SDK selection: https://developers.cloudflare.com/realtime/realtimekit/sdk-selection/
- RealtimeKit pricing: https://developers.cloudflare.com/realtime/realtimekit/pricing/
- RealtimeKit limits: https://developers.cloudflare.com/realtime/realtimekit/limits/
- RealtimeKit FAQ: https://developers.cloudflare.com/realtime/realtimekit/faq/
- Webinar: https://developers.cloudflare.com/realtime/realtimekit/webinar/
- RealtimeKit REST API: https://developers.cloudflare.com/api/resources/realtime_kit/
- SFU overview: https://developers.cloudflare.com/realtime/sfu/
- SFU sessions and tracks: https://developers.cloudflare.com/realtime/sfu/concepts/sessions-tracks/
- SFU Connection API: https://developers.cloudflare.com/realtime/sfu/api/
- SFU limits: https://developers.cloudflare.com/realtime/sfu/platform/limits/
- SFU pricing: https://developers.cloudflare.com/realtime/sfu/platform/pricing/
- TURN: https://developers.cloudflare.com/realtime/turn/
- TURN credentials: https://developers.cloudflare.com/realtime/turn/generate-credentials/

---

## 5. MoQ (Media over QUIC)

From [MoQ overview](https://developers.cloudflare.com/moq/), [background](https://developers.cloudflare.com/moq/about/), [demo streams](https://developers.cloudflare.com/moq/demo-streams/) and [feature matrix](https://developers.cloudflare.com/moq/feature-matrix/):

- MoQ is an IETF protocol for live media over QUIC, which Cloudflare describes as an Internet-infrastructure-level service "similar to how HTTP provides content delivery and WebRTC provides real-time communication".
- Cloudflare supports MoQ Transport draft-14 and draft-16 as of 2026-10-05, and is working on draft-18 (testable via `moq-interop-runner`).
- Relays are provisioned in the dashboard (Media > Realtime > MoQ Relay) or the API, and are free during the beta.
- Each relay isolates its namespaces, tracks and objects.
- Creating a relay returns two default tokens, one publish+subscribe and one subscribe-only, and token secrets are shown once.

```sh
curl -X POST "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/moq/relays" \
  -H "Authorization: Bearer $API_TOKEN" -H "Content-Type: application/json" -d '{"name": "My Relay"}'
```

- Draft-16 requires authentication, sent as a token in the URL path, such as `https://draft-16.cloudflare.mediaoverquic.com/<token>`.
- Because path tokens appear in server access logs, the docs advise per-client, short-lived, rotated tokens, and say Cloudflare plans to support the C4M and Privacy Pass in-band auth drafts.
- Draft-14 clients connect to `https://draft-14.cloudflare.mediaoverquic.com/`.
- Clients come from the open-source `cloudflare/moq-rs` project (`moq-pub`, `moq-sub`), fed by `ffmpeg` fragmented MP4.
- Demo namespaces are `/bbb` (draft-14 and draft-16) and `/demo-tos-360p|720p|1080p|4k` (draft-14 only), and a public subscribe JWT is published for draft-16.
- In the feature matrix, draft-16 supports SUBSCRIBE, PUBLISH, SUBSCRIBE_NAMESPACE, TRACK_STATUS and the SETUP messages, with partial support for MAX_REQUEST_ID and REQUESTS_BLOCKED and no support for GOAWAY, SUBSCRIBE_UPDATE, PUBLISH_ERROR or the FETCH family.
- In the feature matrix, draft-14 supports SUBSCRIBE, the PUBLISH_NAMESPACE family and TRACK_STATUS, and does not support FETCH or SUBSCRIBE_NAMESPACE.
- The relay REST API has 8 endpoints: relays CRUD plus token list, create and delete (`raw/api/endpoints.tsv`, `https://developers.cloudflare.com/api/resources/moq`).

There is no MoQ pricing page, limits page or changelog in the mirror.

---

## 6. Choosing a live-media product

This comparison only restates figures from the pages cited above (as of 2026-10-05).

| Need | Product | Latency stated by docs | Audience model | Billing basis |
| --- | --- | --- | --- | --- |
| VOD library, trailers, recorded AMAs | Stream (VOD) | n/a | Unlimited viewers via HLS/DASH | Minutes stored + minutes delivered |
| One-to-many broadcast from OBS/hardware | Stream Live (RTMPS/SRT) | LL-HLS beta for lower latency | Many viewers, recordings, simulcast to 50 outputs | Same as VOD |
| One-to-many sub-second broadcast from a browser | Stream WebRTC (WHIP/WHEP) | Under 500 ms | "No fixed limits" on viewers; no recording | Minutes delivered, billing from 2026-10-15 |
| Interactive meeting, AMA with speakers, classroom | RealtimeKit | Not stated as a number | Participants with presets; stage for large events | Participant-minutes |
| Custom WebRTC topology, data fan-out, devices, AI audio | Realtime SFU | Not stated as a number | Whatever your app composes | GB egress |
| Peer-to-peer calls through NAT | TURN | n/a | 1:1 | GB egress |
| Experimental QUIC-native live delivery | MoQ relays | "low-latency" | Pub/sub namespaces | Free in beta |

---

## 7. REST API surface and GitHub repos

Endpoint counts from `raw/api/endpoints.tsv` (OpenAPI snapshot, as of 2026-10-05):

| API family | Endpoints | Notable resources |
| --- | --- | --- |
| Images (`/accounts/{id}/images/...`) | 37 | `v1` images, `v1/keys`, `v1/variants`, `v1/stats`, `v2` list, `v2/direct_upload`, `v2/metadata`, `v2/sourcingkit` (15, S3 import) |
| Stream (`/accounts/{id}/stream...`) | 61 | Videos, `copy`, `direct_upload`, `clip`, `live_inputs` (12), `keys`, `watermarks`, `webhook`, `storage-usage`, `usage` |
| RealtimeKit (`/accounts/{id}/realtime/kit/{app_id}/...`) | 61 | `meetings` (22), `sessions` (10), `webhooks` (7), `presets` (6), `recordings` (6), `livestreams` (4), `analytics` (3) |
| Realtime account API (`/accounts/{id}/calls/...`) | 10 | SFU apps CRUD, TURN keys CRUD |
| MoQ (`/accounts/{id}/moq/...`) | 8 | Relays and relay tokens |

The SFU Connection API (`rtc.live.cloudflare.com/v1`) is separate from `api.cloudflare.com` and is documented by its own OpenAPI file ([API](https://developers.cloudflare.com/realtime/sfu/api/)).

Related public repos in the `cloudflare` org (from `raw/github/repos.tsv`; stars and last push as of 2026-10-05):

| Repo | Stars | Language | Last push | What it is |
| --- | --- | --- | --- | --- |
| `svg-hush` | 435 | Rust | 2026-08-25 | SVG sanitizer used by Images |
| `stream-react` | 198 | TypeScript | 2026-04-23 | React component for the Stream player |
| `moq-rs` | 171 | Rust | 2026-09-29 | Rust MoQ Transport implementation (`moq-pub`, `moq-sub`) |
| `realtime-examples` | 150 | TypeScript | 2026-09-22 | SFU examples including the quickstart video room |
| `images.pages.dev` | 127 | TypeScript | 2026-04-23 | Images demo site |
| `realtimekit-web-examples` | 70 | TypeScript | 2026-09-28 | RealtimeKit React, HTML and Angular templates |
| `realtimekit-ui` | 68 | TypeScript | 2026-10-05 | RealtimeKit UI component source |
| `pages-stream-demo` | 38 | HTML | 2026-04-23 | Stream on Pages demo |
| `stream-angular` | 13 | TypeScript | 2026-04-23 | Angular Stream player component |
| `realtimekit-ios-ui`, `realtimekit-ios-core` | 9, 6 | Swift | 2026-09 | Swift package definitions |
| `realtimekit-ui-addons` | 3 | TypeScript | 2026-04-23 | UI Kit add-ons |
| `realtimekit-flutter-bridge` | 1 | Swift | 2026-06-30 | Flutter bridge |
| `stream-wordpress` | 8 | JavaScript | 2026-04-23 | Archived WordPress plugin |

---

## 8. Build hooks for Web3 projects

These are suggested uses for dapps, launchpads, indexers and trading UIs on Solana, Ethereum, Base and Robinhood Chain (an EVM L2, chain id 4663).
Each one rests on a documented capability cited above; the Web3 framing is this file's own suggestion, not something the media docs discuss.

**Token logos, NFT art and launch assets (Images)**

- Accept token-logo and banner uploads from launchers with Direct Creator Upload (`hosted.createDirectUpload`, expiry 2 minutes to 6 hours) so the browser never sees your API token, then attach `metadata: { chainId: 4663, address: "0x..." }` or a Solana mint address.
- List a project's assets with `hosted.list({ filter: { metadata: { chainId: 4663 } } })`, keeping in mind the five-condition limit per call.
- Use a custom ID such as `base/0xabc.../logo` for predictable token-list URLs, but note that custom-ID images cannot be private.
- Serve user-uploaded SVG logos through Images so they pass `svg-hush`, which strips scripts, links and cross-origin references and closes an XSS vector common in token lists.
- If token metadata and images live in R2 (see `build/03-storage-database.md`), serve them with `/cdn-cgi/image/width=64,format=auto/<r2-url>` instead of storing hosted copies, which the docs call the most cost-effective approach.
- A fixed set of sizes (for example 32, 64, 256 px) keeps unique transformations, and therefore cost, predictable.
- Images on Free return error `9422` after 5,000 unique transformations, so a busy launchpad needs the Paid plan.
- Generate share cards for launches or PnL screenshots in a Worker with the binding's `.text()` (up to 1,000 characters) and `.draw()` overlays on a template from R2 or KV, and cache them with Workers Cache because binding output is not cached automatically.
- Use `segment=foreground` to cut out mascot art for meme-coin pages.
- Preserve C2PA Content Credentials where provenance of NFT artwork matters.

**Launch videos, AMAs and token-gated content (Stream)**

- Host launch trailers and roadmap videos on Stream at $5 per 1,000 minutes stored and $1 per 1,000 minutes delivered; by that rate, 10,000 views of a 2-minute trailer would be 20,000 minutes, or $20 delivered.
- Gate holder-only videos with `requireSignedURLs`: the backend verifies a wallet signature (SIWE or a Solana signMessage) and an on-chain balance, then issues a token with a signing key or `env.STREAM.video(id).generateToken()`.
- Use `creator` on uploads to tie videos to a launcher's wallet or account ID, and `allowedOrigins` to stop hot-linking.
- Run live launch countdowns or trading streams through WebRTC WHEP for under 500 ms latency to an unlimited audience, but plan a parallel RTMPS input if you need a recording, because WebRTC broadcasts are not recorded.
- For OBS-based AMAs, use RTMPS or SRT inputs with automatic recording, Live Instant Clipping for 60-second highlight clips, and simulcast to X and YouTube (up to 50 outputs).
- Generate preview frames or short muted MP4 loops of user-submitted promo clips stored in R2 with Media Transformations (`mode=frame` or `mode=video,duration=5s`), keeping inputs under 100 MB and 10 minutes.

**Live trading rooms and community calls (Realtime)**

- Model a trading room or AMA as a RealtimeKit webinar: team members use `webinar_presenter`, and holders use `webinar_viewer` with `stage_access: CAN_REQUEST`.
- Token-gate rooms by having the backend check holdings before calling Add Participant.
- Because tokens live 100 days and refreshing does not revoke old ones, handle a holder who sells by calling Kick Participants and then Delete Participant.
- Push trade alerts or "new pool created" events into a meeting with `broadcastMessage` (5 per second per participant), and keep a shared watchlist in a collaborative store for the session.
- Recap AMAs with post-meeting transcription and `summarize_on_end`, and export recordings to your own R2 bucket before RealtimeKit's 7-day retention expires.
- By the published rates, 300 participants on video for 60 minutes is 18,000 participant-minutes, or $36, and the same room as audio-only is $9.
- For high-rate market-data fan-out to many browsers (order-book or price ticks from an indexer), the SFU DataChannels pattern of one publisher and many subscribers fits better than the RealtimeKit message APIs: ingress is free, egress is $0.05 per GB after 1,000 GB, and only one subscriber can reply on a channel.
- Feed SFU audio to a Worker-side AI agent ("voice trading assistant") with the WebSocket adapter (beta, PCM in and out), as in the AI audio example.
- Use TURN alone for one-to-one OTC-desk or support calls, and tag each credential with a `customIdentifier` such as the user's wallet-linked account ID to bill or rate-limit heavy users.

**Experimental (MoQ)**

- MoQ relays are free during the beta and could carry a low-latency launch stream to custom clients built on `moq-rs`, but the docs publish no limits or SLA, and draft-16 path tokens leak into logs, so treat MoQ as experimental.

---

## 9. Gaps and contradictions

Contradictions between pages (not resolved here):

1. **Stream upload frame rate.** [Upload videos](https://developers.cloudflare.com/stream/uploading-videos/) recommends "60 or fewer frames per second", while the [FAQ](https://developers.cloudflare.com/stream/faq/) recommends "30 or below frames per second".
2. **Stream MP4 download billing.** [Pricing](https://developers.cloudflare.com/stream/pricing/) says "MP4 Downloads are billed by percentage of the file delivered", while [Download videos](https://developers.cloudflare.com/stream/viewing-videos/download-videos/) says you are billed "for the duration of the video each time the MP4 for the video is downloaded".
3. **Stream Live recording.** [Stream live video](https://developers.cloudflare.com/stream/stream-live/) says "All Stream Live videos are automatically recorded"; [WebRTC](https://developers.cloudflare.com/stream/webrtc-beta/) and [pricing](https://developers.cloudflare.com/stream/pricing/) say WebRTC broadcasts cannot be recorded; and [Get started](https://developers.cloudflare.com/stream/get-started/) shows recording as a configurable `recording.mode`.
4. **WHIP draft version.** The [WebRTC page](https://developers.cloudflare.com/stream/webrtc-beta/) links to `draft-ietf-wish-whip-16`, but states Stream uses `draft-ietf-wish-whip-06`.
5. **WebRTC status.** The URL slug is `webrtc-beta` and the changelog lists it as beta (2022-09-27), while the pricing, get-started and WebRTC pages carry a "going GA" banner with billing from 2026-10-15 and still list major limitations.
6. **TURN pricing when used with the SFU.** The [TURN overview](https://developers.cloudflare.com/realtime/turn/) says TURN "is available free of charge when used together with the Realtime SFU", while [SFU pricing](https://developers.cloudflare.com/realtime/sfu/platform/pricing/) says "The SFU and TURN services cost $0.05 per GB" and that TURN-to-SFU traffic is "not charged twice".
7. **TURN port 53.** [Generate credentials](https://developers.cloudflare.com/realtime/turn/generate-credentials/) warns about "the alternate port 53" in the returned URLs, but the port tables and the example response list only 3478, 443, 80 and 5349.
8. **RealtimeKit package names.** [SDK selection](https://developers.cloudflare.com/realtime/realtimekit/sdk-selection/) lists `@cloudflare/realtimekit` as the Core SDK for Web Components and Angular, while the [quickstart](https://developers.cloudflare.com/realtime/realtimekit/quickstart/) installs `@cloudflare/realtimekit-web` for Web Components and `@cloudflare/realtimekit-angular` for Angular, and the [Core SDK page](https://developers.cloudflare.com/realtime/realtimekit/core/) uses `@cloudflare/realtimekit` and `@cloudflare/realtimekit-angular`.
9. **RealtimeKit Android version.** The [quickstart](https://developers.cloudflare.com/realtime/realtimekit/quickstart/) pins `com.cloudflare.realtimekit:ui-android:0.3.0`, while [release notes](https://developers.cloudflare.com/realtime/realtimekit/release-notes/android-ui-kit/) show Android UI Kit 3.2.0 (2026-09-16).
10. **Flutter and iOS sources.** Flutter Core and UI Kit have release notes (2026-08-07) and the org has `realtimekit-flutter-bridge`, but [SDK selection](https://developers.cloudflare.com/realtime/realtimekit/sdk-selection/) omits Flutter; it also points iOS at `github.com/dyte-in/...` repos while the cloudflare org hosts `realtimekit-ios-core` and `realtimekit-ios-ui`.
11. **RealtimeKit recording storage targets.** The [recording guide](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/) says transfers go to "AWS, Azure, and DigitalOcean", while [custom cloud storage](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/custom-cloud-storage/) and the [RealtimeKit overview](https://developers.cloudflare.com/realtime/realtimekit/) also list Cloudflare R2 (and GCS).
12. **Images doc links.** The [Images overview](https://developers.cloudflare.com/images/) links "limits and supported formats" to the features page instead of [Limits and formats](https://developers.cloudflare.com/images/get-started/limits/), and [Transform via fetch](https://developers.cloudflare.com/images/optimization/transformations/transform-via-workers/) links a `#url-interface` anchor on the transformations overview that only exists on the features page.
13. **Broken link.** The [Stream binding page](https://developers.cloudflare.com/stream/manage-video-library/bindings/) links large direct uploads to `http://localhost:1111/stream/uploading-videos/direct-creator-uploads/...`.
14. **Stale wording.** [Transform videos](https://developers.cloudflare.com/stream/transform-videos/) still says "After November 1st, 2025, Media Transformations and Image Transformations will use the same subscriptions", while [Stream pricing](https://developers.cloudflare.com/stream/pricing/) states it in the present tense.

Gaps:

1. **MoQ is not in the sidebar.** The Build > Media dropdown lists only Images, Stream and Realtime (`raw/nav/home-sidebar.md`), although MoQ has a top-level docs section and its dashboard location is described as Media > Realtime > MoQ Relay ([MoQ](https://developers.cloudflare.com/moq/)).
2. **MoQ has no pricing after beta, no limits, no SLA and no changelog page.**
3. **The Realtime SFU has no GA date.** The SFU changelog records the closed beta (2022), the open beta (2024-04-04) and TURN GA (2024-09-25), but no GA entry for the SFU itself, and the SFU pages do not label it beta either ([SFU changelog](https://developers.cloudflare.com/realtime/sfu/platform/changelog/)).
4. **RealtimeKit has no participant cap.** The [limits page](https://developers.cloudflare.com/realtime/realtimekit/limits/) documents rate limits but no maximum participants per meeting or per stage.
5. **RealtimeKit lacks a status label.** Only sub-features (breakout rooms, the Livestream meeting type) are marked beta, and there is no RealtimeKit-wide changelog beyond per-SDK release notes.
6. **The Images changelog is stale.** [The changelog](https://developers.cloudflare.com/images/platform/changelog/) ends at 2024-04-04 (upload widget and face cropping closed betas) even though pages updated in 2026 describe the hosted binding namespace, metadata filters and `segment`; the current status of the upload widget is not stated anywhere.
7. **No Stream limits page.** Upload and concurrency limits live in the [FAQ](https://developers.cloudflare.com/stream/faq/) and scattered pages rather than a limits page.
8. **The Orange Meets repo is not in the catalog.** The SFU changelog points to `github.com/cloudflare/orange` as the open-source Orange Meets app, but that repo is not among the 580 repos in `raw/github/repos.tsv`.
9. **Collaborative store lifetime is ambiguous.** The page says data "is stored until a session is active", which reads as "while a session is active" but is not explicit ([collaborative stores](https://developers.cloudflare.com/realtime/realtimekit/collaborative-stores/)).
10. **Polish availability is not on the pricing page.** Polish requires Pro or higher ([Polish](https://developers.cloudflare.com/images/polish/)), but the Images pricing page does not mention it.
