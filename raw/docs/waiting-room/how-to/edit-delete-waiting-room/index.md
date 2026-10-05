---
description: Edit or delete existing waiting rooms.
title: Edit and delete waiting rooms
image: https://developers.cloudflare.com/waiting-room/how-to/edit-delete-waiting-room/og.png?v=a438095d369e58b1
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/waiting-room/llms.txt  
> Use this file to discover all available pages before exploring further.

# Edit and delete waiting rooms

Last updated Apr 16, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/waiting-room/how-to/edit-delete-waiting-room/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can manage your waiting rooms using the [Waiting Room dashboard](https://developers.cloudflare.com/waiting-room/how-to/waiting-room-dashboard/) or the [API](https://developers.cloudflare.com/waiting-room/reference/waiting-room-api/).

Note

For details about updating an active waiting room, refer to [Best practices](https://developers.cloudflare.com/waiting-room/reference/best-practices/).

## Use the dashboard

### Edit a waiting room

1. In your application, go to **Traffic** > **Waiting Room**.
2. On a record, select **Edit**.
3. Select **Settings**.
4. Edit the settings. For a description of settings, refer to [Configuration settings](https://developers.cloudflare.com/waiting-room/reference/configuration-settings/).
5. Select **Next**. If you have access to [customized templates](https://developers.cloudflare.com/waiting-room/how-to/customize-waiting-room/), you could also adjust the template.
6. Once you get to **Review**, select **Save**.

### Delete a waiting room

1. In your application, go to **Traffic** > **Waiting Room**.
2. On a record, select **Delete**.
3. Select **Delete** again.

## Use the API

### Edit a waiting room

[Replace ↗︎](https://api.cloudflare.com#waiting-room-update-waiting-room) a configured waiting room by appending the following endpoint to the Cloudflare API base URL.

<details>

<summary>

Required API token permissions

</summary>

At least one of the following <a href="https://developers.cloudflare.com/fundamentals/api/reference/permissions/">token permissions</a> is required:

- <code>Waiting Rooms Write</code>

</details>

*Update waiting roombash*

```bash
curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/waiting_rooms/$WAITING_ROOM_ID" \
	--request PUT \
	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
	--json '{
		"name": "webshop-waiting-room",
		"host": "example.com",
		"new_users_per_minute": 200,
		"total_active_users": 300
	}'
```

[Update ↗︎](https://api.cloudflare.com#waiting-room-patch-waiting-room) a configured waiting room by appending the following endpoint to the Cloudflare API base URL.

<details>

<summary>

Required API token permissions

</summary>

At least one of the following <a href="https://developers.cloudflare.com/fundamentals/api/reference/permissions/">token permissions</a> is required:

- <code>Waiting Rooms Write</code>

</details>

*Patch waiting roombash*

```bash
curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/waiting_rooms/$WAITING_ROOM_ID" \
	--request PATCH \
	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
	--json '{
		"name": "webshop-waiting-room",
		"host": "example.com",
		"new_users_per_minute": 200,
		"total_active_users": 300
	}'
```

You only need to include the fields you want to update in the payload of the PATCH request.

### Delete a waiting room

Delete a waiting room by appending the following endpoint in the [Waiting Room API ↗︎](https://api.cloudflare.com#waiting-room-delete-waiting-room) to the Cloudflare API base URL.

<details>

<summary>

Required API token permissions

</summary>

At least one of the following <a href="https://developers.cloudflare.com/fundamentals/api/reference/permissions/">token permissions</a> is required:

- <code>Waiting Rooms Write</code>

</details>

*Delete waiting roombash*

```bash
curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/waiting_rooms/$WAITING_ROOM_ID" \
	--request DELETE \
	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
```
