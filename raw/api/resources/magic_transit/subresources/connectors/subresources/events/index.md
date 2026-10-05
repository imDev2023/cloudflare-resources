---
title: Events
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Magic Transit](https://developers.cloudflare.com/api/resources/magic_transit)

[Connectors](https://developers.cloudflare.com/api/resources/magic_transit/subresources/connectors)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Events

##### [List Events](https://developers.cloudflare.com/api/resources/magic_transit/subresources/connectors/subresources/events/methods/list)

GET/accounts/{account\_id}/magic/connectors/{connector\_id}/telemetry/events

##### [Get Event](https://developers.cloudflare.com/api/resources/magic_transit/subresources/connectors/subresources/events/methods/get)

GET/accounts/{account\_id}/magic/connectors/{connector\_id}/telemetry/events/{event\_t}.{event\_n}

##### ModelsExpand Collapse

<details>

<summary>

EventListResponse object {count, items, cursor }

</summary>

count: number

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20count">Link to this property</a>

<details>

<summary>

items: array of object {a, k, n, t }

</summary>

a: number

Time the Event was collected (seconds since the Unix epoch)

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20a">Link to this property</a>

k: string

Kind

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20k">Link to this property</a>

n: number

Sequence number, used to order events with the same timestamp

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20n">Link to this property</a>

t: number

Time the Event was recorded (seconds since the Unix epoch)

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20t">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20items">Link to this property</a>

cursor: optional string

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)%20%3E%20(property)%20cursor">Link to this property</a>

</details>

[Link to this property](<#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_list_response%20%3E%20(schema)>)

<details>

<summary>

EventGetResponse object {e, n, t, v }

Recorded Event

</summary>

<details>

<summary>

e: object {k }

Event kind plus event-specific payload fields.

Event kinds:

- <code>Init</code>: Initialized process
- <code>Leave</code>: Stopped process
- <code>StartAttestation</code>: Started attestation
- <code>FinishAttestationSuccess</code>: Finished attestation
- <code>FinishAttestationFailure</code>: Failed attestation
- <code>StartRotateCryptKey</code>: Started crypt key rotation
- <code>FinishRotateCryptKeySuccess</code>: Finished crypt key rotation
- <code>FinishRotateCryptKeyFailure</code>: Failed crypt key rotation
- <code>StartRotatePki</code>: Started PKI rotation
- <code>FinishRotatePkiSuccess</code>: Finished PKI rotation
- <code>FinishRotatePkiFailure</code>: Failed PKI rotation
- <code>StartUpgrade</code>: Started upgrade
- <code>FinishUpgradeSuccess</code>: Finished upgrade
- <code>FinishUpgradeFailure</code>: Failed upgrade
- <code>BlessSlotSuccess</code>: Blessed boot entry slot
- <code>BlessSlotPending</code>: Boot entry slot is not yet blessed
- <code>BlessSlotFailure</code>: Failed to bless boot entry slot
- <code>Reconcile</code>: Reconciled
- <code>ConfigureCloudflaredTunnel</code>: Configured Cloudflared tunnel
- <code>RekeyInstallBoth</code>: Installed initial inbound and outbound keys
- <code>RekeyStart</code>: Installed new inbound key, kept old outbound
- <code>RekeyRestart</code>: Restarted in-progress rekey with newer key material
- <code>RekeyAdvance</code>: Confirmed traffic on new inbound key, swapped outbound to new
- <code>RekeyComplete</code>: Deleted old keys
- <code>RekeyReset</code>: Deleted all keys after receiving an unexpected key
- <code>HaTransition</code>: Completed HA state transition
- <code>HaError</code>: Received unexpected HA error
- <code>HaInit</code>: Initialized HA subsystem
- <code>HaLeave</code>: Stopped HA subsystem

</summary>

<details>

<summary>

k: "Init"or "Leave"or "StartAttestation"or 26 more

Event kind

</summary>

One of the following:

"Init"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%200">Link to this property</a>

"Leave"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%201">Link to this property</a>

"StartAttestation"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%202">Link to this property</a>

"FinishAttestationSuccess"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%203">Link to this property</a>

"FinishAttestationFailure"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%204">Link to this property</a>

"StartRotateCryptKey"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%205">Link to this property</a>

"FinishRotateCryptKeySuccess"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%206">Link to this property</a>

"FinishRotateCryptKeyFailure"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%207">Link to this property</a>

"StartRotatePki"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%208">Link to this property</a>

"FinishRotatePkiSuccess"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%209">Link to this property</a>

"FinishRotatePkiFailure"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2010">Link to this property</a>

"StartUpgrade"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2011">Link to this property</a>

"FinishUpgradeSuccess"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2012">Link to this property</a>

"FinishUpgradeFailure"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2013">Link to this property</a>

"BlessSlotSuccess"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2014">Link to this property</a>

"BlessSlotPending"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2015">Link to this property</a>

"BlessSlotFailure"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2016">Link to this property</a>

"Reconcile"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2017">Link to this property</a>

"ConfigureCloudflaredTunnel"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2018">Link to this property</a>

"RekeyInstallBoth"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2019">Link to this property</a>

"RekeyStart"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2020">Link to this property</a>

"RekeyRestart"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2021">Link to this property</a>

"RekeyAdvance"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2022">Link to this property</a>

"RekeyComplete"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2023">Link to this property</a>

"RekeyReset"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2024">Link to this property</a>

"HaTransition"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2025">Link to this property</a>

"HaError"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2026">Link to this property</a>

"HaInit"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2027">Link to this property</a>

"HaLeave"

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2028">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e%20%3E%20(property)%20k">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20e">Link to this property</a>

n: number

Sequence number, used to order events with the same timestamp

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20n">Link to this property</a>

t: number

Time the Event was recorded (seconds since the Unix epoch)

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20t">Link to this property</a>

v: optional string

Version

<a href="#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)%20%3E%20(property)%20v">Link to this property</a>

</details>

[Link to this property](<#(resource)%20magic_transit.connectors.events%20%3E%20(model)%20event_get_response%20%3E%20(schema)>)

#### EventsLatest

##### [Get latest Events](https://developers.cloudflare.com/api/resources/magic_transit/subresources/connectors/subresources/events/subresources/latest/methods/list)

GET/accounts/{account\_id}/magic/connectors/{connector\_id}/telemetry/events/latest

##### ModelsExpand Collapse

<details>

<summary>

LatestListResponse object {count, items }

</summary>

count: number

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20count">Link to this property</a>

<details>

<summary>

items: array of object {e, n, t, v }

</summary>

<details>

<summary>

e: object {k }

Event kind plus event-specific payload fields.

Event kinds:

- <code>Init</code>: Initialized process
- <code>Leave</code>: Stopped process
- <code>StartAttestation</code>: Started attestation
- <code>FinishAttestationSuccess</code>: Finished attestation
- <code>FinishAttestationFailure</code>: Failed attestation
- <code>StartRotateCryptKey</code>: Started crypt key rotation
- <code>FinishRotateCryptKeySuccess</code>: Finished crypt key rotation
- <code>FinishRotateCryptKeyFailure</code>: Failed crypt key rotation
- <code>StartRotatePki</code>: Started PKI rotation
- <code>FinishRotatePkiSuccess</code>: Finished PKI rotation
- <code>FinishRotatePkiFailure</code>: Failed PKI rotation
- <code>StartUpgrade</code>: Started upgrade
- <code>FinishUpgradeSuccess</code>: Finished upgrade
- <code>FinishUpgradeFailure</code>: Failed upgrade
- <code>BlessSlotSuccess</code>: Blessed boot entry slot
- <code>BlessSlotPending</code>: Boot entry slot is not yet blessed
- <code>BlessSlotFailure</code>: Failed to bless boot entry slot
- <code>Reconcile</code>: Reconciled
- <code>ConfigureCloudflaredTunnel</code>: Configured Cloudflared tunnel
- <code>RekeyInstallBoth</code>: Installed initial inbound and outbound keys
- <code>RekeyStart</code>: Installed new inbound key, kept old outbound
- <code>RekeyRestart</code>: Restarted in-progress rekey with newer key material
- <code>RekeyAdvance</code>: Confirmed traffic on new inbound key, swapped outbound to new
- <code>RekeyComplete</code>: Deleted old keys
- <code>RekeyReset</code>: Deleted all keys after receiving an unexpected key
- <code>HaTransition</code>: Completed HA state transition
- <code>HaError</code>: Received unexpected HA error
- <code>HaInit</code>: Initialized HA subsystem
- <code>HaLeave</code>: Stopped HA subsystem

</summary>

<details>

<summary>

k: "Init"or "Leave"or "StartAttestation"or 26 more

Event kind

</summary>

One of the following:

"Init"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%200">Link to this property</a>

"Leave"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%201">Link to this property</a>

"StartAttestation"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%202">Link to this property</a>

"FinishAttestationSuccess"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%203">Link to this property</a>

"FinishAttestationFailure"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%204">Link to this property</a>

"StartRotateCryptKey"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%205">Link to this property</a>

"FinishRotateCryptKeySuccess"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%206">Link to this property</a>

"FinishRotateCryptKeyFailure"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%207">Link to this property</a>

"StartRotatePki"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%208">Link to this property</a>

"FinishRotatePkiSuccess"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%209">Link to this property</a>

"FinishRotatePkiFailure"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2010">Link to this property</a>

"StartUpgrade"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2011">Link to this property</a>

"FinishUpgradeSuccess"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2012">Link to this property</a>

"FinishUpgradeFailure"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2013">Link to this property</a>

"BlessSlotSuccess"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2014">Link to this property</a>

"BlessSlotPending"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2015">Link to this property</a>

"BlessSlotFailure"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2016">Link to this property</a>

"Reconcile"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2017">Link to this property</a>

"ConfigureCloudflaredTunnel"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2018">Link to this property</a>

"RekeyInstallBoth"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2019">Link to this property</a>

"RekeyStart"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2020">Link to this property</a>

"RekeyRestart"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2021">Link to this property</a>

"RekeyAdvance"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2022">Link to this property</a>

"RekeyComplete"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2023">Link to this property</a>

"RekeyReset"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2024">Link to this property</a>

"HaTransition"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2025">Link to this property</a>

"HaError"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2026">Link to this property</a>

"HaInit"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2027">Link to this property</a>

"HaLeave"

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k%20%3E%20(member)%2028">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e%20%3E%20(property)%20k">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20e">Link to this property</a>

n: number

Sequence number, used to order events with the same timestamp

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20n">Link to this property</a>

t: number

Time the Event was recorded (seconds since the Unix epoch)

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20t">Link to this property</a>

v: optional string

Version

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items%20%3E%20(items)%20%3E%20(property)%20v">Link to this property</a>

</details>

<a href="#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)%20%3E%20(property)%20items">Link to this property</a>

</details>

[Link to this property](<#(resource)%20magic_transit.connectors.events.latest%20%3E%20(model)%20latest_list_response%20%3E%20(schema)>)