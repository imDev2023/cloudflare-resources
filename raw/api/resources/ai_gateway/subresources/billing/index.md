---
title: Billing
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[AI Gateway](https://developers.cloudflare.com/api/resources/ai_gateway)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Billing

##### [Get credit balance](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/billing/methods/credit_balance)

GET/accounts/{account\_id}/ai-gateway/billing/credit-balance

##### [Get usage history](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/billing/methods/usage_history)

GET/accounts/{account\_id}/ai-gateway/billing/usage-history

##### [Get invoice history](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/billing/methods/invoice_history)

GET/accounts/{account\_id}/ai-gateway/billing/invoice-history

##### [Get invoice preview](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/billing/methods/invoice_preview)

GET/accounts/{account\_id}/ai-gateway/billing/invoice-preview

##### ModelsExpand Collapse

<details>

<summary>

BillingCreditBalanceResponse object {balance, has\_default\_payment\_method, payment\_method, 2 more }

</summary>

balance: number

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_credit_balance_response%20%3E%20(schema)%20%3E%20(property)%20balance">Link to this property</a>

has\_default\_payment\_method: boolean

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_credit_balance_response%20%3E%20(schema)%20%3E%20(property)%20has_default_payment_method">Link to this property</a>

<details>

<summary>

payment\_method: object {brand, last4 }

</summary>

brand: optional string

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_credit_balance_response%20%3E%20(schema)%20%3E%20(property)%20payment_method%20%3E%20(property)%20brand">Link to this property</a>

last4: optional string

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_credit_balance_response%20%3E%20(schema)%20%3E%20(property)%20payment_method%20%3E%20(property)%20last4">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_credit_balance_response%20%3E%20(schema)%20%3E%20(property)%20payment_method">Link to this property</a>

<details>

<summary>

topup\_config: object {amount, threshold, disabledReason, 2 more }

</summary>

amount: number

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_credit_balance_response%20%3E%20(schema)%20%3E%20(property)%20topup_config%20%3E%20(property)%20amount">Link to this property</a>

threshold: number

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_credit_balance_response%20%3E%20(schema)%20%3E%20(property)%20topup_config%20%3E%20(property)%20threshold">Link to this property</a>

disabledReason: optional string

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_credit_balance_response%20%3E%20(schema)%20%3E%20(property)%20topup_config%20%3E%20(property)%20disabledReason">Link to this property</a>

error: optional string

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_credit_balance_response%20%3E%20(schema)%20%3E%20(property)%20topup_config%20%3E%20(property)%20error">Link to this property</a>

lastFailedAt: optional number

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_credit_balance_response%20%3E%20(schema)%20%3E%20(property)%20topup_config%20%3E%20(property)%20lastFailedAt">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_credit_balance_response%20%3E%20(schema)%20%3E%20(property)%20topup_config">Link to this property</a>

first\_topup\_success: optional boolean

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_credit_balance_response%20%3E%20(schema)%20%3E%20(property)%20first_topup_success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_credit_balance_response%20%3E%20(schema)>)

<details>

<summary>

BillingUsageHistoryResponse object {history }

</summary>

<details>

<summary>

history: array of object {id, aggregated\_value, end\_time, start\_time }

</summary>

id: string

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_usage_history_response%20%3E%20(schema)%20%3E%20(property)%20history%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

aggregated\_value: number

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_usage_history_response%20%3E%20(schema)%20%3E%20(property)%20history%20%3E%20(items)%20%3E%20(property)%20aggregated_value">Link to this property</a>

end\_time: number

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_usage_history_response%20%3E%20(schema)%20%3E%20(property)%20history%20%3E%20(items)%20%3E%20(property)%20end_time">Link to this property</a>

start\_time: number

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_usage_history_response%20%3E%20(schema)%20%3E%20(property)%20history%20%3E%20(items)%20%3E%20(property)%20start_time">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_usage_history_response%20%3E%20(schema)%20%3E%20(property)%20history">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_usage_history_response%20%3E%20(schema)>)

<details>

<summary>

BillingInvoiceHistoryResponse object {invoices, pagination }

</summary>

<details>

<summary>

invoices: array of object {amount\_due, amount\_paid, amount\_remaining, 11 more }

</summary>

amount\_due: number

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_history_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20amount_due">Link to this property</a>

