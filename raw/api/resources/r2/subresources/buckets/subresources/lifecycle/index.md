---
title: Lifecycle
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[R2](https://developers.cloudflare.com/api/resources/r2)

[Buckets](https://developers.cloudflare.com/api/resources/r2/subresources/buckets)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Lifecycle

##### [Get Object Lifecycle Rules](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/lifecycle/methods/get)

GET/accounts/{account\_id}/r2/buckets/{bucket\_name}/lifecycle

##### [Set Object Lifecycle Rules](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/lifecycle/methods/update)

PUT/accounts/{account\_id}/r2/buckets/{bucket\_name}/lifecycle

##### ModelsExpand Collapse

<details>

<summary>

LifecycleGetResponse object {rules }

</summary>

<details>

<summary>

rules: optional array of object {id, conditions, enabled, 3 more }

</summary>

id: string

Unique identifier for this rule.

<a href="#(resource)%20r2.buckets.lifecycle%20%3E%20(model)%20lifecycle_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

conditions: object {prefix }

Conditions that apply to all transitions of this rule.

</summary>

prefix: string

Transitions will only apply to objects/uploads in the bucket that start with the given prefix, an empty prefix can be provided to scope rule to all objects/uploads.

<a href="#(resource)%20r2.buckets.lifecycle%20%3E%20(model)%20lifecycle_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20conditions%20%3E%20(property)%20prefix">Link to this property</a>

</details>

<a href="#(resource)%20r2.buckets.lifecycle%20%3E%20(model)%20lifecycle_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20conditions">Link to this property</a>

enabled: boolean

Whether or not this rule is in effect.

<a href="#(resource)%20r2.buckets.lifecycle%20%3E%20(model)%20lifecycle_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20enabled">Link to this property</a>

<details>

<summary>

abortMultipartUploadsTransition: optional object {condition }

Transition to abort ongoing multipart uploads.

</summary>

<details>

<summary>

condition: optional object {maxAge, type }

Condition for lifecycle transitions to apply after an object reaches an age in seconds.

</summary>

maxAge: number

<a href="#(resource)%20r2.buckets.lifecycle%20%3E%20(model)%20lifecycle_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20abortMultipartUploadsTransition%20%3E%20(property)%20condition%20%3E%20(property)%20maxAge">Link to this property</a>

type: "Age"

<a href="#(resource)%20r2.buckets.lifecycle%20%3E%20(model)%20lifecycle_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20abortMultipartUploadsTransition%20%3E%20(property)%20condition%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20r2.buckets.lifecycle%20%3E%20(model)%20lifecycle_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20abortMultipartUploadsTransition%20%3E%20(property)%20condition">Link to this property</a>

</details>

<a href="#(resource)%20r2.buckets.lifecycle%20%3E%20(model)%20lifecycle_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20abortMultipartUploadsTransition">Link to this property</a>

<details>

<summary>

deleteObjectsTransition: optional object {condition }

Transition to delete objects.

</summary>

<details>

<summary>

condition: optional object {maxAge, type } or object {date, type }

Condition for lifecycle transitions to apply after an object reaches an age in seconds.

</summary>

One of the following:

<details>

<summary>

R2LifecycleAgeCondition object {maxAge, type }

Condition for lifecycle transitions to apply after an object reaches an age in seconds.

</summary>

maxAge: number

<a href="#(resource)%20r2.buckets.lifecycle%20%3E%20(model)%20lifecycle_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20deleteObjectsTransition%20%3E%20(property)%20condition%20%3E%20(variant)%200%20%3E%20(property)%20maxAge">Link to this property</a>

type: "Age"

<a href="#(resource)%20r2.buckets.lifecycle%20%3E%20(model)%20lifecycle_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20deleteObjectsTransition%20%3E%20(property)%20condition%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20r2.buckets.lifecycle%20%3E%20(model)%20lifecycle_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20deleteObjectsTransition%20%3E%20(property)%20condition%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

R2LifecycleDateCondition object {date, type }

Condition for lifecycle transitions to apply on a specific date.

</summary>

date: string

formatdate-time

<a href="#(resource)%20r2.buckets.lifecycle%20%3E%20(model)%20lifecycle_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20deleteObjectsTransition%20%3E%20(property)%20condition%20%3E%20(variant)%201%20%3E%20(property)%20date">Link to this property</a>

type: "Date"

<a href="#(resource)%20r2.buckets.lifecycle%20%3E%20(model)%20lifecycle_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20deleteObjectsTransition%20%3E%20(property)%20condition%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20r2.buckets.lifecycle%20%3E%20(model)%20lifecycle_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20deleteObjectsTransition%20%3E%20(property)%20condition%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20r2.buckets.lifecycle%20%3E%20(model)%20lifecycle_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20deleteObjectsTransition%20%3E%20(property)%20condition">Link to this property</a>

</details>

<a href="#(resource)%20r2.buckets.lifecycle%20%3E%20(model)%20lifecycle_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20deleteObjectsTransition">Link to this property</a>

<details>

<summary>

storageClassTransitions: optional array of object {condition, storageClass }

Transitions to change the storage class of objects.

</summary>

<details>

<summary>

condition: object {maxAge, type } or object {date, type }

Condition for lifecycle transitions to apply after an object reaches an age in seconds.

</summary>

One of the following:

<details>

<summary>

R2LifecycleAgeCondition object {maxAge, type }

Condition for lifecycle transitions to apply after an object reaches an age in seconds.

</summary>

maxAge: number

<a href="#(resource)%20r2.buckets.lifecycle%20%3E%20(model)%20lifecycle_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20storageClassTransitions%20%3E%20(items)%20%3E%20(property)%20condition%20%3E%20(variant)%200%20%3E%20(property)%20maxAge">Link to this property</a>

type: "Age"

<a href="#(resource)%20r2.buckets.lifecycle%20%3E%20(model)%20lifecycle_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20storageClassTransitions%20%3E%20(items)%20%3E%20(property)%20condition%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20r2.buckets.lifecycle%20%3E%20(model)%20lifecycle_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20storageClassTransitions%20%3E%20(items)%20%3E%20(property)%20condition%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

R2LifecycleDateCondition object {date, type }

Condition for lifecycle transitions to apply on a specific date.

</summary>

date: string

formatdate-time

<a href="#(resource)%20r2.buckets.lifecycle%20%3E%20(model)%20lifecycle_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20storageClassTransitions%20%3E%20(items)%20%3E%20(property)%20condition%20%3E%20(variant)%201%20%3E%20(property)%20date">Link to this property</a>

type: "Date"

<a href="#(resource)%20r2.buckets.lifecycle%20%3E%20(model)%20lifecycle_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20storageClassTransitions%20%3E%20(items)%20%3E%20(property)%20condition%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20r2.buckets.lifecycle%20%3E%20(model)%20lifecycle_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20storageClassTransitions%20%3E%20(items)%20%3E%20(property)%20condition%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20r2.buckets.lifecycle%20%3E%20(model)%20lifecycle_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20storageClassTransitions%20%3E%20(items)%20%3E%20(property)%20condition">Link to this property</a>

storageClass: "InfrequentAccess"

<a href="#(resource)%20r2.buckets.lifecycle%20%3E%20(model)%20lifecycle_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20storageClassTransitions%20%3E%20(items)%20%3E%20(property)%20storageClass">Link to this property</a>

</details>

<a href="#(resource)%20r2.buckets.lifecycle%20%3E%20(model)%20lifecycle_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20storageClassTransitions">Link to this property</a>

</details>

<a href="#(resource)%20r2.buckets.lifecycle%20%3E%20(model)%20lifecycle_get_response%20%3E%20(schema)%20%3E%20(property)%20rules">Link to this property</a>

</details>

[Link to this property](<#(resource)%20r2.buckets.lifecycle%20%3E%20(model)%20lifecycle_get_response%20%3E%20(schema)>)

LifecycleUpdateResponse = unknown

[Link to this property](<#(resource)%20r2.buckets.lifecycle%20%3E%20(model)%20lifecycle_update_response%20%3E%20(schema)>)