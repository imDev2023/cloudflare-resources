---
title: Annotations
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Radar](https://developers.cloudflare.com/api/resources/radar)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Annotations

##### [Get latest annotations](https://developers.cloudflare.com/api/resources/radar/subresources/annotations/methods/list)

GET/radar/annotations

##### ModelsExpand Collapse

<details>

<summary>

AnnotationListResponse object {annotations }

</summary>

<details>

<summary>

annotations: array of object {id, asns, asnsDetails, 15 more }

</summary>

id: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

asns: array of number

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20asns">Link to this property</a>

<details>

<summary>

asnsDetails: array of object {asn, location, name }

</summary>

asn: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20asnsDetails%20%3E%20(items)%20%3E%20(property)%20asn">Link to this property</a>

<details>

<summary>

location: object {code, name }

</summary>

code: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20asnsDetails%20%3E%20(items)%20%3E%20(property)%20location%20%3E%20(property)%20code">Link to this property</a>

name: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20asnsDetails%20%3E%20(items)%20%3E%20(property)%20location%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20asnsDetails%20%3E%20(items)%20%3E%20(property)%20location">Link to this property</a>

name: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20asnsDetails%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20asnsDetails">Link to this property</a>

dataSource: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

entities: array of object {entityName, entityType, entityValue }

</summary>

entityName: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20entities%20%3E%20(items)%20%3E%20(property)%20entityName">Link to this property</a>

entityType: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20entities%20%3E%20(items)%20%3E%20(property)%20entityType">Link to this property</a>

entityValue: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20entities%20%3E%20(items)%20%3E%20(property)%20entityValue">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20entities">Link to this property</a>

eventType: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

geoIds: array of string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20geoIds">Link to this property</a>

linkedUrl: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

locations: array of string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20locations">Link to this property</a>

<details>

<summary>

locationsDetails: array of object {code, name }

</summary>

code: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20locationsDetails%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

name: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20locationsDetails%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20locationsDetails">Link to this property</a>

origins: array of string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20origins">Link to this property</a>

<details>

<summary>

originsDetails: array of object {name, origin }

</summary>

name: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20originsDetails%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

origin: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20originsDetails%20%3E%20(items)%20%3E%20(property)%20origin">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20originsDetails">Link to this property</a>

<details>

<summary>

outage: object {outageCause, outageType }

</summary>

outageCause: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20outage%20%3E%20(property)%20outageCause">Link to this property</a>

outageType: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20outage%20%3E%20(property)%20outageType">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20outage">Link to this property</a>

scope: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20scope">Link to this property</a>

startDate: string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: array of string

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)%20%3E%20(property)%20annotations">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.annotations%20%3E%20(model)%20annotation_list_response%20%3E%20(schema)>)

#### AnnotationsOutages

##### [Get latest Internet outages and anomalies](https://developers.cloudflare.com/api/resources/radar/subresources/annotations/subresources/outages/methods/get)

GET/radar/annotations/outages

##### [Get the number of outages by location](https://developers.cloudflare.com/api/resources/radar/subresources/annotations/subresources/outages/methods/locations)

GET/radar/annotations/outages/locations

##### ModelsExpand Collapse

<details>

<summary>

OutageGetResponse object {annotations }

</summary>

<details>

<summary>

annotations: array of object {id, asns, asnsDetails, 15 more }

</summary>

id: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

asns: array of number

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20asns">Link to this property</a>

<details>

<summary>

asnsDetails: array of object {asn, location, name }

</summary>

asn: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20asnsDetails%20%3E%20(items)%20%3E%20(property)%20asn">Link to this property</a>

<details>

<summary>

location: object {code, name }

</summary>

code: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20asnsDetails%20%3E%20(items)%20%3E%20(property)%20location%20%3E%20(property)%20code">Link to this property</a>

name: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20asnsDetails%20%3E%20(items)%20%3E%20(property)%20location%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20asnsDetails%20%3E%20(items)%20%3E%20(property)%20location">Link to this property</a>

name: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20asnsDetails%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20asnsDetails">Link to this property</a>

dataSource: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20dataSource">Link to this property</a>

description: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

entities: array of object {entityName, entityType, entityValue }

</summary>

entityName: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20entities%20%3E%20(items)%20%3E%20(property)%20entityName">Link to this property</a>

entityType: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20entities%20%3E%20(items)%20%3E%20(property)%20entityType">Link to this property</a>

entityValue: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20entities%20%3E%20(items)%20%3E%20(property)%20entityValue">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20entities">Link to this property</a>

eventType: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20eventType">Link to this property</a>

geoIds: array of string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20geoIds">Link to this property</a>

linkedUrl: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20linkedUrl">Link to this property</a>

locations: array of string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20locations">Link to this property</a>

<details>

<summary>

locationsDetails: array of object {code, name }

</summary>

code: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20locationsDetails%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

name: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20locationsDetails%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20locationsDetails">Link to this property</a>

origins: array of string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20origins">Link to this property</a>

<details>

<summary>

originsDetails: array of object {name, origin }

</summary>

name: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20originsDetails%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

origin: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20originsDetails%20%3E%20(items)%20%3E%20(property)%20origin">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20originsDetails">Link to this property</a>

<details>

<summary>

outage: object {outageCause, outageType }

</summary>

outageCause: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20outage%20%3E%20(property)%20outageCause">Link to this property</a>

outageType: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20outage%20%3E%20(property)%20outageType">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20outage">Link to this property</a>

scope: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20scope">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

tags: array of string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_get_response%20%3E%20(schema)>)

<details>

<summary>

OutageLocationsResponse object {annotations }

</summary>

<details>

<summary>

annotations: array of object {clientCountryAlpha2, clientCountryName, value }

</summary>

clientCountryAlpha2: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_locations_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20clientCountryAlpha2">Link to this property</a>

clientCountryName: string

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_locations_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20clientCountryName">Link to this property</a>

value: string

A numeric string.

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_locations_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_locations_response%20%3E%20(schema)%20%3E%20(property)%20annotations">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.annotations.outages%20%3E%20(model)%20outage_locations_response%20%3E%20(schema)>)