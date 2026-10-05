---
title: Resources
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Magic Cloud Networking](https://developers.cloudflare.com/api/resources/magic_cloud_networking)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Resources

##### [List Resources](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/resources/methods/list)

GET/accounts/{account\_id}/magic/cloud/resources

##### [Read Resource](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/resources/methods/get)

GET/accounts/{account\_id}/magic/cloud/resources/{resource\_id}

##### [Export Resources](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/resources/methods/export)

GET/accounts/{account\_id}/magic/cloud/resources/export

##### [Preview Rego Query](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/resources/methods/policy_preview)

POST/accounts/{account\_id}/magic/cloud/resources/policy-preview

##### ModelsExpand Collapse

<details>

<summary>

ResourceListResponse object {id, account\_id, cloud\_type, 18 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

account\_id: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20account_id">Link to this property</a>

<details>

<summary>

cloud\_type: "AWS"or "AZURE"or "GOOGLE"or "CLOUDFLARE"

</summary>

One of the following:

"AWS"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20cloud_type%20%3E%20(member)%200">Link to this property</a>

"AZURE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20cloud_type%20%3E%20(member)%201">Link to this property</a>

"GOOGLE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20cloud_type%20%3E%20(member)%202">Link to this property</a>

"CLOUDFLARE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20cloud_type%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20cloud_type">Link to this property</a>

config: map\[unknown]

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20config">Link to this property</a>

deployment\_provider: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20deployment_provider">Link to this property</a>

managed: boolean

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20managed">Link to this property</a>

<details>

<summary>

monthly\_cost\_estimate: object {currency, monthly\_cost }

</summary>

currency: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20monthly_cost_estimate%20%3E%20(property)%20currency">Link to this property</a>

monthly\_cost: number

formatdouble

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20monthly_cost_estimate%20%3E%20(property)%20monthly_cost">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20monthly_cost_estimate">Link to this property</a>

name: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

native\_id: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20native_id">Link to this property</a>

<details>

<summary>

observations: map\[object {first\_observed\_at, last\_observed\_at, provider\_id, resource\_id } ]

</summary>

first\_observed\_at: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20observations%20%3E%20(items)%20%3E%20(property)%20first_observed_at">Link to this property</a>

last\_observed\_at: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20observations%20%3E%20(items)%20%3E%20(property)%20last_observed_at">Link to this property</a>

provider\_id: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20observations%20%3E%20(items)%20%3E%20(property)%20provider_id">Link to this property</a>

resource\_id: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20observations%20%3E%20(items)%20%3E%20(property)%20resource_id">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20observations">Link to this property</a>

provider\_ids: array of string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20provider_ids">Link to this property</a>

provider\_names\_by\_id: map\[string]

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20provider_names_by_id">Link to this property</a>

region: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20region">Link to this property</a>

resource\_group: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_group">Link to this property</a>

<details>

<summary>

resource\_type: "aws\_customer\_gateway"or "aws\_egress\_only\_internet\_gateway"or "aws\_internet\_gateway"or 54 more

</summary>

One of the following:

"aws\_customer\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%200">Link to this property</a>

"aws\_egress\_only\_internet\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%201">Link to this property</a>

"aws\_internet\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%202">Link to this property</a>

"aws\_instance"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%203">Link to this property</a>

"aws\_network\_interface"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%204">Link to this property</a>

"aws\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%205">Link to this property</a>

"aws\_route\_table"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%206">Link to this property</a>

"aws\_route\_table\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%207">Link to this property</a>

"aws\_subnet"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%208">Link to this property</a>

"aws\_vpc"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%209">Link to this property</a>

"aws\_vpc\_ipv4\_cidr\_block\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2010">Link to this property</a>

"aws\_vpn\_connection"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2011">Link to this property</a>

"aws\_vpn\_connection\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2012">Link to this property</a>

"aws\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2013">Link to this property</a>

"aws\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2014">Link to this property</a>

"aws\_vpc\_security\_group\_ingress\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2015">Link to this property</a>

"aws\_vpc\_security\_group\_egress\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2016">Link to this property</a>

"aws\_ec2\_managed\_prefix\_list"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2017">Link to this property</a>

"aws\_ec2\_transit\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2018">Link to this property</a>

"aws\_ec2\_transit\_gateway\_prefix\_list\_reference"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2019">Link to this property</a>

"aws\_ec2\_transit\_gateway\_vpc\_attachment"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2020">Link to this property</a>

"azurerm\_application\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2021">Link to this property</a>

"azurerm\_lb"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2022">Link to this property</a>

"azurerm\_lb\_backend\_address\_pool"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2023">Link to this property</a>

"azurerm\_lb\_nat\_pool"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2024">Link to this property</a>

"azurerm\_lb\_nat\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2025">Link to this property</a>

"azurerm\_lb\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2026">Link to this property</a>

"azurerm\_local\_network\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2027">Link to this property</a>

"azurerm\_network\_interface"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2028">Link to this property</a>

"azurerm\_network\_interface\_application\_security\_group\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2029">Link to this property</a>

"azurerm\_network\_interface\_backend\_address\_pool\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2030">Link to this property</a>

"azurerm\_network\_interface\_security\_group\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2031">Link to this property</a>

"azurerm\_network\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2032">Link to this property</a>

"azurerm\_public\_ip"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2033">Link to this property</a>

"azurerm\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2034">Link to this property</a>

"azurerm\_route\_table"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2035">Link to this property</a>

"azurerm\_subnet"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2036">Link to this property</a>

"azurerm\_subnet\_route\_table\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2037">Link to this property</a>

"azurerm\_virtual\_machine"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2038">Link to this property</a>

"azurerm\_virtual\_network\_gateway\_connection"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2039">Link to this property</a>

"azurerm\_virtual\_network"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2040">Link to this property</a>

"azurerm\_virtual\_network\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2041">Link to this property</a>

"google\_compute\_network"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2042">Link to this property</a>

"google\_compute\_subnetwork"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2043">Link to this property</a>

"google\_compute\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2044">Link to this property</a>

"google\_compute\_vpn\_tunnel"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2045">Link to this property</a>

"google\_compute\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2046">Link to this property</a>

"google\_compute\_address"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2047">Link to this property</a>

"google\_compute\_global\_address"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2048">Link to this property</a>

"google\_compute\_router"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2049">Link to this property</a>

"google\_compute\_interconnect\_attachment"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2050">Link to this property</a>

"google\_compute\_ha\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2051">Link to this property</a>

"google\_compute\_forwarding\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2052">Link to this property</a>

"google\_compute\_network\_firewall\_policy"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2053">Link to this property</a>

"google\_compute\_network\_firewall\_policy\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2054">Link to this property</a>

"cloudflare\_static\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2055">Link to this property</a>

"cloudflare\_ipsec\_tunnel"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2056">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20resource_type">Link to this property</a>

<details>

<summary>

sections: array of object {hidden\_items, name, visible\_items, help\_text }

</summary>

<details>

<summary>

hidden\_items: array of object {helpText, name, value }

</summary>

helpText: optional string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20helpText">Link to this property</a>

name: optional string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

value: optional object {item\_type, string } or object {item\_type, yaml } or object {item\_type, yaml\_diff } or 2 more

</summary>

One of the following:

<details>

<summary>

McnStringItem object {item\_type, string }

</summary>

item\_type: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%200%20%3E%20(property)%20item_type">Link to this property</a>

string: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%200%20%3E%20(property)%20string">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

McnYamlItem object {item\_type, yaml }

</summary>

item\_type: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%201%20%3E%20(property)%20item_type">Link to this property</a>

yaml: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%201%20%3E%20(property)%20yaml">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

McnYamlDiffItem object {item\_type, yaml\_diff }

</summary>

item\_type: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202%20%3E%20(property)%20item_type">Link to this property</a>

<details>

<summary>

yaml\_diff: object {diff, left\_description, left\_yaml, 2 more }

</summary>

diff: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202%20%3E%20(property)%20yaml_diff%20%3E%20(property)%20diff">Link to this property</a>

left\_description: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202%20%3E%20(property)%20yaml_diff%20%3E%20(property)%20left_description">Link to this property</a>

left\_yaml: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202%20%3E%20(property)%20yaml_diff%20%3E%20(property)%20left_yaml">Link to this property</a>

right\_description: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202%20%3E%20(property)%20yaml_diff%20%3E%20(property)%20right_description">Link to this property</a>

right\_yaml: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202%20%3E%20(property)%20yaml_diff%20%3E%20(property)%20right_yaml">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202%20%3E%20(property)%20yaml_diff">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

McnResourcePreviewItem object {item\_type, resource\_preview }

</summary>

item\_type: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20item_type">Link to this property</a>

<details>

<summary>

resource\_preview: object {id, cloud\_type, detail, 3 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

cloud\_type: "AWS"or "AZURE"or "GOOGLE"or "CLOUDFLARE"

</summary>

One of the following:

"AWS"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%200">Link to this property</a>

"AZURE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%201">Link to this property</a>

"GOOGLE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%202">Link to this property</a>

"CLOUDFLARE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type">Link to this property</a>

detail: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20detail">Link to this property</a>

name: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

resource\_type: "aws\_customer\_gateway"or "aws\_egress\_only\_internet\_gateway"or "aws\_internet\_gateway"or 54 more

</summary>

One of the following:

"aws\_customer\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%200">Link to this property</a>

"aws\_egress\_only\_internet\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%201">Link to this property</a>

"aws\_internet\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%202">Link to this property</a>

"aws\_instance"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%203">Link to this property</a>

"aws\_network\_interface"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%204">Link to this property</a>

"aws\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%205">Link to this property</a>

"aws\_route\_table"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%206">Link to this property</a>

"aws\_route\_table\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%207">Link to this property</a>

"aws\_subnet"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%208">Link to this property</a>

"aws\_vpc"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%209">Link to this property</a>

"aws\_vpc\_ipv4\_cidr\_block\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2010">Link to this property</a>

"aws\_vpn\_connection"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2011">Link to this property</a>

"aws\_vpn\_connection\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2012">Link to this property</a>

"aws\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2013">Link to this property</a>

"aws\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2014">Link to this property</a>

"aws\_vpc\_security\_group\_ingress\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2015">Link to this property</a>

"aws\_vpc\_security\_group\_egress\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2016">Link to this property</a>

"aws\_ec2\_managed\_prefix\_list"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2017">Link to this property</a>

"aws\_ec2\_transit\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2018">Link to this property</a>

"aws\_ec2\_transit\_gateway\_prefix\_list\_reference"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2019">Link to this property</a>

"aws\_ec2\_transit\_gateway\_vpc\_attachment"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2020">Link to this property</a>

"azurerm\_application\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2021">Link to this property</a>

"azurerm\_lb"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2022">Link to this property</a>

"azurerm\_lb\_backend\_address\_pool"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2023">Link to this property</a>

"azurerm\_lb\_nat\_pool"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2024">Link to this property</a>

"azurerm\_lb\_nat\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2025">Link to this property</a>

"azurerm\_lb\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2026">Link to this property</a>

"azurerm\_local\_network\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2027">Link to this property</a>

"azurerm\_network\_interface"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2028">Link to this property</a>

"azurerm\_network\_interface\_application\_security\_group\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2029">Link to this property</a>

"azurerm\_network\_interface\_backend\_address\_pool\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2030">Link to this property</a>

"azurerm\_network\_interface\_security\_group\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2031">Link to this property</a>

"azurerm\_network\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2032">Link to this property</a>

"azurerm\_public\_ip"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2033">Link to this property</a>

"azurerm\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2034">Link to this property</a>

"azurerm\_route\_table"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2035">Link to this property</a>

"azurerm\_subnet"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2036">Link to this property</a>

"azurerm\_subnet\_route\_table\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2037">Link to this property</a>

"azurerm\_virtual\_machine"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2038">Link to this property</a>

"azurerm\_virtual\_network\_gateway\_connection"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2039">Link to this property</a>

"azurerm\_virtual\_network"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2040">Link to this property</a>

"azurerm\_virtual\_network\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2041">Link to this property</a>

"google\_compute\_network"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2042">Link to this property</a>

"google\_compute\_subnetwork"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2043">Link to this property</a>

"google\_compute\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2044">Link to this property</a>

"google\_compute\_vpn\_tunnel"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2045">Link to this property</a>

"google\_compute\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2046">Link to this property</a>

"google\_compute\_address"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2047">Link to this property</a>

"google\_compute\_global\_address"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2048">Link to this property</a>

"google\_compute\_router"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2049">Link to this property</a>

"google\_compute\_interconnect\_attachment"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2050">Link to this property</a>

"google\_compute\_ha\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2051">Link to this property</a>

"google\_compute\_forwarding\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2052">Link to this property</a>

"google\_compute\_network\_firewall\_policy"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2053">Link to this property</a>

"google\_compute\_network\_firewall\_policy\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2054">Link to this property</a>

"cloudflare\_static\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2055">Link to this property</a>

"cloudflare\_ipsec\_tunnel"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2056">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type">Link to this property</a>

title: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20title">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

McnListItem object {item\_type, list }

</summary>

item\_type: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20item_type">Link to this property</a>

<details>

<summary>

list: array of object {item\_type, string } or object {item\_type, resource\_preview }

</summary>

One of the following:

<details>

<summary>

McnStringItem object {item\_type, string }

</summary>

item\_type: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20item_type">Link to this property</a>

string: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20string">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

McnResourcePreviewItem object {item\_type, resource\_preview }

</summary>

item\_type: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20item_type">Link to this property</a>

<details>

<summary>

resource\_preview: object {id, cloud\_type, detail, 3 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

cloud\_type: "AWS"or "AZURE"or "GOOGLE"or "CLOUDFLARE"

</summary>

One of the following:

"AWS"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%200">Link to this property</a>

"AZURE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%201">Link to this property</a>

"GOOGLE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%202">Link to this property</a>

"CLOUDFLARE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type">Link to this property</a>

detail: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20detail">Link to this property</a>

name: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

resource\_type: "aws\_customer\_gateway"or "aws\_egress\_only\_internet\_gateway"or "aws\_internet\_gateway"or 54 more

</summary>

One of the following:

"aws\_customer\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%200">Link to this property</a>

"aws\_egress\_only\_internet\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%201">Link to this property</a>

"aws\_internet\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%202">Link to this property</a>

"aws\_instance"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%203">Link to this property</a>

"aws\_network\_interface"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%204">Link to this property</a>

"aws\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%205">Link to this property</a>

"aws\_route\_table"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%206">Link to this property</a>

"aws\_route\_table\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%207">Link to this property</a>

"aws\_subnet"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%208">Link to this property</a>

"aws\_vpc"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%209">Link to this property</a>

"aws\_vpc\_ipv4\_cidr\_block\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2010">Link to this property</a>

"aws\_vpn\_connection"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2011">Link to this property</a>

"aws\_vpn\_connection\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2012">Link to this property</a>

"aws\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2013">Link to this property</a>

"aws\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2014">Link to this property</a>

"aws\_vpc\_security\_group\_ingress\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2015">Link to this property</a>

"aws\_vpc\_security\_group\_egress\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2016">Link to this property</a>

"aws\_ec2\_managed\_prefix\_list"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2017">Link to this property</a>

"aws\_ec2\_transit\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2018">Link to this property</a>

"aws\_ec2\_transit\_gateway\_prefix\_list\_reference"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2019">Link to this property</a>

"aws\_ec2\_transit\_gateway\_vpc\_attachment"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2020">Link to this property</a>

"azurerm\_application\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2021">Link to this property</a>

"azurerm\_lb"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2022">Link to this property</a>

"azurerm\_lb\_backend\_address\_pool"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2023">Link to this property</a>

"azurerm\_lb\_nat\_pool"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2024">Link to this property</a>

"azurerm\_lb\_nat\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2025">Link to this property</a>

"azurerm\_lb\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2026">Link to this property</a>

"azurerm\_local\_network\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2027">Link to this property</a>

"azurerm\_network\_interface"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2028">Link to this property</a>

"azurerm\_network\_interface\_application\_security\_group\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2029">Link to this property</a>

"azurerm\_network\_interface\_backend\_address\_pool\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2030">Link to this property</a>

"azurerm\_network\_interface\_security\_group\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2031">Link to this property</a>

"azurerm\_network\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2032">Link to this property</a>

"azurerm\_public\_ip"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2033">Link to this property</a>

"azurerm\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2034">Link to this property</a>

"azurerm\_route\_table"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2035">Link to this property</a>

"azurerm\_subnet"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2036">Link to this property</a>

"azurerm\_subnet\_route\_table\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2037">Link to this property</a>

"azurerm\_virtual\_machine"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2038">Link to this property</a>

"azurerm\_virtual\_network\_gateway\_connection"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2039">Link to this property</a>

"azurerm\_virtual\_network"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2040">Link to this property</a>

"azurerm\_virtual\_network\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2041">Link to this property</a>

"google\_compute\_network"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2042">Link to this property</a>

"google\_compute\_subnetwork"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2043">Link to this property</a>

"google\_compute\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2044">Link to this property</a>

"google\_compute\_vpn\_tunnel"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2045">Link to this property</a>

"google\_compute\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2046">Link to this property</a>

"google\_compute\_address"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2047">Link to this property</a>

"google\_compute\_global\_address"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2048">Link to this property</a>

"google\_compute\_router"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2049">Link to this property</a>

"google\_compute\_interconnect\_attachment"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2050">Link to this property</a>

"google\_compute\_ha\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2051">Link to this property</a>

"google\_compute\_forwarding\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2052">Link to this property</a>

"google\_compute\_network\_firewall\_policy"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2053">Link to this property</a>

"google\_compute\_network\_firewall\_policy\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2054">Link to this property</a>

"cloudflare\_static\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2055">Link to this property</a>

"cloudflare\_ipsec\_tunnel"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2056">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type">Link to this property</a>

title: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20title">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items">Link to this property</a>

name: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

visible\_items: array of object {helpText, name, value }

</summary>

helpText: optional string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20helpText">Link to this property</a>

name: optional string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

value: optional object {item\_type, string } or object {item\_type, yaml } or object {item\_type, yaml\_diff } or 2 more

</summary>

One of the following:

<details>

<summary>

McnStringItem object {item\_type, string }

</summary>

item\_type: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%200%20%3E%20(property)%20item_type">Link to this property</a>

string: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%200%20%3E%20(property)%20string">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

McnYamlItem object {item\_type, yaml }

</summary>

item\_type: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%201%20%3E%20(property)%20item_type">Link to this property</a>

yaml: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%201%20%3E%20(property)%20yaml">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

McnYamlDiffItem object {item\_type, yaml\_diff }

</summary>

item\_type: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202%20%3E%20(property)%20item_type">Link to this property</a>

<details>

<summary>

yaml\_diff: object {diff, left\_description, left\_yaml, 2 more }

</summary>

diff: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202%20%3E%20(property)%20yaml_diff%20%3E%20(property)%20diff">Link to this property</a>

left\_description: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202%20%3E%20(property)%20yaml_diff%20%3E%20(property)%20left_description">Link to this property</a>

left\_yaml: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202%20%3E%20(property)%20yaml_diff%20%3E%20(property)%20left_yaml">Link to this property</a>

right\_description: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202%20%3E%20(property)%20yaml_diff%20%3E%20(property)%20right_description">Link to this property</a>

right\_yaml: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202%20%3E%20(property)%20yaml_diff%20%3E%20(property)%20right_yaml">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202%20%3E%20(property)%20yaml_diff">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

McnResourcePreviewItem object {item\_type, resource\_preview }

</summary>

item\_type: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20item_type">Link to this property</a>

<details>

<summary>

resource\_preview: object {id, cloud\_type, detail, 3 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

cloud\_type: "AWS"or "AZURE"or "GOOGLE"or "CLOUDFLARE"

</summary>

One of the following:

"AWS"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%200">Link to this property</a>

"AZURE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%201">Link to this property</a>

"GOOGLE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%202">Link to this property</a>

"CLOUDFLARE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type">Link to this property</a>

detail: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20detail">Link to this property</a>

name: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

resource\_type: "aws\_customer\_gateway"or "aws\_egress\_only\_internet\_gateway"or "aws\_internet\_gateway"or 54 more

</summary>

One of the following:

"aws\_customer\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%200">Link to this property</a>

"aws\_egress\_only\_internet\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%201">Link to this property</a>

"aws\_internet\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%202">Link to this property</a>

"aws\_instance"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%203">Link to this property</a>

"aws\_network\_interface"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%204">Link to this property</a>

"aws\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%205">Link to this property</a>

"aws\_route\_table"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%206">Link to this property</a>

"aws\_route\_table\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%207">Link to this property</a>

"aws\_subnet"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%208">Link to this property</a>

"aws\_vpc"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%209">Link to this property</a>

"aws\_vpc\_ipv4\_cidr\_block\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2010">Link to this property</a>

"aws\_vpn\_connection"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2011">Link to this property</a>

"aws\_vpn\_connection\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2012">Link to this property</a>

"aws\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2013">Link to this property</a>

"aws\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2014">Link to this property</a>

"aws\_vpc\_security\_group\_ingress\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2015">Link to this property</a>

"aws\_vpc\_security\_group\_egress\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2016">Link to this property</a>

"aws\_ec2\_managed\_prefix\_list"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2017">Link to this property</a>

"aws\_ec2\_transit\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2018">Link to this property</a>

"aws\_ec2\_transit\_gateway\_prefix\_list\_reference"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2019">Link to this property</a>

"aws\_ec2\_transit\_gateway\_vpc\_attachment"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2020">Link to this property</a>

"azurerm\_application\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2021">Link to this property</a>

"azurerm\_lb"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2022">Link to this property</a>

"azurerm\_lb\_backend\_address\_pool"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2023">Link to this property</a>

"azurerm\_lb\_nat\_pool"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2024">Link to this property</a>

"azurerm\_lb\_nat\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2025">Link to this property</a>

"azurerm\_lb\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2026">Link to this property</a>

"azurerm\_local\_network\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2027">Link to this property</a>

"azurerm\_network\_interface"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2028">Link to this property</a>

"azurerm\_network\_interface\_application\_security\_group\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2029">Link to this property</a>

"azurerm\_network\_interface\_backend\_address\_pool\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2030">Link to this property</a>

"azurerm\_network\_interface\_security\_group\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2031">Link to this property</a>

"azurerm\_network\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2032">Link to this property</a>

"azurerm\_public\_ip"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2033">Link to this property</a>

"azurerm\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2034">Link to this property</a>

"azurerm\_route\_table"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2035">Link to this property</a>

"azurerm\_subnet"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2036">Link to this property</a>

"azurerm\_subnet\_route\_table\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2037">Link to this property</a>

"azurerm\_virtual\_machine"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2038">Link to this property</a>

"azurerm\_virtual\_network\_gateway\_connection"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2039">Link to this property</a>

"azurerm\_virtual\_network"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2040">Link to this property</a>

"azurerm\_virtual\_network\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2041">Link to this property</a>

"google\_compute\_network"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2042">Link to this property</a>

"google\_compute\_subnetwork"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2043">Link to this property</a>

"google\_compute\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2044">Link to this property</a>

"google\_compute\_vpn\_tunnel"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2045">Link to this property</a>

"google\_compute\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2046">Link to this property</a>

"google\_compute\_address"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2047">Link to this property</a>

"google\_compute\_global\_address"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2048">Link to this property</a>

"google\_compute\_router"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2049">Link to this property</a>

"google\_compute\_interconnect\_attachment"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2050">Link to this property</a>

"google\_compute\_ha\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2051">Link to this property</a>

"google\_compute\_forwarding\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2052">Link to this property</a>

"google\_compute\_network\_firewall\_policy"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2053">Link to this property</a>

"google\_compute\_network\_firewall\_policy\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2054">Link to this property</a>

"cloudflare\_static\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2055">Link to this property</a>

"cloudflare\_ipsec\_tunnel"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2056">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type">Link to this property</a>

title: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20title">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

McnListItem object {item\_type, list }

</summary>

item\_type: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20item_type">Link to this property</a>

<details>

<summary>

list: array of object {item\_type, string } or object {item\_type, resource\_preview }

</summary>

One of the following:

<details>

<summary>

McnStringItem object {item\_type, string }

</summary>

item\_type: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20item_type">Link to this property</a>

string: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20string">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

McnResourcePreviewItem object {item\_type, resource\_preview }

</summary>

item\_type: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20item_type">Link to this property</a>

<details>

<summary>

resource\_preview: object {id, cloud\_type, detail, 3 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

cloud\_type: "AWS"or "AZURE"or "GOOGLE"or "CLOUDFLARE"

</summary>

One of the following:

"AWS"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%200">Link to this property</a>

"AZURE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%201">Link to this property</a>

"GOOGLE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%202">Link to this property</a>

"CLOUDFLARE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type">Link to this property</a>

detail: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20detail">Link to this property</a>

name: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

resource\_type: "aws\_customer\_gateway"or "aws\_egress\_only\_internet\_gateway"or "aws\_internet\_gateway"or 54 more

</summary>

One of the following:

"aws\_customer\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%200">Link to this property</a>

"aws\_egress\_only\_internet\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%201">Link to this property</a>

"aws\_internet\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%202">Link to this property</a>

"aws\_instance"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%203">Link to this property</a>

"aws\_network\_interface"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%204">Link to this property</a>

"aws\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%205">Link to this property</a>

"aws\_route\_table"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%206">Link to this property</a>

"aws\_route\_table\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%207">Link to this property</a>

"aws\_subnet"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%208">Link to this property</a>

"aws\_vpc"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%209">Link to this property</a>

"aws\_vpc\_ipv4\_cidr\_block\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2010">Link to this property</a>

"aws\_vpn\_connection"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2011">Link to this property</a>

"aws\_vpn\_connection\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2012">Link to this property</a>

"aws\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2013">Link to this property</a>

"aws\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2014">Link to this property</a>

"aws\_vpc\_security\_group\_ingress\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2015">Link to this property</a>

"aws\_vpc\_security\_group\_egress\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2016">Link to this property</a>

"aws\_ec2\_managed\_prefix\_list"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2017">Link to this property</a>

"aws\_ec2\_transit\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2018">Link to this property</a>

"aws\_ec2\_transit\_gateway\_prefix\_list\_reference"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2019">Link to this property</a>

"aws\_ec2\_transit\_gateway\_vpc\_attachment"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2020">Link to this property</a>

"azurerm\_application\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2021">Link to this property</a>

"azurerm\_lb"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2022">Link to this property</a>

"azurerm\_lb\_backend\_address\_pool"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2023">Link to this property</a>

"azurerm\_lb\_nat\_pool"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2024">Link to this property</a>

"azurerm\_lb\_nat\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2025">Link to this property</a>

"azurerm\_lb\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2026">Link to this property</a>

"azurerm\_local\_network\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2027">Link to this property</a>

"azurerm\_network\_interface"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2028">Link to this property</a>

"azurerm\_network\_interface\_application\_security\_group\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2029">Link to this property</a>

"azurerm\_network\_interface\_backend\_address\_pool\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2030">Link to this property</a>

"azurerm\_network\_interface\_security\_group\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2031">Link to this property</a>

"azurerm\_network\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2032">Link to this property</a>

"azurerm\_public\_ip"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2033">Link to this property</a>

"azurerm\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2034">Link to this property</a>

"azurerm\_route\_table"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2035">Link to this property</a>

"azurerm\_subnet"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2036">Link to this property</a>

"azurerm\_subnet\_route\_table\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2037">Link to this property</a>

"azurerm\_virtual\_machine"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2038">Link to this property</a>

"azurerm\_virtual\_network\_gateway\_connection"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2039">Link to this property</a>

"azurerm\_virtual\_network"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2040">Link to this property</a>

"azurerm\_virtual\_network\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2041">Link to this property</a>

"google\_compute\_network"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2042">Link to this property</a>

"google\_compute\_subnetwork"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2043">Link to this property</a>

"google\_compute\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2044">Link to this property</a>

"google\_compute\_vpn\_tunnel"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2045">Link to this property</a>

"google\_compute\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2046">Link to this property</a>

"google\_compute\_address"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2047">Link to this property</a>

"google\_compute\_global\_address"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2048">Link to this property</a>

"google\_compute\_router"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2049">Link to this property</a>

"google\_compute\_interconnect\_attachment"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2050">Link to this property</a>

"google\_compute\_ha\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2051">Link to this property</a>

"google\_compute\_forwarding\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2052">Link to this property</a>

"google\_compute\_network\_firewall\_policy"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2053">Link to this property</a>

"google\_compute\_network\_firewall\_policy\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2054">Link to this property</a>

"cloudflare\_static\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2055">Link to this property</a>

"cloudflare\_ipsec\_tunnel"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2056">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type">Link to this property</a>

title: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20title">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items">Link to this property</a>

help\_text: optional string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20help_text">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20sections">Link to this property</a>

state: map\[unknown]

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20state">Link to this property</a>

tags: map\[string]

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20tags">Link to this property</a>

updated\_at: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

url: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20url">Link to this property</a>

<details>

<summary>

managed\_by: optional array of object {id, client\_type, name }

</summary>

id: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20managed_by%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

client\_type: "MAGIC\_WAN\_CLOUD\_ONRAMP"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20managed_by%20%3E%20(items)%20%3E%20(property)%20client_type">Link to this property</a>

name: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20managed_by%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)%20%3E%20(property)%20managed_by">Link to this property</a>

</details>

[Link to this property](<#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_list_response%20%3E%20(schema)>)

<details>

<summary>

ResourceGetResponse object {id, account\_id, cloud\_type, 18 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

account\_id: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20account_id">Link to this property</a>

<details>

<summary>

cloud\_type: "AWS"or "AZURE"or "GOOGLE"or "CLOUDFLARE"

</summary>

One of the following:

"AWS"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20cloud_type%20%3E%20(member)%200">Link to this property</a>

"AZURE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20cloud_type%20%3E%20(member)%201">Link to this property</a>

"GOOGLE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20cloud_type%20%3E%20(member)%202">Link to this property</a>

"CLOUDFLARE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20cloud_type%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20cloud_type">Link to this property</a>

config: map\[unknown]

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20config">Link to this property</a>

deployment\_provider: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20deployment_provider">Link to this property</a>

managed: boolean

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20managed">Link to this property</a>

<details>

<summary>

monthly\_cost\_estimate: object {currency, monthly\_cost }

</summary>

currency: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20monthly_cost_estimate%20%3E%20(property)%20currency">Link to this property</a>

monthly\_cost: number

formatdouble

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20monthly_cost_estimate%20%3E%20(property)%20monthly_cost">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20monthly_cost_estimate">Link to this property</a>

name: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

native\_id: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20native_id">Link to this property</a>

<details>

<summary>

observations: map\[object {first\_observed\_at, last\_observed\_at, provider\_id, resource\_id } ]

</summary>

first\_observed\_at: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20observations%20%3E%20(items)%20%3E%20(property)%20first_observed_at">Link to this property</a>

last\_observed\_at: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20observations%20%3E%20(items)%20%3E%20(property)%20last_observed_at">Link to this property</a>

provider\_id: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20observations%20%3E%20(items)%20%3E%20(property)%20provider_id">Link to this property</a>

resource\_id: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20observations%20%3E%20(items)%20%3E%20(property)%20resource_id">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20observations">Link to this property</a>

provider\_ids: array of string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20provider_ids">Link to this property</a>

provider\_names\_by\_id: map\[string]

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20provider_names_by_id">Link to this property</a>

region: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20region">Link to this property</a>

resource\_group: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_group">Link to this property</a>

<details>

<summary>

resource\_type: "aws\_customer\_gateway"or "aws\_egress\_only\_internet\_gateway"or "aws\_internet\_gateway"or 54 more

</summary>

One of the following:

"aws\_customer\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%200">Link to this property</a>

"aws\_egress\_only\_internet\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%201">Link to this property</a>

"aws\_internet\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%202">Link to this property</a>

"aws\_instance"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%203">Link to this property</a>

"aws\_network\_interface"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%204">Link to this property</a>

"aws\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%205">Link to this property</a>

"aws\_route\_table"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%206">Link to this property</a>

"aws\_route\_table\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%207">Link to this property</a>

"aws\_subnet"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%208">Link to this property</a>

"aws\_vpc"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%209">Link to this property</a>

"aws\_vpc\_ipv4\_cidr\_block\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2010">Link to this property</a>

"aws\_vpn\_connection"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2011">Link to this property</a>

"aws\_vpn\_connection\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2012">Link to this property</a>

"aws\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2013">Link to this property</a>

"aws\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2014">Link to this property</a>

"aws\_vpc\_security\_group\_ingress\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2015">Link to this property</a>

"aws\_vpc\_security\_group\_egress\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2016">Link to this property</a>

"aws\_ec2\_managed\_prefix\_list"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2017">Link to this property</a>

"aws\_ec2\_transit\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2018">Link to this property</a>

"aws\_ec2\_transit\_gateway\_prefix\_list\_reference"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2019">Link to this property</a>

"aws\_ec2\_transit\_gateway\_vpc\_attachment"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2020">Link to this property</a>

"azurerm\_application\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2021">Link to this property</a>

"azurerm\_lb"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2022">Link to this property</a>

"azurerm\_lb\_backend\_address\_pool"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2023">Link to this property</a>

"azurerm\_lb\_nat\_pool"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2024">Link to this property</a>

"azurerm\_lb\_nat\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2025">Link to this property</a>

"azurerm\_lb\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2026">Link to this property</a>

"azurerm\_local\_network\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2027">Link to this property</a>

"azurerm\_network\_interface"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2028">Link to this property</a>

"azurerm\_network\_interface\_application\_security\_group\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2029">Link to this property</a>

"azurerm\_network\_interface\_backend\_address\_pool\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2030">Link to this property</a>

"azurerm\_network\_interface\_security\_group\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2031">Link to this property</a>

"azurerm\_network\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2032">Link to this property</a>

"azurerm\_public\_ip"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2033">Link to this property</a>

"azurerm\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2034">Link to this property</a>

"azurerm\_route\_table"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2035">Link to this property</a>

"azurerm\_subnet"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2036">Link to this property</a>

"azurerm\_subnet\_route\_table\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2037">Link to this property</a>

"azurerm\_virtual\_machine"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2038">Link to this property</a>

"azurerm\_virtual\_network\_gateway\_connection"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2039">Link to this property</a>

"azurerm\_virtual\_network"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2040">Link to this property</a>

"azurerm\_virtual\_network\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2041">Link to this property</a>

"google\_compute\_network"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2042">Link to this property</a>

"google\_compute\_subnetwork"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2043">Link to this property</a>

"google\_compute\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2044">Link to this property</a>

"google\_compute\_vpn\_tunnel"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2045">Link to this property</a>

"google\_compute\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2046">Link to this property</a>

"google\_compute\_address"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2047">Link to this property</a>

"google\_compute\_global\_address"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2048">Link to this property</a>

"google\_compute\_router"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2049">Link to this property</a>

"google\_compute\_interconnect\_attachment"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2050">Link to this property</a>

"google\_compute\_ha\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2051">Link to this property</a>

"google\_compute\_forwarding\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2052">Link to this property</a>

"google\_compute\_network\_firewall\_policy"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2053">Link to this property</a>

"google\_compute\_network\_firewall\_policy\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2054">Link to this property</a>

"cloudflare\_static\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2055">Link to this property</a>

"cloudflare\_ipsec\_tunnel"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type%20%3E%20(member)%2056">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20resource_type">Link to this property</a>

<details>

<summary>

sections: array of object {hidden\_items, name, visible\_items, help\_text }

</summary>

<details>

<summary>

hidden\_items: array of object {helpText, name, value }

</summary>

helpText: optional string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20helpText">Link to this property</a>

name: optional string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

value: optional object {item\_type, string } or object {item\_type, yaml } or object {item\_type, yaml\_diff } or 2 more

</summary>

One of the following:

<details>

<summary>

McnStringItem object {item\_type, string }

</summary>

item\_type: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%200%20%3E%20(property)%20item_type">Link to this property</a>

string: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%200%20%3E%20(property)%20string">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

McnYamlItem object {item\_type, yaml }

</summary>

item\_type: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%201%20%3E%20(property)%20item_type">Link to this property</a>

yaml: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%201%20%3E%20(property)%20yaml">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

McnYamlDiffItem object {item\_type, yaml\_diff }

</summary>

item\_type: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202%20%3E%20(property)%20item_type">Link to this property</a>

<details>

<summary>

yaml\_diff: object {diff, left\_description, left\_yaml, 2 more }

</summary>

diff: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202%20%3E%20(property)%20yaml_diff%20%3E%20(property)%20diff">Link to this property</a>

left\_description: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202%20%3E%20(property)%20yaml_diff%20%3E%20(property)%20left_description">Link to this property</a>

left\_yaml: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202%20%3E%20(property)%20yaml_diff%20%3E%20(property)%20left_yaml">Link to this property</a>

right\_description: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202%20%3E%20(property)%20yaml_diff%20%3E%20(property)%20right_description">Link to this property</a>

right\_yaml: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202%20%3E%20(property)%20yaml_diff%20%3E%20(property)%20right_yaml">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202%20%3E%20(property)%20yaml_diff">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

McnResourcePreviewItem object {item\_type, resource\_preview }

</summary>

item\_type: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20item_type">Link to this property</a>

<details>

<summary>

resource\_preview: object {id, cloud\_type, detail, 3 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

cloud\_type: "AWS"or "AZURE"or "GOOGLE"or "CLOUDFLARE"

</summary>

One of the following:

"AWS"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%200">Link to this property</a>

"AZURE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%201">Link to this property</a>

"GOOGLE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%202">Link to this property</a>

"CLOUDFLARE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type">Link to this property</a>

detail: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20detail">Link to this property</a>

name: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

resource\_type: "aws\_customer\_gateway"or "aws\_egress\_only\_internet\_gateway"or "aws\_internet\_gateway"or 54 more

</summary>

One of the following:

"aws\_customer\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%200">Link to this property</a>

"aws\_egress\_only\_internet\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%201">Link to this property</a>

"aws\_internet\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%202">Link to this property</a>

"aws\_instance"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%203">Link to this property</a>

"aws\_network\_interface"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%204">Link to this property</a>

"aws\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%205">Link to this property</a>

"aws\_route\_table"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%206">Link to this property</a>

"aws\_route\_table\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%207">Link to this property</a>

"aws\_subnet"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%208">Link to this property</a>

"aws\_vpc"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%209">Link to this property</a>

"aws\_vpc\_ipv4\_cidr\_block\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2010">Link to this property</a>

"aws\_vpn\_connection"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2011">Link to this property</a>

"aws\_vpn\_connection\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2012">Link to this property</a>

"aws\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2013">Link to this property</a>

"aws\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2014">Link to this property</a>

"aws\_vpc\_security\_group\_ingress\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2015">Link to this property</a>

"aws\_vpc\_security\_group\_egress\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2016">Link to this property</a>

"aws\_ec2\_managed\_prefix\_list"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2017">Link to this property</a>

"aws\_ec2\_transit\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2018">Link to this property</a>

"aws\_ec2\_transit\_gateway\_prefix\_list\_reference"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2019">Link to this property</a>

"aws\_ec2\_transit\_gateway\_vpc\_attachment"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2020">Link to this property</a>

"azurerm\_application\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2021">Link to this property</a>

"azurerm\_lb"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2022">Link to this property</a>

"azurerm\_lb\_backend\_address\_pool"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2023">Link to this property</a>

"azurerm\_lb\_nat\_pool"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2024">Link to this property</a>

"azurerm\_lb\_nat\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2025">Link to this property</a>

"azurerm\_lb\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2026">Link to this property</a>

"azurerm\_local\_network\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2027">Link to this property</a>

"azurerm\_network\_interface"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2028">Link to this property</a>

"azurerm\_network\_interface\_application\_security\_group\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2029">Link to this property</a>

"azurerm\_network\_interface\_backend\_address\_pool\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2030">Link to this property</a>

"azurerm\_network\_interface\_security\_group\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2031">Link to this property</a>

"azurerm\_network\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2032">Link to this property</a>

"azurerm\_public\_ip"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2033">Link to this property</a>

"azurerm\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2034">Link to this property</a>

"azurerm\_route\_table"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2035">Link to this property</a>

"azurerm\_subnet"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2036">Link to this property</a>

"azurerm\_subnet\_route\_table\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2037">Link to this property</a>

"azurerm\_virtual\_machine"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2038">Link to this property</a>

"azurerm\_virtual\_network\_gateway\_connection"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2039">Link to this property</a>

"azurerm\_virtual\_network"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2040">Link to this property</a>

"azurerm\_virtual\_network\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2041">Link to this property</a>

"google\_compute\_network"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2042">Link to this property</a>

"google\_compute\_subnetwork"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2043">Link to this property</a>

"google\_compute\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2044">Link to this property</a>

"google\_compute\_vpn\_tunnel"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2045">Link to this property</a>

"google\_compute\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2046">Link to this property</a>

"google\_compute\_address"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2047">Link to this property</a>

"google\_compute\_global\_address"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2048">Link to this property</a>

"google\_compute\_router"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2049">Link to this property</a>

"google\_compute\_interconnect\_attachment"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2050">Link to this property</a>

"google\_compute\_ha\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2051">Link to this property</a>

"google\_compute\_forwarding\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2052">Link to this property</a>

"google\_compute\_network\_firewall\_policy"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2053">Link to this property</a>

"google\_compute\_network\_firewall\_policy\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2054">Link to this property</a>

"cloudflare\_static\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2055">Link to this property</a>

"cloudflare\_ipsec\_tunnel"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2056">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type">Link to this property</a>

title: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20title">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

McnListItem object {item\_type, list }

</summary>

item\_type: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20item_type">Link to this property</a>

<details>

<summary>

list: array of object {item\_type, string } or object {item\_type, resource\_preview }

</summary>

One of the following:

<details>

<summary>

McnStringItem object {item\_type, string }

</summary>

item\_type: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20item_type">Link to this property</a>

string: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20string">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

McnResourcePreviewItem object {item\_type, resource\_preview }

</summary>

item\_type: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20item_type">Link to this property</a>

<details>

<summary>

resource\_preview: object {id, cloud\_type, detail, 3 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

cloud\_type: "AWS"or "AZURE"or "GOOGLE"or "CLOUDFLARE"

</summary>

One of the following:

"AWS"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%200">Link to this property</a>

"AZURE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%201">Link to this property</a>

"GOOGLE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%202">Link to this property</a>

"CLOUDFLARE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type">Link to this property</a>

detail: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20detail">Link to this property</a>

name: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

resource\_type: "aws\_customer\_gateway"or "aws\_egress\_only\_internet\_gateway"or "aws\_internet\_gateway"or 54 more

</summary>

One of the following:

"aws\_customer\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%200">Link to this property</a>

"aws\_egress\_only\_internet\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%201">Link to this property</a>

"aws\_internet\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%202">Link to this property</a>

"aws\_instance"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%203">Link to this property</a>

"aws\_network\_interface"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%204">Link to this property</a>

"aws\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%205">Link to this property</a>

"aws\_route\_table"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%206">Link to this property</a>

"aws\_route\_table\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%207">Link to this property</a>

"aws\_subnet"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%208">Link to this property</a>

"aws\_vpc"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%209">Link to this property</a>

"aws\_vpc\_ipv4\_cidr\_block\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2010">Link to this property</a>

"aws\_vpn\_connection"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2011">Link to this property</a>

"aws\_vpn\_connection\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2012">Link to this property</a>

"aws\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2013">Link to this property</a>

"aws\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2014">Link to this property</a>

"aws\_vpc\_security\_group\_ingress\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2015">Link to this property</a>

"aws\_vpc\_security\_group\_egress\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2016">Link to this property</a>

"aws\_ec2\_managed\_prefix\_list"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2017">Link to this property</a>

"aws\_ec2\_transit\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2018">Link to this property</a>

"aws\_ec2\_transit\_gateway\_prefix\_list\_reference"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2019">Link to this property</a>

"aws\_ec2\_transit\_gateway\_vpc\_attachment"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2020">Link to this property</a>

"azurerm\_application\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2021">Link to this property</a>

"azurerm\_lb"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2022">Link to this property</a>

"azurerm\_lb\_backend\_address\_pool"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2023">Link to this property</a>

"azurerm\_lb\_nat\_pool"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2024">Link to this property</a>

"azurerm\_lb\_nat\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2025">Link to this property</a>

"azurerm\_lb\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2026">Link to this property</a>

"azurerm\_local\_network\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2027">Link to this property</a>

"azurerm\_network\_interface"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2028">Link to this property</a>

"azurerm\_network\_interface\_application\_security\_group\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2029">Link to this property</a>

"azurerm\_network\_interface\_backend\_address\_pool\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2030">Link to this property</a>

"azurerm\_network\_interface\_security\_group\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2031">Link to this property</a>

"azurerm\_network\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2032">Link to this property</a>

"azurerm\_public\_ip"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2033">Link to this property</a>

"azurerm\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2034">Link to this property</a>

"azurerm\_route\_table"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2035">Link to this property</a>

"azurerm\_subnet"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2036">Link to this property</a>

"azurerm\_subnet\_route\_table\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2037">Link to this property</a>

"azurerm\_virtual\_machine"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2038">Link to this property</a>

"azurerm\_virtual\_network\_gateway\_connection"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2039">Link to this property</a>

"azurerm\_virtual\_network"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2040">Link to this property</a>

"azurerm\_virtual\_network\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2041">Link to this property</a>

"google\_compute\_network"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2042">Link to this property</a>

"google\_compute\_subnetwork"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2043">Link to this property</a>

"google\_compute\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2044">Link to this property</a>

"google\_compute\_vpn\_tunnel"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2045">Link to this property</a>

"google\_compute\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2046">Link to this property</a>

"google\_compute\_address"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2047">Link to this property</a>

"google\_compute\_global\_address"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2048">Link to this property</a>

"google\_compute\_router"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2049">Link to this property</a>

"google\_compute\_interconnect\_attachment"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2050">Link to this property</a>

"google\_compute\_ha\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2051">Link to this property</a>

"google\_compute\_forwarding\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2052">Link to this property</a>

"google\_compute\_network\_firewall\_policy"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2053">Link to this property</a>

"google\_compute\_network\_firewall\_policy\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2054">Link to this property</a>

"cloudflare\_static\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2055">Link to this property</a>

"cloudflare\_ipsec\_tunnel"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2056">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type">Link to this property</a>

title: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20title">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20hidden_items">Link to this property</a>

name: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

visible\_items: array of object {helpText, name, value }

</summary>

helpText: optional string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20helpText">Link to this property</a>

name: optional string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

value: optional object {item\_type, string } or object {item\_type, yaml } or object {item\_type, yaml\_diff } or 2 more

</summary>

One of the following:

<details>

<summary>

McnStringItem object {item\_type, string }

</summary>

item\_type: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%200%20%3E%20(property)%20item_type">Link to this property</a>

string: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%200%20%3E%20(property)%20string">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

McnYamlItem object {item\_type, yaml }

</summary>

item\_type: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%201%20%3E%20(property)%20item_type">Link to this property</a>

yaml: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%201%20%3E%20(property)%20yaml">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

McnYamlDiffItem object {item\_type, yaml\_diff }

</summary>

item\_type: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202%20%3E%20(property)%20item_type">Link to this property</a>

<details>

<summary>

yaml\_diff: object {diff, left\_description, left\_yaml, 2 more }

</summary>

diff: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202%20%3E%20(property)%20yaml_diff%20%3E%20(property)%20diff">Link to this property</a>

left\_description: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202%20%3E%20(property)%20yaml_diff%20%3E%20(property)%20left_description">Link to this property</a>

left\_yaml: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202%20%3E%20(property)%20yaml_diff%20%3E%20(property)%20left_yaml">Link to this property</a>

right\_description: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202%20%3E%20(property)%20yaml_diff%20%3E%20(property)%20right_description">Link to this property</a>

right\_yaml: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202%20%3E%20(property)%20yaml_diff%20%3E%20(property)%20right_yaml">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202%20%3E%20(property)%20yaml_diff">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

McnResourcePreviewItem object {item\_type, resource\_preview }

</summary>

item\_type: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20item_type">Link to this property</a>

<details>

<summary>

resource\_preview: object {id, cloud\_type, detail, 3 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

cloud\_type: "AWS"or "AZURE"or "GOOGLE"or "CLOUDFLARE"

</summary>

One of the following:

"AWS"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%200">Link to this property</a>

"AZURE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%201">Link to this property</a>

"GOOGLE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%202">Link to this property</a>

"CLOUDFLARE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type">Link to this property</a>

detail: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20detail">Link to this property</a>

name: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

resource\_type: "aws\_customer\_gateway"or "aws\_egress\_only\_internet\_gateway"or "aws\_internet\_gateway"or 54 more

</summary>

One of the following:

"aws\_customer\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%200">Link to this property</a>

"aws\_egress\_only\_internet\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%201">Link to this property</a>

"aws\_internet\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%202">Link to this property</a>

"aws\_instance"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%203">Link to this property</a>

"aws\_network\_interface"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%204">Link to this property</a>

"aws\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%205">Link to this property</a>

"aws\_route\_table"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%206">Link to this property</a>

"aws\_route\_table\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%207">Link to this property</a>

"aws\_subnet"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%208">Link to this property</a>

"aws\_vpc"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%209">Link to this property</a>

"aws\_vpc\_ipv4\_cidr\_block\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2010">Link to this property</a>

"aws\_vpn\_connection"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2011">Link to this property</a>

"aws\_vpn\_connection\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2012">Link to this property</a>

"aws\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2013">Link to this property</a>

"aws\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2014">Link to this property</a>

"aws\_vpc\_security\_group\_ingress\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2015">Link to this property</a>

"aws\_vpc\_security\_group\_egress\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2016">Link to this property</a>

"aws\_ec2\_managed\_prefix\_list"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2017">Link to this property</a>

"aws\_ec2\_transit\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2018">Link to this property</a>

"aws\_ec2\_transit\_gateway\_prefix\_list\_reference"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2019">Link to this property</a>

"aws\_ec2\_transit\_gateway\_vpc\_attachment"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2020">Link to this property</a>

"azurerm\_application\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2021">Link to this property</a>

"azurerm\_lb"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2022">Link to this property</a>

"azurerm\_lb\_backend\_address\_pool"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2023">Link to this property</a>

"azurerm\_lb\_nat\_pool"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2024">Link to this property</a>

"azurerm\_lb\_nat\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2025">Link to this property</a>

"azurerm\_lb\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2026">Link to this property</a>

"azurerm\_local\_network\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2027">Link to this property</a>

"azurerm\_network\_interface"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2028">Link to this property</a>

"azurerm\_network\_interface\_application\_security\_group\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2029">Link to this property</a>

"azurerm\_network\_interface\_backend\_address\_pool\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2030">Link to this property</a>

"azurerm\_network\_interface\_security\_group\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2031">Link to this property</a>

"azurerm\_network\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2032">Link to this property</a>

"azurerm\_public\_ip"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2033">Link to this property</a>

"azurerm\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2034">Link to this property</a>

"azurerm\_route\_table"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2035">Link to this property</a>

"azurerm\_subnet"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2036">Link to this property</a>

"azurerm\_subnet\_route\_table\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2037">Link to this property</a>

"azurerm\_virtual\_machine"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2038">Link to this property</a>

"azurerm\_virtual\_network\_gateway\_connection"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2039">Link to this property</a>

"azurerm\_virtual\_network"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2040">Link to this property</a>

"azurerm\_virtual\_network\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2041">Link to this property</a>

"google\_compute\_network"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2042">Link to this property</a>

"google\_compute\_subnetwork"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2043">Link to this property</a>

"google\_compute\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2044">Link to this property</a>

"google\_compute\_vpn\_tunnel"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2045">Link to this property</a>

"google\_compute\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2046">Link to this property</a>

"google\_compute\_address"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2047">Link to this property</a>

"google\_compute\_global\_address"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2048">Link to this property</a>

"google\_compute\_router"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2049">Link to this property</a>

"google\_compute\_interconnect\_attachment"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2050">Link to this property</a>

"google\_compute\_ha\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2051">Link to this property</a>

"google\_compute\_forwarding\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2052">Link to this property</a>

"google\_compute\_network\_firewall\_policy"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2053">Link to this property</a>

"google\_compute\_network\_firewall\_policy\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2054">Link to this property</a>

"cloudflare\_static\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2055">Link to this property</a>

"cloudflare\_ipsec\_tunnel"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2056">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type">Link to this property</a>

title: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview%20%3E%20(property)%20title">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203%20%3E%20(property)%20resource_preview">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

McnListItem object {item\_type, list }

</summary>

item\_type: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20item_type">Link to this property</a>

<details>

<summary>

list: array of object {item\_type, string } or object {item\_type, resource\_preview }

</summary>

One of the following:

<details>

<summary>

McnStringItem object {item\_type, string }

</summary>

item\_type: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20item_type">Link to this property</a>

string: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20string">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

McnResourcePreviewItem object {item\_type, resource\_preview }

</summary>

item\_type: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20item_type">Link to this property</a>

<details>

<summary>

resource\_preview: object {id, cloud\_type, detail, 3 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

cloud\_type: "AWS"or "AZURE"or "GOOGLE"or "CLOUDFLARE"

</summary>

One of the following:

"AWS"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%200">Link to this property</a>

"AZURE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%201">Link to this property</a>

"GOOGLE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%202">Link to this property</a>

"CLOUDFLARE"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20cloud_type">Link to this property</a>

detail: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20detail">Link to this property</a>

name: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

resource\_type: "aws\_customer\_gateway"or "aws\_egress\_only\_internet\_gateway"or "aws\_internet\_gateway"or 54 more

</summary>

One of the following:

"aws\_customer\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%200">Link to this property</a>

"aws\_egress\_only\_internet\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%201">Link to this property</a>

"aws\_internet\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%202">Link to this property</a>

"aws\_instance"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%203">Link to this property</a>

"aws\_network\_interface"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%204">Link to this property</a>

"aws\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%205">Link to this property</a>

"aws\_route\_table"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%206">Link to this property</a>

"aws\_route\_table\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%207">Link to this property</a>

"aws\_subnet"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%208">Link to this property</a>

"aws\_vpc"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%209">Link to this property</a>

"aws\_vpc\_ipv4\_cidr\_block\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2010">Link to this property</a>

"aws\_vpn\_connection"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2011">Link to this property</a>

"aws\_vpn\_connection\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2012">Link to this property</a>

"aws\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2013">Link to this property</a>

"aws\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2014">Link to this property</a>

"aws\_vpc\_security\_group\_ingress\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2015">Link to this property</a>

"aws\_vpc\_security\_group\_egress\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2016">Link to this property</a>

"aws\_ec2\_managed\_prefix\_list"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2017">Link to this property</a>

"aws\_ec2\_transit\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2018">Link to this property</a>

"aws\_ec2\_transit\_gateway\_prefix\_list\_reference"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2019">Link to this property</a>

"aws\_ec2\_transit\_gateway\_vpc\_attachment"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2020">Link to this property</a>

"azurerm\_application\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2021">Link to this property</a>

"azurerm\_lb"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2022">Link to this property</a>

"azurerm\_lb\_backend\_address\_pool"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2023">Link to this property</a>

"azurerm\_lb\_nat\_pool"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2024">Link to this property</a>

"azurerm\_lb\_nat\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2025">Link to this property</a>

"azurerm\_lb\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2026">Link to this property</a>

"azurerm\_local\_network\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2027">Link to this property</a>

"azurerm\_network\_interface"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2028">Link to this property</a>

"azurerm\_network\_interface\_application\_security\_group\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2029">Link to this property</a>

"azurerm\_network\_interface\_backend\_address\_pool\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2030">Link to this property</a>

"azurerm\_network\_interface\_security\_group\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2031">Link to this property</a>

"azurerm\_network\_security\_group"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2032">Link to this property</a>

"azurerm\_public\_ip"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2033">Link to this property</a>

"azurerm\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2034">Link to this property</a>

"azurerm\_route\_table"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2035">Link to this property</a>

"azurerm\_subnet"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2036">Link to this property</a>

"azurerm\_subnet\_route\_table\_association"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2037">Link to this property</a>

"azurerm\_virtual\_machine"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2038">Link to this property</a>

"azurerm\_virtual\_network\_gateway\_connection"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2039">Link to this property</a>

"azurerm\_virtual\_network"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2040">Link to this property</a>

"azurerm\_virtual\_network\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2041">Link to this property</a>

"google\_compute\_network"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2042">Link to this property</a>

"google\_compute\_subnetwork"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2043">Link to this property</a>

"google\_compute\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2044">Link to this property</a>

"google\_compute\_vpn\_tunnel"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2045">Link to this property</a>

"google\_compute\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2046">Link to this property</a>

"google\_compute\_address"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2047">Link to this property</a>

"google\_compute\_global\_address"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2048">Link to this property</a>

"google\_compute\_router"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2049">Link to this property</a>

"google\_compute\_interconnect\_attachment"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2050">Link to this property</a>

"google\_compute\_ha\_vpn\_gateway"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2051">Link to this property</a>

"google\_compute\_forwarding\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2052">Link to this property</a>

"google\_compute\_network\_firewall\_policy"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2053">Link to this property</a>

"google\_compute\_network\_firewall\_policy\_rule"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2054">Link to this property</a>

"cloudflare\_static\_route"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2055">Link to this property</a>

"cloudflare\_ipsec\_tunnel"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type%20%3E%20(member)%2056">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20resource_type">Link to this property</a>

title: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview%20%3E%20(property)%20title">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resource_preview">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204%20%3E%20(property)%20list">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value%20%3E%20(variant)%204">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20visible_items">Link to this property</a>

help\_text: optional string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections%20%3E%20(items)%20%3E%20(property)%20help_text">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20sections">Link to this property</a>

state: map\[unknown]

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20state">Link to this property</a>

tags: map\[string]

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20tags">Link to this property</a>

updated\_at: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

url: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20url">Link to this property</a>

<details>

<summary>

managed\_by: optional array of object {id, client\_type, name }

</summary>

id: string

formatuuid

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20managed_by%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

client\_type: "MAGIC\_WAN\_CLOUD\_ONRAMP"

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20managed_by%20%3E%20(items)%20%3E%20(property)%20client_type">Link to this property</a>

name: string

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20managed_by%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)%20%3E%20(property)%20managed_by">Link to this property</a>

</details>

[Link to this property](<#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_get_response%20%3E%20(schema)>)

ResourcePolicyPreviewResponse = string

[Link to this property](<#(resource)%20magic_cloud_networking.resources%20%3E%20(model)%20resource_policy_preview_response%20%3E%20(schema)>)