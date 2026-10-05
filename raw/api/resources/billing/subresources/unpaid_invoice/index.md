---
title: Unpaid Invoice
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Billing](https://developers.cloudflare.com/api/resources/billing)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Unpaid Invoice

##### [Get Unpaid Invoices](https://developers.cloudflare.com/api/resources/billing/subresources/unpaid_invoice/methods/get)

GET/accounts/{account\_id}/billing/unpaid-invoice

##### ModelsExpand Collapse

<details>

<summary>

UnpaidInvoiceGetResponse object {invoices }

</summary>

<details>

<summary>

invoices: optional array of object {id, action, amount, 12 more }

List of unpaid invoices.

</summary>

id: optional string

Billing history item identifier.

<a href="#(resource)%20billing.unpaid_invoice%20%3E%20(model)%20unpaid_invoice_get_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

action: optional string

The billing item action.

<a href="#(resource)%20billing.unpaid_invoice%20%3E%20(model)%20unpaid_invoice_get_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20action">Link to this property</a>

amount: optional number

The amount associated with this billing item.

<a href="#(resource)%20billing.unpaid_invoice%20%3E%20(model)%20unpaid_invoice_get_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20amount">Link to this property</a>

amount\_to\_pay: optional number

The amount remaining to pay.

<a href="#(resource)%20billing.unpaid_invoice%20%3E%20(model)%20unpaid_invoice_get_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20amount_to_pay">Link to this property</a>

currency: optional string

The currency of the billing item.

<a href="#(resource)%20billing.unpaid_invoice%20%3E%20(model)%20unpaid_invoice_get_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20currency">Link to this property</a>

description: optional string

The billing item description.

<a href="#(resource)%20billing.unpaid_invoice%20%3E%20(model)%20unpaid_invoice_get_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

external\_invoice\_id: optional string

The external invoice identifier.

<a href="#(resource)%20billing.unpaid_invoice%20%3E%20(model)%20unpaid_invoice_get_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20external_invoice_id">Link to this property</a>

hosted\_invoice\_url: optional string

URL to the hosted invoice.

<a href="#(resource)%20billing.unpaid_invoice%20%3E%20(model)%20unpaid_invoice_get_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20hosted_invoice_url">Link to this property</a>

invoice\_id: optional string

The associated invoice identifier.

<a href="#(resource)%20billing.unpaid_invoice%20%3E%20(model)%20unpaid_invoice_get_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20invoice_id">Link to this property</a>

occurred\_at: optional string

When the billing event occurred.

formatdate-time

<a href="#(resource)%20billing.unpaid_invoice%20%3E%20(model)%20unpaid_invoice_get_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20occurred_at">Link to this property</a>

receipt\_id: optional string

The associated receipt identifier.

<a href="#(resource)%20billing.unpaid_invoice%20%3E%20(model)%20unpaid_invoice_get_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20receipt_id">Link to this property</a>

source: optional string

The source of the billing item.

<a href="#(resource)%20billing.unpaid_invoice%20%3E%20(model)%20unpaid_invoice_get_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

source\_invoice\_id: optional string

The source invoice identifier.

<a href="#(resource)%20billing.unpaid_invoice%20%3E%20(model)%20unpaid_invoice_get_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20source_invoice_id">Link to this property</a>

status: optional string

The status of the billing item.

<a href="#(resource)%20billing.unpaid_invoice%20%3E%20(model)%20unpaid_invoice_get_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

type: optional string

The billing item type.

<a href="#(resource)%20billing.unpaid_invoice%20%3E%20(model)%20unpaid_invoice_get_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20billing.unpaid_invoice%20%3E%20(model)%20unpaid_invoice_get_response%20%3E%20(schema)%20%3E%20(property)%20invoices">Link to this property</a>

</details>

[Link to this property](<#(resource)%20billing.unpaid_invoice%20%3E%20(model)%20unpaid_invoice_get_response%20%3E%20(schema)>)