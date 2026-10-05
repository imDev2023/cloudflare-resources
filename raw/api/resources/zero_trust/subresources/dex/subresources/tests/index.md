---
title: Tests
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

[DEX](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Tests

##### [List DEX test analytics](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/tests/methods/list)

GET/accounts/{account\_id}/dex/tests/overview

##### ModelsExpand Collapse

<details>

<summary>

AggregateTimePeriod object {units, value }

</summary>

<details>

<summary>

units: "hours"or "days"or "testRuns"

</summary>

One of the following:

"hours"

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20aggregate_time_period%20%3E%20(schema)%20%3E%20(property)%20units%20%3E%20(member)%200">Link to this property</a>

"days"

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20aggregate_time_period%20%3E%20(schema)%20%3E%20(property)%20units%20%3E%20(member)%201">Link to this property</a>

"testRuns"

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20aggregate_time_period%20%3E%20(schema)%20%3E%20(property)%20units%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20aggregate_time_period%20%3E%20(schema)%20%3E%20(property)%20units">Link to this property</a>

value: number

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20aggregate_time_period%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20aggregate_time_period%20%3E%20(schema)>)

<details>

<summary>

Tests object {overviewMetrics, tests }

</summary>

<details>

<summary>

overviewMetrics: object {testsTotal, avgHttpAvailabilityPct, avgTracerouteAvailabilityPct }

</summary>

testsTotal: number

number of tests.

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20overviewMetrics%20%3E%20(property)%20testsTotal">Link to this property</a>

avgHttpAvailabilityPct: optional number

percentage availability for all HTTP test results in response.

formatfloat

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20overviewMetrics%20%3E%20(property)%20avgHttpAvailabilityPct">Link to this property</a>

avgTracerouteAvailabilityPct: optional number

percentage availability for all traceroutes results in response.

formatfloat

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20overviewMetrics%20%3E%20(property)%20avgTracerouteAvailabilityPct">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20overviewMetrics">Link to this property</a>

<details>

<summary>

tests: array of object {id, created, description, 13 more }

array of test results objects.

</summary>

id: string

API Resource UUID tag.

maxLength36

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

created: string

date the test was created.

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20created">Link to this property</a>

description: string

the test description defined during configuration

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

enabled: boolean

if true, then the test will run on targeted devices. Else, the test will not run.

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20enabled">Link to this property</a>

host: string

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20host">Link to this property</a>

interval: string

The interval at which the synthetic application test is set to run.

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20interval">Link to this property</a>

<details>

<summary>

kind: "http"or "traceroute"

test type, http or traceroute

</summary>

One of the following:

"http"

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20kind%20%3E%20(member)%200">Link to this property</a>

"traceroute"

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20kind%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20kind">Link to this property</a>

name: string

name given to this test

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

updated: string

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20updated">Link to this property</a>

<details>

<summary>

httpResults: optional object {resourceFetchTime }

</summary>

<details>

<summary>

resourceFetchTime: object {history, avgMs, overTime }

</summary>

<details>

<summary>

history: array of object {timePeriod, avgMs, deltaPct }

</summary>

timePeriod: <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20aggregate_time_period%20%3E%20(schema)">AggregateTimePeriod</a> { units, value }

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20httpResults%20%3E%20(property)%20resourceFetchTime%20%3E%20(property)%20history%20%3E%20(items)%20%3E%20(property)%20timePeriod">Link to this property</a>

avgMs: optional number

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20httpResults%20%3E%20(property)%20resourceFetchTime%20%3E%20(property)%20history%20%3E%20(items)%20%3E%20(property)%20avgMs">Link to this property</a>

deltaPct: optional number

formatfloat

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20httpResults%20%3E%20(property)%20resourceFetchTime%20%3E%20(property)%20history%20%3E%20(items)%20%3E%20(property)%20deltaPct">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20httpResults%20%3E%20(property)%20resourceFetchTime%20%3E%20(property)%20history">Link to this property</a>

