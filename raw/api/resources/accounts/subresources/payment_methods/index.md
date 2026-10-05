---
title: Payment Methods
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Accounts](https://developers.cloudflare.com/api/resources/accounts)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Payment Methods

##### [List Payment Methods](https://developers.cloudflare.com/api/resources/accounts/subresources/payment_methods/methods/list)

GET/accounts/{account\_id}/payment-methods

##### [Create Payment Method](https://developers.cloudflare.com/api/resources/accounts/subresources/payment_methods/methods/create)

POST/accounts/{account\_id}/payment-methods

##### [Get Payment Method](https://developers.cloudflare.com/api/resources/accounts/subresources/payment_methods/methods/get)

GET/accounts/{account\_id}/payment-methods/{payment\_method\_id}

##### [Update Payment Method](https://developers.cloudflare.com/api/resources/accounts/subresources/payment_methods/methods/update)

PUT/accounts/{account\_id}/payment-methods/{payment\_method\_id}

##### [Delete Payment Method](https://developers.cloudflare.com/api/resources/accounts/subresources/payment_methods/methods/delete)

DELETE/accounts/{account\_id}/payment-methods/{payment\_method\_id}

##### [Set Default Payment Method](https://developers.cloudflare.com/api/resources/accounts/subresources/payment_methods/methods/set_as_default)

POST/accounts/{account\_id}/payment-methods/{payment\_method\_id}/set-as-default

##### ModelsExpand Collapse

<details>

<summary>

PaymentMethodListResponse object {id, address, address2, 22 more }

</summary>

id: optional string

Payment method identifier.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

address: optional string

Billing address line 1.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20address">Link to this property</a>

address2: optional string

Billing address line 2.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20address2">Link to this property</a>

bank\_account\_type: optional string

Bank account type.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20bank_account_type">Link to this property</a>

bank\_code: optional string

Bank code.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20bank_code">Link to this property</a>

bank\_country: optional string

Bank country.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20bank_country">Link to this property</a>

bank\_name: optional string

Bank name for bank-based payment methods.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20bank_name">Link to this property</a>

bank\_routing\_number: optional string

Bank routing number.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20bank_routing_number">Link to this property</a>

cashapp\_cash\_tag: optional string

Cash App cash tag.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20cashapp_cash_tag">Link to this property</a>

city: optional string

Billing city.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20city">Link to this property</a>

country: optional string

Billing country.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20country">Link to this property</a>

default: optional boolean

Whether this is the default payment method.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20default">Link to this property</a>

device\_data: optional string

Device data for fraud prevention.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20device_data">Link to this property</a>

expiration\_date: optional string

Card expiration date.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20expiration_date">Link to this property</a>

first\_name: optional string

Billing first name.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20first_name">Link to this property</a>

last\_four: optional string

Last four digits of the card number.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20last_four">Link to this property</a>

last\_name: optional string

Billing last name.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20last_name">Link to this property</a>

nick\_name: optional string

A nickname for the payment method.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20nick_name">Link to this property</a>

payment\_account\_email: optional string

Email associated with the payment account.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20payment_account_email">Link to this property</a>

payment\_email: optional string

Payment email address.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20payment_email">Link to this property</a>

payment\_gateway: optional string

The payment gateway used.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20payment_gateway">Link to this property</a>

payment\_nonce: optional string

Payment nonce for tokenized payments.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20payment_nonce">Link to this property</a>

state: optional string

Billing state.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20state">Link to this property</a>

<details>

<summary>

type: optional "CREDIT\_CARD"or "PAYPAL"or "CASHAPP"or 3 more

The payment method type.

</summary>

One of the following:

"CREDIT\_CARD"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"PAYPAL"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"CASHAPP"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"SEPA\_DEBIT"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

"LINK"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%204">Link to this property</a>

"ACH\_DIRECT\_DEBIT"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

zipcode: optional string

Billing zip code.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)%20%3E%20(property)%20zipcode">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_list_response%20%3E%20(schema)>)

<details>

<summary>

PaymentMethodCreateResponse object {id, address, address2, 22 more }

</summary>

id: optional string

Payment method identifier.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

address: optional string

