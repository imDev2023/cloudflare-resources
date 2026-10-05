---
title: Scans
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[URL Scanner](https://developers.cloudflare.com/api/resources/url_scanner)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Scans

##### [Search URL scans](https://developers.cloudflare.com/api/resources/url_scanner/subresources/scans/methods/list)

GET/accounts/{account\_id}/urlscanner/v2/search

##### [Get URL scan](https://developers.cloudflare.com/api/resources/url_scanner/subresources/scans/methods/get)

GET/accounts/{account\_id}/urlscanner/v2/result/{scan\_id}

##### [Create URL Scan](https://developers.cloudflare.com/api/resources/url_scanner/subresources/scans/methods/create)

POST/accounts/{account\_id}/urlscanner/v2/scan

##### [Bulk create URL Scans](https://developers.cloudflare.com/api/resources/url_scanner/subresources/scans/methods/bulk_create)

POST/accounts/{account\_id}/urlscanner/v2/bulk

##### [Get URL scan's HAR](https://developers.cloudflare.com/api/resources/url_scanner/subresources/scans/methods/har)

GET/accounts/{account\_id}/urlscanner/v2/har/{scan\_id}

##### [Get screenshot](https://developers.cloudflare.com/api/resources/url_scanner/subresources/scans/methods/screenshot)

GET/accounts/{account\_id}/urlscanner/v2/screenshots/{scan\_id}.png

##### [Get URL scan's DOM](https://developers.cloudflare.com/api/resources/url_scanner/subresources/scans/methods/dom)

GET/accounts/{account\_id}/urlscanner/v2/dom/{scan\_id}

##### ModelsExpand Collapse

<details>

<summary>

ScanListResponse object {results }

</summary>

<details>

<summary>

results: array of object {\_id, page, result, 3 more }

</summary>

\_id: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_list_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20_id">Link to this property</a>

<details>

<summary>

page: object {asn, country, ip, url }

</summary>

asn: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_list_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20page%20%3E%20(property)%20asn">Link to this property</a>

country: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_list_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20page%20%3E%20(property)%20country">Link to this property</a>

ip: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_list_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20page%20%3E%20(property)%20ip">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_list_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20page%20%3E%20(property)%20url">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_list_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20page">Link to this property</a>

result: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_list_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20result">Link to this property</a>

<details>

<summary>

stats: object {dataLength, requests, uniqCountries, uniqIPs }

</summary>

dataLength: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_list_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20stats%20%3E%20(property)%20dataLength">Link to this property</a>

requests: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_list_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20stats%20%3E%20(property)%20requests">Link to this property</a>

uniqCountries: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_list_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20stats%20%3E%20(property)%20uniqCountries">Link to this property</a>

uniqIPs: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_list_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20stats%20%3E%20(property)%20uniqIPs">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_list_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20stats">Link to this property</a>

<details>

<summary>

task: object {time, url, uuid, visibility }

</summary>

time: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_list_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20task%20%3E%20(property)%20time">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_list_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20task%20%3E%20(property)%20url">Link to this property</a>

uuid: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_list_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20task%20%3E%20(property)%20uuid">Link to this property</a>

visibility: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_list_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20task%20%3E%20(property)%20visibility">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_list_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20task">Link to this property</a>

<details>

<summary>

verdicts: object {malicious }

</summary>

malicious: boolean

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_list_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20verdicts%20%3E%20(property)%20malicious">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_list_response%20%3E%20(schema)%20%3E%20(property)%20results%20%3E%20(items)%20%3E%20(property)%20verdicts">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_list_response%20%3E%20(schema)%20%3E%20(property)%20results">Link to this property</a>

</details>

[Link to this property](<#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_list_response%20%3E%20(schema)>)

<details>

<summary>

ScanGetResponse object {data, lists, meta, 5 more }

</summary>

<details>

<summary>

data: object {console, cookies, globals, 3 more }

</summary>

<details>

<summary>

console: array of object {message }

</summary>

<details>

<summary>

message: object {level, source, text, url }

</summary>

level: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20console%20%3E%20(items)%20%3E%20(property)%20message%20%3E%20(property)%20level">Link to this property</a>

source: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20console%20%3E%20(items)%20%3E%20(property)%20message%20%3E%20(property)%20source">Link to this property</a>

text: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20console%20%3E%20(items)%20%3E%20(property)%20message%20%3E%20(property)%20text">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20console%20%3E%20(items)%20%3E%20(property)%20message%20%3E%20(property)%20url">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20console%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20console">Link to this property</a>

<details>

<summary>

cookies: array of object {domain, expires, httpOnly, 10 more }

</summary>

domain: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20cookies%20%3E%20(items)%20%3E%20(property)%20domain">Link to this property</a>

expires: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20cookies%20%3E%20(items)%20%3E%20(property)%20expires">Link to this property</a>

httpOnly: boolean

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20cookies%20%3E%20(items)%20%3E%20(property)%20httpOnly">Link to this property</a>

name: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20cookies%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

path: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20cookies%20%3E%20(items)%20%3E%20(property)%20path">Link to this property</a>

priority: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20cookies%20%3E%20(items)%20%3E%20(property)%20priority">Link to this property</a>

sameParty: boolean

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20cookies%20%3E%20(items)%20%3E%20(property)%20sameParty">Link to this property</a>

secure: boolean

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20cookies%20%3E%20(items)%20%3E%20(property)%20secure">Link to this property</a>

session: boolean

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20cookies%20%3E%20(items)%20%3E%20(property)%20session">Link to this property</a>

size: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20cookies%20%3E%20(items)%20%3E%20(property)%20size">Link to this property</a>

sourcePort: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20cookies%20%3E%20(items)%20%3E%20(property)%20sourcePort">Link to this property</a>

sourceScheme: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20cookies%20%3E%20(items)%20%3E%20(property)%20sourceScheme">Link to this property</a>

value: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20cookies%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20cookies">Link to this property</a>

<details>

<summary>

globals: array of object {prop, type }

</summary>

prop: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20globals%20%3E%20(items)%20%3E%20(property)%20prop">Link to this property</a>

type: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20globals%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20globals">Link to this property</a>

<details>

<summary>

links: array of object {href, text }

</summary>

href: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20links%20%3E%20(items)%20%3E%20(property)%20href">Link to this property</a>

text: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20links%20%3E%20(items)%20%3E%20(property)%20text">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20links">Link to this property</a>

<details>

<summary>

performance: array of object {duration, entryType, name, startTime }

</summary>

duration: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20performance%20%3E%20(items)%20%3E%20(property)%20duration">Link to this property</a>

entryType: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20performance%20%3E%20(items)%20%3E%20(property)%20entryType">Link to this property</a>

name: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20performance%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

startTime: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20performance%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20performance">Link to this property</a>

<details>

<summary>

requests: array of object {request, response, requests }

</summary>

<details>

<summary>

request: object {documentURL, hasUserGesture, initiator, 9 more }

</summary>

documentURL: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20documentURL">Link to this property</a>

hasUserGesture: boolean

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20hasUserGesture">Link to this property</a>

<details>

<summary>

initiator: object {host, type, url }

</summary>

host: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20initiator%20%3E%20(property)%20host">Link to this property</a>

type: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20initiator%20%3E%20(property)%20type">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20initiator%20%3E%20(property)%20url">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20initiator">Link to this property</a>

redirectHasExtraInfo: boolean

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20redirectHasExtraInfo">Link to this property</a>

<details>

<summary>

request: object {initialPriority, isSameSite, method, 4 more }

</summary>

initialPriority: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20request%20%3E%20(property)%20initialPriority">Link to this property</a>

isSameSite: boolean

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20request%20%3E%20(property)%20isSameSite">Link to this property</a>

method: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20request%20%3E%20(property)%20method">Link to this property</a>

mixedContentType: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20request%20%3E%20(property)%20mixedContentType">Link to this property</a>

referrerPolicy: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20request%20%3E%20(property)%20referrerPolicy">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20request%20%3E%20(property)%20url">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20request%20%3E%20(property)%20headers">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20request">Link to this property</a>

requestId: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20requestId">Link to this property</a>

type: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20type">Link to this property</a>

wallTime: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20wallTime">Link to this property</a>

frameId: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20frameId">Link to this property</a>

loaderId: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20loaderId">Link to this property</a>

primaryRequest: optional boolean

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20primaryRequest">Link to this property</a>

<details>

<summary>

redirectResponse: optional object {charset, mimeType, protocol, 8 more }

</summary>

charset: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20redirectResponse%20%3E%20(property)%20charset">Link to this property</a>

mimeType: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20redirectResponse%20%3E%20(property)%20mimeType">Link to this property</a>

protocol: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20redirectResponse%20%3E%20(property)%20protocol">Link to this property</a>

remoteIPAddress: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20redirectResponse%20%3E%20(property)%20remoteIPAddress">Link to this property</a>

remotePort: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20redirectResponse%20%3E%20(property)%20remotePort">Link to this property</a>

<details>

<summary>

securityHeaders: array of object {name, value }

</summary>

name: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20redirectResponse%20%3E%20(property)%20securityHeaders%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20redirectResponse%20%3E%20(property)%20securityHeaders%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20redirectResponse%20%3E%20(property)%20securityHeaders">Link to this property</a>

securityState: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20redirectResponse%20%3E%20(property)%20securityState">Link to this property</a>

status: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20redirectResponse%20%3E%20(property)%20status">Link to this property</a>

statusText: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20redirectResponse%20%3E%20(property)%20statusText">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20redirectResponse%20%3E%20(property)%20url">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20redirectResponse%20%3E%20(property)%20headers">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20redirectResponse">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request">Link to this property</a>

<details>

<summary>

response: object {asn, dataLength, encodedDataLength, 8 more }

</summary>

<details>

<summary>

asn: object {asn, country, description, 3 more }

</summary>

asn: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20asn%20%3E%20(property)%20asn">Link to this property</a>

country: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20asn%20%3E%20(property)%20country">Link to this property</a>

description: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20asn%20%3E%20(property)%20description">Link to this property</a>

ip: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20asn%20%3E%20(property)%20ip">Link to this property</a>

name: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20asn%20%3E%20(property)%20name">Link to this property</a>

org: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20asn%20%3E%20(property)%20org">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20asn">Link to this property</a>

dataLength: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20dataLength">Link to this property</a>

encodedDataLength: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20encodedDataLength">Link to this property</a>

<details>

<summary>

geoip: object {city, country, country\_name, 3 more }

</summary>

city: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20geoip%20%3E%20(property)%20city">Link to this property</a>

country: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20geoip%20%3E%20(property)%20country">Link to this property</a>

country\_name: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20geoip%20%3E%20(property)%20country_name">Link to this property</a>

geonameId: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20geoip%20%3E%20(property)%20geonameId">Link to this property</a>

ll: array of number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20geoip%20%3E%20(property)%20ll">Link to this property</a>

region: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20geoip%20%3E%20(property)%20region">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20geoip">Link to this property</a>

hasExtraInfo: boolean

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20hasExtraInfo">Link to this property</a>

requestId: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20requestId">Link to this property</a>

<details>

<summary>

response: object {charset, mimeType, protocol, 9 more }

</summary>

charset: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20response%20%3E%20(property)%20charset">Link to this property</a>

mimeType: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20response%20%3E%20(property)%20mimeType">Link to this property</a>

protocol: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20response%20%3E%20(property)%20protocol">Link to this property</a>

remoteIPAddress: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20response%20%3E%20(property)%20remoteIPAddress">Link to this property</a>

remotePort: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20response%20%3E%20(property)%20remotePort">Link to this property</a>

<details>

<summary>

securityDetails: object {certificateId, certificateTransparencyCompliance, cipher, 10 more }

</summary>

certificateId: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20response%20%3E%20(property)%20securityDetails%20%3E%20(property)%20certificateId">Link to this property</a>

certificateTransparencyCompliance: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20response%20%3E%20(property)%20securityDetails%20%3E%20(property)%20certificateTransparencyCompliance">Link to this property</a>

cipher: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20response%20%3E%20(property)%20securityDetails%20%3E%20(property)%20cipher">Link to this property</a>

encryptedClientHello: boolean

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20response%20%3E%20(property)%20securityDetails%20%3E%20(property)%20encryptedClientHello">Link to this property</a>

issuer: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20response%20%3E%20(property)%20securityDetails%20%3E%20(property)%20issuer">Link to this property</a>

keyExchange: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20response%20%3E%20(property)%20securityDetails%20%3E%20(property)%20keyExchange">Link to this property</a>

keyExchangeGroup: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20response%20%3E%20(property)%20securityDetails%20%3E%20(property)%20keyExchangeGroup">Link to this property</a>

protocol: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20response%20%3E%20(property)%20securityDetails%20%3E%20(property)%20protocol">Link to this property</a>

sanList: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20response%20%3E%20(property)%20securityDetails%20%3E%20(property)%20sanList">Link to this property</a>

serverSignatureAlgorithm: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20response%20%3E%20(property)%20securityDetails%20%3E%20(property)%20serverSignatureAlgorithm">Link to this property</a>

subjectName: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20response%20%3E%20(property)%20securityDetails%20%3E%20(property)%20subjectName">Link to this property</a>

validFrom: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20response%20%3E%20(property)%20securityDetails%20%3E%20(property)%20validFrom">Link to this property</a>

validTo: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20response%20%3E%20(property)%20securityDetails%20%3E%20(property)%20validTo">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20response%20%3E%20(property)%20securityDetails">Link to this property</a>

<details>

<summary>

securityHeaders: array of object {name, value }

</summary>

name: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20response%20%3E%20(property)%20securityHeaders%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20response%20%3E%20(property)%20securityHeaders%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20response%20%3E%20(property)%20securityHeaders">Link to this property</a>

securityState: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20response%20%3E%20(property)%20securityState">Link to this property</a>

status: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20response%20%3E%20(property)%20status">Link to this property</a>

statusText: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20response%20%3E%20(property)%20statusText">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20response%20%3E%20(property)%20url">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20response%20%3E%20(property)%20headers">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20response">Link to this property</a>

size: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20size">Link to this property</a>

type: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20type">Link to this property</a>

contentAvailable: optional boolean

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20contentAvailable">Link to this property</a>

hash: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20hash">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20response">Link to this property</a>

<details>

<summary>

requests: optional array of object {documentURL, frameId, hasUserGesture, 7 more }

</summary>

documentURL: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20documentURL">Link to this property</a>

frameId: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20frameId">Link to this property</a>

hasUserGesture: boolean

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20hasUserGesture">Link to this property</a>

<details>

<summary>

initiator: object {type }

</summary>

type: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20initiator%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20initiator">Link to this property</a>

loaderId: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20loaderId">Link to this property</a>

redirectHasExtraInfo: boolean

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20redirectHasExtraInfo">Link to this property</a>

<details>

<summary>

request: object {headers, initialPriority, isSameSite, 4 more }

</summary>

<details>

<summary>

headers: object {name }

</summary>

name: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20headers%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20headers">Link to this property</a>

initialPriority: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20initialPriority">Link to this property</a>

isSameSite: boolean

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20isSameSite">Link to this property</a>

method: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20method">Link to this property</a>

mixedContentType: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20mixedContentType">Link to this property</a>

referrerPolicy: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20referrerPolicy">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20url">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20request">Link to this property</a>

requestId: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20requestId">Link to this property</a>

type: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

wallTime: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20wallTime">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests%20%3E%20(items)%20%3E%20(property)%20requests">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20requests">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20data">Link to this property</a>

<details>

<summary>

lists: object {asns, certificates, continents, 7 more }

</summary>

asns: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20lists%20%3E%20(property)%20asns">Link to this property</a>

<details>

<summary>

certificates: array of object {issuer, subjectName, validFrom, validTo }

</summary>

issuer: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20lists%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20issuer">Link to this property</a>

subjectName: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20lists%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20subjectName">Link to this property</a>

validFrom: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20lists%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20validFrom">Link to this property</a>

validTo: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20lists%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20validTo">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20lists%20%3E%20(property)%20certificates">Link to this property</a>

continents: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20lists%20%3E%20(property)%20continents">Link to this property</a>

countries: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20lists%20%3E%20(property)%20countries">Link to this property</a>

domains: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20lists%20%3E%20(property)%20domains">Link to this property</a>

hashes: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20lists%20%3E%20(property)%20hashes">Link to this property</a>

ips: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20lists%20%3E%20(property)%20ips">Link to this property</a>

linkDomains: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20lists%20%3E%20(property)%20linkDomains">Link to this property</a>

servers: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20lists%20%3E%20(property)%20servers">Link to this property</a>

urls: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20lists%20%3E%20(property)%20urls">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20lists">Link to this property</a>

<details>

<summary>

meta: object {processors }

</summary>

<details>

<summary>

processors: object {asn, dns, domainCategories, 8 more }

</summary>

<details>

<summary>

asn: object {data }

</summary>

<details>

<summary>

data: array of object {asn, country, description, 2 more }

</summary>

asn: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20asn%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20asn">Link to this property</a>

country: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20asn%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20country">Link to this property</a>

description: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20asn%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

ip: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20asn%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20ip">Link to this property</a>

name: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20asn%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20asn%20%3E%20(property)%20data">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20asn">Link to this property</a>

<details>

<summary>

dns: object {data }

</summary>

<details>

<summary>

data: array of object {address, dnssec\_valid, name, type }

</summary>

address: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20dns%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20address">Link to this property</a>

dnssec\_valid: boolean

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20dns%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20dnssec_valid">Link to this property</a>

name: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20dns%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

type: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20dns%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20dns%20%3E%20(property)%20data">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20dns">Link to this property</a>

<details>

<summary>

domainCategories: object {data }

</summary>

<details>

<summary>

data: array of object {inherited, isPrimary, name }

</summary>

inherited: unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20domainCategories%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20inherited">Link to this property</a>

isPrimary: boolean

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20domainCategories%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20isPrimary">Link to this property</a>

name: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20domainCategories%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20domainCategories%20%3E%20(property)%20data">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20domainCategories">Link to this property</a>

<details>

<summary>

geoip: object {data }

</summary>

<details>

<summary>

data: array of object {geoip, ip }

</summary>

<details>

<summary>

geoip: object {city, country, country\_name, 2 more }

</summary>

city: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20geoip%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20geoip%20%3E%20(property)%20city">Link to this property</a>

country: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20geoip%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20geoip%20%3E%20(property)%20country">Link to this property</a>

country\_name: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20geoip%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20geoip%20%3E%20(property)%20country_name">Link to this property</a>

ll: array of number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20geoip%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20geoip%20%3E%20(property)%20ll">Link to this property</a>

region: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20geoip%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20geoip%20%3E%20(property)%20region">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20geoip%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20geoip">Link to this property</a>

ip: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20geoip%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20ip">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20geoip%20%3E%20(property)%20data">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20geoip">Link to this property</a>

<details>

<summary>

phishing: object {data }

</summary>

data: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20phishing%20%3E%20(property)%20data">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20phishing">Link to this property</a>

<details>

<summary>

radarRank: object {data }

</summary>

<details>

<summary>

data: array of object {bucket, hostname, rank }

</summary>

bucket: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20radarRank%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20bucket">Link to this property</a>

hostname: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20radarRank%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20hostname">Link to this property</a>

rank: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20radarRank%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20rank">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20radarRank%20%3E%20(property)%20data">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20radarRank">Link to this property</a>

<details>

<summary>

wappa: object {data }

</summary>

<details>

<summary>

data: array of object {app, categories, confidence, 3 more }

</summary>

app: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20wappa%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20app">Link to this property</a>

<details>

<summary>

categories: array of object {name, priority }

</summary>

name: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20wappa%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

priority: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20wappa%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20priority">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20wappa%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20categories">Link to this property</a>

<details>

<summary>

confidence: array of object {confidence, name, pattern, patternType }

</summary>

confidence: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20wappa%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20confidence%20%3E%20(items)%20%3E%20(property)%20confidence">Link to this property</a>

name: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20wappa%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20confidence%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

pattern: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20wappa%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20confidence%20%3E%20(items)%20%3E%20(property)%20pattern">Link to this property</a>

patternType: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20wappa%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20confidence%20%3E%20(items)%20%3E%20(property)%20patternType">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20wappa%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20confidence">Link to this property</a>

confidenceTotal: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20wappa%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20confidenceTotal">Link to this property</a>

icon: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20wappa%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20icon">Link to this property</a>

website: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20wappa%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20website">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20wappa%20%3E%20(property)%20data">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20wappa">Link to this property</a>

<details>

<summary>

agentReadiness: optional object {checks, level, levelName, 3 more }

</summary>

<details>

<summary>

checks: object {botAccessControl, commerce, contentAccessibility, 2 more }

</summary>

<details>

<summary>

botAccessControl: object {contentSignals, robotsTxtAiRules, webBotAuth }

</summary>

<details>

<summary>

contentSignals: object {status, details, durationMs, 3 more }

</summary>

status: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20contentSignals%20%3E%20(property)%20status">Link to this property</a>

details: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20contentSignals%20%3E%20(property)%20details">Link to this property</a>

durationMs: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20contentSignals%20%3E%20(property)%20durationMs">Link to this property</a>

<details>

<summary>

evidence: optional array of object {action, label, finding, 2 more }

</summary>

action: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20contentSignals%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20action">Link to this property</a>

label: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20contentSignals%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

finding: optional object {outcome, summary }

</summary>

outcome: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20contentSignals%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20outcome">Link to this property</a>

summary: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20contentSignals%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20summary">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20contentSignals%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding">Link to this property</a>

<details>

<summary>

request: optional object {method, url, headers }

</summary>

method: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20contentSignals%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20method">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20contentSignals%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20url">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20contentSignals%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20headers">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20contentSignals%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request">Link to this property</a>

<details>

<summary>

response: optional object {status, statusText, bodyPreview, 3 more }

</summary>

status: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20contentSignals%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20status">Link to this property</a>

statusText: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20contentSignals%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20statusText">Link to this property</a>

bodyPreview: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20contentSignals%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodyPreview">Link to this property</a>

bodySize: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20contentSignals%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodySize">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20contentSignals%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20headers">Link to this property</a>

redirectedTo: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20contentSignals%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20redirectedTo">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20contentSignals%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20contentSignals%20%3E%20(property)%20evidence">Link to this property</a>

message: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20contentSignals%20%3E%20(property)%20message">Link to this property</a>

<details>

<summary>

messageRef: optional object {code, params }

</summary>

code: string

Stable, translatable message code.

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20contentSignals%20%3E%20(property)%20messageRef%20%3E%20(property)%20code">Link to this property</a>

params: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20contentSignals%20%3E%20(property)%20messageRef%20%3E%20(property)%20params">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20contentSignals%20%3E%20(property)%20messageRef">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20contentSignals">Link to this property</a>

<details>

<summary>

robotsTxtAiRules: object {status, details, durationMs, 3 more }

</summary>

status: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20robotsTxtAiRules%20%3E%20(property)%20status">Link to this property</a>

details: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20robotsTxtAiRules%20%3E%20(property)%20details">Link to this property</a>

durationMs: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20robotsTxtAiRules%20%3E%20(property)%20durationMs">Link to this property</a>

<details>

<summary>

evidence: optional array of object {action, label, finding, 2 more }

</summary>

action: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20robotsTxtAiRules%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20action">Link to this property</a>

label: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20robotsTxtAiRules%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

finding: optional object {outcome, summary }

</summary>

outcome: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20robotsTxtAiRules%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20outcome">Link to this property</a>

summary: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20robotsTxtAiRules%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20summary">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20robotsTxtAiRules%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding">Link to this property</a>

<details>

<summary>

request: optional object {method, url, headers }

</summary>

method: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20robotsTxtAiRules%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20method">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20robotsTxtAiRules%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20url">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20robotsTxtAiRules%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20headers">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20robotsTxtAiRules%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request">Link to this property</a>

<details>

<summary>

response: optional object {status, statusText, bodyPreview, 3 more }

</summary>

status: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20robotsTxtAiRules%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20status">Link to this property</a>

statusText: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20robotsTxtAiRules%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20statusText">Link to this property</a>

bodyPreview: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20robotsTxtAiRules%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodyPreview">Link to this property</a>

bodySize: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20robotsTxtAiRules%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodySize">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20robotsTxtAiRules%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20headers">Link to this property</a>

redirectedTo: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20robotsTxtAiRules%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20redirectedTo">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20robotsTxtAiRules%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20robotsTxtAiRules%20%3E%20(property)%20evidence">Link to this property</a>

message: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20robotsTxtAiRules%20%3E%20(property)%20message">Link to this property</a>

<details>

<summary>

messageRef: optional object {code, params }

</summary>

code: string

Stable, translatable message code.

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20robotsTxtAiRules%20%3E%20(property)%20messageRef%20%3E%20(property)%20code">Link to this property</a>

params: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20robotsTxtAiRules%20%3E%20(property)%20messageRef%20%3E%20(property)%20params">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20robotsTxtAiRules%20%3E%20(property)%20messageRef">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20robotsTxtAiRules">Link to this property</a>

<details>

<summary>

webBotAuth: object {status, details, durationMs, 3 more }

</summary>

status: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20webBotAuth%20%3E%20(property)%20status">Link to this property</a>

details: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20webBotAuth%20%3E%20(property)%20details">Link to this property</a>

durationMs: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20webBotAuth%20%3E%20(property)%20durationMs">Link to this property</a>

<details>

<summary>

evidence: optional array of object {action, label, finding, 2 more }

</summary>

action: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20webBotAuth%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20action">Link to this property</a>

label: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20webBotAuth%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

finding: optional object {outcome, summary }

</summary>

outcome: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20webBotAuth%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20outcome">Link to this property</a>

summary: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20webBotAuth%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20summary">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20webBotAuth%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding">Link to this property</a>

<details>

<summary>

request: optional object {method, url, headers }

</summary>

method: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20webBotAuth%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20method">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20webBotAuth%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20url">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20webBotAuth%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20headers">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20webBotAuth%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request">Link to this property</a>

<details>

<summary>

response: optional object {status, statusText, bodyPreview, 3 more }

</summary>

status: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20webBotAuth%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20status">Link to this property</a>

statusText: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20webBotAuth%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20statusText">Link to this property</a>

bodyPreview: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20webBotAuth%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodyPreview">Link to this property</a>

bodySize: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20webBotAuth%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodySize">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20webBotAuth%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20headers">Link to this property</a>

redirectedTo: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20webBotAuth%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20redirectedTo">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20webBotAuth%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20webBotAuth%20%3E%20(property)%20evidence">Link to this property</a>

message: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20webBotAuth%20%3E%20(property)%20message">Link to this property</a>

<details>

<summary>

messageRef: optional object {code, params }

</summary>

code: string

Stable, translatable message code.

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20webBotAuth%20%3E%20(property)%20messageRef%20%3E%20(property)%20code">Link to this property</a>

params: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20webBotAuth%20%3E%20(property)%20messageRef%20%3E%20(property)%20params">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20webBotAuth%20%3E%20(property)%20messageRef">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl%20%3E%20(property)%20webBotAuth">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20botAccessControl">Link to this property</a>

<details>

<summary>

commerce: object {acp, ap2, mpp, 2 more }

</summary>

<details>

<summary>

acp: object {status, details, durationMs, 3 more }

</summary>

status: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20acp%20%3E%20(property)%20status">Link to this property</a>

details: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20acp%20%3E%20(property)%20details">Link to this property</a>

durationMs: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20acp%20%3E%20(property)%20durationMs">Link to this property</a>

<details>

<summary>

evidence: optional array of object {action, label, finding, 2 more }

</summary>

action: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20acp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20action">Link to this property</a>

label: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20acp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

finding: optional object {outcome, summary }

</summary>

outcome: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20acp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20outcome">Link to this property</a>

summary: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20acp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20summary">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20acp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding">Link to this property</a>

<details>

<summary>

request: optional object {method, url, headers }

</summary>

method: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20acp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20method">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20acp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20url">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20acp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20headers">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20acp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request">Link to this property</a>

<details>

<summary>

response: optional object {status, statusText, bodyPreview, 3 more }

</summary>

status: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20acp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20status">Link to this property</a>

statusText: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20acp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20statusText">Link to this property</a>

bodyPreview: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20acp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodyPreview">Link to this property</a>

bodySize: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20acp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodySize">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20acp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20headers">Link to this property</a>

redirectedTo: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20acp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20redirectedTo">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20acp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20acp%20%3E%20(property)%20evidence">Link to this property</a>

message: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20acp%20%3E%20(property)%20message">Link to this property</a>

<details>

<summary>

messageRef: optional object {code, params }

</summary>

code: string

Stable, translatable message code.

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20acp%20%3E%20(property)%20messageRef%20%3E%20(property)%20code">Link to this property</a>

params: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20acp%20%3E%20(property)%20messageRef%20%3E%20(property)%20params">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20acp%20%3E%20(property)%20messageRef">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20acp">Link to this property</a>

<details>

<summary>

ap2: object {status, details, durationMs, 3 more }

</summary>

status: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ap2%20%3E%20(property)%20status">Link to this property</a>

details: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ap2%20%3E%20(property)%20details">Link to this property</a>

durationMs: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ap2%20%3E%20(property)%20durationMs">Link to this property</a>

<details>

<summary>

evidence: optional array of object {action, label, finding, 2 more }

</summary>

action: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ap2%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20action">Link to this property</a>

label: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ap2%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

finding: optional object {outcome, summary }

</summary>

outcome: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ap2%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20outcome">Link to this property</a>

summary: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ap2%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20summary">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ap2%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding">Link to this property</a>

<details>

<summary>

request: optional object {method, url, headers }

</summary>

method: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ap2%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20method">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ap2%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20url">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ap2%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20headers">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ap2%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request">Link to this property</a>

<details>

<summary>

response: optional object {status, statusText, bodyPreview, 3 more }

</summary>

status: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ap2%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20status">Link to this property</a>

statusText: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ap2%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20statusText">Link to this property</a>

bodyPreview: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ap2%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodyPreview">Link to this property</a>

bodySize: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ap2%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodySize">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ap2%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20headers">Link to this property</a>

redirectedTo: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ap2%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20redirectedTo">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ap2%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ap2%20%3E%20(property)%20evidence">Link to this property</a>

message: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ap2%20%3E%20(property)%20message">Link to this property</a>

<details>

<summary>

messageRef: optional object {code, params }

</summary>

code: string

Stable, translatable message code.

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ap2%20%3E%20(property)%20messageRef%20%3E%20(property)%20code">Link to this property</a>

params: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ap2%20%3E%20(property)%20messageRef%20%3E%20(property)%20params">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ap2%20%3E%20(property)%20messageRef">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ap2">Link to this property</a>

<details>

<summary>

mpp: object {status, details, durationMs, 3 more }

</summary>

status: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20mpp%20%3E%20(property)%20status">Link to this property</a>

details: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20mpp%20%3E%20(property)%20details">Link to this property</a>

durationMs: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20mpp%20%3E%20(property)%20durationMs">Link to this property</a>

<details>

<summary>

evidence: optional array of object {action, label, finding, 2 more }

</summary>

action: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20mpp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20action">Link to this property</a>

label: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20mpp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

finding: optional object {outcome, summary }

</summary>

outcome: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20mpp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20outcome">Link to this property</a>

summary: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20mpp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20summary">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20mpp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding">Link to this property</a>

<details>

<summary>

request: optional object {method, url, headers }

</summary>

method: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20mpp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20method">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20mpp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20url">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20mpp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20headers">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20mpp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request">Link to this property</a>

<details>

<summary>

response: optional object {status, statusText, bodyPreview, 3 more }

</summary>

status: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20mpp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20status">Link to this property</a>

statusText: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20mpp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20statusText">Link to this property</a>

bodyPreview: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20mpp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodyPreview">Link to this property</a>

bodySize: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20mpp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodySize">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20mpp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20headers">Link to this property</a>

redirectedTo: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20mpp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20redirectedTo">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20mpp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20mpp%20%3E%20(property)%20evidence">Link to this property</a>

message: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20mpp%20%3E%20(property)%20message">Link to this property</a>

<details>

<summary>

messageRef: optional object {code, params }

</summary>

code: string

Stable, translatable message code.

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20mpp%20%3E%20(property)%20messageRef%20%3E%20(property)%20code">Link to this property</a>

params: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20mpp%20%3E%20(property)%20messageRef%20%3E%20(property)%20params">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20mpp%20%3E%20(property)%20messageRef">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20mpp">Link to this property</a>

<details>

<summary>

ucp: object {status, details, durationMs, 3 more }

</summary>

status: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ucp%20%3E%20(property)%20status">Link to this property</a>

details: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ucp%20%3E%20(property)%20details">Link to this property</a>

durationMs: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ucp%20%3E%20(property)%20durationMs">Link to this property</a>

<details>

<summary>

evidence: optional array of object {action, label, finding, 2 more }

</summary>

action: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ucp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20action">Link to this property</a>

label: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ucp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

finding: optional object {outcome, summary }

</summary>

outcome: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ucp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20outcome">Link to this property</a>

summary: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ucp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20summary">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ucp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding">Link to this property</a>

<details>

<summary>

request: optional object {method, url, headers }

</summary>

method: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ucp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20method">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ucp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20url">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ucp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20headers">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ucp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request">Link to this property</a>

<details>

<summary>

response: optional object {status, statusText, bodyPreview, 3 more }

</summary>

status: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ucp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20status">Link to this property</a>

statusText: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ucp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20statusText">Link to this property</a>

bodyPreview: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ucp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodyPreview">Link to this property</a>

bodySize: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ucp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodySize">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ucp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20headers">Link to this property</a>

redirectedTo: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ucp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20redirectedTo">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ucp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ucp%20%3E%20(property)%20evidence">Link to this property</a>

message: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ucp%20%3E%20(property)%20message">Link to this property</a>

<details>

<summary>

messageRef: optional object {code, params }

</summary>

code: string

Stable, translatable message code.

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ucp%20%3E%20(property)%20messageRef%20%3E%20(property)%20code">Link to this property</a>

params: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ucp%20%3E%20(property)%20messageRef%20%3E%20(property)%20params">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ucp%20%3E%20(property)%20messageRef">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20ucp">Link to this property</a>

<details>

<summary>

x402: object {status, details, durationMs, 3 more }

</summary>

status: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20x402%20%3E%20(property)%20status">Link to this property</a>

details: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20x402%20%3E%20(property)%20details">Link to this property</a>

durationMs: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20x402%20%3E%20(property)%20durationMs">Link to this property</a>

<details>

<summary>

evidence: optional array of object {action, label, finding, 2 more }

</summary>

action: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20x402%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20action">Link to this property</a>

label: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20x402%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

finding: optional object {outcome, summary }

</summary>

outcome: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20x402%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20outcome">Link to this property</a>

summary: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20x402%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20summary">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20x402%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding">Link to this property</a>

<details>

<summary>

request: optional object {method, url, headers }

</summary>

method: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20x402%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20method">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20x402%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20url">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20x402%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20headers">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20x402%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request">Link to this property</a>

<details>

<summary>

response: optional object {status, statusText, bodyPreview, 3 more }

</summary>

status: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20x402%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20status">Link to this property</a>

statusText: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20x402%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20statusText">Link to this property</a>

bodyPreview: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20x402%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodyPreview">Link to this property</a>

bodySize: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20x402%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodySize">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20x402%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20headers">Link to this property</a>

redirectedTo: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20x402%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20redirectedTo">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20x402%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20x402%20%3E%20(property)%20evidence">Link to this property</a>

message: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20x402%20%3E%20(property)%20message">Link to this property</a>

<details>

<summary>

messageRef: optional object {code, params }

</summary>

code: string

Stable, translatable message code.

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20x402%20%3E%20(property)%20messageRef%20%3E%20(property)%20code">Link to this property</a>

params: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20x402%20%3E%20(property)%20messageRef%20%3E%20(property)%20params">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20x402%20%3E%20(property)%20messageRef">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce%20%3E%20(property)%20x402">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20commerce">Link to this property</a>

<details>

<summary>

contentAccessibility: object {markdownNegotiation }

</summary>

<details>

<summary>

markdownNegotiation: object {status, details, durationMs, 3 more }

</summary>

status: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20contentAccessibility%20%3E%20(property)%20markdownNegotiation%20%3E%20(property)%20status">Link to this property</a>

details: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20contentAccessibility%20%3E%20(property)%20markdownNegotiation%20%3E%20(property)%20details">Link to this property</a>

durationMs: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20contentAccessibility%20%3E%20(property)%20markdownNegotiation%20%3E%20(property)%20durationMs">Link to this property</a>

<details>

<summary>

evidence: optional array of object {action, label, finding, 2 more }

</summary>

action: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20contentAccessibility%20%3E%20(property)%20markdownNegotiation%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20action">Link to this property</a>

label: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20contentAccessibility%20%3E%20(property)%20markdownNegotiation%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

finding: optional object {outcome, summary }

</summary>

outcome: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20contentAccessibility%20%3E%20(property)%20markdownNegotiation%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20outcome">Link to this property</a>

summary: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20contentAccessibility%20%3E%20(property)%20markdownNegotiation%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20summary">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20contentAccessibility%20%3E%20(property)%20markdownNegotiation%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding">Link to this property</a>

<details>

<summary>

request: optional object {method, url, headers }

</summary>

method: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20contentAccessibility%20%3E%20(property)%20markdownNegotiation%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20method">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20contentAccessibility%20%3E%20(property)%20markdownNegotiation%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20url">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20contentAccessibility%20%3E%20(property)%20markdownNegotiation%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20headers">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20contentAccessibility%20%3E%20(property)%20markdownNegotiation%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request">Link to this property</a>

<details>

<summary>

response: optional object {status, statusText, bodyPreview, 3 more }

</summary>

status: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20contentAccessibility%20%3E%20(property)%20markdownNegotiation%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20status">Link to this property</a>

statusText: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20contentAccessibility%20%3E%20(property)%20markdownNegotiation%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20statusText">Link to this property</a>

bodyPreview: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20contentAccessibility%20%3E%20(property)%20markdownNegotiation%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodyPreview">Link to this property</a>

bodySize: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20contentAccessibility%20%3E%20(property)%20markdownNegotiation%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodySize">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20contentAccessibility%20%3E%20(property)%20markdownNegotiation%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20headers">Link to this property</a>

redirectedTo: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20contentAccessibility%20%3E%20(property)%20markdownNegotiation%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20redirectedTo">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20contentAccessibility%20%3E%20(property)%20markdownNegotiation%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20contentAccessibility%20%3E%20(property)%20markdownNegotiation%20%3E%20(property)%20evidence">Link to this property</a>

message: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20contentAccessibility%20%3E%20(property)%20markdownNegotiation%20%3E%20(property)%20message">Link to this property</a>

<details>

<summary>

messageRef: optional object {code, params }

</summary>

code: string

Stable, translatable message code.

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20contentAccessibility%20%3E%20(property)%20markdownNegotiation%20%3E%20(property)%20messageRef%20%3E%20(property)%20code">Link to this property</a>

params: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20contentAccessibility%20%3E%20(property)%20markdownNegotiation%20%3E%20(property)%20messageRef%20%3E%20(property)%20params">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20contentAccessibility%20%3E%20(property)%20markdownNegotiation%20%3E%20(property)%20messageRef">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20contentAccessibility%20%3E%20(property)%20markdownNegotiation">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20contentAccessibility">Link to this property</a>

<details>

<summary>

discoverability: object {dnsAid, linkHeaders, robotsTxt, sitemap }

</summary>

<details>

<summary>

dnsAid: object {status, details, durationMs, 3 more }

</summary>

status: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20dnsAid%20%3E%20(property)%20status">Link to this property</a>

details: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20dnsAid%20%3E%20(property)%20details">Link to this property</a>

durationMs: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20dnsAid%20%3E%20(property)%20durationMs">Link to this property</a>

<details>

<summary>

evidence: optional array of object {action, label, finding, 2 more }

</summary>

action: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20dnsAid%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20action">Link to this property</a>

label: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20dnsAid%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

finding: optional object {outcome, summary }

</summary>

outcome: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20dnsAid%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20outcome">Link to this property</a>

summary: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20dnsAid%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20summary">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20dnsAid%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding">Link to this property</a>

<details>

<summary>

request: optional object {method, url, headers }

</summary>

method: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20dnsAid%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20method">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20dnsAid%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20url">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20dnsAid%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20headers">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20dnsAid%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request">Link to this property</a>

<details>

<summary>

response: optional object {status, statusText, bodyPreview, 3 more }

</summary>

status: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20dnsAid%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20status">Link to this property</a>

statusText: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20dnsAid%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20statusText">Link to this property</a>

bodyPreview: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20dnsAid%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodyPreview">Link to this property</a>

bodySize: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20dnsAid%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodySize">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20dnsAid%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20headers">Link to this property</a>

redirectedTo: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20dnsAid%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20redirectedTo">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20dnsAid%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20dnsAid%20%3E%20(property)%20evidence">Link to this property</a>

message: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20dnsAid%20%3E%20(property)%20message">Link to this property</a>

<details>

<summary>

messageRef: optional object {code, params }

</summary>

code: string

Stable, translatable message code.

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20dnsAid%20%3E%20(property)%20messageRef%20%3E%20(property)%20code">Link to this property</a>

params: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20dnsAid%20%3E%20(property)%20messageRef%20%3E%20(property)%20params">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20dnsAid%20%3E%20(property)%20messageRef">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20dnsAid">Link to this property</a>

<details>

<summary>

linkHeaders: object {status, details, durationMs, 3 more }

</summary>

status: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20linkHeaders%20%3E%20(property)%20status">Link to this property</a>

details: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20linkHeaders%20%3E%20(property)%20details">Link to this property</a>

durationMs: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20linkHeaders%20%3E%20(property)%20durationMs">Link to this property</a>

<details>

<summary>

evidence: optional array of object {action, label, finding, 2 more }

</summary>

action: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20linkHeaders%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20action">Link to this property</a>

label: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20linkHeaders%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

finding: optional object {outcome, summary }

</summary>

outcome: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20linkHeaders%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20outcome">Link to this property</a>

summary: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20linkHeaders%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20summary">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20linkHeaders%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding">Link to this property</a>

<details>

<summary>

request: optional object {method, url, headers }

</summary>

method: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20linkHeaders%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20method">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20linkHeaders%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20url">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20linkHeaders%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20headers">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20linkHeaders%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request">Link to this property</a>

<details>

<summary>

response: optional object {status, statusText, bodyPreview, 3 more }

</summary>

status: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20linkHeaders%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20status">Link to this property</a>

statusText: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20linkHeaders%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20statusText">Link to this property</a>

bodyPreview: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20linkHeaders%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodyPreview">Link to this property</a>

bodySize: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20linkHeaders%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodySize">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20linkHeaders%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20headers">Link to this property</a>

redirectedTo: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20linkHeaders%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20redirectedTo">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20linkHeaders%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20linkHeaders%20%3E%20(property)%20evidence">Link to this property</a>

message: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20linkHeaders%20%3E%20(property)%20message">Link to this property</a>

<details>

<summary>

messageRef: optional object {code, params }

</summary>

code: string

Stable, translatable message code.

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20linkHeaders%20%3E%20(property)%20messageRef%20%3E%20(property)%20code">Link to this property</a>

params: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20linkHeaders%20%3E%20(property)%20messageRef%20%3E%20(property)%20params">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20linkHeaders%20%3E%20(property)%20messageRef">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20linkHeaders">Link to this property</a>

<details>

<summary>

robotsTxt: object {status, details, durationMs, 3 more }

</summary>

status: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20status">Link to this property</a>

details: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20details">Link to this property</a>

durationMs: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20durationMs">Link to this property</a>

<details>

<summary>

evidence: optional array of object {action, label, finding, 2 more }

</summary>

action: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20action">Link to this property</a>

label: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

finding: optional object {outcome, summary }

</summary>

outcome: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20outcome">Link to this property</a>

summary: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20summary">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding">Link to this property</a>

<details>

<summary>

request: optional object {method, url, headers }

</summary>

method: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20method">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20url">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20headers">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request">Link to this property</a>

<details>

<summary>

response: optional object {status, statusText, bodyPreview, 3 more }

</summary>

status: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20status">Link to this property</a>

statusText: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20statusText">Link to this property</a>

bodyPreview: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodyPreview">Link to this property</a>

bodySize: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodySize">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20headers">Link to this property</a>

redirectedTo: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20redirectedTo">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20evidence">Link to this property</a>

message: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20message">Link to this property</a>

<details>

<summary>

messageRef: optional object {code, params }

</summary>

code: string

Stable, translatable message code.

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20messageRef%20%3E%20(property)%20code">Link to this property</a>

params: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20messageRef%20%3E%20(property)%20params">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20messageRef">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20robotsTxt">Link to this property</a>

<details>

<summary>

sitemap: object {status, details, durationMs, 3 more }

</summary>

status: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20sitemap%20%3E%20(property)%20status">Link to this property</a>

details: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20sitemap%20%3E%20(property)%20details">Link to this property</a>

durationMs: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20sitemap%20%3E%20(property)%20durationMs">Link to this property</a>

<details>

<summary>

evidence: optional array of object {action, label, finding, 2 more }

</summary>

action: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20sitemap%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20action">Link to this property</a>

label: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20sitemap%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

finding: optional object {outcome, summary }

</summary>

outcome: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20sitemap%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20outcome">Link to this property</a>

summary: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20sitemap%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20summary">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20sitemap%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding">Link to this property</a>

<details>

<summary>

request: optional object {method, url, headers }

</summary>

method: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20sitemap%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20method">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20sitemap%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20url">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20sitemap%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20headers">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20sitemap%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request">Link to this property</a>

<details>

<summary>

response: optional object {status, statusText, bodyPreview, 3 more }

</summary>

status: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20sitemap%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20status">Link to this property</a>

statusText: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20sitemap%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20statusText">Link to this property</a>

bodyPreview: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20sitemap%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodyPreview">Link to this property</a>

bodySize: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20sitemap%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodySize">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20sitemap%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20headers">Link to this property</a>

redirectedTo: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20sitemap%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20redirectedTo">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20sitemap%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20sitemap%20%3E%20(property)%20evidence">Link to this property</a>

message: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20sitemap%20%3E%20(property)%20message">Link to this property</a>

<details>

<summary>

messageRef: optional object {code, params }

</summary>

code: string

Stable, translatable message code.

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20sitemap%20%3E%20(property)%20messageRef%20%3E%20(property)%20code">Link to this property</a>

params: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20sitemap%20%3E%20(property)%20messageRef%20%3E%20(property)%20params">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20sitemap%20%3E%20(property)%20messageRef">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability%20%3E%20(property)%20sitemap">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discoverability">Link to this property</a>

<details>

<summary>

discovery: object {a2aAgentCard, agentSkills, apiCatalog, 6 more }

</summary>

<details>

<summary>

a2aAgentCard: object {status, details, durationMs, 3 more }

</summary>

status: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20a2aAgentCard%20%3E%20(property)%20status">Link to this property</a>

details: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20a2aAgentCard%20%3E%20(property)%20details">Link to this property</a>

durationMs: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20a2aAgentCard%20%3E%20(property)%20durationMs">Link to this property</a>

<details>

<summary>

evidence: optional array of object {action, label, finding, 2 more }

</summary>

action: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20a2aAgentCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20action">Link to this property</a>

label: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20a2aAgentCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

finding: optional object {outcome, summary }

</summary>

outcome: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20a2aAgentCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20outcome">Link to this property</a>

summary: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20a2aAgentCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20summary">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20a2aAgentCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding">Link to this property</a>

<details>

<summary>

request: optional object {method, url, headers }

</summary>

method: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20a2aAgentCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20method">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20a2aAgentCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20url">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20a2aAgentCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20headers">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20a2aAgentCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request">Link to this property</a>

<details>

<summary>

response: optional object {status, statusText, bodyPreview, 3 more }

</summary>

status: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20a2aAgentCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20status">Link to this property</a>

statusText: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20a2aAgentCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20statusText">Link to this property</a>

bodyPreview: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20a2aAgentCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodyPreview">Link to this property</a>

bodySize: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20a2aAgentCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodySize">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20a2aAgentCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20headers">Link to this property</a>

redirectedTo: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20a2aAgentCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20redirectedTo">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20a2aAgentCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20a2aAgentCard%20%3E%20(property)%20evidence">Link to this property</a>

message: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20a2aAgentCard%20%3E%20(property)%20message">Link to this property</a>

<details>

<summary>

messageRef: optional object {code, params }

</summary>

code: string

Stable, translatable message code.

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20a2aAgentCard%20%3E%20(property)%20messageRef%20%3E%20(property)%20code">Link to this property</a>

params: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20a2aAgentCard%20%3E%20(property)%20messageRef%20%3E%20(property)%20params">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20a2aAgentCard%20%3E%20(property)%20messageRef">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20a2aAgentCard">Link to this property</a>

<details>

<summary>

agentSkills: object {status, details, durationMs, 3 more }

</summary>

status: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20agentSkills%20%3E%20(property)%20status">Link to this property</a>

details: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20agentSkills%20%3E%20(property)%20details">Link to this property</a>

durationMs: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20agentSkills%20%3E%20(property)%20durationMs">Link to this property</a>

<details>

<summary>

evidence: optional array of object {action, label, finding, 2 more }

</summary>

action: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20agentSkills%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20action">Link to this property</a>

label: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20agentSkills%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

finding: optional object {outcome, summary }

</summary>

outcome: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20agentSkills%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20outcome">Link to this property</a>

summary: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20agentSkills%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20summary">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20agentSkills%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding">Link to this property</a>

<details>

<summary>

request: optional object {method, url, headers }

</summary>

method: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20agentSkills%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20method">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20agentSkills%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20url">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20agentSkills%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20headers">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20agentSkills%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request">Link to this property</a>

<details>

<summary>

response: optional object {status, statusText, bodyPreview, 3 more }

</summary>

status: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20agentSkills%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20status">Link to this property</a>

statusText: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20agentSkills%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20statusText">Link to this property</a>

bodyPreview: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20agentSkills%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodyPreview">Link to this property</a>

bodySize: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20agentSkills%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodySize">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20agentSkills%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20headers">Link to this property</a>

redirectedTo: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20agentSkills%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20redirectedTo">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20agentSkills%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20agentSkills%20%3E%20(property)%20evidence">Link to this property</a>

message: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20agentSkills%20%3E%20(property)%20message">Link to this property</a>

<details>

<summary>

messageRef: optional object {code, params }

</summary>

code: string

Stable, translatable message code.

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20agentSkills%20%3E%20(property)%20messageRef%20%3E%20(property)%20code">Link to this property</a>

params: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20agentSkills%20%3E%20(property)%20messageRef%20%3E%20(property)%20params">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20agentSkills%20%3E%20(property)%20messageRef">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20agentSkills">Link to this property</a>

<details>

<summary>

apiCatalog: object {status, details, durationMs, 3 more }

</summary>

status: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20apiCatalog%20%3E%20(property)%20status">Link to this property</a>

details: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20apiCatalog%20%3E%20(property)%20details">Link to this property</a>

durationMs: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20apiCatalog%20%3E%20(property)%20durationMs">Link to this property</a>

<details>

<summary>

evidence: optional array of object {action, label, finding, 2 more }

</summary>

action: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20apiCatalog%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20action">Link to this property</a>

label: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20apiCatalog%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

finding: optional object {outcome, summary }

</summary>

outcome: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20apiCatalog%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20outcome">Link to this property</a>

summary: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20apiCatalog%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20summary">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20apiCatalog%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding">Link to this property</a>

<details>

<summary>

request: optional object {method, url, headers }

</summary>

method: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20apiCatalog%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20method">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20apiCatalog%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20url">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20apiCatalog%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20headers">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20apiCatalog%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request">Link to this property</a>

<details>

<summary>

response: optional object {status, statusText, bodyPreview, 3 more }

</summary>

status: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20apiCatalog%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20status">Link to this property</a>

statusText: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20apiCatalog%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20statusText">Link to this property</a>

bodyPreview: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20apiCatalog%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodyPreview">Link to this property</a>

bodySize: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20apiCatalog%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodySize">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20apiCatalog%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20headers">Link to this property</a>

redirectedTo: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20apiCatalog%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20redirectedTo">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20apiCatalog%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20apiCatalog%20%3E%20(property)%20evidence">Link to this property</a>

message: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20apiCatalog%20%3E%20(property)%20message">Link to this property</a>

<details>

<summary>

messageRef: optional object {code, params }

</summary>

code: string

Stable, translatable message code.

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20apiCatalog%20%3E%20(property)%20messageRef%20%3E%20(property)%20code">Link to this property</a>

params: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20apiCatalog%20%3E%20(property)%20messageRef%20%3E%20(property)%20params">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20apiCatalog%20%3E%20(property)%20messageRef">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20apiCatalog">Link to this property</a>

<details>

<summary>

ard: object {status, details, durationMs, 3 more }

</summary>

status: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20ard%20%3E%20(property)%20status">Link to this property</a>

details: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20ard%20%3E%20(property)%20details">Link to this property</a>

durationMs: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20ard%20%3E%20(property)%20durationMs">Link to this property</a>

<details>

<summary>

evidence: optional array of object {action, label, finding, 2 more }

</summary>

action: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20ard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20action">Link to this property</a>

label: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20ard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

finding: optional object {outcome, summary }

</summary>

outcome: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20ard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20outcome">Link to this property</a>

summary: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20ard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20summary">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20ard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding">Link to this property</a>

<details>

<summary>

request: optional object {method, url, headers }

</summary>

method: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20ard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20method">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20ard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20url">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20ard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20headers">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20ard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request">Link to this property</a>

<details>

<summary>

response: optional object {status, statusText, bodyPreview, 3 more }

</summary>

status: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20ard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20status">Link to this property</a>

statusText: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20ard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20statusText">Link to this property</a>

bodyPreview: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20ard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodyPreview">Link to this property</a>

bodySize: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20ard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodySize">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20ard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20headers">Link to this property</a>

redirectedTo: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20ard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20redirectedTo">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20ard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20ard%20%3E%20(property)%20evidence">Link to this property</a>

message: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20ard%20%3E%20(property)%20message">Link to this property</a>

<details>

<summary>

messageRef: optional object {code, params }

</summary>

code: string

Stable, translatable message code.

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20ard%20%3E%20(property)%20messageRef%20%3E%20(property)%20code">Link to this property</a>

params: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20ard%20%3E%20(property)%20messageRef%20%3E%20(property)%20params">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20ard%20%3E%20(property)%20messageRef">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20ard">Link to this property</a>

<details>

<summary>

authMd: object {status, details, durationMs, 3 more }

</summary>

status: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20authMd%20%3E%20(property)%20status">Link to this property</a>

details: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20authMd%20%3E%20(property)%20details">Link to this property</a>

durationMs: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20authMd%20%3E%20(property)%20durationMs">Link to this property</a>

<details>

<summary>

evidence: optional array of object {action, label, finding, 2 more }

</summary>

action: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20authMd%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20action">Link to this property</a>

label: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20authMd%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

finding: optional object {outcome, summary }

</summary>

outcome: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20authMd%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20outcome">Link to this property</a>

summary: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20authMd%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20summary">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20authMd%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding">Link to this property</a>

<details>

<summary>

request: optional object {method, url, headers }

</summary>

method: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20authMd%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20method">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20authMd%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20url">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20authMd%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20headers">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20authMd%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request">Link to this property</a>

<details>

<summary>

response: optional object {status, statusText, bodyPreview, 3 more }

</summary>

status: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20authMd%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20status">Link to this property</a>

statusText: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20authMd%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20statusText">Link to this property</a>

bodyPreview: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20authMd%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodyPreview">Link to this property</a>

bodySize: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20authMd%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodySize">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20authMd%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20headers">Link to this property</a>

redirectedTo: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20authMd%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20redirectedTo">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20authMd%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20authMd%20%3E%20(property)%20evidence">Link to this property</a>

message: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20authMd%20%3E%20(property)%20message">Link to this property</a>

<details>

<summary>

messageRef: optional object {code, params }

</summary>

code: string

Stable, translatable message code.

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20authMd%20%3E%20(property)%20messageRef%20%3E%20(property)%20code">Link to this property</a>

params: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20authMd%20%3E%20(property)%20messageRef%20%3E%20(property)%20params">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20authMd%20%3E%20(property)%20messageRef">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20authMd">Link to this property</a>

<details>

<summary>

mcpServerCard: object {status, details, durationMs, 3 more }

</summary>

status: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20mcpServerCard%20%3E%20(property)%20status">Link to this property</a>

details: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20mcpServerCard%20%3E%20(property)%20details">Link to this property</a>

durationMs: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20mcpServerCard%20%3E%20(property)%20durationMs">Link to this property</a>

<details>

<summary>

evidence: optional array of object {action, label, finding, 2 more }

</summary>

action: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20mcpServerCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20action">Link to this property</a>

label: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20mcpServerCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

finding: optional object {outcome, summary }

</summary>

outcome: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20mcpServerCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20outcome">Link to this property</a>

summary: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20mcpServerCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20summary">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20mcpServerCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding">Link to this property</a>

<details>

<summary>

request: optional object {method, url, headers }

</summary>

method: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20mcpServerCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20method">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20mcpServerCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20url">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20mcpServerCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20headers">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20mcpServerCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request">Link to this property</a>

<details>

<summary>

response: optional object {status, statusText, bodyPreview, 3 more }

</summary>

status: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20mcpServerCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20status">Link to this property</a>

statusText: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20mcpServerCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20statusText">Link to this property</a>

bodyPreview: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20mcpServerCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodyPreview">Link to this property</a>

bodySize: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20mcpServerCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodySize">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20mcpServerCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20headers">Link to this property</a>

redirectedTo: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20mcpServerCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20redirectedTo">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20mcpServerCard%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20mcpServerCard%20%3E%20(property)%20evidence">Link to this property</a>

message: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20mcpServerCard%20%3E%20(property)%20message">Link to this property</a>

<details>

<summary>

messageRef: optional object {code, params }

</summary>

code: string

Stable, translatable message code.

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20mcpServerCard%20%3E%20(property)%20messageRef%20%3E%20(property)%20code">Link to this property</a>

params: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20mcpServerCard%20%3E%20(property)%20messageRef%20%3E%20(property)%20params">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20mcpServerCard%20%3E%20(property)%20messageRef">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20mcpServerCard">Link to this property</a>

<details>

<summary>

oauthDiscovery: object {status, details, durationMs, 3 more }

</summary>

status: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthDiscovery%20%3E%20(property)%20status">Link to this property</a>

details: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthDiscovery%20%3E%20(property)%20details">Link to this property</a>

durationMs: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthDiscovery%20%3E%20(property)%20durationMs">Link to this property</a>

<details>

<summary>

evidence: optional array of object {action, label, finding, 2 more }

</summary>

action: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthDiscovery%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20action">Link to this property</a>

label: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthDiscovery%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

finding: optional object {outcome, summary }

</summary>

outcome: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthDiscovery%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20outcome">Link to this property</a>

summary: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthDiscovery%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20summary">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthDiscovery%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding">Link to this property</a>

<details>

<summary>

request: optional object {method, url, headers }

</summary>

method: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthDiscovery%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20method">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthDiscovery%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20url">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthDiscovery%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20headers">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthDiscovery%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request">Link to this property</a>

<details>

<summary>

response: optional object {status, statusText, bodyPreview, 3 more }

</summary>

status: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthDiscovery%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20status">Link to this property</a>

statusText: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthDiscovery%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20statusText">Link to this property</a>

bodyPreview: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthDiscovery%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodyPreview">Link to this property</a>

bodySize: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthDiscovery%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodySize">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthDiscovery%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20headers">Link to this property</a>

redirectedTo: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthDiscovery%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20redirectedTo">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthDiscovery%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthDiscovery%20%3E%20(property)%20evidence">Link to this property</a>

message: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthDiscovery%20%3E%20(property)%20message">Link to this property</a>

<details>

<summary>

messageRef: optional object {code, params }

</summary>

code: string

Stable, translatable message code.

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthDiscovery%20%3E%20(property)%20messageRef%20%3E%20(property)%20code">Link to this property</a>

params: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthDiscovery%20%3E%20(property)%20messageRef%20%3E%20(property)%20params">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthDiscovery%20%3E%20(property)%20messageRef">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthDiscovery">Link to this property</a>

<details>

<summary>

oauthProtectedResource: object {status, details, durationMs, 3 more }

</summary>

status: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthProtectedResource%20%3E%20(property)%20status">Link to this property</a>

details: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthProtectedResource%20%3E%20(property)%20details">Link to this property</a>

durationMs: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthProtectedResource%20%3E%20(property)%20durationMs">Link to this property</a>

<details>

<summary>

evidence: optional array of object {action, label, finding, 2 more }

</summary>

action: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthProtectedResource%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20action">Link to this property</a>

label: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthProtectedResource%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

finding: optional object {outcome, summary }

</summary>

outcome: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthProtectedResource%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20outcome">Link to this property</a>

summary: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthProtectedResource%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20summary">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthProtectedResource%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding">Link to this property</a>

<details>

<summary>

request: optional object {method, url, headers }

</summary>

method: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthProtectedResource%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20method">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthProtectedResource%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20url">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthProtectedResource%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20headers">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthProtectedResource%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request">Link to this property</a>

<details>

<summary>

response: optional object {status, statusText, bodyPreview, 3 more }

</summary>

status: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthProtectedResource%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20status">Link to this property</a>

statusText: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthProtectedResource%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20statusText">Link to this property</a>

bodyPreview: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthProtectedResource%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodyPreview">Link to this property</a>

bodySize: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthProtectedResource%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodySize">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthProtectedResource%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20headers">Link to this property</a>

redirectedTo: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthProtectedResource%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20redirectedTo">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthProtectedResource%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthProtectedResource%20%3E%20(property)%20evidence">Link to this property</a>

message: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthProtectedResource%20%3E%20(property)%20message">Link to this property</a>

<details>

<summary>

messageRef: optional object {code, params }

</summary>

code: string

Stable, translatable message code.

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthProtectedResource%20%3E%20(property)%20messageRef%20%3E%20(property)%20code">Link to this property</a>

params: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthProtectedResource%20%3E%20(property)%20messageRef%20%3E%20(property)%20params">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthProtectedResource%20%3E%20(property)%20messageRef">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20oauthProtectedResource">Link to this property</a>

<details>

<summary>

webMcp: object {status, details, durationMs, 3 more }

</summary>

status: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20webMcp%20%3E%20(property)%20status">Link to this property</a>

details: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20webMcp%20%3E%20(property)%20details">Link to this property</a>

durationMs: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20webMcp%20%3E%20(property)%20durationMs">Link to this property</a>

<details>

<summary>

evidence: optional array of object {action, label, finding, 2 more }

</summary>

action: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20webMcp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20action">Link to this property</a>

label: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20webMcp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

<details>

<summary>

finding: optional object {outcome, summary }

</summary>

outcome: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20webMcp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20outcome">Link to this property</a>

summary: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20webMcp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding%20%3E%20(property)%20summary">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20webMcp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20finding">Link to this property</a>

<details>

<summary>

request: optional object {method, url, headers }

</summary>

method: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20webMcp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20method">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20webMcp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20url">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20webMcp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20headers">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20webMcp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20request">Link to this property</a>

<details>

<summary>

response: optional object {status, statusText, bodyPreview, 3 more }

</summary>

status: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20webMcp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20status">Link to this property</a>

statusText: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20webMcp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20statusText">Link to this property</a>

bodyPreview: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20webMcp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodyPreview">Link to this property</a>

bodySize: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20webMcp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodySize">Link to this property</a>

headers: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20webMcp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20headers">Link to this property</a>

redirectedTo: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20webMcp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20redirectedTo">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20webMcp%20%3E%20(property)%20evidence%20%3E%20(items)%20%3E%20(property)%20response">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20webMcp%20%3E%20(property)%20evidence">Link to this property</a>

message: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20webMcp%20%3E%20(property)%20message">Link to this property</a>

<details>

<summary>

messageRef: optional object {code, params }

</summary>

code: string

Stable, translatable message code.

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20webMcp%20%3E%20(property)%20messageRef%20%3E%20(property)%20code">Link to this property</a>

params: optional unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20webMcp%20%3E%20(property)%20messageRef%20%3E%20(property)%20params">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20webMcp%20%3E%20(property)%20messageRef">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery%20%3E%20(property)%20webMcp">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks%20%3E%20(property)%20discovery">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20checks">Link to this property</a>

level: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20level">Link to this property</a>

levelName: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20levelName">Link to this property</a>

commerceSignals: optional array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20commerceSignals">Link to this property</a>

isCommerce: optional boolean

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20isCommerce">Link to this property</a>

<details>

<summary>

nextLevel: optional object {name, requirements, target }

</summary>

name: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20nextLevel%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

requirements: array of object {check, description, prompt, 2 more }

</summary>

check: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20nextLevel%20%3E%20(property)%20requirements%20%3E%20(items)%20%3E%20(property)%20check">Link to this property</a>

description: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20nextLevel%20%3E%20(property)%20requirements%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

prompt: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20nextLevel%20%3E%20(property)%20requirements%20%3E%20(items)%20%3E%20(property)%20prompt">Link to this property</a>

skillUrl: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20nextLevel%20%3E%20(property)%20requirements%20%3E%20(items)%20%3E%20(property)%20skillUrl">Link to this property</a>

specUrls: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20nextLevel%20%3E%20(property)%20requirements%20%3E%20(items)%20%3E%20(property)%20specUrls">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20nextLevel%20%3E%20(property)%20requirements">Link to this property</a>

target: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20nextLevel%20%3E%20(property)%20target">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness%20%3E%20(property)%20nextLevel">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20agentReadiness">Link to this property</a>

<details>

<summary>

phishing\_v2: optional object {data }

</summary>

data: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20phishing_v2%20%3E%20(property)%20data">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20phishing_v2">Link to this property</a>

<details>

<summary>

robotsTxt: optional object {data }

</summary>

<details>

<summary>

data: array of object {rules, sitemaps, hash }

</summary>

<details>

<summary>

rules: map\[object {allow, disallow, contentSignal, crawlDelay } ]

</summary>

allow: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20allow">Link to this property</a>

disallow: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20disallow">Link to this property</a>

<details>

<summary>

contentSignal: optional object {"ai-input", "ai-train", search }

</summary>

"ai-input": optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20contentSignal%20%3E%20(property)%20ai-input">Link to this property</a>

"ai-train": optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20contentSignal%20%3E%20(property)%20ai-train">Link to this property</a>

search: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20contentSignal%20%3E%20(property)%20search">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20contentSignal">Link to this property</a>

crawlDelay: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20crawlDelay">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20rules">Link to this property</a>

sitemaps: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20sitemaps">Link to this property</a>

hash: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20hash">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20robotsTxt%20%3E%20(property)%20data">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20robotsTxt">Link to this property</a>

<details>

<summary>

urlCategories: optional object {data }

</summary>

<details>

<summary>

data: array of object {content, inherited, name, risks }

</summary>

<details>

<summary>

content: array of object {id, name, super\_category\_id }

</summary>

id: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20urlCategories%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

name: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20urlCategories%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

super\_category\_id: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20urlCategories%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20super_category_id">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20urlCategories%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20content">Link to this property</a>

<details>

<summary>

inherited: object {content, from, risks }

</summary>

<details>

<summary>

content: array of object {id, name, super\_category\_id }

</summary>

id: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20urlCategories%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20inherited%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

name: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20urlCategories%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20inherited%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

super\_category\_id: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20urlCategories%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20inherited%20%3E%20(property)%20content%20%3E%20(items)%20%3E%20(property)%20super_category_id">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20urlCategories%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20inherited%20%3E%20(property)%20content">Link to this property</a>

from: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20urlCategories%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20inherited%20%3E%20(property)%20from">Link to this property</a>

<details>

<summary>

risks: array of object {id, name, super\_category\_id }

</summary>

id: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20urlCategories%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20inherited%20%3E%20(property)%20risks%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

name: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20urlCategories%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20inherited%20%3E%20(property)%20risks%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

super\_category\_id: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20urlCategories%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20inherited%20%3E%20(property)%20risks%20%3E%20(items)%20%3E%20(property)%20super_category_id">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20urlCategories%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20inherited%20%3E%20(property)%20risks">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20urlCategories%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20inherited">Link to this property</a>

name: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20urlCategories%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

risks: array of object {id, name, super\_category\_id }

</summary>

id: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20urlCategories%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20risks%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

name: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20urlCategories%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20risks%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

super\_category\_id: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20urlCategories%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20risks%20%3E%20(items)%20%3E%20(property)%20super_category_id">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20urlCategories%20%3E%20(property)%20data%20%3E%20(items)%20%3E%20(property)%20risks">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20urlCategories%20%3E%20(property)%20data">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors%20%3E%20(property)%20urlCategories">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta%20%3E%20(property)%20processors">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20meta">Link to this property</a>

<details>

<summary>

page: object {apexDomain, asn, asnname, 14 more }

</summary>

apexDomain: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20page%20%3E%20(property)%20apexDomain">Link to this property</a>

asn: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20page%20%3E%20(property)%20asn">Link to this property</a>

asnname: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20page%20%3E%20(property)%20asnname">Link to this property</a>

city: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20page%20%3E%20(property)%20city">Link to this property</a>

country: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20page%20%3E%20(property)%20country">Link to this property</a>

domain: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20page%20%3E%20(property)%20domain">Link to this property</a>

ip: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20page%20%3E%20(property)%20ip">Link to this property</a>

mimeType: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20page%20%3E%20(property)%20mimeType">Link to this property</a>

server: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20page%20%3E%20(property)%20server">Link to this property</a>

status: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20page%20%3E%20(property)%20status">Link to this property</a>

title: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20page%20%3E%20(property)%20title">Link to this property</a>

tlsAgeDays: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20page%20%3E%20(property)%20tlsAgeDays">Link to this property</a>

tlsIssuer: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20page%20%3E%20(property)%20tlsIssuer">Link to this property</a>

tlsValidDays: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20page%20%3E%20(property)%20tlsValidDays">Link to this property</a>

tlsValidFrom: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20page%20%3E%20(property)%20tlsValidFrom">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20page%20%3E%20(property)%20url">Link to this property</a>

<details>

<summary>

screenshot: optional object {dhash, mm3Hash, name, phash }

</summary>

dhash: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20page%20%3E%20(property)%20screenshot%20%3E%20(property)%20dhash">Link to this property</a>

mm3Hash: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20page%20%3E%20(property)%20screenshot%20%3E%20(property)%20mm3Hash">Link to this property</a>

name: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20page%20%3E%20(property)%20screenshot%20%3E%20(property)%20name">Link to this property</a>

phash: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20page%20%3E%20(property)%20screenshot%20%3E%20(property)%20phash">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20page%20%3E%20(property)%20screenshot">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20page">Link to this property</a>

<details>

<summary>

scanner: object {colo, country }

</summary>

colo: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20scanner%20%3E%20(property)%20colo">Link to this property</a>

country: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20scanner%20%3E%20(property)%20country">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20scanner">Link to this property</a>

<details>

<summary>

stats: object {domainStats, ipStats, IPv6Percentage, 10 more }

</summary>

<details>

<summary>

domainStats: array of object {count, countries, domain, 6 more }

</summary>

count: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20domainStats%20%3E%20(items)%20%3E%20(property)%20count">Link to this property</a>

countries: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20domainStats%20%3E%20(items)%20%3E%20(property)%20countries">Link to this property</a>

domain: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20domainStats%20%3E%20(items)%20%3E%20(property)%20domain">Link to this property</a>

encodedSize: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20domainStats%20%3E%20(items)%20%3E%20(property)%20encodedSize">Link to this property</a>

index: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20domainStats%20%3E%20(items)%20%3E%20(property)%20index">Link to this property</a>

initiators: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20domainStats%20%3E%20(items)%20%3E%20(property)%20initiators">Link to this property</a>

ips: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20domainStats%20%3E%20(items)%20%3E%20(property)%20ips">Link to this property</a>

redirects: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20domainStats%20%3E%20(items)%20%3E%20(property)%20redirects">Link to this property</a>

size: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20domainStats%20%3E%20(items)%20%3E%20(property)%20size">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20domainStats">Link to this property</a>

<details>

<summary>

ipStats: array of object {asn, countries, domains, 9 more }

</summary>

<details>

<summary>

asn: object {asn, country, description, 3 more }

</summary>

asn: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20ipStats%20%3E%20(items)%20%3E%20(property)%20asn%20%3E%20(property)%20asn">Link to this property</a>

country: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20ipStats%20%3E%20(items)%20%3E%20(property)%20asn%20%3E%20(property)%20country">Link to this property</a>

description: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20ipStats%20%3E%20(items)%20%3E%20(property)%20asn%20%3E%20(property)%20description">Link to this property</a>

ip: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20ipStats%20%3E%20(items)%20%3E%20(property)%20asn%20%3E%20(property)%20ip">Link to this property</a>

name: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20ipStats%20%3E%20(items)%20%3E%20(property)%20asn%20%3E%20(property)%20name">Link to this property</a>

org: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20ipStats%20%3E%20(items)%20%3E%20(property)%20asn%20%3E%20(property)%20org">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20ipStats%20%3E%20(items)%20%3E%20(property)%20asn">Link to this property</a>

countries: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20ipStats%20%3E%20(items)%20%3E%20(property)%20countries">Link to this property</a>

domains: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20ipStats%20%3E%20(items)%20%3E%20(property)%20domains">Link to this property</a>

encodedSize: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20ipStats%20%3E%20(items)%20%3E%20(property)%20encodedSize">Link to this property</a>

<details>

<summary>

geoip: object {city, country, country\_name, 2 more }

</summary>

city: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20ipStats%20%3E%20(items)%20%3E%20(property)%20geoip%20%3E%20(property)%20city">Link to this property</a>

country: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20ipStats%20%3E%20(items)%20%3E%20(property)%20geoip%20%3E%20(property)%20country">Link to this property</a>

country\_name: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20ipStats%20%3E%20(items)%20%3E%20(property)%20geoip%20%3E%20(property)%20country_name">Link to this property</a>

ll: array of number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20ipStats%20%3E%20(items)%20%3E%20(property)%20geoip%20%3E%20(property)%20ll">Link to this property</a>

region: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20ipStats%20%3E%20(items)%20%3E%20(property)%20geoip%20%3E%20(property)%20region">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20ipStats%20%3E%20(items)%20%3E%20(property)%20geoip">Link to this property</a>

index: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20ipStats%20%3E%20(items)%20%3E%20(property)%20index">Link to this property</a>

ip: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20ipStats%20%3E%20(items)%20%3E%20(property)%20ip">Link to this property</a>

ipv6: boolean

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20ipStats%20%3E%20(items)%20%3E%20(property)%20ipv6">Link to this property</a>

redirects: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20ipStats%20%3E%20(items)%20%3E%20(property)%20redirects">Link to this property</a>

requests: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20ipStats%20%3E%20(items)%20%3E%20(property)%20requests">Link to this property</a>

size: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20ipStats%20%3E%20(items)%20%3E%20(property)%20size">Link to this property</a>

count: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20ipStats%20%3E%20(items)%20%3E%20(property)%20count">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20ipStats">Link to this property</a>

IPv6Percentage: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20IPv6Percentage">Link to this property</a>

malicious: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20malicious">Link to this property</a>

<details>

<summary>

protocolStats: array of object {count, countries, encodedSize, 3 more }

</summary>

count: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20protocolStats%20%3E%20(items)%20%3E%20(property)%20count">Link to this property</a>

countries: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20protocolStats%20%3E%20(items)%20%3E%20(property)%20countries">Link to this property</a>

encodedSize: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20protocolStats%20%3E%20(items)%20%3E%20(property)%20encodedSize">Link to this property</a>

ips: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20protocolStats%20%3E%20(items)%20%3E%20(property)%20ips">Link to this property</a>

protocol: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20protocolStats%20%3E%20(items)%20%3E%20(property)%20protocol">Link to this property</a>

size: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20protocolStats%20%3E%20(items)%20%3E%20(property)%20size">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20protocolStats">Link to this property</a>

<details>

<summary>

resourceStats: array of object {compression, count, countries, 5 more }

</summary>

compression: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20resourceStats%20%3E%20(items)%20%3E%20(property)%20compression">Link to this property</a>

count: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20resourceStats%20%3E%20(items)%20%3E%20(property)%20count">Link to this property</a>

countries: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20resourceStats%20%3E%20(items)%20%3E%20(property)%20countries">Link to this property</a>

encodedSize: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20resourceStats%20%3E%20(items)%20%3E%20(property)%20encodedSize">Link to this property</a>

ips: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20resourceStats%20%3E%20(items)%20%3E%20(property)%20ips">Link to this property</a>

percentage: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20resourceStats%20%3E%20(items)%20%3E%20(property)%20percentage">Link to this property</a>

size: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20resourceStats%20%3E%20(items)%20%3E%20(property)%20size">Link to this property</a>

type: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20resourceStats%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20resourceStats">Link to this property</a>

securePercentage: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20securePercentage">Link to this property</a>

secureRequests: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20secureRequests">Link to this property</a>

<details>

<summary>

serverStats: array of object {count, countries, encodedSize, 3 more }

</summary>

count: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20serverStats%20%3E%20(items)%20%3E%20(property)%20count">Link to this property</a>

countries: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20serverStats%20%3E%20(items)%20%3E%20(property)%20countries">Link to this property</a>

encodedSize: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20serverStats%20%3E%20(items)%20%3E%20(property)%20encodedSize">Link to this property</a>

ips: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20serverStats%20%3E%20(items)%20%3E%20(property)%20ips">Link to this property</a>

server: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20serverStats%20%3E%20(items)%20%3E%20(property)%20server">Link to this property</a>

size: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20serverStats%20%3E%20(items)%20%3E%20(property)%20size">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20serverStats">Link to this property</a>

<details>

<summary>

tlsStats: array of object {count, countries, encodedSize, 4 more }

</summary>

count: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20tlsStats%20%3E%20(items)%20%3E%20(property)%20count">Link to this property</a>

countries: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20tlsStats%20%3E%20(items)%20%3E%20(property)%20countries">Link to this property</a>

encodedSize: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20tlsStats%20%3E%20(items)%20%3E%20(property)%20encodedSize">Link to this property</a>

ips: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20tlsStats%20%3E%20(items)%20%3E%20(property)%20ips">Link to this property</a>

<details>

<summary>

protocols: object {"TLS 1.3 / AES\_128\_GCM" }

</summary>

"TLS 1.3 / AES\_128\_GCM": number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20tlsStats%20%3E%20(items)%20%3E%20(property)%20protocols%20%3E%20(property)%20TLS%201.3%20%2F%20AES_128_GCM">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20tlsStats%20%3E%20(items)%20%3E%20(property)%20protocols">Link to this property</a>

securityState: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20tlsStats%20%3E%20(items)%20%3E%20(property)%20securityState">Link to this property</a>

size: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20tlsStats%20%3E%20(items)%20%3E%20(property)%20size">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20tlsStats">Link to this property</a>

totalLinks: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20totalLinks">Link to this property</a>

uniqASNs: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20uniqASNs">Link to this property</a>

uniqCountries: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats%20%3E%20(property)%20uniqCountries">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20stats">Link to this property</a>

<details>

<summary>

task: object {apexDomain, domain, domURL, 10 more }

</summary>

apexDomain: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20task%20%3E%20(property)%20apexDomain">Link to this property</a>

domain: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20task%20%3E%20(property)%20domain">Link to this property</a>

domURL: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20task%20%3E%20(property)%20domURL">Link to this property</a>

method: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20task%20%3E%20(property)%20method">Link to this property</a>

<details>

<summary>

options: object {customHeaders, screenshotsResolutions }

</summary>

customHeaders: optional unknown

Custom headers set.

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20task%20%3E%20(property)%20options%20%3E%20(property)%20customHeaders">Link to this property</a>

screenshotsResolutions: optional array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20task%20%3E%20(property)%20options%20%3E%20(property)%20screenshotsResolutions">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20task%20%3E%20(property)%20options">Link to this property</a>

reportURL: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20task%20%3E%20(property)%20reportURL">Link to this property</a>

screenshotURL: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20task%20%3E%20(property)%20screenshotURL">Link to this property</a>

source: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20task%20%3E%20(property)%20source">Link to this property</a>

success: boolean

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20task%20%3E%20(property)%20success">Link to this property</a>

time: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20task%20%3E%20(property)%20time">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20task%20%3E%20(property)%20url">Link to this property</a>

uuid: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20task%20%3E%20(property)%20uuid">Link to this property</a>

visibility: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20task%20%3E%20(property)%20visibility">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20task">Link to this property</a>

<details>

<summary>

verdicts: object {overall }

</summary>

<details>

<summary>

overall: object {categories, hasVerdicts, malicious, tags }

</summary>

categories: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20verdicts%20%3E%20(property)%20overall%20%3E%20(property)%20categories">Link to this property</a>

hasVerdicts: boolean

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20verdicts%20%3E%20(property)%20overall%20%3E%20(property)%20hasVerdicts">Link to this property</a>

malicious: boolean

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20verdicts%20%3E%20(property)%20overall%20%3E%20(property)%20malicious">Link to this property</a>

tags: array of string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20verdicts%20%3E%20(property)%20overall%20%3E%20(property)%20tags">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20verdicts%20%3E%20(property)%20overall">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)%20%3E%20(property)%20verdicts">Link to this property</a>

</details>

[Link to this property](<#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_get_response%20%3E%20(schema)>)

<details>

<summary>

ScanCreateResponse object {api, message, result, 4 more }

</summary>

api: string

URL to api report.

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_create_response%20%3E%20(schema)%20%3E%20(property)%20api">Link to this property</a>

message: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_create_response%20%3E%20(schema)%20%3E%20(property)%20message">Link to this property</a>

result: string

Public URL to report.

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_create_response%20%3E%20(schema)%20%3E%20(property)%20result">Link to this property</a>

url: string

Canonical form of submitted URL. Use this if you want to later search by URL.

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_create_response%20%3E%20(schema)%20%3E%20(property)%20url">Link to this property</a>

uuid: string

Scan ID.

formatuuid

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_create_response%20%3E%20(schema)%20%3E%20(property)%20uuid">Link to this property</a>

<details>

<summary>

visibility: "public"or "unlisted"

Submitted visibility status.

</summary>

One of the following:

"public"

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_create_response%20%3E%20(schema)%20%3E%20(property)%20visibility%20%3E%20(member)%200">Link to this property</a>

"unlisted"

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_create_response%20%3E%20(schema)%20%3E%20(property)%20visibility%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_create_response%20%3E%20(schema)%20%3E%20(property)%20visibility">Link to this property</a>

<details>

<summary>

options: optional object {useragent }

</summary>

useragent: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_create_response%20%3E%20(schema)%20%3E%20(property)%20options%20%3E%20(property)%20useragent">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_create_response%20%3E%20(schema)%20%3E%20(property)%20options">Link to this property</a>

</details>

[Link to this property](<#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_create_response%20%3E%20(schema)>)

<details>

<summary>

ScanBulkCreateResponse = array of object {api, result, url, 3 more }

</summary>

api: string

URL to api report.

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_bulk_create_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20api">Link to this property</a>

result: string

URL to report.

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_bulk_create_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20result">Link to this property</a>

url: string

Submitted URL

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_bulk_create_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20url">Link to this property</a>

uuid: string

Scan ID.

formatuuid

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_bulk_create_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

<details>

<summary>

visibility: "public"or "unlisted"

Submitted visibility status.

</summary>

One of the following:

"public"

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_bulk_create_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20visibility%20%3E%20(member)%200">Link to this property</a>

"unlisted"

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_bulk_create_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20visibility%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_bulk_create_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20visibility">Link to this property</a>

<details>

<summary>

options: optional object {useragent }

</summary>

useragent: optional string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_bulk_create_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20options%20%3E%20(property)%20useragent">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_bulk_create_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20options">Link to this property</a>

</details>

[Link to this property](<#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_bulk_create_response%20%3E%20(schema)>)

<details>

<summary>

ScanHARResponse object {log }

</summary>

<details>

<summary>

log: object {creator, entries, pages, version }

</summary>

<details>

<summary>

creator: object {comment, name, version }

</summary>

comment: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20creator%20%3E%20(property)%20comment">Link to this property</a>

name: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20creator%20%3E%20(property)%20name">Link to this property</a>

version: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20creator%20%3E%20(property)%20version">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20creator">Link to this property</a>

<details>

<summary>

entries: array of object {\_initialPriority, \_initiator\_type, \_priority, 11 more }

</summary>

\_initialPriority: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20_initialPriority">Link to this property</a>

\_initiator\_type: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20_initiator_type">Link to this property</a>

\_priority: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20_priority">Link to this property</a>

\_requestId: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20_requestId">Link to this property</a>

\_requestTime: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20_requestTime">Link to this property</a>

\_resourceType: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20_resourceType">Link to this property</a>

cache: unknown

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20cache">Link to this property</a>

connection: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20connection">Link to this property</a>

pageref: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20pageref">Link to this property</a>

<details>

<summary>

request: object {bodySize, headers, headersSize, 3 more }

</summary>

bodySize: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20bodySize">Link to this property</a>

<details>

<summary>

headers: array of object {name, value }

</summary>

name: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20headers">Link to this property</a>

headersSize: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20headersSize">Link to this property</a>

httpVersion: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20httpVersion">Link to this property</a>

method: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20method">Link to this property</a>

url: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20request%20%3E%20(property)%20url">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20request">Link to this property</a>

<details>

<summary>

response: object {\_transferSize, bodySize, content, 6 more }

</summary>

\_transferSize: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20_transferSize">Link to this property</a>

bodySize: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20bodySize">Link to this property</a>

<details>

<summary>

content: object {mimeType, size, compression }

</summary>

mimeType: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20content%20%3E%20(property)%20mimeType">Link to this property</a>

size: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20content%20%3E%20(property)%20size">Link to this property</a>

compression: optional number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20content%20%3E%20(property)%20compression">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20content">Link to this property</a>

<details>

<summary>

headers: array of object {name, value }

</summary>

name: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20headers">Link to this property</a>

headersSize: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20headersSize">Link to this property</a>

httpVersion: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20httpVersion">Link to this property</a>

redirectURL: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20redirectURL">Link to this property</a>

status: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20status">Link to this property</a>

statusText: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20response%20%3E%20(property)%20statusText">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20response">Link to this property</a>

serverIPAddress: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20serverIPAddress">Link to this property</a>

startedDateTime: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20startedDateTime">Link to this property</a>

time: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(property)%20time">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20entries">Link to this property</a>

<details>

<summary>

pages: array of object {id, pageTimings, startedDateTime, title }

</summary>

id: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20pages%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

pageTimings: object {onContentLoad, onLoad }

</summary>

onContentLoad: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20pages%20%3E%20(items)%20%3E%20(property)%20pageTimings%20%3E%20(property)%20onContentLoad">Link to this property</a>

onLoad: number

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20pages%20%3E%20(items)%20%3E%20(property)%20pageTimings%20%3E%20(property)%20onLoad">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20pages%20%3E%20(items)%20%3E%20(property)%20pageTimings">Link to this property</a>

startedDateTime: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20pages%20%3E%20(items)%20%3E%20(property)%20startedDateTime">Link to this property</a>

title: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20pages%20%3E%20(items)%20%3E%20(property)%20title">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20pages">Link to this property</a>

version: string

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log%20%3E%20(property)%20version">Link to this property</a>

</details>

<a href="#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)%20%3E%20(property)%20log">Link to this property</a>

</details>

[Link to this property](<#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_har_response%20%3E%20(schema)>)

ScanDOMResponse = string

HTML of webpage.

[Link to this property](<#(resource)%20url_scanner.scans%20%3E%20(model)%20scan_dom_response%20%3E%20(schema)>)