avgMs: optional number

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20httpResults%20%3E%20(property)%20resourceFetchTime%20%3E%20(property)%20avgMs">Link to this property</a>

<details>

<summary>

overTime: optional object {timePeriod, values }

</summary>

timePeriod: <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20aggregate_time_period%20%3E%20(schema)">AggregateTimePeriod</a> { units, value }

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20httpResults%20%3E%20(property)%20resourceFetchTime%20%3E%20(property)%20overTime%20%3E%20(property)%20timePeriod">Link to this property</a>

<details>

<summary>

values: array of object {avgMs, timestamp }

</summary>

avgMs: number

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20httpResults%20%3E%20(property)%20resourceFetchTime%20%3E%20(property)%20overTime%20%3E%20(property)%20values%20%3E%20(items)%20%3E%20(property)%20avgMs">Link to this property</a>

timestamp: string

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20httpResults%20%3E%20(property)%20resourceFetchTime%20%3E%20(property)%20overTime%20%3E%20(property)%20values%20%3E%20(items)%20%3E%20(property)%20timestamp">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20httpResults%20%3E%20(property)%20resourceFetchTime%20%3E%20(property)%20overTime%20%3E%20(property)%20values">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20httpResults%20%3E%20(property)%20resourceFetchTime%20%3E%20(property)%20overTime">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20httpResults%20%3E%20(property)%20resourceFetchTime">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20httpResults">Link to this property</a>

<details>

<summary>

httpResultsByColo: optional array of object {colo, resourceFetchTime }

</summary>

colo: string

Cloudflare colo

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20httpResultsByColo%20%3E%20(items)%20%3E%20(property)%20colo">Link to this property</a>

<details>

<summary>

resourceFetchTime: object {history, avgMs, overTime }

</summary>

<details>

<summary>

history: array of object {timePeriod, avgMs, deltaPct }

</summary>

timePeriod: <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20aggregate_time_period%20%3E%20(schema)">AggregateTimePeriod</a> { units, value }

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20httpResultsByColo%20%3E%20(items)%20%3E%20(property)%20resourceFetchTime%20%3E%20(property)%20history%20%3E%20(items)%20%3E%20(property)%20timePeriod">Link to this property</a>

avgMs: optional number

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20httpResultsByColo%20%3E%20(items)%20%3E%20(property)%20resourceFetchTime%20%3E%20(property)%20history%20%3E%20(items)%20%3E%20(property)%20avgMs">Link to this property</a>

deltaPct: optional number

formatfloat

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20httpResultsByColo%20%3E%20(items)%20%3E%20(property)%20resourceFetchTime%20%3E%20(property)%20history%20%3E%20(items)%20%3E%20(property)%20deltaPct">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20httpResultsByColo%20%3E%20(items)%20%3E%20(property)%20resourceFetchTime%20%3E%20(property)%20history">Link to this property</a>

avgMs: optional number

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20httpResultsByColo%20%3E%20(items)%20%3E%20(property)%20resourceFetchTime%20%3E%20(property)%20avgMs">Link to this property</a>

<details>

<summary>

overTime: optional object {timePeriod, values }

</summary>

timePeriod: <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20aggregate_time_period%20%3E%20(schema)">AggregateTimePeriod</a> { units, value }

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20httpResultsByColo%20%3E%20(items)%20%3E%20(property)%20resourceFetchTime%20%3E%20(property)%20overTime%20%3E%20(property)%20timePeriod">Link to this property</a>

<details>

<summary>

values: array of object {avgMs, timestamp }

</summary>

avgMs: number

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20httpResultsByColo%20%3E%20(items)%20%3E%20(property)%20resourceFetchTime%20%3E%20(property)%20overTime%20%3E%20(property)%20values%20%3E%20(items)%20%3E%20(property)%20avgMs">Link to this property</a>

