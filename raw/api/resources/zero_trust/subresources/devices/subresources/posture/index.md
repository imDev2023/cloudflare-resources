---
title: Posture
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

[Devices](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Posture

##### [List posture rules](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/posture/methods/list)

GET/accounts/{account\_id}/devices/posture

##### [Get posture rule](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/posture/methods/get)

GET/accounts/{account\_id}/devices/posture/{rule\_id}

##### [Create posture rule](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/posture/methods/create)

POST/accounts/{account\_id}/devices/posture

##### [Update posture rule](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/posture/methods/update)

PUT/accounts/{account\_id}/devices/posture/{rule\_id}

##### [Delete posture rule](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/posture/methods/delete)

DELETE/accounts/{account\_id}/devices/posture/{rule\_id}

##### ModelsExpand Collapse

CarbonblackInput = string

[Link to this property](<#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20carbonblack_input%20%3E%20(schema)>)

<details>

<summary>

ClientCertificateInput object {certificate\_id, cn }

</summary>

certificate\_id: string

UUID of Cloudflare managed certificate.

maxLength36

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20client_certificate_input%20%3E%20(schema)%20%3E%20(property)%20certificate_id">Link to this property</a>

cn: string

Common Name that is protected by the certificate.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20client_certificate_input%20%3E%20(schema)%20%3E%20(property)%20cn">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20client_certificate_input%20%3E%20(schema)>)

<details>

<summary>

CrowdstrikeInput object {connection\_id, last\_seen, operator, 6 more }

</summary>

connection\_id: string

Posture Integration ID.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20connection_id">Link to this property</a>

last\_seen: optional string

For more details on last seen, please refer to the Crowdstrike documentation.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20last_seen">Link to this property</a>

<details>

<summary>

operator: optional "&lt;"or "&lt;="or "&gt;"or 2 more

Operator.

</summary>

One of the following:

"&lt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%200">Link to this property</a>

"&lt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%201">Link to this property</a>

"&gt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%202">Link to this property</a>

"&gt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%203">Link to this property</a>

"=="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20operator">Link to this property</a>

os: optional string

Os Version.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20os">Link to this property</a>

overall: optional string

Overall.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20overall">Link to this property</a>

sensor\_config: optional string

SensorConfig.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20sensor_config">Link to this property</a>

<details>

<summary>

state: optional "online"or "offline"or "unknown"

For more details on state, please refer to the Crowdstrike documentation.

</summary>

One of the following:

"online"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20state%20%3E%20(member)%200">Link to this property</a>

"offline"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20state%20%3E%20(member)%201">Link to this property</a>

"unknown"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20state%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20state">Link to this property</a>

version: optional string

Version.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

<details>

<summary>

versionOperator: optional "&lt;"or "&lt;="or "&gt;"or 2 more

Version Operator.

</summary>

One of the following:

"&lt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20versionOperator%20%3E%20(member)%200">Link to this property</a>

"&lt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20versionOperator%20%3E%20(member)%201">Link to this property</a>

"&gt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20versionOperator%20%3E%20(member)%202">Link to this property</a>

"&gt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20versionOperator%20%3E%20(member)%203">Link to this property</a>

"=="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20versionOperator%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20versionOperator">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)>)

<details>

<summary>

DeviceInput = <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20file_input%20%3E%20(schema)">FileInput</a> { operating\_system, path, exists, 2 more } or <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20unique_client_id_input%20%3E%20(schema)">UniqueClientIDInput</a> { id, operating\_system } or <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20domain_joined_input%20%3E%20(schema)">DomainJoinedInput</a> { operating\_system, domain } or 17 more

The value to be checked against.

</summary>

One of the following:

<details>

<summary>

FileInput object {operating\_system, path, exists, 2 more }

</summary>

<details>

<summary>

operating\_system: "windows"or "linux"or "mac"

Operating system.

</summary>

One of the following:

"windows"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20file_input%20%3E%20(schema)%20%3E%20(property)%20operating_system%20%3E%20(member)%200">Link to this property</a>

"linux"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20file_input%20%3E%20(schema)%20%3E%20(property)%20operating_system%20%3E%20(member)%201">Link to this property</a>

"mac"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20file_input%20%3E%20(schema)%20%3E%20(property)%20operating_system%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20file_input%20%3E%20(schema)%20%3E%20(property)%20operating_system">Link to this property</a>

path: string

File path.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20file_input%20%3E%20(schema)%20%3E%20(property)%20path">Link to this property</a>

exists: optional boolean

Whether or not file exists.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20file_input%20%3E%20(schema)%20%3E%20(property)%20exists">Link to this property</a>

sha256: optional string

SHA-256.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20file_input%20%3E%20(schema)%20%3E%20(property)%20sha256">Link to this property</a>

thumbprint: optional string

Signing certificate thumbprint.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20file_input%20%3E%20(schema)%20%3E%20(property)%20thumbprint">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20file_input%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

UniqueClientIDInput object {id, operating\_system }

</summary>

id: string

List ID.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20unique_client_id_input%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

operating\_system: "android"or "ios"or "chromeos"

Operating System.

</summary>

One of the following:

"android"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20unique_client_id_input%20%3E%20(schema)%20%3E%20(property)%20operating_system%20%3E%20(member)%200">Link to this property</a>

"ios"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20unique_client_id_input%20%3E%20(schema)%20%3E%20(property)%20operating_system%20%3E%20(member)%201">Link to this property</a>

"chromeos"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20unique_client_id_input%20%3E%20(schema)%20%3E%20(property)%20operating_system%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20unique_client_id_input%20%3E%20(schema)%20%3E%20(property)%20operating_system">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20unique_client_id_input%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

DomainJoinedInput object {operating\_system, domain }

</summary>

operating\_system: "windows"

Operating System.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20domain_joined_input%20%3E%20(schema)%20%3E%20(property)%20operating_system">Link to this property</a>

domain: optional string

Domain.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20domain_joined_input%20%3E%20(schema)%20%3E%20(property)%20domain">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20domain_joined_input%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

OSVersionInput object {operating\_system, operator, version, 3 more }

</summary>

operating\_system: "windows"

Operating System.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20os_version_input%20%3E%20(schema)%20%3E%20(property)%20operating_system">Link to this property</a>

<details>

<summary>

operator: "&lt;"or "&lt;="or "&gt;"or 2 more

Operator.

</summary>

One of the following:

"&lt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20os_version_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%200">Link to this property</a>

"&lt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20os_version_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%201">Link to this property</a>

"&gt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20os_version_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%202">Link to this property</a>

"&gt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20os_version_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%203">Link to this property</a>

"=="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20os_version_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20os_version_input%20%3E%20(schema)%20%3E%20(property)%20operator">Link to this property</a>

version: string

Version of OS.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20os_version_input%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

os\_distro\_name: optional string

Operating System Distribution Name (linux only).

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20os_version_input%20%3E%20(schema)%20%3E%20(property)%20os_distro_name">Link to this property</a>

os\_distro\_revision: optional string

Version of OS Distribution (linux only).

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20os_version_input%20%3E%20(schema)%20%3E%20(property)%20os_distro_revision">Link to this property</a>

os\_version\_extra: optional string

Additional operating system version details. For Windows, the UBR (Update Build Revision). For Mac or iOS, the Product Version Extra. For Linux, the distribution name and version.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20os_version_input%20%3E%20(schema)%20%3E%20(property)%20os_version_extra">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20os_version_input%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

FirewallInput object {enabled, operating\_system }

</summary>

enabled: boolean

Enabled.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20firewall_input%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

<details>

<summary>

operating\_system: "windows"or "mac"

Operating System.

</summary>

One of the following:

"windows"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20firewall_input%20%3E%20(schema)%20%3E%20(property)%20operating_system%20%3E%20(member)%200">Link to this property</a>

"mac"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20firewall_input%20%3E%20(schema)%20%3E%20(property)%20operating_system%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20firewall_input%20%3E%20(schema)%20%3E%20(property)%20operating_system">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20firewall_input%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

SentineloneInput object {operating\_system, path, sha256, thumbprint }

</summary>

<details>

<summary>

operating\_system: "windows"or "linux"or "mac"

Operating system.

</summary>

One of the following:

"windows"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_input%20%3E%20(schema)%20%3E%20(property)%20operating_system%20%3E%20(member)%200">Link to this property</a>

"linux"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_input%20%3E%20(schema)%20%3E%20(property)%20operating_system%20%3E%20(member)%201">Link to this property</a>

"mac"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_input%20%3E%20(schema)%20%3E%20(property)%20operating_system%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_input%20%3E%20(schema)%20%3E%20(property)%20operating_system">Link to this property</a>

path: string

File path.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_input%20%3E%20(schema)%20%3E%20(property)%20path">Link to this property</a>

sha256: optional string

SHA-256.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_input%20%3E%20(schema)%20%3E%20(property)%20sha256">Link to this property</a>

thumbprint: optional string

Signing certificate thumbprint.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_input%20%3E%20(schema)%20%3E%20(property)%20thumbprint">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_input%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

TeamsDevicesCarbonblackInputRequest object {operating\_system, path, sha256, thumbprint }

</summary>

<details>

<summary>

operating\_system: "windows"or "linux"or "mac"

Operating system.

</summary>

One of the following:

"windows"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%206%20%3E%20(property)%20operating_system%20%3E%20(member)%200">Link to this property</a>

"linux"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%206%20%3E%20(property)%20operating_system%20%3E%20(member)%201">Link to this property</a>

"mac"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%206%20%3E%20(property)%20operating_system%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%206%20%3E%20(property)%20operating_system">Link to this property</a>

path: string

File path.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%206%20%3E%20(property)%20path">Link to this property</a>

sha256: optional string

SHA-256.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%206%20%3E%20(property)%20sha256">Link to this property</a>

thumbprint: optional string

Signing certificate thumbprint.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%206%20%3E%20(property)%20thumbprint">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%206">Link to this property</a>

<details>

<summary>

TeamsDevicesAccessSerialNumberListInputRequest object {id }

</summary>

id: string

UUID of Access List.

maxLength36

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%207%20%3E%20(property)%20id">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%207">Link to this property</a>

<details>

<summary>

DiskEncryptionInput object {checkDisks, requireAll }

</summary>

checkDisks: optional array of <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20carbonblack_input%20%3E%20(schema)">CarbonblackInput</a>

List of volume names to be checked for encryption.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20disk_encryption_input%20%3E%20(schema)%20%3E%20(property)%20checkDisks">Link to this property</a>

requireAll: optional boolean

Whether to check all disks for encryption.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20disk_encryption_input%20%3E%20(schema)%20%3E%20(property)%20requireAll">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20disk_encryption_input%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

TeamsDevicesApplicationInputRequest object {operating\_system, path, sha256, thumbprint }

</summary>

<details>

<summary>

operating\_system: "windows"or "linux"or "mac"

Operating system.

</summary>

One of the following:

"windows"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%209%20%3E%20(property)%20operating_system%20%3E%20(member)%200">Link to this property</a>

"linux"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%209%20%3E%20(property)%20operating_system%20%3E%20(member)%201">Link to this property</a>

"mac"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%209%20%3E%20(property)%20operating_system%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%209%20%3E%20(property)%20operating_system">Link to this property</a>

path: string

Path for the application.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%209%20%3E%20(property)%20path">Link to this property</a>

sha256: optional string

SHA-256.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%209%20%3E%20(property)%20sha256">Link to this property</a>

thumbprint: optional string

Signing certificate thumbprint.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%209%20%3E%20(property)%20thumbprint">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%209">Link to this property</a>

<details>

<summary>

ClientCertificateInput object {certificate\_id, cn }

</summary>

certificate\_id: string

UUID of Cloudflare managed certificate.

maxLength36

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20client_certificate_input%20%3E%20(schema)%20%3E%20(property)%20certificate_id">Link to this property</a>

cn: string

Common Name that is protected by the certificate.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20client_certificate_input%20%3E%20(schema)%20%3E%20(property)%20cn">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20client_certificate_input%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

TeamsDevicesClientCertificateV2InputRequest object {certificate\_id, check\_private\_key, operating\_system, 4 more }

</summary>

certificate\_id: string

UUID of Cloudflare managed certificate.

maxLength36

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%2011%20%3E%20(property)%20certificate_id">Link to this property</a>

check\_private\_key: boolean

Confirm the certificate was not imported from another device. We recommend keeping this enabled unless the certificate was deployed without a private key.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%2011%20%3E%20(property)%20check_private_key">Link to this property</a>

<details>

<summary>

operating\_system: "windows"or "linux"or "mac"

Operating system.

</summary>

One of the following:

"windows"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%2011%20%3E%20(property)%20operating_system%20%3E%20(member)%200">Link to this property</a>

"linux"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%2011%20%3E%20(property)%20operating_system%20%3E%20(member)%201">Link to this property</a>

"mac"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%2011%20%3E%20(property)%20operating_system%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%2011%20%3E%20(property)%20operating_system">Link to this property</a>

cn: optional string

Certificate Common Name. This may include one or more variables in the ${ } notation. Only ${serial\_number} and ${hostname} are valid variables.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%2011%20%3E%20(property)%20cn">Link to this property</a>

<details>

<summary>

extended\_key\_usage: optional array of "clientAuth"or "emailProtection"

List of values indicating purposes for which the certificate public key can be used.

</summary>

One of the following:

"clientAuth"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%2011%20%3E%20(property)%20extended_key_usage%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"emailProtection"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%2011%20%3E%20(property)%20extended_key_usage%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%2011%20%3E%20(property)%20extended_key_usage">Link to this property</a>

<details>

<summary>

locations: optional object {paths, trust\_stores }

</summary>

paths: optional array of string

List of paths to check for client certificate on linux.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%2011%20%3E%20(property)%20locations%20%3E%20(property)%20paths">Link to this property</a>

<details>

<summary>

trust\_stores: optional array of "system"or "user"

List of trust stores to check for client certificate.

</summary>

One of the following:

"system"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%2011%20%3E%20(property)%20locations%20%3E%20(property)%20trust_stores%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"user"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%2011%20%3E%20(property)%20locations%20%3E%20(property)%20trust_stores%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%2011%20%3E%20(property)%20locations%20%3E%20(property)%20trust_stores">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%2011%20%3E%20(property)%20locations">Link to this property</a>

subject\_alternative\_names: optional array of string

List of certificate Subject Alternative Names.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%2011%20%3E%20(property)%20subject_alternative_names">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%2011">Link to this property</a>

<details>

<summary>

TeamsDevicesAntivirusInputRequest object {update\_window\_days }

</summary>

update\_window\_days: optional number

Number of days that the antivirus should be updated within.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%2012%20%3E%20(property)%20update_window_days">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%2012">Link to this property</a>

<details>

<summary>

WorkspaceOneInput object {compliance\_status, connection\_id }

</summary>

<details>

<summary>

compliance\_status: "compliant"or "noncompliant"or "unknown"

Compliance Status.

</summary>

One of the following:

"compliant"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20workspace_one_input%20%3E%20(schema)%20%3E%20(property)%20compliance_status%20%3E%20(member)%200">Link to this property</a>

"noncompliant"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20workspace_one_input%20%3E%20(schema)%20%3E%20(property)%20compliance_status%20%3E%20(member)%201">Link to this property</a>

"unknown"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20workspace_one_input%20%3E%20(schema)%20%3E%20(property)%20compliance_status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20workspace_one_input%20%3E%20(schema)%20%3E%20(property)%20compliance_status">Link to this property</a>

connection\_id: string

Posture Integration ID.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20workspace_one_input%20%3E%20(schema)%20%3E%20(property)%20connection_id">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20workspace_one_input%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

CrowdstrikeInput object {connection\_id, last\_seen, operator, 6 more }

</summary>

connection\_id: string

Posture Integration ID.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20connection_id">Link to this property</a>

last\_seen: optional string

For more details on last seen, please refer to the Crowdstrike documentation.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20last_seen">Link to this property</a>

<details>

<summary>

operator: optional "&lt;"or "&lt;="or "&gt;"or 2 more

Operator.

</summary>

One of the following:

"&lt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%200">Link to this property</a>

"&lt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%201">Link to this property</a>

"&gt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%202">Link to this property</a>

"&gt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%203">Link to this property</a>

"=="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20operator">Link to this property</a>

os: optional string

Os Version.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20os">Link to this property</a>

overall: optional string

Overall.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20overall">Link to this property</a>

sensor\_config: optional string

SensorConfig.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20sensor_config">Link to this property</a>

<details>

<summary>

state: optional "online"or "offline"or "unknown"

For more details on state, please refer to the Crowdstrike documentation.

</summary>

One of the following:

"online"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20state%20%3E%20(member)%200">Link to this property</a>

"offline"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20state%20%3E%20(member)%201">Link to this property</a>

"unknown"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20state%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20state">Link to this property</a>

version: optional string

Version.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

<details>

<summary>

versionOperator: optional "&lt;"or "&lt;="or "&gt;"or 2 more

Version Operator.

</summary>

One of the following:

"&lt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20versionOperator%20%3E%20(member)%200">Link to this property</a>

"&lt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20versionOperator%20%3E%20(member)%201">Link to this property</a>

"&gt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20versionOperator%20%3E%20(member)%202">Link to this property</a>

"&gt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20versionOperator%20%3E%20(member)%203">Link to this property</a>

"=="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20versionOperator%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)%20%3E%20(property)%20versionOperator">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20crowdstrike_input%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

IntuneInput object {compliance\_status, connection\_id }

</summary>

<details>

<summary>

compliance\_status: "compliant"or "noncompliant"or "unknown"or 3 more

Compliance Status.

</summary>

One of the following:

"compliant"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20intune_input%20%3E%20(schema)%20%3E%20(property)%20compliance_status%20%3E%20(member)%200">Link to this property</a>

"noncompliant"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20intune_input%20%3E%20(schema)%20%3E%20(property)%20compliance_status%20%3E%20(member)%201">Link to this property</a>

"unknown"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20intune_input%20%3E%20(schema)%20%3E%20(property)%20compliance_status%20%3E%20(member)%202">Link to this property</a>

"notapplicable"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20intune_input%20%3E%20(schema)%20%3E%20(property)%20compliance_status%20%3E%20(member)%203">Link to this property</a>

"ingraceperiod"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20intune_input%20%3E%20(schema)%20%3E%20(property)%20compliance_status%20%3E%20(member)%204">Link to this property</a>

"error"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20intune_input%20%3E%20(schema)%20%3E%20(property)%20compliance_status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20intune_input%20%3E%20(schema)%20%3E%20(property)%20compliance_status">Link to this property</a>

connection\_id: string

Posture Integration ID.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20intune_input%20%3E%20(schema)%20%3E%20(property)%20connection_id">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20intune_input%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

KolideInput object {connection\_id, auth\_state, countOperator, issue\_count }

</summary>

connection\_id: string

Posture Integration ID.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20kolide_input%20%3E%20(schema)%20%3E%20(property)%20connection_id">Link to this property</a>

<details>

<summary>

auth\_state: optional array of "Good"or "Notified"or "Will Block"or "Blocked"

The set of Kolide device authentication states that pass the posture check. Device must match one of the specified states.

</summary>

One of the following:

"Good"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20kolide_input%20%3E%20(schema)%20%3E%20(property)%20auth_state%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"Notified"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20kolide_input%20%3E%20(schema)%20%3E%20(property)%20auth_state%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"Will Block"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20kolide_input%20%3E%20(schema)%20%3E%20(property)%20auth_state%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"Blocked"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20kolide_input%20%3E%20(schema)%20%3E%20(property)%20auth_state%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20kolide_input%20%3E%20(schema)%20%3E%20(property)%20auth_state">Link to this property</a>

<details>

<summary>

countOperator: optional "&lt;"or "&lt;="or "&gt;"or 2 more

Count Operator.

</summary>

One of the following:

"&lt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20kolide_input%20%3E%20(schema)%20%3E%20(property)%20countOperator%20%3E%20(member)%200">Link to this property</a>

"&lt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20kolide_input%20%3E%20(schema)%20%3E%20(property)%20countOperator%20%3E%20(member)%201">Link to this property</a>

"&gt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20kolide_input%20%3E%20(schema)%20%3E%20(property)%20countOperator%20%3E%20(member)%202">Link to this property</a>

"&gt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20kolide_input%20%3E%20(schema)%20%3E%20(property)%20countOperator%20%3E%20(member)%203">Link to this property</a>

"=="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20kolide_input%20%3E%20(schema)%20%3E%20(property)%20countOperator%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20kolide_input%20%3E%20(schema)%20%3E%20(property)%20countOperator">Link to this property</a>

issue\_count: optional string

The Number of Issues.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20kolide_input%20%3E%20(schema)%20%3E%20(property)%20issue_count">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20kolide_input%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

TaniumInput object {connection\_id, eid\_last\_seen, operator, 3 more }

</summary>

connection\_id: string

Posture Integration ID.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20connection_id">Link to this property</a>

eid\_last\_seen: optional string

For more details on eid last seen, refer to the Tanium documentation.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20eid_last_seen">Link to this property</a>

<details>

<summary>

operator: optional "&lt;"or "&lt;="or "&gt;"or 2 more

Operator to evaluate risk\_level or eid\_last\_seen.

</summary>

One of the following:

"&lt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%200">Link to this property</a>

"&lt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%201">Link to this property</a>

"&gt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%202">Link to this property</a>

"&gt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%203">Link to this property</a>

"=="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20operator">Link to this property</a>

<details>

<summary>

risk\_level: optional "low"or "medium"or "high"or "critical"

For more details on risk level, refer to the Tanium documentation.

</summary>

One of the following:

"low"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20risk_level%20%3E%20(member)%200">Link to this property</a>

"medium"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20risk_level%20%3E%20(member)%201">Link to this property</a>

"high"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20risk_level%20%3E%20(member)%202">Link to this property</a>

"critical"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20risk_level%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20risk_level">Link to this property</a>

<details>

<summary>

scoreOperator: optional "&lt;"or "&lt;="or "&gt;"or 2 more

Score Operator.

</summary>

One of the following:

"&lt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20scoreOperator%20%3E%20(member)%200">Link to this property</a>

"&lt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20scoreOperator%20%3E%20(member)%201">Link to this property</a>

"&gt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20scoreOperator%20%3E%20(member)%202">Link to this property</a>

"&gt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20scoreOperator%20%3E%20(member)%203">Link to this property</a>

"=="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20scoreOperator%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20scoreOperator">Link to this property</a>

total\_score: optional number

For more details on total score, refer to the Tanium documentation.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20total_score">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

SentineloneS2sInput object {connection\_id, active\_threats, infected, 4 more }

</summary>

connection\_id: string

Posture Integration ID.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20connection_id">Link to this property</a>

active\_threats: optional number

The Number of active threats.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20active_threats">Link to this property</a>

infected: optional boolean

Whether device is infected.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20infected">Link to this property</a>

is\_active: optional boolean

Whether device is active.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20is_active">Link to this property</a>

<details>

<summary>

network\_status: optional "connected"or "disconnected"or "disconnecting"or "connecting"

Network status of device.

</summary>

One of the following:

"connected"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20network_status%20%3E%20(member)%200">Link to this property</a>

"disconnected"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20network_status%20%3E%20(member)%201">Link to this property</a>

"disconnecting"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20network_status%20%3E%20(member)%202">Link to this property</a>

"connecting"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20network_status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20network_status">Link to this property</a>

<details>

<summary>

operational\_state: optional "na"or "partially\_disabled"or "auto\_fully\_disabled"or 4 more

Agent operational state.

</summary>

One of the following:

"na"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20operational_state%20%3E%20(member)%200">Link to this property</a>

"partially\_disabled"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20operational_state%20%3E%20(member)%201">Link to this property</a>

"auto\_fully\_disabled"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20operational_state%20%3E%20(member)%202">Link to this property</a>

"fully\_disabled"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20operational_state%20%3E%20(member)%203">Link to this property</a>

"auto\_partially\_disabled"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20operational_state%20%3E%20(member)%204">Link to this property</a>

"disabled\_error"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20operational_state%20%3E%20(member)%205">Link to this property</a>

"db\_corruption"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20operational_state%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20operational_state">Link to this property</a>

<details>

<summary>

operator: optional "&lt;"or "&lt;="or "&gt;"or 2 more

Operator.

</summary>

One of the following:

"&lt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%200">Link to this property</a>

"&lt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%201">Link to this property</a>

"&gt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%202">Link to this property</a>

"&gt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%203">Link to this property</a>

"=="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20operator">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

TeamsDevicesCustomS2sInputRequest object {connection\_id, operator, score }

</summary>

connection\_id: string

Posture Integration ID.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%2019%20%3E%20(property)%20connection_id">Link to this property</a>

<details>

<summary>

operator: "&lt;"or "&lt;="or "&gt;"or 2 more

Operator.

</summary>

One of the following:

"&lt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%2019%20%3E%20(property)%20operator%20%3E%20(member)%200">Link to this property</a>

"&lt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%2019%20%3E%20(property)%20operator%20%3E%20(member)%201">Link to this property</a>

"&gt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%2019%20%3E%20(property)%20operator%20%3E%20(member)%202">Link to this property</a>

"&gt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%2019%20%3E%20(property)%20operator%20%3E%20(member)%203">Link to this property</a>

"=="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%2019%20%3E%20(property)%20operator%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%2019%20%3E%20(property)%20operator">Link to this property</a>

score: number

A value between 0-100 assigned to devices set by the 3rd party posture provider.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%2019%20%3E%20(property)%20score">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)%20%3E%20(variant)%2019">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)>)

