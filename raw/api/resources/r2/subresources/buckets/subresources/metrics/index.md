---
title: Metrics
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[R2](https://developers.cloudflare.com/api/resources/r2)

[Buckets](https://developers.cloudflare.com/api/resources/r2/subresources/buckets)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Metrics

##### [Get Account-Level Metrics](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/metrics/methods/list)

GET/accounts/{account\_id}/r2/metrics

##### ModelsExpand Collapse

<details>

<summary>

MetricListResponse object {infrequentAccess, standard }

Metrics based on the class they belong to.

</summary>

<details>

<summary>

infrequentAccess: optional object {published, uploaded }

Metrics based on what state they are in(uploaded or published).

</summary>

<details>

<summary>

published: optional object {metadataSize, objects, payloadSize }

Metrics on number of objects/amount of storage used.

</summary>

metadataSize: optional number

Amount of.

<a href="#(resource)%20r2.buckets.metrics%20%3E%20(model)%20metric_list_response%20%3E%20(schema)%20%3E%20(property)%20infrequentAccess%20%3E%20(property)%20published%20%3E%20(property)%20metadataSize">Link to this property</a>

objects: optional number

Number of objects stored.

<a href="#(resource)%20r2.buckets.metrics%20%3E%20(model)%20metric_list_response%20%3E%20(schema)%20%3E%20(property)%20infrequentAccess%20%3E%20(property)%20published%20%3E%20(property)%20objects">Link to this property</a>

payloadSize: optional number

Amount of storage used by object data.

<a href="#(resource)%20r2.buckets.metrics%20%3E%20(model)%20metric_list_response%20%3E%20(schema)%20%3E%20(property)%20infrequentAccess%20%3E%20(property)%20published%20%3E%20(property)%20payloadSize">Link to this property</a>

</details>

<a href="#(resource)%20r2.buckets.metrics%20%3E%20(model)%20metric_list_response%20%3E%20(schema)%20%3E%20(property)%20infrequentAccess%20%3E%20(property)%20published">Link to this property</a>

<details>

<summary>

uploaded: optional object {metadataSize, objects, payloadSize }

Metrics on number of objects/amount of storage used.

</summary>

metadataSize: optional number

Amount of.

<a href="#(resource)%20r2.buckets.metrics%20%3E%20(model)%20metric_list_response%20%3E%20(schema)%20%3E%20(property)%20infrequentAccess%20%3E%20(property)%20uploaded%20%3E%20(property)%20metadataSize">Link to this property</a>

objects: optional number

Number of objects stored.

<a href="#(resource)%20r2.buckets.metrics%20%3E%20(model)%20metric_list_response%20%3E%20(schema)%20%3E%20(property)%20infrequentAccess%20%3E%20(property)%20uploaded%20%3E%20(property)%20objects">Link to this property</a>

payloadSize: optional number

Amount of storage used by object data.

<a href="#(resource)%20r2.buckets.metrics%20%3E%20(model)%20metric_list_response%20%3E%20(schema)%20%3E%20(property)%20infrequentAccess%20%3E%20(property)%20uploaded%20%3E%20(property)%20payloadSize">Link to this property</a>

</details>

<a href="#(resource)%20r2.buckets.metrics%20%3E%20(model)%20metric_list_response%20%3E%20(schema)%20%3E%20(property)%20infrequentAccess%20%3E%20(property)%20uploaded">Link to this property</a>

</details>

<a href="#(resource)%20r2.buckets.metrics%20%3E%20(model)%20metric_list_response%20%3E%20(schema)%20%3E%20(property)%20infrequentAccess">Link to this property</a>

<details>

<summary>

standard: optional object {published, uploaded }

Metrics based on what state they are in(uploaded or published).

</summary>

<details>

<summary>

published: optional object {metadataSize, objects, payloadSize }

Metrics on number of objects/amount of storage used.

</summary>

metadataSize: optional number

Amount of.

<a href="#(resource)%20r2.buckets.metrics%20%3E%20(model)%20metric_list_response%20%3E%20(schema)%20%3E%20(property)%20standard%20%3E%20(property)%20published%20%3E%20(property)%20metadataSize">Link to this property</a>

objects: optional number

Number of objects stored.

<a href="#(resource)%20r2.buckets.metrics%20%3E%20(model)%20metric_list_response%20%3E%20(schema)%20%3E%20(property)%20standard%20%3E%20(property)%20published%20%3E%20(property)%20objects">Link to this property</a>

payloadSize: optional number

Amount of storage used by object data.

<a href="#(resource)%20r2.buckets.metrics%20%3E%20(model)%20metric_list_response%20%3E%20(schema)%20%3E%20(property)%20standard%20%3E%20(property)%20published%20%3E%20(property)%20payloadSize">Link to this property</a>

</details>

<a href="#(resource)%20r2.buckets.metrics%20%3E%20(model)%20metric_list_response%20%3E%20(schema)%20%3E%20(property)%20standard%20%3E%20(property)%20published">Link to this property</a>

<details>

<summary>

uploaded: optional object {metadataSize, objects, payloadSize }

Metrics on number of objects/amount of storage used.

</summary>

metadataSize: optional number

Amount of.

<a href="#(resource)%20r2.buckets.metrics%20%3E%20(model)%20metric_list_response%20%3E%20(schema)%20%3E%20(property)%20standard%20%3E%20(property)%20uploaded%20%3E%20(property)%20metadataSize">Link to this property</a>

objects: optional number

Number of objects stored.

<a href="#(resource)%20r2.buckets.metrics%20%3E%20(model)%20metric_list_response%20%3E%20(schema)%20%3E%20(property)%20standard%20%3E%20(property)%20uploaded%20%3E%20(property)%20objects">Link to this property</a>

payloadSize: optional number

Amount of storage used by object data.

<a href="#(resource)%20r2.buckets.metrics%20%3E%20(model)%20metric_list_response%20%3E%20(schema)%20%3E%20(property)%20standard%20%3E%20(property)%20uploaded%20%3E%20(property)%20payloadSize">Link to this property</a>

</details>

<a href="#(resource)%20r2.buckets.metrics%20%3E%20(model)%20metric_list_response%20%3E%20(schema)%20%3E%20(property)%20standard%20%3E%20(property)%20uploaded">Link to this property</a>

</details>

<a href="#(resource)%20r2.buckets.metrics%20%3E%20(model)%20metric_list_response%20%3E%20(schema)%20%3E%20(property)%20standard">Link to this property</a>

</details>

[Link to this property](<#(resource)%20r2.buckets.metrics%20%3E%20(model)%20metric_list_response%20%3E%20(schema)>)