timestamp: string

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20httpResultsByColo%20%3E%20(items)%20%3E%20(property)%20resourceFetchTime%20%3E%20(property)%20overTime%20%3E%20(property)%20values%20%3E%20(items)%20%3E%20(property)%20timestamp">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20httpResultsByColo%20%3E%20(items)%20%3E%20(property)%20resourceFetchTime%20%3E%20(property)%20overTime%20%3E%20(property)%20values">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20httpResultsByColo%20%3E%20(items)%20%3E%20(property)%20resourceFetchTime%20%3E%20(property)%20overTime">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20httpResultsByColo%20%3E%20(items)%20%3E%20(property)%20resourceFetchTime">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20httpResultsByColo">Link to this property</a>

method: optional string

for HTTP, the method to use when running the test

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20method">Link to this property</a>

<details>

<summary>

target\_policies: optional array of <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.dex%20%3E%20(model)%20digital_experience_monitor%20%3E%20(schema)">DigitalExperienceMonitor</a> { id, default, name }

</summary>

id: string

API Resource UUID tag.

maxLength36

<a href="#(resource)%20zero_trust.dex%20%3E%20(model)%20digital_experience_monitor%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

default: boolean

Whether the policy is the default for the account.

<a href="#(resource)%20zero_trust.dex%20%3E%20(model)%20digital_experience_monitor%20%3E%20(schema)%20%3E%20(property)%20default">Link to this property</a>

name: string

<a href="#(resource)%20zero_trust.dex%20%3E%20(model)%20digital_experience_monitor%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20target_policies">Link to this property</a>

targeted: optional boolean

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20targeted">Link to this property</a>

<details>

<summary>

tracerouteResults: optional object {roundTripTime }

</summary>

<details>

<summary>

roundTripTime: object {history, avgMs, overTime }

</summary>

<details>

<summary>

history: array of object {timePeriod, avgMs, deltaPct }

</summary>

timePeriod: <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20aggregate_time_period%20%3E%20(schema)">AggregateTimePeriod</a> { units, value }

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20tracerouteResults%20%3E%20(property)%20roundTripTime%20%3E%20(property)%20history%20%3E%20(items)%20%3E%20(property)%20timePeriod">Link to this property</a>

avgMs: optional number

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20tracerouteResults%20%3E%20(property)%20roundTripTime%20%3E%20(property)%20history%20%3E%20(items)%20%3E%20(property)%20avgMs">Link to this property</a>

deltaPct: optional number

formatfloat

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20tracerouteResults%20%3E%20(property)%20roundTripTime%20%3E%20(property)%20history%20%3E%20(items)%20%3E%20(property)%20deltaPct">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20tracerouteResults%20%3E%20(property)%20roundTripTime%20%3E%20(property)%20history">Link to this property</a>

avgMs: optional number

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20tracerouteResults%20%3E%20(property)%20roundTripTime%20%3E%20(property)%20avgMs">Link to this property</a>

<details>

<summary>

overTime: optional object {timePeriod, values }

</summary>

timePeriod: <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20aggregate_time_period%20%3E%20(schema)">AggregateTimePeriod</a> { units, value }

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20tracerouteResults%20%3E%20(property)%20roundTripTime%20%3E%20(property)%20overTime%20%3E%20(property)%20timePeriod">Link to this property</a>

<details>

<summary>

values: array of object {avgMs, timestamp }

</summary>

avgMs: number

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20tracerouteResults%20%3E%20(property)%20roundTripTime%20%3E%20(property)%20overTime%20%3E%20(property)%20values%20%3E%20(items)%20%3E%20(property)%20avgMs">Link to this property</a>

timestamp: string

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20tracerouteResults%20%3E%20(property)%20roundTripTime%20%3E%20(property)%20overTime%20%3E%20(property)%20values%20%3E%20(items)%20%3E%20(property)%20timestamp">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20tracerouteResults%20%3E%20(property)%20roundTripTime%20%3E%20(property)%20overTime%20%3E%20(property)%20values">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20tracerouteResults%20%3E%20(property)%20roundTripTime%20%3E%20(property)%20overTime">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20tracerouteResults%20%3E%20(property)%20roundTripTime">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20tracerouteResults">Link to this property</a>

