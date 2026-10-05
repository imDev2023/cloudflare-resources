---
title: Catalog Syncs
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Magic Cloud Networking](https://developers.cloudflare.com/api/resources/magic_cloud_networking)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Catalog Syncs

##### [List Catalog Syncs](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/catalog_syncs/methods/list)

GET/accounts/{account\_id}/magic/cloud/catalog-syncs

##### [Read Catalog Sync](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/catalog_syncs/methods/get)

GET/accounts/{account\_id}/magic/cloud/catalog-syncs/{sync\_id}

##### [Create Catalog Sync](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/catalog_syncs/methods/create)

POST/accounts/{account\_id}/magic/cloud/catalog-syncs

##### [Update Catalog Sync](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/catalog_syncs/methods/update)

PUT/accounts/{account\_id}/magic/cloud/catalog-syncs/{sync\_id}

##### [Patch Catalog Sync](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/catalog_syncs/methods/edit)

PATCH/accounts/{account\_id}/magic/cloud/catalog-syncs/{sync\_id}

##### [Delete Catalog Sync](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/catalog_syncs/methods/delete)

DELETE/accounts/{account\_id}/magic/cloud/catalog-syncs/{sync\_id}

##### [Run Catalog Sync](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/catalog_syncs/methods/refresh)

POST/accounts/{account\_id}/magic/cloud/catalog-syncs/{sync\_id}/refresh

##### ModelsExpand Collapse

<details>

<summary>

CatalogSyncListResponse object {id, description, destination\_id, 9 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

description: string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

destination\_id: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20destination_id">Link to this property</a>

<details>

<summary>

destination\_type: "NONE"or "ZERO\_TRUST\_LIST"

</summary>

One of the following:

"NONE"

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20destination_type%20%3E%20(member)%200">Link to this property</a>

"ZERO\_TRUST\_LIST"

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20destination_type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20destination_type">Link to this property</a>

last\_user\_update\_at: string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20last_user_update_at">Link to this property</a>

name: string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

policy: string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20policy">Link to this property</a>

<details>

<summary>

update\_mode: "AUTO"or "MANUAL"

</summary>

One of the following:

"AUTO"

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20update_mode%20%3E%20(member)%200">Link to this property</a>

"MANUAL"

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20update_mode%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20update_mode">Link to this property</a>

<details>

<summary>

errors: optional map\[object {code, message, documentation\_url, 2 more } ]

</summary>

<details>

<summary>

code: 1001or 1002or 1003or 152 more

</summary>

One of the following:

1001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%200">Link to this property</a>

1002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%201">Link to this property</a>

1003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%202">Link to this property</a>

1004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%203">Link to this property</a>

1005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%204">Link to this property</a>

1006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%205">Link to this property</a>

1007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%206">Link to this property</a>

1008

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%207">Link to this property</a>

1009

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%208">Link to this property</a>

1010

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%209">Link to this property</a>

1011

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2010">Link to this property</a>

1012

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2011">Link to this property</a>

1013

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2012">Link to this property</a>

1014

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2013">Link to this property</a>

1015

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2014">Link to this property</a>

1016

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2015">Link to this property</a>

1017

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2016">Link to this property</a>

1018

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2017">Link to this property</a>

2001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2018">Link to this property</a>

2002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2019">Link to this property</a>

2003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2020">Link to this property</a>

2004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2021">Link to this property</a>

2005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2022">Link to this property</a>

2006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2023">Link to this property</a>

2007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2024">Link to this property</a>

2008

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2025">Link to this property</a>

2009

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2026">Link to this property</a>

2010

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2027">Link to this property</a>

2011

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2028">Link to this property</a>

2012

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2029">Link to this property</a>

2013

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2030">Link to this property</a>

2014

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2031">Link to this property</a>

2015

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2032">Link to this property</a>

2016

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2033">Link to this property</a>

2017

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2034">Link to this property</a>

2018

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2035">Link to this property</a>

2019

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2036">Link to this property</a>

2020

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2037">Link to this property</a>

2021

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2038">Link to this property</a>

2022

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2039">Link to this property</a>

3001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2040">Link to this property</a>

3002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2041">Link to this property</a>

3003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2042">Link to this property</a>

3004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2043">Link to this property</a>

3005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2044">Link to this property</a>

3006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2045">Link to this property</a>

3007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2046">Link to this property</a>

4001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2047">Link to this property</a>

4002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2048">Link to this property</a>

4003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2049">Link to this property</a>

4004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2050">Link to this property</a>

4005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2051">Link to this property</a>

4006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2052">Link to this property</a>

4007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2053">Link to this property</a>

4008

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2054">Link to this property</a>

4009

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2055">Link to this property</a>

4010

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2056">Link to this property</a>

4011

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2057">Link to this property</a>

4012

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2058">Link to this property</a>

4013

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2059">Link to this property</a>

4014

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2060">Link to this property</a>

4015

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2061">Link to this property</a>

4016

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2062">Link to this property</a>

4017

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2063">Link to this property</a>

4018

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2064">Link to this property</a>

4019

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2065">Link to this property</a>

4020

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2066">Link to this property</a>

4021

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2067">Link to this property</a>

4022

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2068">Link to this property</a>

4023

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2069">Link to this property</a>

5001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2070">Link to this property</a>

5002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2071">Link to this property</a>

5003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2072">Link to this property</a>

5004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2073">Link to this property</a>

102000

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2074">Link to this property</a>

102001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2075">Link to this property</a>

102002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2076">Link to this property</a>

102003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2077">Link to this property</a>

102004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2078">Link to this property</a>

102005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2079">Link to this property</a>

102006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2080">Link to this property</a>

102007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2081">Link to this property</a>

102008

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2082">Link to this property</a>

102009

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2083">Link to this property</a>

102010

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2084">Link to this property</a>

102011

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2085">Link to this property</a>

102012

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2086">Link to this property</a>

102013

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2087">Link to this property</a>

102014

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2088">Link to this property</a>

102015

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2089">Link to this property</a>

102016

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2090">Link to this property</a>

102017

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2091">Link to this property</a>

102018

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2092">Link to this property</a>

102019

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2093">Link to this property</a>

102020

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2094">Link to this property</a>

102021

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2095">Link to this property</a>

102022

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2096">Link to this property</a>

102023

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2097">Link to this property</a>

102024

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2098">Link to this property</a>

102025

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2099">Link to this property</a>

102026

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20100">Link to this property</a>

102027

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20101">Link to this property</a>

102028

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20102">Link to this property</a>

102029

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20103">Link to this property</a>

102030

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20104">Link to this property</a>

102031

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20105">Link to this property</a>

102032

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20106">Link to this property</a>

102033

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20107">Link to this property</a>

102034

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20108">Link to this property</a>

102035

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20109">Link to this property</a>

102036

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20110">Link to this property</a>

102037

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20111">Link to this property</a>

102038

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20112">Link to this property</a>

102039

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20113">Link to this property</a>

102040

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20114">Link to this property</a>

102041

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20115">Link to this property</a>

102042

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20116">Link to this property</a>

102043

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20117">Link to this property</a>

102044

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20118">Link to this property</a>

102045

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20119">Link to this property</a>

102046

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20120">Link to this property</a>

102047

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20121">Link to this property</a>

102048

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20122">Link to this property</a>

102049

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20123">Link to this property</a>

102050

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20124">Link to this property</a>

102051

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20125">Link to this property</a>

102052

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20126">Link to this property</a>

102053

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20127">Link to this property</a>

102054

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20128">Link to this property</a>

102055

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20129">Link to this property</a>

102056

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20130">Link to this property</a>

102057

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20131">Link to this property</a>

102058

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20132">Link to this property</a>

102059

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20133">Link to this property</a>

102060

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20134">Link to this property</a>

102061

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20135">Link to this property</a>

102062

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20136">Link to this property</a>

102063

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20137">Link to this property</a>

102064

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20138">Link to this property</a>

102065

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20139">Link to this property</a>

102066

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20140">Link to this property</a>

102067

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20141">Link to this property</a>

102068

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20142">Link to this property</a>

102069

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20143">Link to this property</a>

102070

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20144">Link to this property</a>

102071

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20145">Link to this property</a>

102072

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20146">Link to this property</a>

103001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20147">Link to this property</a>

103002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20148">Link to this property</a>

103003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20149">Link to this property</a>

103004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20150">Link to this property</a>

103005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20151">Link to this property</a>

103006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20152">Link to this property</a>

103007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20153">Link to this property</a>

103008

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20154">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

meta: optional object {l10n\_key, loggable\_error, template\_data, trace\_id }

</summary>

l10n\_key: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20meta%20%3E%20(property)%20l10n_key">Link to this property</a>

loggable\_error: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20meta%20%3E%20(property)%20loggable_error">Link to this property</a>

template\_data: optional unknown

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20meta%20%3E%20(property)%20template_data">Link to this property</a>

trace\_id: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20meta%20%3E%20(property)%20trace_id">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

source: optional object {parameter, parameter\_value\_index, pointer }

</summary>

parameter: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20parameter">Link to this property</a>

parameter\_value\_index: optional number

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20parameter_value_index">Link to this property</a>

pointer: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

includes\_discoveries\_until: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20includes_discoveries_until">Link to this property</a>

last\_attempted\_update\_at: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20last_attempted_update_at">Link to this property</a>

last\_successful\_update\_at: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)%20%3E%20(property)%20last_successful_update_at">Link to this property</a>

</details>

[Link to this property](<#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_list_response%20%3E%20(schema)>)

<details>

<summary>

CatalogSyncGetResponse object {id, description, destination\_id, 9 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

description: string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

destination\_id: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20destination_id">Link to this property</a>

<details>

<summary>

destination\_type: "NONE"or "ZERO\_TRUST\_LIST"

</summary>

One of the following:

"NONE"

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20destination_type%20%3E%20(member)%200">Link to this property</a>

"ZERO\_TRUST\_LIST"

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20destination_type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20destination_type">Link to this property</a>

last\_user\_update\_at: string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20last_user_update_at">Link to this property</a>

name: string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

policy: string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20policy">Link to this property</a>

<details>

<summary>

update\_mode: "AUTO"or "MANUAL"

</summary>

One of the following:

"AUTO"

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20update_mode%20%3E%20(member)%200">Link to this property</a>

"MANUAL"

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20update_mode%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20update_mode">Link to this property</a>

<details>

<summary>

errors: optional map\[object {code, message, documentation\_url, 2 more } ]

</summary>

<details>

<summary>

code: 1001or 1002or 1003or 152 more

</summary>

One of the following:

1001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%200">Link to this property</a>

1002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%201">Link to this property</a>

1003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%202">Link to this property</a>

1004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%203">Link to this property</a>

1005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%204">Link to this property</a>

1006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%205">Link to this property</a>

1007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%206">Link to this property</a>

1008

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%207">Link to this property</a>

1009

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%208">Link to this property</a>

1010

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%209">Link to this property</a>

1011

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2010">Link to this property</a>

1012

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2011">Link to this property</a>

1013

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2012">Link to this property</a>

1014

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2013">Link to this property</a>

1015

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2014">Link to this property</a>

1016

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2015">Link to this property</a>

1017

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2016">Link to this property</a>

1018

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2017">Link to this property</a>

2001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2018">Link to this property</a>

2002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2019">Link to this property</a>

2003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2020">Link to this property</a>

2004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2021">Link to this property</a>

2005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2022">Link to this property</a>

2006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2023">Link to this property</a>

2007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2024">Link to this property</a>

2008

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2025">Link to this property</a>

2009

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2026">Link to this property</a>

2010

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2027">Link to this property</a>

2011

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2028">Link to this property</a>

2012

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2029">Link to this property</a>

2013

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2030">Link to this property</a>

2014

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2031">Link to this property</a>

2015

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2032">Link to this property</a>

2016

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2033">Link to this property</a>

2017

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2034">Link to this property</a>

2018

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2035">Link to this property</a>

2019

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2036">Link to this property</a>

2020

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2037">Link to this property</a>

2021

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2038">Link to this property</a>

2022

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2039">Link to this property</a>

3001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2040">Link to this property</a>

3002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2041">Link to this property</a>

3003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2042">Link to this property</a>

3004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2043">Link to this property</a>

3005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2044">Link to this property</a>

3006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2045">Link to this property</a>

3007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2046">Link to this property</a>

4001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2047">Link to this property</a>

4002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2048">Link to this property</a>

4003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2049">Link to this property</a>

4004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2050">Link to this property</a>

4005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2051">Link to this property</a>

4006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2052">Link to this property</a>

4007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2053">Link to this property</a>

4008

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2054">Link to this property</a>

4009

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2055">Link to this property</a>

4010

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2056">Link to this property</a>

4011

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2057">Link to this property</a>

4012

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2058">Link to this property</a>

4013

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2059">Link to this property</a>

4014

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2060">Link to this property</a>

4015

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2061">Link to this property</a>

4016

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2062">Link to this property</a>

4017

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2063">Link to this property</a>

4018

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2064">Link to this property</a>

4019

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2065">Link to this property</a>

4020

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2066">Link to this property</a>

4021

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2067">Link to this property</a>

4022

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2068">Link to this property</a>

4023

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2069">Link to this property</a>

5001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2070">Link to this property</a>

5002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2071">Link to this property</a>

5003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2072">Link to this property</a>

5004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2073">Link to this property</a>

102000

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2074">Link to this property</a>

102001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2075">Link to this property</a>

102002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2076">Link to this property</a>

102003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2077">Link to this property</a>

102004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2078">Link to this property</a>

102005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2079">Link to this property</a>

102006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2080">Link to this property</a>

102007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2081">Link to this property</a>

102008

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2082">Link to this property</a>

102009

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2083">Link to this property</a>

102010

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2084">Link to this property</a>

102011

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2085">Link to this property</a>

102012

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2086">Link to this property</a>

102013

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2087">Link to this property</a>

102014

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2088">Link to this property</a>

102015

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2089">Link to this property</a>

102016

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2090">Link to this property</a>

102017

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2091">Link to this property</a>

102018

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2092">Link to this property</a>

102019

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2093">Link to this property</a>

102020

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2094">Link to this property</a>

102021

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2095">Link to this property</a>

102022

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2096">Link to this property</a>

102023

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2097">Link to this property</a>

102024

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2098">Link to this property</a>

102025

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2099">Link to this property</a>

102026

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20100">Link to this property</a>

102027

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20101">Link to this property</a>

102028

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20102">Link to this property</a>

102029

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20103">Link to this property</a>

102030

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20104">Link to this property</a>

102031

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20105">Link to this property</a>

102032

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20106">Link to this property</a>

102033

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20107">Link to this property</a>

102034

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20108">Link to this property</a>

102035

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20109">Link to this property</a>

102036

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20110">Link to this property</a>

102037

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20111">Link to this property</a>

102038

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20112">Link to this property</a>

102039

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20113">Link to this property</a>

102040

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20114">Link to this property</a>

102041

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20115">Link to this property</a>

102042

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20116">Link to this property</a>

102043

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20117">Link to this property</a>

102044

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20118">Link to this property</a>

102045

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20119">Link to this property</a>

102046

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20120">Link to this property</a>

102047

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20121">Link to this property</a>

102048

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20122">Link to this property</a>

102049

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20123">Link to this property</a>

102050

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20124">Link to this property</a>

102051

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20125">Link to this property</a>

102052

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20126">Link to this property</a>

102053

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20127">Link to this property</a>

102054

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20128">Link to this property</a>

102055

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20129">Link to this property</a>

102056

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20130">Link to this property</a>

102057

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20131">Link to this property</a>

102058

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20132">Link to this property</a>

102059

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20133">Link to this property</a>

102060

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20134">Link to this property</a>

102061

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20135">Link to this property</a>

102062

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20136">Link to this property</a>

102063

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20137">Link to this property</a>

102064

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20138">Link to this property</a>

102065

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20139">Link to this property</a>

102066

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20140">Link to this property</a>

102067

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20141">Link to this property</a>

102068

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20142">Link to this property</a>

102069

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20143">Link to this property</a>

102070

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20144">Link to this property</a>

102071

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20145">Link to this property</a>

102072

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20146">Link to this property</a>

103001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20147">Link to this property</a>

103002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20148">Link to this property</a>

103003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20149">Link to this property</a>

103004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20150">Link to this property</a>

103005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20151">Link to this property</a>

103006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20152">Link to this property</a>

103007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20153">Link to this property</a>

103008

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20154">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

meta: optional object {l10n\_key, loggable\_error, template\_data, trace\_id }

</summary>

l10n\_key: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20meta%20%3E%20(property)%20l10n_key">Link to this property</a>

loggable\_error: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20meta%20%3E%20(property)%20loggable_error">Link to this property</a>

template\_data: optional unknown

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20meta%20%3E%20(property)%20template_data">Link to this property</a>

trace\_id: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20meta%20%3E%20(property)%20trace_id">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

source: optional object {parameter, parameter\_value\_index, pointer }

</summary>

parameter: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20parameter">Link to this property</a>

parameter\_value\_index: optional number

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20parameter_value_index">Link to this property</a>

pointer: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

includes\_discoveries\_until: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20includes_discoveries_until">Link to this property</a>

last\_attempted\_update\_at: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20last_attempted_update_at">Link to this property</a>

last\_successful\_update\_at: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)%20%3E%20(property)%20last_successful_update_at">Link to this property</a>

</details>

[Link to this property](<#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_get_response%20%3E%20(schema)>)

<details>

<summary>

CatalogSyncCreateResponse object {id, description, destination\_id, 9 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

description: string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

destination\_id: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20destination_id">Link to this property</a>

<details>

<summary>

destination\_type: "NONE"or "ZERO\_TRUST\_LIST"

</summary>

One of the following:

"NONE"

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20destination_type%20%3E%20(member)%200">Link to this property</a>

"ZERO\_TRUST\_LIST"

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20destination_type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20destination_type">Link to this property</a>

last\_user\_update\_at: string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20last_user_update_at">Link to this property</a>

name: string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

policy: string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20policy">Link to this property</a>

<details>

<summary>

update\_mode: "AUTO"or "MANUAL"

</summary>

One of the following:

"AUTO"

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20update_mode%20%3E%20(member)%200">Link to this property</a>

"MANUAL"

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20update_mode%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20update_mode">Link to this property</a>

<details>

<summary>

errors: optional map\[object {code, message, documentation\_url, 2 more } ]

</summary>

<details>

<summary>

code: 1001or 1002or 1003or 152 more

</summary>

One of the following:

1001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%200">Link to this property</a>

1002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%201">Link to this property</a>

1003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%202">Link to this property</a>

1004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%203">Link to this property</a>

1005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%204">Link to this property</a>

1006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%205">Link to this property</a>

1007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%206">Link to this property</a>

1008

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%207">Link to this property</a>

1009

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%208">Link to this property</a>

1010

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%209">Link to this property</a>

1011

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2010">Link to this property</a>

1012

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2011">Link to this property</a>

1013

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2012">Link to this property</a>

1014

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2013">Link to this property</a>

1015

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2014">Link to this property</a>

1016

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2015">Link to this property</a>

1017

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2016">Link to this property</a>

1018

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2017">Link to this property</a>

2001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2018">Link to this property</a>

2002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2019">Link to this property</a>

2003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2020">Link to this property</a>

2004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2021">Link to this property</a>

2005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2022">Link to this property</a>

2006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2023">Link to this property</a>

2007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2024">Link to this property</a>

2008

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2025">Link to this property</a>

2009

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2026">Link to this property</a>

2010

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2027">Link to this property</a>

2011

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2028">Link to this property</a>

2012

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2029">Link to this property</a>

2013

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2030">Link to this property</a>

2014

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2031">Link to this property</a>

2015

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2032">Link to this property</a>

2016

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2033">Link to this property</a>

2017

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2034">Link to this property</a>

2018

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2035">Link to this property</a>

2019

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2036">Link to this property</a>

2020

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2037">Link to this property</a>

2021

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2038">Link to this property</a>

2022

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2039">Link to this property</a>

3001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2040">Link to this property</a>

3002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2041">Link to this property</a>

3003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2042">Link to this property</a>

3004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2043">Link to this property</a>

3005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2044">Link to this property</a>

3006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2045">Link to this property</a>

3007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2046">Link to this property</a>

4001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2047">Link to this property</a>

4002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2048">Link to this property</a>

4003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2049">Link to this property</a>

4004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2050">Link to this property</a>

4005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2051">Link to this property</a>

4006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2052">Link to this property</a>

4007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2053">Link to this property</a>

4008

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2054">Link to this property</a>

4009

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2055">Link to this property</a>

4010

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2056">Link to this property</a>

4011

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2057">Link to this property</a>

4012

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2058">Link to this property</a>

4013

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2059">Link to this property</a>

4014

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2060">Link to this property</a>

4015

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2061">Link to this property</a>

4016

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2062">Link to this property</a>

4017

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2063">Link to this property</a>

4018

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2064">Link to this property</a>

4019

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2065">Link to this property</a>

4020

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2066">Link to this property</a>

4021

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2067">Link to this property</a>

4022

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2068">Link to this property</a>

4023

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2069">Link to this property</a>

5001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2070">Link to this property</a>

5002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2071">Link to this property</a>

5003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2072">Link to this property</a>

5004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2073">Link to this property</a>

102000

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2074">Link to this property</a>

102001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2075">Link to this property</a>

102002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2076">Link to this property</a>

102003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2077">Link to this property</a>

102004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2078">Link to this property</a>

102005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2079">Link to this property</a>

102006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2080">Link to this property</a>

102007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2081">Link to this property</a>

102008

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2082">Link to this property</a>

102009

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2083">Link to this property</a>

102010

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2084">Link to this property</a>

102011

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2085">Link to this property</a>

102012

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2086">Link to this property</a>

102013

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2087">Link to this property</a>

102014

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2088">Link to this property</a>

102015

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2089">Link to this property</a>

102016

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2090">Link to this property</a>

102017

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2091">Link to this property</a>

102018

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2092">Link to this property</a>

102019

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2093">Link to this property</a>

102020

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2094">Link to this property</a>

102021

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2095">Link to this property</a>

102022

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2096">Link to this property</a>

102023

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2097">Link to this property</a>

102024

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2098">Link to this property</a>

102025

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2099">Link to this property</a>

102026

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20100">Link to this property</a>

102027

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20101">Link to this property</a>

102028

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20102">Link to this property</a>

102029

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20103">Link to this property</a>

102030

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20104">Link to this property</a>

102031

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20105">Link to this property</a>

102032

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20106">Link to this property</a>

102033

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20107">Link to this property</a>

102034

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20108">Link to this property</a>

102035

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20109">Link to this property</a>

102036

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20110">Link to this property</a>

102037

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20111">Link to this property</a>

102038

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20112">Link to this property</a>

102039

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20113">Link to this property</a>

102040

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20114">Link to this property</a>

102041

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20115">Link to this property</a>

102042

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20116">Link to this property</a>

102043

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20117">Link to this property</a>

102044

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20118">Link to this property</a>

102045

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20119">Link to this property</a>

102046

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20120">Link to this property</a>

102047

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20121">Link to this property</a>

102048

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20122">Link to this property</a>

102049

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20123">Link to this property</a>

102050

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20124">Link to this property</a>

102051

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20125">Link to this property</a>

102052

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20126">Link to this property</a>

102053

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20127">Link to this property</a>

102054

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20128">Link to this property</a>

102055

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20129">Link to this property</a>

102056

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20130">Link to this property</a>

102057

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20131">Link to this property</a>

102058

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20132">Link to this property</a>

102059

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20133">Link to this property</a>

102060

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20134">Link to this property</a>

102061

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20135">Link to this property</a>

102062

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20136">Link to this property</a>

102063

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20137">Link to this property</a>

102064

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20138">Link to this property</a>

102065

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20139">Link to this property</a>

102066

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20140">Link to this property</a>

102067

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20141">Link to this property</a>

102068

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20142">Link to this property</a>

102069

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20143">Link to this property</a>

102070

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20144">Link to this property</a>

102071

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20145">Link to this property</a>

102072

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20146">Link to this property</a>

103001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20147">Link to this property</a>

103002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20148">Link to this property</a>

103003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20149">Link to this property</a>

103004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20150">Link to this property</a>

103005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20151">Link to this property</a>

103006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20152">Link to this property</a>

103007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20153">Link to this property</a>

103008

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20154">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

meta: optional object {l10n\_key, loggable\_error, template\_data, trace\_id }

</summary>

l10n\_key: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20meta%20%3E%20(property)%20l10n_key">Link to this property</a>

loggable\_error: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20meta%20%3E%20(property)%20loggable_error">Link to this property</a>

template\_data: optional unknown

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20meta%20%3E%20(property)%20template_data">Link to this property</a>

trace\_id: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20meta%20%3E%20(property)%20trace_id">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

source: optional object {parameter, parameter\_value\_index, pointer }

</summary>

parameter: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20parameter">Link to this property</a>

parameter\_value\_index: optional number

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20parameter_value_index">Link to this property</a>

pointer: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

includes\_discoveries\_until: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20includes_discoveries_until">Link to this property</a>

last\_attempted\_update\_at: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20last_attempted_update_at">Link to this property</a>

last\_successful\_update\_at: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)%20%3E%20(property)%20last_successful_update_at">Link to this property</a>

</details>

[Link to this property](<#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_create_response%20%3E%20(schema)>)

<details>

<summary>

CatalogSyncUpdateResponse object {id, description, destination\_id, 9 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

description: string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

destination\_id: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20destination_id">Link to this property</a>

<details>

<summary>

destination\_type: "NONE"or "ZERO\_TRUST\_LIST"

</summary>

One of the following:

"NONE"

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20destination_type%20%3E%20(member)%200">Link to this property</a>

"ZERO\_TRUST\_LIST"

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20destination_type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20destination_type">Link to this property</a>

last\_user\_update\_at: string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20last_user_update_at">Link to this property</a>

name: string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

policy: string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20policy">Link to this property</a>

<details>

<summary>

update\_mode: "AUTO"or "MANUAL"

</summary>

One of the following:

"AUTO"

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20update_mode%20%3E%20(member)%200">Link to this property</a>

"MANUAL"

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20update_mode%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20update_mode">Link to this property</a>

<details>

<summary>

errors: optional map\[object {code, message, documentation\_url, 2 more } ]

</summary>

<details>

<summary>

code: 1001or 1002or 1003or 152 more

</summary>

One of the following:

1001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%200">Link to this property</a>

1002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%201">Link to this property</a>

1003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%202">Link to this property</a>

1004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%203">Link to this property</a>

1005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%204">Link to this property</a>

1006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%205">Link to this property</a>

1007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%206">Link to this property</a>

1008

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%207">Link to this property</a>

1009

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%208">Link to this property</a>

1010

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%209">Link to this property</a>

1011

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2010">Link to this property</a>

1012

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2011">Link to this property</a>

1013

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2012">Link to this property</a>

1014

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2013">Link to this property</a>

1015

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2014">Link to this property</a>

1016

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2015">Link to this property</a>

1017

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2016">Link to this property</a>

1018

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2017">Link to this property</a>

2001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2018">Link to this property</a>

2002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2019">Link to this property</a>

2003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2020">Link to this property</a>

2004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2021">Link to this property</a>

2005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2022">Link to this property</a>

2006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2023">Link to this property</a>

2007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2024">Link to this property</a>

2008

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2025">Link to this property</a>

2009

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2026">Link to this property</a>

2010

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2027">Link to this property</a>

2011

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2028">Link to this property</a>

2012

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2029">Link to this property</a>

2013

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2030">Link to this property</a>

2014

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2031">Link to this property</a>

2015

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2032">Link to this property</a>

2016

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2033">Link to this property</a>

2017

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2034">Link to this property</a>

2018

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2035">Link to this property</a>

2019

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2036">Link to this property</a>

2020

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2037">Link to this property</a>

2021

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2038">Link to this property</a>

2022

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2039">Link to this property</a>

3001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2040">Link to this property</a>

3002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2041">Link to this property</a>

3003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2042">Link to this property</a>

3004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2043">Link to this property</a>

3005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2044">Link to this property</a>

3006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2045">Link to this property</a>

3007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2046">Link to this property</a>

4001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2047">Link to this property</a>

4002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2048">Link to this property</a>

4003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2049">Link to this property</a>

4004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2050">Link to this property</a>

4005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2051">Link to this property</a>

4006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2052">Link to this property</a>

4007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2053">Link to this property</a>

4008

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2054">Link to this property</a>

4009

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2055">Link to this property</a>

4010

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2056">Link to this property</a>

4011

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2057">Link to this property</a>

4012

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2058">Link to this property</a>

4013

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2059">Link to this property</a>

4014

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2060">Link to this property</a>

4015

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2061">Link to this property</a>

4016

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2062">Link to this property</a>

4017

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2063">Link to this property</a>

4018

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2064">Link to this property</a>

4019

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2065">Link to this property</a>

4020

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2066">Link to this property</a>

4021

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2067">Link to this property</a>

4022

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2068">Link to this property</a>

4023

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2069">Link to this property</a>

5001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2070">Link to this property</a>

5002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2071">Link to this property</a>

5003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2072">Link to this property</a>

5004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2073">Link to this property</a>

102000

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2074">Link to this property</a>

102001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2075">Link to this property</a>

102002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2076">Link to this property</a>

102003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2077">Link to this property</a>

102004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2078">Link to this property</a>

102005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2079">Link to this property</a>

102006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2080">Link to this property</a>

102007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2081">Link to this property</a>

102008

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2082">Link to this property</a>

102009

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2083">Link to this property</a>

102010

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2084">Link to this property</a>

102011

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2085">Link to this property</a>

102012

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2086">Link to this property</a>

102013

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2087">Link to this property</a>

102014

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2088">Link to this property</a>

102015

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2089">Link to this property</a>

102016

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2090">Link to this property</a>

102017

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2091">Link to this property</a>

102018

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2092">Link to this property</a>

102019

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2093">Link to this property</a>

102020

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2094">Link to this property</a>

102021

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2095">Link to this property</a>

102022

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2096">Link to this property</a>

102023

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2097">Link to this property</a>

102024

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2098">Link to this property</a>

102025

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2099">Link to this property</a>

102026

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20100">Link to this property</a>

102027

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20101">Link to this property</a>

102028

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20102">Link to this property</a>

102029

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20103">Link to this property</a>

102030

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20104">Link to this property</a>

102031

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20105">Link to this property</a>

102032

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20106">Link to this property</a>

102033

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20107">Link to this property</a>

102034

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20108">Link to this property</a>

102035

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20109">Link to this property</a>

102036

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20110">Link to this property</a>

102037

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20111">Link to this property</a>

102038

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20112">Link to this property</a>

102039

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20113">Link to this property</a>

102040

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20114">Link to this property</a>

102041

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20115">Link to this property</a>

102042

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20116">Link to this property</a>

102043

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20117">Link to this property</a>

102044

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20118">Link to this property</a>

102045

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20119">Link to this property</a>

102046

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20120">Link to this property</a>

102047

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20121">Link to this property</a>

102048

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20122">Link to this property</a>

102049

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20123">Link to this property</a>

102050

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20124">Link to this property</a>

102051

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20125">Link to this property</a>

102052

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20126">Link to this property</a>

102053

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20127">Link to this property</a>

102054

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20128">Link to this property</a>

102055

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20129">Link to this property</a>

102056

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20130">Link to this property</a>

102057

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20131">Link to this property</a>

102058

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20132">Link to this property</a>

102059

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20133">Link to this property</a>

102060

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20134">Link to this property</a>

102061

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20135">Link to this property</a>

102062

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20136">Link to this property</a>

102063

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20137">Link to this property</a>

102064

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20138">Link to this property</a>

102065

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20139">Link to this property</a>

102066

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20140">Link to this property</a>

102067

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20141">Link to this property</a>

102068

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20142">Link to this property</a>

102069

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20143">Link to this property</a>

102070

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20144">Link to this property</a>

102071

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20145">Link to this property</a>

102072

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20146">Link to this property</a>

103001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20147">Link to this property</a>

103002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20148">Link to this property</a>

103003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20149">Link to this property</a>

103004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20150">Link to this property</a>

103005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20151">Link to this property</a>

103006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20152">Link to this property</a>

103007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20153">Link to this property</a>

103008

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20154">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

meta: optional object {l10n\_key, loggable\_error, template\_data, trace\_id }

</summary>

l10n\_key: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20meta%20%3E%20(property)%20l10n_key">Link to this property</a>

loggable\_error: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20meta%20%3E%20(property)%20loggable_error">Link to this property</a>

template\_data: optional unknown

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20meta%20%3E%20(property)%20template_data">Link to this property</a>

trace\_id: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20meta%20%3E%20(property)%20trace_id">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

source: optional object {parameter, parameter\_value\_index, pointer }

</summary>

parameter: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20parameter">Link to this property</a>

parameter\_value\_index: optional number

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20parameter_value_index">Link to this property</a>

pointer: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

includes\_discoveries\_until: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20includes_discoveries_until">Link to this property</a>

last\_attempted\_update\_at: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20last_attempted_update_at">Link to this property</a>

last\_successful\_update\_at: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)%20%3E%20(property)%20last_successful_update_at">Link to this property</a>

</details>

[Link to this property](<#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_update_response%20%3E%20(schema)>)

<details>

<summary>

CatalogSyncEditResponse object {id, description, destination\_id, 9 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

description: string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

destination\_id: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20destination_id">Link to this property</a>

<details>

<summary>

destination\_type: "NONE"or "ZERO\_TRUST\_LIST"

</summary>

One of the following:

"NONE"

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20destination_type%20%3E%20(member)%200">Link to this property</a>

"ZERO\_TRUST\_LIST"

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20destination_type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20destination_type">Link to this property</a>

last\_user\_update\_at: string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20last_user_update_at">Link to this property</a>

name: string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

policy: string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20policy">Link to this property</a>

<details>

<summary>

update\_mode: "AUTO"or "MANUAL"

</summary>

One of the following:

"AUTO"

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20update_mode%20%3E%20(member)%200">Link to this property</a>

"MANUAL"

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20update_mode%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20update_mode">Link to this property</a>

<details>

<summary>

errors: optional map\[object {code, message, documentation\_url, 2 more } ]

</summary>

<details>

<summary>

code: 1001or 1002or 1003or 152 more

</summary>

One of the following:

1001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%200">Link to this property</a>

1002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%201">Link to this property</a>

1003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%202">Link to this property</a>

1004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%203">Link to this property</a>

1005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%204">Link to this property</a>

1006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%205">Link to this property</a>

1007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%206">Link to this property</a>

1008

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%207">Link to this property</a>

1009

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%208">Link to this property</a>

1010

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%209">Link to this property</a>

1011

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2010">Link to this property</a>

1012

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2011">Link to this property</a>

1013

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2012">Link to this property</a>

1014

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2013">Link to this property</a>

1015

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2014">Link to this property</a>

1016

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2015">Link to this property</a>

1017

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2016">Link to this property</a>

1018

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2017">Link to this property</a>

2001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2018">Link to this property</a>

2002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2019">Link to this property</a>

2003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2020">Link to this property</a>

2004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2021">Link to this property</a>

2005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2022">Link to this property</a>

2006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2023">Link to this property</a>

2007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2024">Link to this property</a>

2008

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2025">Link to this property</a>

2009

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2026">Link to this property</a>

2010

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2027">Link to this property</a>

2011

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2028">Link to this property</a>

2012

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2029">Link to this property</a>

2013

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2030">Link to this property</a>

2014

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2031">Link to this property</a>

2015

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2032">Link to this property</a>

2016

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2033">Link to this property</a>

2017

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2034">Link to this property</a>

2018

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2035">Link to this property</a>

2019

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2036">Link to this property</a>

2020

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2037">Link to this property</a>

2021

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2038">Link to this property</a>

2022

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2039">Link to this property</a>

3001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2040">Link to this property</a>

3002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2041">Link to this property</a>

3003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2042">Link to this property</a>

3004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2043">Link to this property</a>

3005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2044">Link to this property</a>

3006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2045">Link to this property</a>

3007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2046">Link to this property</a>

4001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2047">Link to this property</a>

4002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2048">Link to this property</a>

4003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2049">Link to this property</a>

4004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2050">Link to this property</a>

4005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2051">Link to this property</a>

4006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2052">Link to this property</a>

4007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2053">Link to this property</a>

4008

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2054">Link to this property</a>

4009

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2055">Link to this property</a>

4010

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2056">Link to this property</a>

4011

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2057">Link to this property</a>

4012

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2058">Link to this property</a>

4013

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2059">Link to this property</a>

4014

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2060">Link to this property</a>

4015

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2061">Link to this property</a>

4016

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2062">Link to this property</a>

4017

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2063">Link to this property</a>

4018

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2064">Link to this property</a>

4019

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2065">Link to this property</a>

4020

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2066">Link to this property</a>

4021

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2067">Link to this property</a>

4022

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2068">Link to this property</a>

4023

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2069">Link to this property</a>

5001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2070">Link to this property</a>

5002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2071">Link to this property</a>

5003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2072">Link to this property</a>

5004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2073">Link to this property</a>

102000

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2074">Link to this property</a>

102001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2075">Link to this property</a>

102002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2076">Link to this property</a>

102003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2077">Link to this property</a>

102004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2078">Link to this property</a>

102005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2079">Link to this property</a>

102006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2080">Link to this property</a>

102007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2081">Link to this property</a>

102008

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2082">Link to this property</a>

102009

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2083">Link to this property</a>

102010

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2084">Link to this property</a>

102011

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2085">Link to this property</a>

102012

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2086">Link to this property</a>

102013

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2087">Link to this property</a>

102014

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2088">Link to this property</a>

102015

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2089">Link to this property</a>

102016

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2090">Link to this property</a>

102017

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2091">Link to this property</a>

102018

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2092">Link to this property</a>

102019

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2093">Link to this property</a>

102020

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2094">Link to this property</a>

102021

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2095">Link to this property</a>

102022

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2096">Link to this property</a>

102023

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2097">Link to this property</a>

102024

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2098">Link to this property</a>

102025

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%2099">Link to this property</a>

102026

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20100">Link to this property</a>

102027

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20101">Link to this property</a>

102028

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20102">Link to this property</a>

102029

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20103">Link to this property</a>

102030

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20104">Link to this property</a>

102031

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20105">Link to this property</a>

102032

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20106">Link to this property</a>

102033

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20107">Link to this property</a>

102034

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20108">Link to this property</a>

102035

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20109">Link to this property</a>

102036

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20110">Link to this property</a>

102037

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20111">Link to this property</a>

102038

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20112">Link to this property</a>

102039

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20113">Link to this property</a>

102040

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20114">Link to this property</a>

102041

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20115">Link to this property</a>

102042

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20116">Link to this property</a>

102043

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20117">Link to this property</a>

102044

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20118">Link to this property</a>

102045

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20119">Link to this property</a>

102046

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20120">Link to this property</a>

102047

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20121">Link to this property</a>

102048

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20122">Link to this property</a>

102049

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20123">Link to this property</a>

102050

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20124">Link to this property</a>

102051

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20125">Link to this property</a>

102052

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20126">Link to this property</a>

102053

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20127">Link to this property</a>

102054

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20128">Link to this property</a>

102055

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20129">Link to this property</a>

102056

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20130">Link to this property</a>

102057

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20131">Link to this property</a>

102058

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20132">Link to this property</a>

102059

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20133">Link to this property</a>

102060

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20134">Link to this property</a>

102061

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20135">Link to this property</a>

102062

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20136">Link to this property</a>

102063

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20137">Link to this property</a>

102064

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20138">Link to this property</a>

102065

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20139">Link to this property</a>

102066

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20140">Link to this property</a>

102067

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20141">Link to this property</a>

102068

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20142">Link to this property</a>

102069

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20143">Link to this property</a>

102070

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20144">Link to this property</a>

102071

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20145">Link to this property</a>

102072

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20146">Link to this property</a>

103001

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20147">Link to this property</a>

103002

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20148">Link to this property</a>

103003

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20149">Link to this property</a>

103004

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20150">Link to this property</a>

103005

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20151">Link to this property</a>

103006

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20152">Link to this property</a>

103007

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20153">Link to this property</a>

103008

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code%20%3E%20(member)%20154">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

meta: optional object {l10n\_key, loggable\_error, template\_data, trace\_id }

</summary>

l10n\_key: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20meta%20%3E%20(property)%20l10n_key">Link to this property</a>

loggable\_error: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20meta%20%3E%20(property)%20loggable_error">Link to this property</a>

template\_data: optional unknown

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20meta%20%3E%20(property)%20template_data">Link to this property</a>

trace\_id: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20meta%20%3E%20(property)%20trace_id">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

source: optional object {parameter, parameter\_value\_index, pointer }

</summary>

parameter: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20parameter">Link to this property</a>

parameter\_value\_index: optional number

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20parameter_value_index">Link to this property</a>

pointer: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

includes\_discoveries\_until: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20includes_discoveries_until">Link to this property</a>

last\_attempted\_update\_at: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20last_attempted_update_at">Link to this property</a>

last\_successful\_update\_at: optional string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)%20%3E%20(property)%20last_successful_update_at">Link to this property</a>

</details>

[Link to this property](<#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_edit_response%20%3E%20(schema)>)

<details>

<summary>

CatalogSyncDeleteResponse object {id }

</summary>

id: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_delete_response%20%3E%20(schema)>)

CatalogSyncRefreshResponse = string

[Link to this property](<#(resource)%20magic_cloud_networking.catalog_syncs%20%3E%20(model)%20catalog_sync_refresh_response%20%3E%20(schema)>)

#### Catalog SyncsPrebuilt Policies

##### [List Prebuilt Policies](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/catalog_syncs/subresources/prebuilt_policies/methods/list)

GET/accounts/{account\_id}/magic/cloud/catalog-syncs/prebuilt-policies

##### ModelsExpand Collapse

<details>

<summary>

PrebuiltPolicyListResponse object {applicable\_destinations, policy\_description, policy\_name, policy\_string }

</summary>

<details>

<summary>

applicable\_destinations: array of "NONE"or "ZERO\_TRUST\_LIST"

</summary>

One of the following:

"NONE"

<a href="#(resource)%20magic_cloud_networking.catalog_syncs.prebuilt_policies%20%3E%20(model)%20prebuilt_policy_list_response%20%3E%20(schema)%20%3E%20(property)%20applicable_destinations%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"ZERO\_TRUST\_LIST"

<a href="#(resource)%20magic_cloud_networking.catalog_syncs.prebuilt_policies%20%3E%20(model)%20prebuilt_policy_list_response%20%3E%20(schema)%20%3E%20(property)%20applicable_destinations%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.catalog_syncs.prebuilt_policies%20%3E%20(model)%20prebuilt_policy_list_response%20%3E%20(schema)%20%3E%20(property)%20applicable_destinations">Link to this property</a>

policy\_description: string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs.prebuilt_policies%20%3E%20(model)%20prebuilt_policy_list_response%20%3E%20(schema)%20%3E%20(property)%20policy_description">Link to this property</a>

policy\_name: string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs.prebuilt_policies%20%3E%20(model)%20prebuilt_policy_list_response%20%3E%20(schema)%20%3E%20(property)%20policy_name">Link to this property</a>

policy\_string: string

<a href="#(resource)%20magic_cloud_networking.catalog_syncs.prebuilt_policies%20%3E%20(model)%20prebuilt_policy_list_response%20%3E%20(schema)%20%3E%20(property)%20policy_string">Link to this property</a>

</details>

[Link to this property](<#(resource)%20magic_cloud_networking.catalog_syncs.prebuilt_policies%20%3E%20(model)%20prebuilt_policy_list_response%20%3E%20(schema)>)