<details>

<summary>

DeviceMatch object {platform }

</summary>

<details>

<summary>

platform: optional "windows"or "mac"or "linux"or 3 more

</summary>

One of the following:

"windows"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_match%20%3E%20(schema)%20%3E%20(property)%20platform%20%3E%20(member)%200">Link to this property</a>

"mac"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_match%20%3E%20(schema)%20%3E%20(property)%20platform%20%3E%20(member)%201">Link to this property</a>

"linux"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_match%20%3E%20(schema)%20%3E%20(property)%20platform%20%3E%20(member)%202">Link to this property</a>

"android"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_match%20%3E%20(schema)%20%3E%20(property)%20platform%20%3E%20(member)%203">Link to this property</a>

"ios"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_match%20%3E%20(schema)%20%3E%20(property)%20platform%20%3E%20(member)%204">Link to this property</a>

"chromeos"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_match%20%3E%20(schema)%20%3E%20(property)%20platform%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_match%20%3E%20(schema)%20%3E%20(property)%20platform">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_match%20%3E%20(schema)>)

<details>

<summary>

DevicePostureRule object {id, description, enabled, 6 more }

</summary>

id: optional string

API UUID.

maxLength36

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

description: optional string

The description of the device posture rule.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Whether the rule is enabled. This is a computed, read-only value. It is false for deprecated Kolide posture rules that still use the issue\_count input, and true otherwise.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

