---
title: Payment Method
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Billing](https://developers.cloudflare.com/api/resources/billing)

[Profiles](https://developers.cloudflare.com/api/resources/billing/subresources/profiles)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Payment Method

##### [Create Payment Intent for Billing Profile](https://developers.cloudflare.com/api/resources/billing/subresources/profiles/subresources/payment_method/methods/create)

POST/accounts/{account\_id}/billing/profile/payment-method

##### ModelsExpand Collapse

<details>

<summary>

PaymentMethodCreateResponse object {client\_secret, intent\_type }

</summary>

client\_secret: optional string

The Stripe client secret for frontend payment method collection.

<a href="#(resource)%20billing.profiles.payment_method%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20client_secret">Link to this property</a>

intent\_type: optional string

The type of Stripe intent created.

<a href="#(resource)%20billing.profiles.payment_method%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20intent_type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20billing.profiles.payment_method%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)>)