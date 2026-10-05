---
description: Workers RPC now supports cross-language calls between Python and JavaScript Workers without additional dependencies or schema definitions.
title: Python and JavaScript Workers can now call each other via RPC
image: https://developers.cloudflare.com/changelog/post/2026-08-03-python-javascript-rpc/og.png?v=0dbe743153c97fdb
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 3, 2026

## Python and JavaScript Workers can now call each other via RPC

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-03-python-javascript-rpc/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now call methods between Python and JavaScript Workers using [Workers RPC](https://developers.cloudflare.com/workers/runtime-apis/rpc/). This works through [Service bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/rpc/) without extra dependencies, schema definitions, or serialization code.

Cross-language RPC calls behave like ordinary function calls. Exceptions propagate to the call site. You can pass [structured cloneable types ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm#supported_types) as parameters or return values, and Pyodide Foreign Function Interface (FFI) automatically converts types between languages.

#### Call a TypeScript Worker from Python

Define a method in a TypeScript Worker:

*index.jsjs*

```js
import { WorkerEntrypoint } from "cloudflare:workers";

export class RpcService extends WorkerEntrypoint {
	async add(a, b) {
		return a + b;
	}
}
```

*index.tsts*

```ts
import { WorkerEntrypoint } from "cloudflare:workers";

export class RpcService extends WorkerEntrypoint {
	async add(a: number, b: number): Promise<number> {
		return a + b;
	}
}
```

Call it from a Python Worker through a Service binding:

```python
from workers import Response, WorkerEntrypoint

class Default(WorkerEntrypoint):
	async def fetch(self, request):
		rpc = self.env.RPC
		result = await rpc.add(42, 144)
		return Response.json({"result": result})
```

Configure the Service binding in the Python Worker's Wrangler configuration:

```jsonc
{
	"services": [
		{
			"binding": "RPC",
			"service": "ts-rpc-server",
			"entrypoint": "RpcService"
		}
	]
}
```

```toml
[[services]]
binding = "RPC"
service = "ts-rpc-server"
entrypoint = "RpcService"
```

#### Call a Python Worker from JavaScript

Define a method in a Python Worker:

```python
from workers import WorkerEntrypoint

class Default(WorkerEntrypoint):
	async def highlight_code(self, code: str, language: str) -> dict:
		from pygments.formatters import HtmlFormatter
		from pygments import highlight
		from pygments.lexers import get_lexer_by_name

		lexer = get_lexer_by_name(language, stripall=True)
		formatter = HtmlFormatter(linenos=True, cssclass="highlight", style="monokai")
		highlighted_html = highlight(code, lexer, formatter)
		css = formatter.get_style_defs(".highlight")

		return {
			"html": highlighted_html,
			"css": css
		}
```

Call it from a JavaScript Worker through a Service binding:

*index.jsjs*

```js
export default {
	async fetch(request, env) {
		const rpc = env.PYTHON_RPC;
		const result = await rpc.highlight_code("print(42)", "python");
		return Response.json(result);
	},
};
```

*index.tsts*

```ts
export default {
	async fetch(request, env) {
		const rpc = env.PYTHON_RPC;
		const result = await rpc.highlight_code("print(42)", "python");
		return Response.json(result);
	},
};
```

Configure the Service binding in the JavaScript Worker's Wrangler configuration:

```jsonc
{
	"services": [
		{
			"binding": "PYTHON_RPC",
			"service": "py-rpc-server"
		}
	]
}
```

```toml
[[services]]
binding = "PYTHON_RPC"
service = "py-rpc-server"
```

For more details on the announcement, read the [blog post ↗︎](https://blog.cloudflare.com/python-workers-rpc/).

For more information, refer to the [Workers RPC documentation](https://developers.cloudflare.com/workers/runtime-apis/rpc/) and the [Python Workers overview](https://developers.cloudflare.com/workers/languages/python/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-03-python-javascript-rpc/#page","headline":"Python and JavaScript Workers can now call each other via RPC","description":"Workers RPC now supports cross-language calls between Python and JavaScript Workers without additional dependencies or schema definitions.","url":"https://developers.cloudflare.com/changelog/post/2026-08-03-python-javascript-rpc/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-03-python-javascript-rpc/og.png?v=0dbe743153c97fdb","dateModified":"2026-08-03","datePublished":"2026-08-03","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