expiration: optional string

Sets the expiration time for a posture check result. If empty, the result remains valid until it is overwritten by new data from the WARP client.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20expiration">Link to this property</a>

input: optional <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_input%20%3E%20(schema)">DeviceInput</a>

The value to be checked against.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20input">Link to this property</a>

<details>

<summary>

match: optional array of <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_match%20%3E%20(schema)">DeviceMatch</a> { platform }

The conditions that the client must match to run the rule.

</summary>

<details>

<summary>

platform: optional "windows"or "mac"or "linux"or 3 more

</summary>

One of the following:

"windows"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_match%20%3E%20(schema)%20%3E%20(property)%20platform%20%3E%20(member)%200">Link to this property</a>

"mac"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_match%20%3E%20(schema)%20%3E%20(property)%20platform%20%3E%20(member)%201">Link to this property</a>

"linux"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_match%20%3E%20(schema)%20%3E%20(property)%20platform%20%3E%20(member)%202">Link to this property</a>

"android"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_match%20%3E%20(schema)%20%3E%20(property)%20platform%20%3E%20(member)%203">Link to this property</a>

"ios"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_match%20%3E%20(schema)%20%3E%20(property)%20platform%20%3E%20(member)%204">Link to this property</a>

"chromeos"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_match%20%3E%20(schema)%20%3E%20(property)%20platform%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_match%20%3E%20(schema)%20%3E%20(property)%20platform">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20match">Link to this property</a>

