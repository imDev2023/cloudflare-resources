---
title: Availabilities
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Speed](https://developers.cloudflare.com/api/resources/speed)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Availabilities

##### [Get quota and availability](https://developers.cloudflare.com/api/resources/speed/subresources/availabilities/methods/list)

GET/zones/{zone\_id}/speed\_api/availabilities

##### ModelsExpand Collapse

<details>

<summary>

Availability object {quota, regions, regionsPerPlan }

</summary>

<details>

<summary>

quota: optional object {plan, quotasPerPlan, remainingSchedules, 2 more }

</summary>

plan: optional string

Cloudflare plan.

<a href="#(resource)%20speed.availabilities%20%3E%20(model)%20availability%20%3E%20(schema)%20%3E%20(property)%20quota%20%3E%20(property)%20plan">Link to this property</a>

<details>

<summary>

quotasPerPlan: optional object {value }

The number of tests available per plan.

</summary>

<details>

<summary>

value: optional object {business, enterprise, free, pro }

Counts per account plan.

</summary>

business: optional number

<a href="#(resource)%20speed.availabilities%20%3E%20(model)%20availability%20%3E%20(schema)%20%3E%20(property)%20quota%20%3E%20(property)%20quotasPerPlan%20%3E%20(property)%20value%20%3E%20(property)%20business">Link to this property</a>

enterprise: optional number

<a href="#(resource)%20speed.availabilities%20%3E%20(model)%20availability%20%3E%20(schema)%20%3E%20(property)%20quota%20%3E%20(property)%20quotasPerPlan%20%3E%20(property)%20value%20%3E%20(property)%20enterprise">Link to this property</a>

free: optional number

<a href="#(resource)%20speed.availabilities%20%3E%20(model)%20availability%20%3E%20(schema)%20%3E%20(property)%20quota%20%3E%20(property)%20quotasPerPlan%20%3E%20(property)%20value%20%3E%20(property)%20free">Link to this property</a>

pro: optional number

<a href="#(resource)%20speed.availabilities%20%3E%20(model)%20availability%20%3E%20(schema)%20%3E%20(property)%20quota%20%3E%20(property)%20quotasPerPlan%20%3E%20(property)%20value%20%3E%20(property)%20pro">Link to this property</a>

</details>

<a href="#(resource)%20speed.availabilities%20%3E%20(model)%20availability%20%3E%20(schema)%20%3E%20(property)%20quota%20%3E%20(property)%20quotasPerPlan%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20speed.availabilities%20%3E%20(model)%20availability%20%3E%20(schema)%20%3E%20(property)%20quota%20%3E%20(property)%20quotasPerPlan">Link to this property</a>

remainingSchedules: optional number

The number of remaining schedules available.

<a href="#(resource)%20speed.availabilities%20%3E%20(model)%20availability%20%3E%20(schema)%20%3E%20(property)%20quota%20%3E%20(property)%20remainingSchedules">Link to this property</a>

remainingTests: optional number

The number of remaining tests available.

<a href="#(resource)%20speed.availabilities%20%3E%20(model)%20availability%20%3E%20(schema)%20%3E%20(property)%20quota%20%3E%20(property)%20remainingTests">Link to this property</a>

<details>

<summary>

scheduleQuotasPerPlan: optional object {value }

The number of schedules available per plan.

</summary>

<details>

<summary>

value: optional object {business, enterprise, free, pro }

Counts per account plan.

</summary>

business: optional number

<a href="#(resource)%20speed.availabilities%20%3E%20(model)%20availability%20%3E%20(schema)%20%3E%20(property)%20quota%20%3E%20(property)%20scheduleQuotasPerPlan%20%3E%20(property)%20value%20%3E%20(property)%20business">Link to this property</a>

enterprise: optional number

<a href="#(resource)%20speed.availabilities%20%3E%20(model)%20availability%20%3E%20(schema)%20%3E%20(property)%20quota%20%3E%20(property)%20scheduleQuotasPerPlan%20%3E%20(property)%20value%20%3E%20(property)%20enterprise">Link to this property</a>

free: optional number

<a href="#(resource)%20speed.availabilities%20%3E%20(model)%20availability%20%3E%20(schema)%20%3E%20(property)%20quota%20%3E%20(property)%20scheduleQuotasPerPlan%20%3E%20(property)%20value%20%3E%20(property)%20free">Link to this property</a>

pro: optional number

<a href="#(resource)%20speed.availabilities%20%3E%20(model)%20availability%20%3E%20(schema)%20%3E%20(property)%20quota%20%3E%20(property)%20scheduleQuotasPerPlan%20%3E%20(property)%20value%20%3E%20(property)%20pro">Link to this property</a>

</details>

<a href="#(resource)%20speed.availabilities%20%3E%20(model)%20availability%20%3E%20(schema)%20%3E%20(property)%20quota%20%3E%20(property)%20scheduleQuotasPerPlan%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20speed.availabilities%20%3E%20(model)%20availability%20%3E%20(schema)%20%3E%20(property)%20quota%20%3E%20(property)%20scheduleQuotasPerPlan">Link to this property</a>

</details>

<a href="#(resource)%20speed.availabilities%20%3E%20(model)%20availability%20%3E%20(schema)%20%3E%20(property)%20quota">Link to this property</a>

<details>

<summary>

regions: optional array of <a href="https://developers.cloudflare.com/api/resources/speed#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)">LabeledRegion</a> { label, value }

</summary>

label: optional string

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

value: optional "asia-east1"or "asia-northeast1"or "asia-northeast2"or 18 more

A test region.

</summary>

One of the following:

"asia-east1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%200">Link to this property</a>

"asia-northeast1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%201">Link to this property</a>

"asia-northeast2"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%202">Link to this property</a>

"asia-south1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%203">Link to this property</a>

"asia-southeast1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%204">Link to this property</a>

"australia-southeast1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%205">Link to this property</a>

"europe-north1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%206">Link to this property</a>

"europe-southwest1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%207">Link to this property</a>

"europe-west1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%208">Link to this property</a>

"europe-west2"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%209">Link to this property</a>

"europe-west3"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2010">Link to this property</a>

"europe-west4"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2011">Link to this property</a>

"europe-west8"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2012">Link to this property</a>

"europe-west9"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2013">Link to this property</a>

"me-west1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2014">Link to this property</a>

"southamerica-east1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2015">Link to this property</a>

"us-central1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2016">Link to this property</a>

"us-east1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2017">Link to this property</a>

"us-east4"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2018">Link to this property</a>

"us-south1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2019">Link to this property</a>

"us-west1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2020">Link to this property</a>

</details>

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20speed.availabilities%20%3E%20(model)%20availability%20%3E%20(schema)%20%3E%20(property)%20regions">Link to this property</a>

<details>

<summary>

regionsPerPlan: optional object {business, enterprise, free, pro }

Available regions.

</summary>

<details>

<summary>

business: optional array of <a href="https://developers.cloudflare.com/api/resources/speed#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)">LabeledRegion</a> { label, value }

</summary>

label: optional string

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

value: optional "asia-east1"or "asia-northeast1"or "asia-northeast2"or 18 more

A test region.

</summary>

One of the following:

"asia-east1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%200">Link to this property</a>

"asia-northeast1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%201">Link to this property</a>

"asia-northeast2"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%202">Link to this property</a>

"asia-south1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%203">Link to this property</a>

"asia-southeast1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%204">Link to this property</a>

"australia-southeast1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%205">Link to this property</a>

"europe-north1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%206">Link to this property</a>

"europe-southwest1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%207">Link to this property</a>

"europe-west1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%208">Link to this property</a>

"europe-west2"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%209">Link to this property</a>

"europe-west3"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2010">Link to this property</a>

"europe-west4"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2011">Link to this property</a>

"europe-west8"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2012">Link to this property</a>

"europe-west9"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2013">Link to this property</a>

"me-west1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2014">Link to this property</a>

"southamerica-east1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2015">Link to this property</a>

"us-central1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2016">Link to this property</a>

"us-east1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2017">Link to this property</a>

"us-east4"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2018">Link to this property</a>

"us-south1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2019">Link to this property</a>

"us-west1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2020">Link to this property</a>

</details>

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20speed.availabilities%20%3E%20(model)%20availability%20%3E%20(schema)%20%3E%20(property)%20regionsPerPlan%20%3E%20(property)%20business">Link to this property</a>

<details>

<summary>

enterprise: optional array of <a href="https://developers.cloudflare.com/api/resources/speed#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)">LabeledRegion</a> { label, value }

</summary>

label: optional string

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

value: optional "asia-east1"or "asia-northeast1"or "asia-northeast2"or 18 more

A test region.

</summary>

One of the following:

"asia-east1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%200">Link to this property</a>

"asia-northeast1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%201">Link to this property</a>

"asia-northeast2"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%202">Link to this property</a>

"asia-south1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%203">Link to this property</a>

"asia-southeast1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%204">Link to this property</a>

"australia-southeast1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%205">Link to this property</a>

"europe-north1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%206">Link to this property</a>

"europe-southwest1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%207">Link to this property</a>

"europe-west1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%208">Link to this property</a>

"europe-west2"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%209">Link to this property</a>

"europe-west3"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2010">Link to this property</a>

"europe-west4"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2011">Link to this property</a>

"europe-west8"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2012">Link to this property</a>

"europe-west9"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2013">Link to this property</a>

"me-west1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2014">Link to this property</a>

"southamerica-east1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2015">Link to this property</a>

"us-central1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2016">Link to this property</a>

"us-east1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2017">Link to this property</a>

"us-east4"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2018">Link to this property</a>

"us-south1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2019">Link to this property</a>

"us-west1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2020">Link to this property</a>

</details>

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20speed.availabilities%20%3E%20(model)%20availability%20%3E%20(schema)%20%3E%20(property)%20regionsPerPlan%20%3E%20(property)%20enterprise">Link to this property</a>

<details>

<summary>

free: optional array of <a href="https://developers.cloudflare.com/api/resources/speed#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)">LabeledRegion</a> { label, value }

</summary>

label: optional string

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

value: optional "asia-east1"or "asia-northeast1"or "asia-northeast2"or 18 more

A test region.

</summary>

One of the following:

"asia-east1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%200">Link to this property</a>

"asia-northeast1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%201">Link to this property</a>

"asia-northeast2"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%202">Link to this property</a>

"asia-south1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%203">Link to this property</a>

"asia-southeast1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%204">Link to this property</a>

"australia-southeast1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%205">Link to this property</a>

"europe-north1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%206">Link to this property</a>

"europe-southwest1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%207">Link to this property</a>

"europe-west1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%208">Link to this property</a>

"europe-west2"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%209">Link to this property</a>

"europe-west3"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2010">Link to this property</a>

"europe-west4"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2011">Link to this property</a>

"europe-west8"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2012">Link to this property</a>

"europe-west9"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2013">Link to this property</a>

"me-west1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2014">Link to this property</a>

"southamerica-east1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2015">Link to this property</a>

"us-central1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2016">Link to this property</a>

"us-east1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2017">Link to this property</a>

"us-east4"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2018">Link to this property</a>

"us-south1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2019">Link to this property</a>

"us-west1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2020">Link to this property</a>

</details>

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20speed.availabilities%20%3E%20(model)%20availability%20%3E%20(schema)%20%3E%20(property)%20regionsPerPlan%20%3E%20(property)%20free">Link to this property</a>

<details>

<summary>

pro: optional array of <a href="https://developers.cloudflare.com/api/resources/speed#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)">LabeledRegion</a> { label, value }

</summary>

label: optional string

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

value: optional "asia-east1"or "asia-northeast1"or "asia-northeast2"or 18 more

A test region.

</summary>

One of the following:

"asia-east1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%200">Link to this property</a>

"asia-northeast1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%201">Link to this property</a>

"asia-northeast2"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%202">Link to this property</a>

"asia-south1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%203">Link to this property</a>

"asia-southeast1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%204">Link to this property</a>

"australia-southeast1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%205">Link to this property</a>

"europe-north1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%206">Link to this property</a>

"europe-southwest1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%207">Link to this property</a>

"europe-west1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%208">Link to this property</a>

"europe-west2"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%209">Link to this property</a>

"europe-west3"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2010">Link to this property</a>

"europe-west4"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2011">Link to this property</a>

"europe-west8"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2012">Link to this property</a>

"europe-west9"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2013">Link to this property</a>

"me-west1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2014">Link to this property</a>

"southamerica-east1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2015">Link to this property</a>

"us-central1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2016">Link to this property</a>

"us-east1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2017">Link to this property</a>

"us-east4"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2018">Link to this property</a>

"us-south1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2019">Link to this property</a>

"us-west1"

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%2020">Link to this property</a>

</details>

<a href="#(resource)%20speed%20%3E%20(model)%20labeled_region%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20speed.availabilities%20%3E%20(model)%20availability%20%3E%20(schema)%20%3E%20(property)%20regionsPerPlan%20%3E%20(property)%20pro">Link to this property</a>

</details>

<a href="#(resource)%20speed.availabilities%20%3E%20(model)%20availability%20%3E%20(schema)%20%3E%20(property)%20regionsPerPlan">Link to this property</a>

</details>

[Link to this property](<#(resource)%20speed.availabilities%20%3E%20(model)%20availability%20%3E%20(schema)>)