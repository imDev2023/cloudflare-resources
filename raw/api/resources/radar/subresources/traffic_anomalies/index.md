---
title: Traffic Anomalies
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Radar](https://developers.cloudflare.com/api/resources/radar)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Traffic Anomalies

##### [Get latest Internet traffic anomalies](https://developers.cloudflare.com/api/resources/radar/subresources/traffic_anomalies/methods/get)

GET/radar/traffic\_anomalies

##### ModelsExpand Collapse

<details>

<summary>

TrafficAnomalyGetResponse object {trafficAnomalies }

</summary>

<details>

<summary>

trafficAnomalies: array of object {asnDetails, endDate, locationDetails, 6 more }

</summary>

<details>

<summary>

asnDetails: object {asn, location, name }

</summary>

asn: string

<a href="#(resource)%20radar.traffic_anomalies%20%3E%20(model)%20traffic_anomaly_get_response%20%3E%20(schema)%20%3E%20(property)%20trafficAnomalies%20%3E%20(items)%20%3E%20(property)%20asnDetails%20%3E%20(property)%20asn">Link to this property</a>

<details>

<summary>

location: object {code, name }

</summary>

code: string

<a href="#(resource)%20radar.traffic_anomalies%20%3E%20(model)%20traffic_anomaly_get_response%20%3E%20(schema)%20%3E%20(property)%20trafficAnomalies%20%3E%20(items)%20%3E%20(property)%20asnDetails%20%3E%20(property)%20location%20%3E%20(property)%20code">Link to this property</a>

name: string

<a href="#(resource)%20radar.traffic_anomalies%20%3E%20(model)%20traffic_anomaly_get_response%20%3E%20(schema)%20%3E%20(property)%20trafficAnomalies%20%3E%20(items)%20%3E%20(property)%20asnDetails%20%3E%20(property)%20location%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20radar.traffic_anomalies%20%3E%20(model)%20traffic_anomaly_get_response%20%3E%20(schema)%20%3E%20(property)%20trafficAnomalies%20%3E%20(items)%20%3E%20(property)%20asnDetails%20%3E%20(property)%20location">Link to this property</a>

name: string

<a href="#(resource)%20radar.traffic_anomalies%20%3E%20(model)%20traffic_anomaly_get_response%20%3E%20(schema)%20%3E%20(property)%20trafficAnomalies%20%3E%20(items)%20%3E%20(property)%20asnDetails%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20radar.traffic_anomalies%20%3E%20(model)%20traffic_anomaly_get_response%20%3E%20(schema)%20%3E%20(property)%20trafficAnomalies%20%3E%20(items)%20%3E%20(property)%20asnDetails">Link to this property</a>

endDate: string

formatdate-time

<a href="#(resource)%20radar.traffic_anomalies%20%3E%20(model)%20traffic_anomaly_get_response%20%3E%20(schema)%20%3E%20(property)%20trafficAnomalies%20%3E%20(items)%20%3E%20(property)%20endDate">Link to this property</a>

<details>

<summary>

locationDetails: object {code, name }

</summary>

code: string

<a href="#(resource)%20radar.traffic_anomalies%20%3E%20(model)%20traffic_anomaly_get_response%20%3E%20(schema)%20%3E%20(property)%20trafficAnomalies%20%3E%20(items)%20%3E%20(property)%20locationDetails%20%3E%20(property)%20code">Link to this property</a>

name: string

<a href="#(resource)%20radar.traffic_anomalies%20%3E%20(model)%20traffic_anomaly_get_response%20%3E%20(schema)%20%3E%20(property)%20trafficAnomalies%20%3E%20(items)%20%3E%20(property)%20locationDetails%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20radar.traffic_anomalies%20%3E%20(model)%20traffic_anomaly_get_response%20%3E%20(schema)%20%3E%20(property)%20trafficAnomalies%20%3E%20(items)%20%3E%20(property)%20locationDetails">Link to this property</a>

<details>

<summary>

originDetails: object {name, origin }

</summary>

name: string

<a href="#(resource)%20radar.traffic_anomalies%20%3E%20(model)%20traffic_anomaly_get_response%20%3E%20(schema)%20%3E%20(property)%20trafficAnomalies%20%3E%20(items)%20%3E%20(property)%20originDetails%20%3E%20(property)%20name">Link to this property</a>

origin: string

<a href="#(resource)%20radar.traffic_anomalies%20%3E%20(model)%20traffic_anomaly_get_response%20%3E%20(schema)%20%3E%20(property)%20trafficAnomalies%20%3E%20(items)%20%3E%20(property)%20originDetails%20%3E%20(property)%20origin">Link to this property</a>

</details>

<a href="#(resource)%20radar.traffic_anomalies%20%3E%20(model)%20traffic_anomaly_get_response%20%3E%20(schema)%20%3E%20(property)%20trafficAnomalies%20%3E%20(items)%20%3E%20(property)%20originDetails">Link to this property</a>

startDate: string

formatdate-time

<a href="#(resource)%20radar.traffic_anomalies%20%3E%20(model)%20traffic_anomaly_get_response%20%3E%20(schema)%20%3E%20(property)%20trafficAnomalies%20%3E%20(items)%20%3E%20(property)%20startDate">Link to this property</a>

status: string

<a href="#(resource)%20radar.traffic_anomalies%20%3E%20(model)%20traffic_anomaly_get_response%20%3E%20(schema)%20%3E%20(property)%20trafficAnomalies%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

type: string

<a href="#(resource)%20radar.traffic_anomalies%20%3E%20(model)%20traffic_anomaly_get_response%20%3E%20(schema)%20%3E%20(property)%20trafficAnomalies%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

uuid: string

<a href="#(resource)%20radar.traffic_anomalies%20%3E%20(model)%20traffic_anomaly_get_response%20%3E%20(schema)%20%3E%20(property)%20trafficAnomalies%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

visibleInDataSources: array of string

<a href="#(resource)%20radar.traffic_anomalies%20%3E%20(model)%20traffic_anomaly_get_response%20%3E%20(schema)%20%3E%20(property)%20trafficAnomalies%20%3E%20(items)%20%3E%20(property)%20visibleInDataSources">Link to this property</a>

</details>

<a href="#(resource)%20radar.traffic_anomalies%20%3E%20(model)%20traffic_anomaly_get_response%20%3E%20(schema)%20%3E%20(property)%20trafficAnomalies">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.traffic_anomalies%20%3E%20(model)%20traffic_anomaly_get_response%20%3E%20(schema)>)