name: optional string

The name of the device posture rule.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

schedule: optional string

Polling frequency for the WARP client posture check. Default: <code>5m</code> (poll every five minutes). Minimum: <code>1m</code>.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20schedule">Link to this property</a>

<details>

<summary>

type: optional "file"or "application"or "tanium"or 20 more

The type of device posture rule.

</summary>

One of the following:

"file"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"application"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"tanium"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"gateway"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

"warp"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%204">Link to this property</a>

"disk\_encryption"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%205">Link to this property</a>

"serial\_number"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%206">Link to this property</a>

"sentinelone"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%207">Link to this property</a>

"carbonblack"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%208">Link to this property</a>

"firewall"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%209">Link to this property</a>

"os\_version"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2010">Link to this property</a>

"domain\_joined"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2011">Link to this property</a>

"client\_certificate"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2012">Link to this property</a>

"client\_certificate\_v2"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2013">Link to this property</a>

"antivirus"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2014">Link to this property</a>

"unique\_client\_id"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2015">Link to this property</a>

"kolide"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2016">Link to this property</a>

"tanium\_s2s"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2017">Link to this property</a>

"crowdstrike\_s2s"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2018">Link to this property</a>

"intune"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2019">Link to this property</a>

"workspace\_one"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2020">Link to this property</a>

