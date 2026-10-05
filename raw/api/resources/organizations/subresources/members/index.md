---
title: Members
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Organizations](https://developers.cloudflare.com/api/resources/organizations)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Members

##### [List organization members](https://developers.cloudflare.com/api/resources/organizations/subresources/members/methods/list)

GET/organizations/{organization\_id}/members

##### [Get organization member](https://developers.cloudflare.com/api/resources/organizations/subresources/members/methods/get)

GET/organizations/{organization\_id}/members/{member\_id}

##### [Create organization member](https://developers.cloudflare.com/api/resources/organizations/subresources/members/methods/create)

POST/organizations/{organization\_id}/members

##### [Delete organization member](https://developers.cloudflare.com/api/resources/organizations/subresources/members/methods/delete)

DELETE/organizations/{organization\_id}/members/{member\_id}

##### ModelsExpand Collapse

<details>

<summary>

OrganizationMember object {id, create\_time, meta, 3 more }

</summary>

id: string

Organization Member ID

<a href="#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

create\_time: string

formatdate-time

<a href="#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)%20%3E%20(property)%20create_time">Link to this property</a>

meta: map\[unknown]

<a href="#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

status: "active"or "pending"or "rejected"or "canceled"

</summary>

One of the following:

"active"

<a href="#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"pending"

<a href="#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"rejected"

<a href="#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"canceled"

<a href="#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

update\_time: string

formatdate-time

<a href="#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)%20%3E%20(property)%20update_time">Link to this property</a>

<details>

<summary>

user: object {id, email, name, two\_factor\_authentication\_enabled }

</summary>

id: string

<a href="#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)%20%3E%20(property)%20user%20%3E%20(property)%20id">Link to this property</a>

email: string

<a href="#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)%20%3E%20(property)%20user%20%3E%20(property)%20email">Link to this property</a>

name: string

<a href="#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)%20%3E%20(property)%20user%20%3E%20(property)%20name">Link to this property</a>

two\_factor\_authentication\_enabled: boolean

<a href="#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)%20%3E%20(property)%20user%20%3E%20(property)%20two_factor_authentication_enabled">Link to this property</a>

</details>

<a href="#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)%20%3E%20(property)%20user">Link to this property</a>

</details>

[Link to this property](<#(resource)%20organizations.members%20%3E%20(model)%20organization_member%20%3E%20(schema)>)