Billing address line 1.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20address">Link to this property</a>

address2: optional string

Billing address line 2.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20address2">Link to this property</a>

bank\_account\_type: optional string

Bank account type.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20bank_account_type">Link to this property</a>

bank\_code: optional string

Bank code.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20bank_code">Link to this property</a>

bank\_country: optional string

Bank country.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20bank_country">Link to this property</a>

bank\_name: optional string

Bank name for bank-based payment methods.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20bank_name">Link to this property</a>

bank\_routing\_number: optional string

Bank routing number.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20bank_routing_number">Link to this property</a>

cashapp\_cash\_tag: optional string

Cash App cash tag.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20cashapp_cash_tag">Link to this property</a>

city: optional string

Billing city.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20city">Link to this property</a>

country: optional string

Billing country.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20country">Link to this property</a>

default: optional boolean

Whether this is the default payment method.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20default">Link to this property</a>

device\_data: optional string

Device data for fraud prevention.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20device_data">Link to this property</a>

expiration\_date: optional string

Card expiration date.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20expiration_date">Link to this property</a>

first\_name: optional string

Billing first name.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20first_name">Link to this property</a>

last\_four: optional string

Last four digits of the card number.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20last_four">Link to this property</a>

last\_name: optional string

Billing last name.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20last_name">Link to this property</a>

nick\_name: optional string

A nickname for the payment method.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20nick_name">Link to this property</a>

payment\_account\_email: optional string

Email associated with the payment account.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20payment_account_email">Link to this property</a>

payment\_email: optional string

Payment email address.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20payment_email">Link to this property</a>

payment\_gateway: optional string

The payment gateway used.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20payment_gateway">Link to this property</a>

payment\_nonce: optional string

Payment nonce for tokenized payments.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20payment_nonce">Link to this property</a>

state: optional string

Billing state.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20state">Link to this property</a>

<details>

<summary>

type: optional "CREDIT\_CARD"or "PAYPAL"or "CASHAPP"or 3 more

The payment method type.

</summary>

One of the following:

"CREDIT\_CARD"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"PAYPAL"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"CASHAPP"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"SEPA\_DEBIT"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

"LINK"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%204">Link to this property</a>

"ACH\_DIRECT\_DEBIT"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

zipcode: optional string

Billing zip code.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)%20%3E%20(property)%20zipcode">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_create_response%20%3E%20(schema)>)

<details>

<summary>

PaymentMethodGetResponse object {id, address, address2, 22 more }

</summary>

id: optional string

Payment method identifier.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

address: optional string

Billing address line 1.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20address">Link to this property</a>

address2: optional string

Billing address line 2.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20address2">Link to this property</a>

bank\_account\_type: optional string

Bank account type.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20bank_account_type">Link to this property</a>

bank\_code: optional string

Bank code.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20bank_code">Link to this property</a>

bank\_country: optional string

Bank country.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20bank_country">Link to this property</a>

bank\_name: optional string

Bank name for bank-based payment methods.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20bank_name">Link to this property</a>

bank\_routing\_number: optional string

Bank routing number.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20bank_routing_number">Link to this property</a>

cashapp\_cash\_tag: optional string

Cash App cash tag.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20cashapp_cash_tag">Link to this property</a>

city: optional string

Billing city.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20city">Link to this property</a>

country: optional string

Billing country.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20country">Link to this property</a>

default: optional boolean

Whether this is the default payment method.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20default">Link to this property</a>

device\_data: optional string

Device data for fraud prevention.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20device_data">Link to this property</a>

expiration\_date: optional string

Card expiration date.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20expiration_date">Link to this property</a>

first\_name: optional string

Billing first name.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20first_name">Link to this property</a>

last\_four: optional string

Last four digits of the card number.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20last_four">Link to this property</a>

last\_name: optional string

Billing last name.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20last_name">Link to this property</a>

nick\_name: optional string

A nickname for the payment method.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20nick_name">Link to this property</a>

payment\_account\_email: optional string

Email associated with the payment account.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20payment_account_email">Link to this property</a>

payment\_email: optional string

Payment email address.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20payment_email">Link to this property</a>

payment\_gateway: optional string

