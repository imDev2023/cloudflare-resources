---
title: Relationships
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Cloudforce One](https://developers.cloudflare.com/api/resources/cloudforce_one)

[Threat Events](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Relationships

##### [Filter and list events related to specific event](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/relationships/methods/list)

Deprecated

GET/accounts/{account\_id}/cloudforce-one/events/{event\_id}/relationships

##### ModelsExpand Collapse

<details>

<summary>

RelationshipListResponse = array of object {attacker, attackerCountry, attackerCountryAlpha3, 26 more }

</summary>

attacker: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20attacker">Link to this property</a>

attackerCountry: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20attackerCountry">Link to this property</a>

attackerCountryAlpha3: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20attackerCountryAlpha3">Link to this property</a>

category: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20category">Link to this property</a>

datasetId: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20datasetId">Link to this property</a>

date: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20date">Link to this property</a>

event: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20event">Link to this property</a>

hasChildren: boolean

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20hasChildren">Link to this property</a>

indicator: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20indicator">Link to this property</a>

indicatorType: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20indicatorType">Link to this property</a>

indicatorTypeId: number

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20indicatorTypeId">Link to this property</a>

killChain: number

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20killChain">Link to this property</a>

mitreAttack: array of string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20mitreAttack">Link to this property</a>

mitreCapec: array of string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20mitreCapec">Link to this property</a>

numReferenced: number

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20numReferenced">Link to this property</a>

numReferences: number

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20numReferences">Link to this property</a>

rawId: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20rawId">Link to this property</a>

referenced: array of string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20referenced">Link to this property</a>

referencedIds: array of number

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20referencedIds">Link to this property</a>

references: array of string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20references">Link to this property</a>

referencesIds: array of number

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20referencesIds">Link to this property</a>

tags: array of string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

targetCountry: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20targetCountry">Link to this property</a>

targetCountryAlpha3: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20targetCountryAlpha3">Link to this property</a>

targetIndustry: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20targetIndustry">Link to this property</a>

tlp: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20tlp">Link to this property</a>

uuid: string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

insight: optional string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20insight">Link to this property</a>

releasabilityId: optional string

<a href="#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20releasabilityId">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.relationships%20%3E%20(model)%20relationship_list_response%20%3E%20(schema)>)