"sentinelone\_s2s"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2021">Link to this property</a>

"custom\_s2s"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2022">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20device_posture_rule%20%3E%20(schema)>)

<details>

<summary>

DiskEncryptionInput object {checkDisks, requireAll }

</summary>

checkDisks: optional array of <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20carbonblack_input%20%3E%20(schema)">CarbonblackInput</a>

List of volume names to be checked for encryption.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20disk_encryption_input%20%3E%20(schema)%20%3E%20(property)%20checkDisks">Link to this property</a>

requireAll: optional boolean

Whether to check all disks for encryption.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20disk_encryption_input%20%3E%20(schema)%20%3E%20(property)%20requireAll">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20disk_encryption_input%20%3E%20(schema)>)

<details>

<summary>

DomainJoinedInput object {operating\_system, domain }

</summary>

operating\_system: "windows"

Operating System.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20domain_joined_input%20%3E%20(schema)%20%3E%20(property)%20operating_system">Link to this property</a>

domain: optional string

Domain.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20domain_joined_input%20%3E%20(schema)%20%3E%20(property)%20domain">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20domain_joined_input%20%3E%20(schema)>)

<details>

<summary>

FileInput object {operating\_system, path, exists, 2 more }

</summary>

<details>

<summary>

operating\_system: "windows"or "linux"or "mac"