<details>

<summary>

tracerouteResultsByColo: optional array of object {colo, roundTripTime }

</summary>

colo: string

Cloudflare colo

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20tracerouteResultsByColo%20%3E%20(items)%20%3E%20(property)%20colo">Link to this property</a>

<details>

<summary>

roundTripTime: object {history, avgMs, overTime }

</summary>

<details>

<summary>

history: array of object {timePeriod, avgMs, deltaPct }

</summary>

timePeriod: <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20aggregate_time_period%20%3E%20(schema)">AggregateTimePeriod</a> { units, value }

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20tracerouteResultsByColo%20%3E%20(items)%20%3E%20(property)%20roundTripTime%20%3E%20(property)%20history%20%3E%20(items)%20%3E%20(property)%20timePeriod">Link to this property</a>

avgMs: optional number

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20tracerouteResultsByColo%20%3E%20(items)%20%3E%20(property)%20roundTripTime%20%3E%20(property)%20history%20%3E%20(items)%20%3E%20(property)%20avgMs">Link to this property</a>

deltaPct: optional number

formatfloat

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20tracerouteResultsByColo%20%3E%20(items)%20%3E%20(property)%20roundTripTime%20%3E%20(property)%20history%20%3E%20(items)%20%3E%20(property)%20deltaPct">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20tracerouteResultsByColo%20%3E%20(items)%20%3E%20(property)%20roundTripTime%20%3E%20(property)%20history">Link to this property</a>

avgMs: optional number

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20tracerouteResultsByColo%20%3E%20(items)%20%3E%20(property)%20roundTripTime%20%3E%20(property)%20avgMs">Link to this property</a>

<details>

<summary>

overTime: optional object {timePeriod, values }

</summary>

timePeriod: <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20aggregate_time_period%20%3E%20(schema)">AggregateTimePeriod</a> { units, value }

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20tracerouteResultsByColo%20%3E%20(items)%20%3E%20(property)%20roundTripTime%20%3E%20(property)%20overTime%20%3E%20(property)%20timePeriod">Link to this property</a>

<details>

<summary>

values: array of object {avgMs, timestamp }

</summary>

avgMs: number

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20tracerouteResultsByColo%20%3E%20(items)%20%3E%20(property)%20roundTripTime%20%3E%20(property)%20overTime%20%3E%20(property)%20values%20%3E%20(items)%20%3E%20(property)%20avgMs">Link to this property</a>

timestamp: string

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20tracerouteResultsByColo%20%3E%20(items)%20%3E%20(property)%20roundTripTime%20%3E%20(property)%20overTime%20%3E%20(property)%20values%20%3E%20(items)%20%3E%20(property)%20timestamp">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20tracerouteResultsByColo%20%3E%20(items)%20%3E%20(property)%20roundTripTime%20%3E%20(property)%20overTime%20%3E%20(property)%20values">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20tracerouteResultsByColo%20%3E%20(items)%20%3E%20(property)%20roundTripTime%20%3E%20(property)%20overTime">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20tracerouteResultsByColo%20%3E%20(items)%20%3E%20(property)%20roundTripTime">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests%20%3E%20(items)%20%3E%20(property)%20tracerouteResultsByColo">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)%20%3E%20(property)%20tests">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.dex.tests%20%3E%20(model)%20tests%20%3E%20(schema)>)

#### TestsUnique Devices

##### [Get count of devices targeted](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/tests/subresources/unique_devices/methods/list)

GET/accounts/{account\_id}/dex/tests/unique-devices

##### ModelsExpand Collapse

<details>

<summary>

UniqueDevices object {uniqueDevicesTotal }

</summary>

uniqueDevicesTotal: number

total number of unique devices

<a href="#(resource)%20zero_trust.dex.tests.unique_devices%20%3E%20(model)%20unique_devices%20%3E%20(schema)%20%3E%20(property)%20uniqueDevicesTotal">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.dex.tests.unique_devices%20%3E%20(model)%20unique_devices%20%3E%20(schema)>)