amount\_paid: number

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_history_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20amount_paid">Link to this property</a>

amount\_remaining: number

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_history_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20amount_remaining">Link to this property</a>

currency: string

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_history_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20currency">Link to this property</a>

id: optional string

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_history_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

attempt\_count: optional number

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_history_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20attempt_count">Link to this property</a>

attempted: optional boolean

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_history_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20attempted">Link to this property</a>

auto\_advance: optional boolean

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_history_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20auto_advance">Link to this property</a>

created: optional number

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_history_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20created">Link to this property</a>

created\_by: optional string

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_history_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20created_by">Link to this property</a>

description: optional string

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_history_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

invoice\_origin: optional string

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_history_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20invoice_origin">Link to this property</a>

invoice\_pdf: optional string

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_history_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20invoice_pdf">Link to this property</a>

status: optional string

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_history_response%20%3E%20(schema)%20%3E%20(property)%20invoices%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_history_response%20%3E%20(schema)%20%3E%20(property)%20invoices">Link to this property</a>

<details>

<summary>

pagination: object {has\_more, page, per\_page, total\_count }

</summary>

has\_more: boolean

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_history_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20has_more">Link to this property</a>

page: number

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_history_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20page">Link to this property</a>

per\_page: number

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_history_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20per_page">Link to this property</a>

total\_count: number

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_history_response%20%3E%20(schema)%20%3E%20(property)%20pagination%20%3E%20(property)%20total_count">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_history_response%20%3E%20(schema)%20%3E%20(property)%20pagination">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_history_response%20%3E%20(schema)>)

<details>

<summary>

BillingInvoicePreviewResponse object {id, amount\_due, amount\_paid, 6 more }

</summary>

id: string

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

amount\_due: number

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)%20%3E%20(property)%20amount_due">Link to this property</a>

amount\_paid: number

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)%20%3E%20(property)%20amount_paid">Link to this property</a>

amount\_remaining: number

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)%20%3E%20(property)%20amount_remaining">Link to this property</a>

currency: string

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)%20%3E%20(property)%20currency">Link to this property</a>

<details>

<summary>

invoice\_lines: array of object {amount, currency, description, 4 more }

</summary>

amount: number

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)%20%3E%20(property)%20invoice_lines%20%3E%20(items)%20%3E%20(property)%20amount">Link to this property</a>

currency: string

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)%20%3E%20(property)%20invoice_lines%20%3E%20(items)%20%3E%20(property)%20currency">Link to this property</a>

description: string

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)%20%3E%20(property)%20invoice_lines%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

period: object {end, start }

</summary>

end: number

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)%20%3E%20(property)%20invoice_lines%20%3E%20(items)%20%3E%20(property)%20period%20%3E%20(property)%20end">Link to this property</a>

start: number

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)%20%3E%20(property)%20invoice_lines%20%3E%20(items)%20%3E%20(property)%20period%20%3E%20(property)%20start">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)%20%3E%20(property)%20invoice_lines%20%3E%20(items)%20%3E%20(property)%20period">Link to this property</a>

<details>

<summary>

pricing: object {unit\_amount\_decimal }

</summary>

unit\_amount\_decimal: string

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)%20%3E%20(property)%20invoice_lines%20%3E%20(items)%20%3E%20(property)%20pricing%20%3E%20(property)%20unit_amount_decimal">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)%20%3E%20(property)%20invoice_lines%20%3E%20(items)%20%3E%20(property)%20pricing">Link to this property</a>

quantity: number

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)%20%3E%20(property)%20invoice_lines%20%3E%20(items)%20%3E%20(property)%20quantity">Link to this property</a>

<details>

<summary>

pretax\_credit\_amounts: optional array of object {amount, type, credit\_balance\_transaction, discount }

</summary>

amount: number

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)%20%3E%20(property)%20invoice_lines%20%3E%20(items)%20%3E%20(property)%20pretax_credit_amounts%20%3E%20(items)%20%3E%20(property)%20amount">Link to this property</a>

type: string

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)%20%3E%20(property)%20invoice_lines%20%3E%20(items)%20%3E%20(property)%20pretax_credit_amounts%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

credit\_balance\_transaction: optional string

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)%20%3E%20(property)%20invoice_lines%20%3E%20(items)%20%3E%20(property)%20pretax_credit_amounts%20%3E%20(items)%20%3E%20(property)%20credit_balance_transaction">Link to this property</a>