Operating system.

</summary>

One of the following:

"windows"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20file_input%20%3E%20(schema)%20%3E%20(property)%20operating_system%20%3E%20(member)%200">Link to this property</a>

"linux"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20file_input%20%3E%20(schema)%20%3E%20(property)%20operating_system%20%3E%20(member)%201">Link to this property</a>

"mac"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20file_input%20%3E%20(schema)%20%3E%20(property)%20operating_system%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20file_input%20%3E%20(schema)%20%3E%20(property)%20operating_system">Link to this property</a>

path: string

File path.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20file_input%20%3E%20(schema)%20%3E%20(property)%20path">Link to this property</a>

exists: optional boolean

Whether or not file exists.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20file_input%20%3E%20(schema)%20%3E%20(property)%20exists">Link to this property</a>

sha256: optional string

SHA-256.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20file_input%20%3E%20(schema)%20%3E%20(property)%20sha256">Link to this property</a>

thumbprint: optional string

Signing certificate thumbprint.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20file_input%20%3E%20(schema)%20%3E%20(property)%20thumbprint">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20file_input%20%3E%20(schema)>)

<details>

<summary>

FirewallInput object {enabled, operating\_system }

</summary>

enabled: boolean

Enabled.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20firewall_input%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

<details>

<summary>

operating\_system: "windows"or "mac"

Operating System.

</summary>

One of the following:

"windows"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20firewall_input%20%3E%20(schema)%20%3E%20(property)%20operating_system%20%3E%20(member)%200">Link to this property</a>

"mac"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20firewall_input%20%3E%20(schema)%20%3E%20(property)%20operating_system%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20firewall_input%20%3E%20(schema)%20%3E%20(property)%20operating_system">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20firewall_input%20%3E%20(schema)>)

<details>

<summary>

IntuneInput object {compliance\_status, connection\_id }

</summary>

<details>

<summary>

compliance\_status: "compliant"or "noncompliant"or "unknown"or 3 more

Compliance Status.

</summary>

One of the following:

"compliant"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20intune_input%20%3E%20(schema)%20%3E%20(property)%20compliance_status%20%3E%20(member)%200">Link to this property</a>

"noncompliant"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20intune_input%20%3E%20(schema)%20%3E%20(property)%20compliance_status%20%3E%20(member)%201">Link to this property</a>

"unknown"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20intune_input%20%3E%20(schema)%20%3E%20(property)%20compliance_status%20%3E%20(member)%202">Link to this property</a>

"notapplicable"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20intune_input%20%3E%20(schema)%20%3E%20(property)%20compliance_status%20%3E%20(member)%203">Link to this property</a>

"ingraceperiod"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20intune_input%20%3E%20(schema)%20%3E%20(property)%20compliance_status%20%3E%20(member)%204">Link to this property</a>

"error"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20intune_input%20%3E%20(schema)%20%3E%20(property)%20compliance_status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20intune_input%20%3E%20(schema)%20%3E%20(property)%20compliance_status">Link to this property</a>

connection\_id: string

Posture Integration ID.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20intune_input%20%3E%20(schema)%20%3E%20(property)%20connection_id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20intune_input%20%3E%20(schema)>)

<details>

<summary>

KolideInput object {connection\_id, auth\_state, countOperator, issue\_count }

</summary>

connection\_id: string

Posture Integration ID.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20kolide_input%20%3E%20(schema)%20%3E%20(property)%20connection_id">Link to this property</a>

<details>

<summary>

auth\_state: optional array of "Good"or "Notified"or "Will Block"or "Blocked"

The set of Kolide device authentication states that pass the posture check. Device must match one of the specified states.

</summary>

One of the following:

"Good"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20kolide_input%20%3E%20(schema)%20%3E%20(property)%20auth_state%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"Notified"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20kolide_input%20%3E%20(schema)%20%3E%20(property)%20auth_state%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"Will Block"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20kolide_input%20%3E%20(schema)%20%3E%20(property)%20auth_state%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"Blocked"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20kolide_input%20%3E%20(schema)%20%3E%20(property)%20auth_state%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20kolide_input%20%3E%20(schema)%20%3E%20(property)%20auth_state">Link to this property</a>

<details>

<summary>

countOperator: optional "&lt;"or "&lt;="or "&gt;"or 2 more

Count Operator.

</summary>

One of the following:

"&lt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20kolide_input%20%3E%20(schema)%20%3E%20(property)%20countOperator%20%3E%20(member)%200">Link to this property</a>

"&lt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20kolide_input%20%3E%20(schema)%20%3E%20(property)%20countOperator%20%3E%20(member)%201">Link to this property</a>

"&gt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20kolide_input%20%3E%20(schema)%20%3E%20(property)%20countOperator%20%3E%20(member)%202">Link to this property</a>

"&gt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20kolide_input%20%3E%20(schema)%20%3E%20(property)%20countOperator%20%3E%20(member)%203">Link to this property</a>

"=="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20kolide_input%20%3E%20(schema)%20%3E%20(property)%20countOperator%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20kolide_input%20%3E%20(schema)%20%3E%20(property)%20countOperator">Link to this property</a>

issue\_count: optional string

The Number of Issues.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20kolide_input%20%3E%20(schema)%20%3E%20(property)%20issue_count">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20kolide_input%20%3E%20(schema)>)

<details>

<summary>

OSVersionInput object {operating\_system, operator, version, 3 more }

</summary>

operating\_system: "windows"

Operating System.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20os_version_input%20%3E%20(schema)%20%3E%20(property)%20operating_system">Link to this property</a>

<details>

<summary>

operator: "&lt;"or "&lt;="or "&gt;"or 2 more

Operator.

</summary>

One of the following:

"&lt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20os_version_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%200">Link to this property</a>

"&lt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20os_version_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%201">Link to this property</a>

"&gt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20os_version_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%202">Link to this property</a>

"&gt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20os_version_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%203">Link to this property</a>

"=="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20os_version_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20os_version_input%20%3E%20(schema)%20%3E%20(property)%20operator">Link to this property</a>

version: string

Version of OS.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20os_version_input%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

os\_distro\_name: optional string

