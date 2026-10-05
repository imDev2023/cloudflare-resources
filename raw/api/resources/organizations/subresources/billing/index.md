---
title: Billing
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Organizations](https://developers.cloudflare.com/api/resources/organizations)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Billing

#### BillingUsage

##### [Get Organization Usage (Version 2, Alpha, Restricted)](https://developers.cloudflare.com/api/resources/organizations/subresources/billing/subresources/usage/methods/get)

GET/organizations/{organization\_id}/billable/usage

##### ModelsExpand Collapse

<details>

<summary>

UsageGetResponse = array of object {ChargeCategory, ChargeDescription, ChargeFrequency, 33 more }

Contains the array of cost and usage records.

</summary>

ChargeCategory: "Usage"

Highest-level classification of a charge based on the nature of how it gets billed. Currently only “Usage” is supported.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20ChargeCategory">Link to this property</a>

ChargeDescription: string

Self-contained summary of the charge’s purpose and price.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20ChargeDescription">Link to this property</a>

ChargeFrequency: "Usage-Based"

Indicates how often a charge occurs. Currently only “Usage-Based” is supported.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20ChargeFrequency">Link to this property</a>

ChargePeriodEnd: string

Exclusive end of the time interval during which the usage was consumed.

formatdate-time

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20ChargePeriodEnd">Link to this property</a>

ChargePeriodStart: string

Inclusive start of the time interval during which the usage was consumed.

formatdate-time

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20ChargePeriodStart">Link to this property</a>

ConsumedQuantity: number

Measured usage amount within the charge period. Reflects raw metered consumption before pricing transformations.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20ConsumedQuantity">Link to this property</a>

ConsumedUnit: string

Unit of measure for the consumed quantity (e.g., “GB”, “Requests”, “vCPU-Hours”).

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20ConsumedUnit">Link to this property</a>

HostProviderName: string

Name of the entity providing the underlying infrastructure or platform.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20HostProviderName">Link to this property</a>

InvoiceIssuerName: string

Name of the entity responsible for invoicing for the services consumed.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20InvoiceIssuerName">Link to this property</a>

ServiceProviderName: string

Name of the entity that made the services available for purchase.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20ServiceProviderName">Link to this property</a>

x\_BillableMetricId: string

The unique identifier for the billable metric in the Cloudflare catalog. Cloudflare extension; replaces FOCUS SkuId.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20x_BillableMetricId">Link to this property</a>

BilledCost: optional number

A charge serving as the basis for invoicing, inclusive of all reduced rates and discounts while excluding the amortization of upfront charges (one-time or recurring).

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20BilledCost">Link to this property</a>

BillingAccountId: optional string

Public identifier of the Cloudflare account (account tag). Omitted when account is not part of the requested grouping, and always omitted for usage measured at contract level, even when grouping by account: that usage is returned as its own record with no account.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20BillingAccountId">Link to this property</a>

BillingAccountName: optional string

Display name of the Cloudflare account. Omitted when account is not part of the requested grouping, and for usage measured at contract level.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20BillingAccountName">Link to this property</a>

BillingCurrency: optional string

Currency that a charge was billed in (ISO 4217).

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20BillingCurrency">Link to this property</a>

BillingPeriodEnd: optional string

Exclusive end of the billing cycle that contains this usage record.

formatdate-time

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20BillingPeriodEnd">Link to this property</a>

BillingPeriodStart: optional string

Inclusive start of the billing cycle that contains this usage record.

formatdate-time

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20BillingPeriodStart">Link to this property</a>

ChargeClass: optional "Correction"

Indicates whether the row represents a correction to one or more charges invoiced in a previous billing period.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20ChargeClass">Link to this property</a>

ContractedCost: optional number

Cost calculated by multiplying ContractedUnitPrice and the corresponding PricingQuantity.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20ContractedCost">Link to this property</a>

ContractedUnitPrice: optional number

The agreed-upon unit price for a single PricingUnit of the associated billable metric, inclusive of negotiated discounts, if present, while excluding any other discounts.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20ContractedUnitPrice">Link to this property</a>

EffectiveCost: optional number

The amortized cost of the charge after applying all reduced rates, discounts, and the applicable portion of relevant, prepaid purchases (one-time or recurring) that covered the charge.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20EffectiveCost">Link to this property</a>

ListCost: optional number

Cost calculated by multiplying ListUnitPrice and the corresponding PricingQuantity.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20ListCost">Link to this property</a>

ListUnitPrice: optional number

Suggested provider-published unit price for a single PricingUnit of the associated billable metric, exclusive of any discounts.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20ListUnitPrice">Link to this property</a>

PricingQuantity: optional number

Volume of a given service used or purchased, based on the PricingUnit.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20PricingQuantity">Link to this property</a>

PricingUnit: optional string

Provider-specified measurement unit for determining unit prices, indicating how the provider rates measured usage after applying pricing rules like block pricing.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20PricingUnit">Link to this property</a>

RegionId: optional string

Provider-assigned identifier for an isolated geographic area where a service is provided.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20RegionId">Link to this property</a>

RegionName: optional string

Name of an isolated geographic area where a service is provided.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20RegionName">Link to this property</a>

SubAccountId: optional string

Unique identifier assigned to a grouping of services. For Cloudflare, this is the subscription or contract ID.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20SubAccountId">Link to this property</a>

SubAccountName: optional string

Name assigned to a grouping of services. For Cloudflare, this is the subscription or contract display name.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20SubAccountName">Link to this property</a>

<details>

<summary>

Tags: optional map\[stringor true]

Tag values for the requested <code>GroupBy</code> keys. Omitted when <code>GroupBy</code> is not provided. Missing keys are omitted, and key-only tags are returned as boolean <code>true</code>. All other tag values are strings.

</summary>

One of the following:

string

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20Tags%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

true

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20Tags%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20Tags">Link to this property</a>

x\_BillableMetricName: optional string

The display name of the billable metric. Cloudflare extension; replaces FOCUS SkuMeter.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20x_BillableMetricName">Link to this property</a>

x\_ProductCategoryName: optional string

The product category the charge belongs to (e.g., “Developer”, “Cloudflare One”). Cloudflare extension; replaces FOCUS ServiceCategory.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20x_ProductCategoryName">Link to this property</a>

x\_ProductFamilyId: optional string

The unique identifier for the product family in the Cloudflare catalog. Cloudflare extension; replaces FOCUS ServiceId.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20x_ProductFamilyId">Link to this property</a>

x\_ProductFamilyName: optional string

The product family the charge belongs to (e.g., “R2”, “Workers”). Cloudflare extension; replaces FOCUS ServiceName.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20x_ProductFamilyName">Link to this property</a>

x\_ZoneId: optional string

The identifier for the Cloudflare zone (zone tag). Omitted when zone is not part of the requested grouping, and always omitted for usage measured at contract level, even when grouping by zone. Cloudflare extension.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20x_ZoneId">Link to this property</a>

x\_ZoneName: optional string

The display name of the Cloudflare zone. Omitted when zone is not part of the requested grouping, and for usage measured at contract level. Cloudflare extension.

<a href="#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20x_ZoneName">Link to this property</a>

</details>

[Link to this property](<#(resource)%20organizations.billing.usage%20%3E%20(model)%20usage_get_response%20%3E%20(schema)>)