discount: optional string

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)%20%3E%20(property)%20invoice_lines%20%3E%20(items)%20%3E%20(property)%20pretax_credit_amounts%20%3E%20(items)%20%3E%20(property)%20discount">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)%20%3E%20(property)%20invoice_lines%20%3E%20(items)%20%3E%20(property)%20pretax_credit_amounts">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)%20%3E%20(property)%20invoice_lines">Link to this property</a>

period\_end: number

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)%20%3E%20(property)%20period_end">Link to this property</a>

period\_start: number

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)%20%3E%20(property)%20period_start">Link to this property</a>

<details>

<summary>

status: "draft"or "open"or "paid"or 2 more

</summary>

One of the following:

"draft"

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"open"

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"paid"

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"uncollectible"

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"void"

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_gateway.billing%20%3E%20(model)%20billing_invoice_preview_response%20%3E%20(schema)>)

#### BillingTopup

##### [Create a top-up](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/billing/subresources/topup/methods/create)

POST/accounts/{account\_id}/ai-gateway/billing/topup

##### [Check top-up status](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/billing/subresources/topup/methods/status)

POST/accounts/{account\_id}/ai-gateway/billing/topup/status

##### ModelsExpand Collapse

<details>

<summary>

TopupCreateResponse object {client\_secret, onboarding, payment\_intent\_id, 2 more }

</summary>

client\_secret: string

Stripe PaymentIntent client secret.

<a href="#(resource)%20ai_gateway.billing.topup%20%3E%20(model)%20topup_create_response%20%3E%20(schema)%20%3E%20(property)%20client_secret">Link to this property</a>

onboarding: boolean

Whether the user was already onboarded.

<a href="#(resource)%20ai_gateway.billing.topup%20%3E%20(model)%20topup_create_response%20%3E%20(schema)%20%3E%20(property)%20onboarding">Link to this property</a>

payment\_intent\_id: string

Stripe invoice ID.

<a href="#(resource)%20ai_gateway.billing.topup%20%3E%20(model)%20topup_create_response%20%3E%20(schema)%20%3E%20(property)%20payment_intent_id">Link to this property</a>

brand: optional string

Card brand (visa, mastercard, etc.).

<a href="#(resource)%20ai_gateway.billing.topup%20%3E%20(model)%20topup_create_response%20%3E%20(schema)%20%3E%20(property)%20brand">Link to this property</a>

last4: optional string

Last 4 digits of card.

<a href="#(resource)%20ai_gateway.billing.topup%20%3E%20(model)%20topup_create_response%20%3E%20(schema)%20%3E%20(property)%20last4">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_gateway.billing.topup%20%3E%20(model)%20topup_create_response%20%3E%20(schema)>)

<details>

<summary>

TopupStatusResponse object {payment\_intent\_id, status }

</summary>

payment\_intent\_id: string

<a href="#(resource)%20ai_gateway.billing.topup%20%3E%20(model)%20topup_status_response%20%3E%20(schema)%20%3E%20(property)%20payment_intent_id">Link to this property</a>

<details>

<summary>

status: "completed"or "pending"

</summary>

One of the following:

"completed"

<a href="#(resource)%20ai_gateway.billing.topup%20%3E%20(model)%20topup_status_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"pending"

<a href="#(resource)%20ai_gateway.billing.topup%20%3E%20(model)%20topup_status_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.billing.topup%20%3E%20(model)%20topup_status_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_gateway.billing.topup%20%3E%20(model)%20topup_status_response%20%3E%20(schema)>)

#### BillingTopupConfig

##### [Get auto top-up configuration](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/billing/subresources/topup/subresources/config/methods/get)

GET/accounts/{account\_id}/ai-gateway/billing/topup/config

##### [Set auto top-up configuration](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/billing/subresources/topup/subresources/config/methods/create)

POST/accounts/{account\_id}/ai-gateway/billing/topup/config

##### [Delete auto top-up configuration](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/billing/subresources/topup/subresources/config/methods/delete)

DELETE/accounts/{account\_id}/ai-gateway/billing/topup/config

##### ModelsExpand Collapse

<details>

<summary>

ConfigGetResponse object {amount, threshold, disabledReason, 2 more }

</summary>

amount: number