#### Traffic AnomaliesLocations

##### [Get top locations by total traffic anomalies](https://developers.cloudflare.com/api/resources/radar/subresources/traffic_anomalies/subresources/locations/methods/get)

GET/radar/traffic\_anomalies/locations

##### ModelsExpand Collapse

<details>

<summary>

LocationGetResponse object {trafficAnomalies }

</summary>

<details>

<summary>

trafficAnomalies: array of object {clientCountryAlpha2, clientCountryName, value }

</summary>

clientCountryAlpha2: string

<a href="#(resource)%20radar.traffic_anomalies.locations%20%3E%20(model)%20location_get_response%20%3E%20(schema)%20%3E%20(property)%20trafficAnomalies%20%3E%20(items)%20%3E%20(property)%20clientCountryAlpha2">Link to this property</a>

clientCountryName: string

<a href="#(resource)%20radar.traffic_anomalies.locations%20%3E%20(model)%20location_get_response%20%3E%20(schema)%20%3E%20(property)%20trafficAnomalies%20%3E%20(items)%20%3E%20(property)%20clientCountryName">Link to this property</a>

value: string

A numeric string.

<a href="#(resource)%20radar.traffic_anomalies.locations%20%3E%20(model)%20location_get_response%20%3E%20(schema)%20%3E%20(property)%20trafficAnomalies%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20radar.traffic_anomalies.locations%20%3E%20(model)%20location_get_response%20%3E%20(schema)%20%3E%20(property)%20trafficAnomalies">Link to this property</a>

</details>

[Link to this property](<#(resource)%20radar.traffic_anomalies.locations%20%3E%20(model)%20location_get_response%20%3E%20(schema)>)