The payment gateway used.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20payment_gateway">Link to this property</a>

payment\_nonce: optional string

Payment nonce for tokenized payments.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20payment_nonce">Link to this property</a>

state: optional string

Billing state.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20state">Link to this property</a>

<details>

<summary>

type: optional "CREDIT\_CARD"or "PAYPAL"or "CASHAPP"or 3 more

The payment method type.

</summary>

One of the following:

"CREDIT\_CARD"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"PAYPAL"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"CASHAPP"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"SEPA\_DEBIT"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

"LINK"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%204">Link to this property</a>

"ACH\_DIRECT\_DEBIT"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

zipcode: optional string

Billing zip code.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)%20%3E%20(property)%20zipcode">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_get_response%20%3E%20(schema)>)

<details>

<summary>

PaymentMethodUpdateResponse object {id, address, address2, 22 more }

</summary>

id: optional string

Payment method identifier.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

address: optional string

Billing address line 1.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20address">Link to this property</a>

address2: optional string

Billing address line 2.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20address2">Link to this property</a>

bank\_account\_type: optional string

Bank account type.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20bank_account_type">Link to this property</a>

bank\_code: optional string

Bank code.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20bank_code">Link to this property</a>

bank\_country: optional string

Bank country.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20bank_country">Link to this property</a>

bank\_name: optional string

Bank name for bank-based payment methods.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20bank_name">Link to this property</a>

bank\_routing\_number: optional string

Bank routing number.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20bank_routing_number">Link to this property</a>

cashapp\_cash\_tag: optional string

Cash App cash tag.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20cashapp_cash_tag">Link to this property</a>

city: optional string

Billing city.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20city">Link to this property</a>

country: optional string

Billing country.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20country">Link to this property</a>

default: optional boolean

Whether this is the default payment method.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20default">Link to this property</a>

device\_data: optional string

Device data for fraud prevention.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20device_data">Link to this property</a>

expiration\_date: optional string

Card expiration date.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20expiration_date">Link to this property</a>

first\_name: optional string

Billing first name.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20first_name">Link to this property</a>

last\_four: optional string

Last four digits of the card number.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20last_four">Link to this property</a>

last\_name: optional string

Billing last name.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20last_name">Link to this property</a>

nick\_name: optional string

A nickname for the payment method.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20nick_name">Link to this property</a>

payment\_account\_email: optional string

Email associated with the payment account.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20payment_account_email">Link to this property</a>

payment\_email: optional string

Payment email address.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20payment_email">Link to this property</a>

payment\_gateway: optional string

The payment gateway used.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20payment_gateway">Link to this property</a>

payment\_nonce: optional string

Payment nonce for tokenized payments.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20payment_nonce">Link to this property</a>

state: optional string

Billing state.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20state">Link to this property</a>

<details>

<summary>

type: optional "CREDIT\_CARD"or "PAYPAL"or "CASHAPP"or 3 more

The payment method type.

</summary>

One of the following:

"CREDIT\_CARD"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"PAYPAL"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"CASHAPP"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"SEPA\_DEBIT"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

"LINK"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%204">Link to this property</a>

"ACH\_DIRECT\_DEBIT"

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

zipcode: optional string

Billing zip code.

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)%20%3E%20(property)%20zipcode">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_update_response%20%3E%20(schema)>)

<details>

<summary>

PaymentMethodDeleteResponse = unknownor string

</summary>

One of the following:

unknown

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_delete_response%20%3E%20(schema)%20%3E%20(variant)%200">Link to this property</a>

string

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_delete_response%20%3E%20(schema)%20%3E%20(variant)%201">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_delete_response%20%3E%20(schema)>)

<details>

<summary>

PaymentMethodSetAsDefaultResponse = unknownor string

</summary>

One of the following:

unknown

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_set_as_default_response%20%3E%20(schema)%20%3E%20(variant)%200">Link to this property</a>

string

<a href="#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_set_as_default_response%20%3E%20(schema)%20%3E%20(variant)%201">Link to this property</a>

</details>

[Link to this property](<#(resource)%20accounts.payment_methods%20%3E%20(model)%20payment_method_set_as_default_response%20%3E%20(schema)>)