<a href="#(resource)%20ai_gateway.billing.topup.config%20%3E%20(model)%20config_get_response%20%3E%20(schema)%20%3E%20(property)%20amount">Link to this property</a>

threshold: number

<a href="#(resource)%20ai_gateway.billing.topup.config%20%3E%20(model)%20config_get_response%20%3E%20(schema)%20%3E%20(property)%20threshold">Link to this property</a>

disabledReason: optional string

<a href="#(resource)%20ai_gateway.billing.topup.config%20%3E%20(model)%20config_get_response%20%3E%20(schema)%20%3E%20(property)%20disabledReason">Link to this property</a>

error: optional string

<a href="#(resource)%20ai_gateway.billing.topup.config%20%3E%20(model)%20config_get_response%20%3E%20(schema)%20%3E%20(property)%20error">Link to this property</a>

lastFailedAt: optional number

<a href="#(resource)%20ai_gateway.billing.topup.config%20%3E%20(model)%20config_get_response%20%3E%20(schema)%20%3E%20(property)%20lastFailedAt">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_gateway.billing.topup.config%20%3E%20(model)%20config_get_response%20%3E%20(schema)>)

<details>

<summary>

ConfigCreateResponse object {amount, threshold }

</summary>

amount: number

<a href="#(resource)%20ai_gateway.billing.topup.config%20%3E%20(model)%20config_create_response%20%3E%20(schema)%20%3E%20(property)%20amount">Link to this property</a>

threshold: number

<a href="#(resource)%20ai_gateway.billing.topup.config%20%3E%20(model)%20config_create_response%20%3E%20(schema)%20%3E%20(property)%20threshold">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_gateway.billing.topup.config%20%3E%20(model)%20config_create_response%20%3E%20(schema)>)

ConfigDeleteResponse = unknown

[Link to this property](<#(resource)%20ai_gateway.billing.topup.config%20%3E%20(model)%20config_delete_response%20%3E%20(schema)>)

#### BillingSpending Limit

##### [Get spending limit (deprecated)](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/billing/subresources/spending_limit/methods/get)

GET/accounts/{account\_id}/ai-gateway/billing/spending-limit

##### [Set spending limit (deprecated)](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/billing/subresources/spending_limit/methods/create)

Deprecated

POST/accounts/{account\_id}/ai-gateway/billing/spending-limit

##### [Delete spending limit (deprecated)](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/billing/subresources/spending_limit/methods/delete)

DELETE/accounts/{account\_id}/ai-gateway/billing/spending-limit

##### ModelsExpand Collapse

<details>

<summary>

SpendingLimitGetResponse object {config, enabled }

</summary>

<details>

<summary>

config: object {amount, duration, strategy }

</summary>

amount: number

<a href="#(resource)%20ai_gateway.billing.spending_limit%20%3E%20(model)%20spending_limit_get_response%20%3E%20(schema)%20%3E%20(property)%20config%20%3E%20(property)%20amount">Link to this property</a>

duration: string

<a href="#(resource)%20ai_gateway.billing.spending_limit%20%3E%20(model)%20spending_limit_get_response%20%3E%20(schema)%20%3E%20(property)%20config%20%3E%20(property)%20duration">Link to this property</a>

strategy: string

<a href="#(resource)%20ai_gateway.billing.spending_limit%20%3E%20(model)%20spending_limit_get_response%20%3E%20(schema)%20%3E%20(property)%20config%20%3E%20(property)%20strategy">Link to this property</a>

</details>

<a href="#(resource)%20ai_gateway.billing.spending_limit%20%3E%20(model)%20spending_limit_get_response%20%3E%20(schema)%20%3E%20(property)%20config">Link to this property</a>

enabled: boolean

<a href="#(resource)%20ai_gateway.billing.spending_limit%20%3E%20(model)%20spending_limit_get_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ai_gateway.billing.spending_limit%20%3E%20(model)%20spending_limit_get_response%20%3E%20(schema)>)

SpendingLimitCreateResponse = unknown

[Link to this property](<#(resource)%20ai_gateway.billing.spending_limit%20%3E%20(model)%20spending_limit_create_response%20%3E%20(schema)>)

SpendingLimitDeleteResponse = unknown

[Link to this property](<#(resource)%20ai_gateway.billing.spending_limit%20%3E%20(model)%20spending_limit_delete_response%20%3E%20(schema)>)