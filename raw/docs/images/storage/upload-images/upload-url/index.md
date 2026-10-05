---
description: Upload an image to Cloudflare Images by providing a source URL instead of a file.
title: Upload via URL
image: https://developers.cloudflare.com/images/storage/upload-images/upload-url/og.png?v=f1cc20878f13118c
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/images/llms.txt  
> Use this file to discover all available pages before exploring further.

# Upload via URL

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/images/storage/upload-images/upload-url/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Before you upload an image, check the list of [supported formats and dimensions](https://developers.cloudflare.com/images/get-started/limits) to confirm your image will be accepted.

You can use the Images API to use a URL of an image instead of uploading the data.

Make a `POST` request using the example below as reference. Keep in mind that the `--form 'file=<FILE>'` and `--form 'url=<URL>'` fields are mutually exclusive.

Note

The `metadata` included in the request is never shared with end-users.

```bash
curl --request POST \
https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1 \
--header "Authorization: Bearer <API_TOKEN>" \
--form 'url=https://[user:password@]example.com/<PATH_TO_IMAGE>' \
--form 'metadata={"key":"value"}' \
--form 'requireSignedURLs=false'
```

After successfully uploading the image, you will receive a response similar to the example below.

```json
{
	"result": {
		"id": "2cdc28f0-017a-49c4-9ed7-87056c83901",
		"filename": "image.jpeg",
		"metadata": {
			"key": "value"
		},
		"uploaded": "2022-01-31T16:39:28.458Z",
		"requireSignedURLs": false,
		"variants": [
			"https://imagedelivery.net/Vi7wi5KSItxGFsWRG2Us6Q/2cdc28f0-017a-49c4-9ed7-87056c83901/public",
			"https://imagedelivery.net/Vi7wi5KSItxGFsWRG2Us6Q/2cdc28f0-017a-49c4-9ed7-87056c83901/thumbnail"
		]
	},
	"success": true,
	"errors": [],
	"messages": []
}
```

If your origin server returns an error while fetching the images, the API response will return a 4xx error.