Operating System Distribution Name (linux only).

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20os_version_input%20%3E%20(schema)%20%3E%20(property)%20os_distro_name">Link to this property</a>

os\_distro\_revision: optional string

Version of OS Distribution (linux only).

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20os_version_input%20%3E%20(schema)%20%3E%20(property)%20os_distro_revision">Link to this property</a>

os\_version\_extra: optional string

Additional operating system version details. For Windows, the UBR (Update Build Revision). For Mac or iOS, the Product Version Extra. For Linux, the distribution name and version.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20os_version_input%20%3E%20(schema)%20%3E%20(property)%20os_version_extra">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20os_version_input%20%3E%20(schema)>)

<details>

<summary>

SentineloneInput object {operating\_system, path, sha256, thumbprint }

</summary>

<details>

<summary>

operating\_system: "windows"or "linux"or "mac"

Operating system.

</summary>

One of the following:

"windows"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_input%20%3E%20(schema)%20%3E%20(property)%20operating_system%20%3E%20(member)%200">Link to this property</a>

"linux"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_input%20%3E%20(schema)%20%3E%20(property)%20operating_system%20%3E%20(member)%201">Link to this property</a>

"mac"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_input%20%3E%20(schema)%20%3E%20(property)%20operating_system%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_input%20%3E%20(schema)%20%3E%20(property)%20operating_system">Link to this property</a>

path: string

File path.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_input%20%3E%20(schema)%20%3E%20(property)%20path">Link to this property</a>

sha256: optional string

SHA-256.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_input%20%3E%20(schema)%20%3E%20(property)%20sha256">Link to this property</a>

thumbprint: optional string

Signing certificate thumbprint.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_input%20%3E%20(schema)%20%3E%20(property)%20thumbprint">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_input%20%3E%20(schema)>)

<details>

<summary>

SentineloneS2sInput object {connection\_id, active\_threats, infected, 4 more }

</summary>

connection\_id: string

Posture Integration ID.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20connection_id">Link to this property</a>

active\_threats: optional number

The Number of active threats.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20active_threats">Link to this property</a>

infected: optional boolean

Whether device is infected.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20infected">Link to this property</a>

is\_active: optional boolean

Whether device is active.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20is_active">Link to this property</a>

<details>

<summary>

network\_status: optional "connected"or "disconnected"or "disconnecting"or "connecting"

Network status of device.

</summary>

One of the following:

"connected"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20network_status%20%3E%20(member)%200">Link to this property</a>

"disconnected"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20network_status%20%3E%20(member)%201">Link to this property</a>

"disconnecting"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20network_status%20%3E%20(member)%202">Link to this property</a>

"connecting"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20network_status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20network_status">Link to this property</a>

<details>

<summary>

operational\_state: optional "na"or "partially\_disabled"or "auto\_fully\_disabled"or 4 more

Agent operational state.

</summary>

One of the following:

"na"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20operational_state%20%3E%20(member)%200">Link to this property</a>

"partially\_disabled"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20operational_state%20%3E%20(member)%201">Link to this property</a>

"auto\_fully\_disabled"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20operational_state%20%3E%20(member)%202">Link to this property</a>

"fully\_disabled"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20operational_state%20%3E%20(member)%203">Link to this property</a>

"auto\_partially\_disabled"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20operational_state%20%3E%20(member)%204">Link to this property</a>

"disabled\_error"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20operational_state%20%3E%20(member)%205">Link to this property</a>

"db\_corruption"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20operational_state%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20operational_state">Link to this property</a>

<details>

<summary>

operator: optional "&lt;"or "&lt;="or "&gt;"or 2 more

Operator.

</summary>

One of the following:

"&lt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%200">Link to this property</a>

"&lt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%201">Link to this property</a>

"&gt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%202">Link to this property</a>

"&gt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%203">Link to this property</a>

"=="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)%20%3E%20(property)%20operator">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20sentinelone_s2s_input%20%3E%20(schema)>)

<details>

<summary>

TaniumInput object {connection\_id, eid\_last\_seen, operator, 3 more }

</summary>

connection\_id: string

Posture Integration ID.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20connection_id">Link to this property</a>

eid\_last\_seen: optional string

For more details on eid last seen, refer to the Tanium documentation.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20eid_last_seen">Link to this property</a>

<details>

<summary>

operator: optional "&lt;"or "&lt;="or "&gt;"or 2 more

Operator to evaluate risk\_level or eid\_last\_seen.

</summary>

One of the following:

"&lt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%200">Link to this property</a>

"&lt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%201">Link to this property</a>

"&gt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%202">Link to this property</a>

"&gt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%203">Link to this property</a>

"=="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20operator%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20operator">Link to this property</a>

<details>

<summary>

risk\_level: optional "low"or "medium"or "high"or "critical"

For more details on risk level, refer to the Tanium documentation.

</summary>

One of the following:

"low"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20risk_level%20%3E%20(member)%200">Link to this property</a>

"medium"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20risk_level%20%3E%20(member)%201">Link to this property</a>

"high"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20risk_level%20%3E%20(member)%202">Link to this property</a>

"critical"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20risk_level%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20risk_level">Link to this property</a>

<details>

<summary>

scoreOperator: optional "&lt;"or "&lt;="or "&gt;"or 2 more

Score Operator.

</summary>

One of the following:

"&lt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20scoreOperator%20%3E%20(member)%200">Link to this property</a>

"&lt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20scoreOperator%20%3E%20(member)%201">Link to this property</a>

"&gt;"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20scoreOperator%20%3E%20(member)%202">Link to this property</a>

"&gt;="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20scoreOperator%20%3E%20(member)%203">Link to this property</a>

"=="

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20scoreOperator%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20scoreOperator">Link to this property</a>

total\_score: optional number

For more details on total score, refer to the Tanium documentation.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)%20%3E%20(property)%20total_score">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20tanium_input%20%3E%20(schema)>)

<details>

<summary>

UniqueClientIDInput object {id, operating\_system }

</summary>

id: string

List ID.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20unique_client_id_input%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

operating\_system: "android"or "ios"or "chromeos"

Operating System.

</summary>

One of the following:

"android"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20unique_client_id_input%20%3E%20(schema)%20%3E%20(property)%20operating_system%20%3E%20(member)%200">Link to this property</a>

"ios"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20unique_client_id_input%20%3E%20(schema)%20%3E%20(property)%20operating_system%20%3E%20(member)%201">Link to this property</a>

"chromeos"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20unique_client_id_input%20%3E%20(schema)%20%3E%20(property)%20operating_system%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20unique_client_id_input%20%3E%20(schema)%20%3E%20(property)%20operating_system">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20unique_client_id_input%20%3E%20(schema)>)

<details>

<summary>

WorkspaceOneInput object {compliance\_status, connection\_id }

</summary>

<details>

<summary>

compliance\_status: "compliant"or "noncompliant"or "unknown"

Compliance Status.

</summary>

One of the following:

"compliant"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20workspace_one_input%20%3E%20(schema)%20%3E%20(property)%20compliance_status%20%3E%20(member)%200">Link to this property</a>

"noncompliant"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20workspace_one_input%20%3E%20(schema)%20%3E%20(property)%20compliance_status%20%3E%20(member)%201">Link to this property</a>

"unknown"

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20workspace_one_input%20%3E%20(schema)%20%3E%20(property)%20compliance_status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20workspace_one_input%20%3E%20(schema)%20%3E%20(property)%20compliance_status">Link to this property</a>

connection\_id: string

Posture Integration ID.

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20workspace_one_input%20%3E%20(schema)%20%3E%20(property)%20connection_id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20workspace_one_input%20%3E%20(schema)>)

<details>

<summary>

PostureDeleteResponse object {id }

</summary>

id: optional string

API UUID.

maxLength36

<a href="#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20posture_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.devices.posture%20%3E%20(model)%20posture_delete_response%20%3E%20(schema)>)

#### PostureIntegrations

##### [List posture integrations](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/posture/subresources/integrations/methods/list)

GET/accounts/{account\_id}/devices/posture/integration

##### [Get posture integration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/posture/subresources/integrations/methods/get)

GET/accounts/{account\_id}/devices/posture/integration/{integration\_id}

##### [Create posture integration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/posture/subresources/integrations/methods/create)

POST/accounts/{account\_id}/devices/posture/integration

##### [Update posture integration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/posture/subresources/integrations/methods/edit)

PATCH/accounts/{account\_id}/devices/posture/integration/{integration\_id}

##### [Delete posture integration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/posture/subresources/integrations/methods/delete)

DELETE/accounts/{account\_id}/devices/posture/integration/{integration\_id}

##### ModelsExpand Collapse

<details>

<summary>

Integration object {id, config, interval, 2 more }

</summary>

id: optional string

API UUID.

maxLength36

<a href="#(resource)%20zero_trust.devices.posture.integrations%20%3E%20(model)%20integration%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

config: optional object {api\_url, auth\_url, client\_id }

The configuration object containing third-party integration information.

</summary>

api\_url: string

The Workspace One API URL provided in the Workspace One Admin Dashboard.

<a href="#(resource)%20zero_trust.devices.posture.integrations%20%3E%20(model)%20integration%20%3E%20(schema)%20%3E%20(property)%20config%20%3E%20(property)%20api_url">Link to this property</a>

auth\_url: string

The Workspace One Authorization URL depending on your region.

<a href="#(resource)%20zero_trust.devices.posture.integrations%20%3E%20(model)%20integration%20%3E%20(schema)%20%3E%20(property)%20config%20%3E%20(property)%20auth_url">Link to this property</a>

client\_id: string

The Workspace One client ID provided in the Workspace One Admin Dashboard.

<a href="#(resource)%20zero_trust.devices.posture.integrations%20%3E%20(model)%20integration%20%3E%20(schema)%20%3E%20(property)%20config%20%3E%20(property)%20client_id">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture.integrations%20%3E%20(model)%20integration%20%3E%20(schema)%20%3E%20(property)%20config">Link to this property</a>

interval: optional string

The interval between each posture check with the third-party API. Use <code>m</code> for minutes (e.g. <code>5m</code>) and <code>h</code> for hours (e.g. <code>12h</code>).

<a href="#(resource)%20zero_trust.devices.posture.integrations%20%3E%20(model)%20integration%20%3E%20(schema)%20%3E%20(property)%20interval">Link to this property</a>

name: optional string

The name of the device posture integration.

<a href="#(resource)%20zero_trust.devices.posture.integrations%20%3E%20(model)%20integration%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

type: optional "workspace\_one"or "crowdstrike\_s2s"or "uptycs"or 5 more

The type of device posture integration.

</summary>

One of the following:

"workspace\_one"

<a href="#(resource)%20zero_trust.devices.posture.integrations%20%3E%20(model)%20integration%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"crowdstrike\_s2s"

<a href="#(resource)%20zero_trust.devices.posture.integrations%20%3E%20(model)%20integration%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"uptycs"

<a href="#(resource)%20zero_trust.devices.posture.integrations%20%3E%20(model)%20integration%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"intune"

<a href="#(resource)%20zero_trust.devices.posture.integrations%20%3E%20(model)%20integration%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

"kolide"

<a href="#(resource)%20zero_trust.devices.posture.integrations%20%3E%20(model)%20integration%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%204">Link to this property</a>

"tanium\_s2s"

<a href="#(resource)%20zero_trust.devices.posture.integrations%20%3E%20(model)%20integration%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%205">Link to this property</a>

"sentinelone\_s2s"

<a href="#(resource)%20zero_trust.devices.posture.integrations%20%3E%20(model)%20integration%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%206">Link to this property</a>

"custom\_s2s"

<a href="#(resource)%20zero_trust.devices.posture.integrations%20%3E%20(model)%20integration%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.posture.integrations%20%3E%20(model)%20integration%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.devices.posture.integrations%20%3E%20(model)%20integration%20%3E%20(schema)>)

<details>

<summary>

IntegrationDeleteResponse = unknownor string

</summary>

One of the following:

unknown

<a href="#(resource)%20zero_trust.devices.posture.integrations%20%3E%20(model)%20integration_delete_response%20%3E%20(schema)%20%3E%20(variant)%200">Link to this property</a>

string

<a href="#(resource)%20zero_trust.devices.posture.integrations%20%3E%20(model)%20integration_delete_response%20%3E%20(schema)%20%3E%20(variant)%201">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.devices.posture.integrations%20%3E%20(model)%20integration_delete_response%20%3E%20(schema)>)