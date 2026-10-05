---
description: The latest release transforms the Sandbox SDK into a full edge-native code execution platform, enabling secure, containerized runtimes with real-time streaming, language interpreters, Git integration, process lifecycle management, and port forwarding.
title: Cloudflare Sandbox SDK adds streaming, code interpreter, Git support, process control and more
image: https://developers.cloudflare.com/changelog/post/2025-08-05-sandbox-sdk-major-update/og.png?v=ce46a23f15be31c5
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 5, 2025

## Cloudflare Sandbox SDK adds streaming, code interpreter, Git support, process control and more

[Agents](https://developers.cloudflare.com/agents/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-05-sandbox-sdk-major-update/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We’ve shipped a major release for the [@cloudflare/sandbox ↗︎](https://github.com/cloudflare/sandbox-sdk) SDK, turning it into a full-featured, container-based execution platform that runs securely on Cloudflare Workers.

This update adds live streaming of output, persistent Python and JavaScript code interpreters with rich output support (charts, tables, HTML, JSON), file system access, Git operations, full background process control, and the ability to expose running services via public URLs.

This makes it ideal for building AI agents, CI runners, cloud REPLs, data analysis pipelines, or full developer tools — all without managing infrastructure.

#### Code interpreter (Python, JS, TS)

Create persistent code contexts with support for rich visual + structured outputs.

#### createCodeContext(options)

Creates a new code execution context with persistent state.

```ts
// Create a Python context
const pythonCtx = await sandbox.createCodeContext({ language: "python" });

// Create a JavaScript context
const jsCtx = await sandbox.createCodeContext({ language: "javascript" });
```

Options:

- language: Programming language ('python' | 'javascript' | 'typescript')
- cwd: Working directory (default: /workspace)
- envVars: Environment variables for the context

#### runCode(code, options)

Executes code with optional streaming callbacks.

```ts
// Simple execution
const execution = await sandbox.runCode('print("Hello World")', {
	context: pythonCtx,
});

// With streaming callbacks
await sandbox.runCode(
	`
for i in range(5):
    print(f"Step {i}")
    time.sleep(1)
`,
	{
		context: pythonCtx,
		onStdout: (output) => console.log("Real-time:", output.text),
		onResult: (result) => console.log("Result:", result),
	},
);
```

Options:

- language: Programming language ('python' | 'javascript' | 'typescript')
- cwd: Working directory (default: /workspace)
- envVars: Environment variables for the context

#### Real-time streaming output

Returns a streaming response for real-time processing.

```ts
const stream = await sandbox.runCodeStream(
	"import time; [print(i) for i in range(10)]",
);
// Process the stream as needed
```

#### Rich output handling

Interpreter outputs are auto-formatted and returned in multiple formats:

- text
- html (e.g., Pandas tables)
- png, svg (e.g., Matplotlib charts)
- json (structured data)
- chart (parsed visualizations)

```ts
const result = await sandbox.runCode(
	`
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("flights")
pivot = data.pivot("month", "year", "passengers")
sns.heatmap(pivot, annot=True, fmt="d")
plt.title("Flight Passengers")
plt.show()

pivot.to_dict()
`,
	{ context: pythonCtx },
);

if (result.png) {
	console.log("Chart output:", result.png);
}
```

#### Preview URLs from Exposed Ports

Start background processes and expose them with live URLs.

```ts
await sandbox.startProcess("python -m http.server 8000");
const preview = await sandbox.exposePort(8000);

console.log("Live preview at:", preview.url);
```

#### Full process lifecycle control

Start, inspect, and terminate long-running background processes.

```ts
const process = await sandbox.startProcess("node server.js");
console.log(`Started process ${process.id} with PID ${process.pid}`);

// Monitor the process
const logStream = await sandbox.streamProcessLogs(process.id);
for await (const log of parseSSEStream<LogEvent>(logStream)) {
	console.log(`Server: ${log.data}`);
}
```

- listProcesses() - List all running processes
- getProcess(id) - Get detailed process status
- killProcess(id, signal) - Terminate specific processes
- killAllProcesses() - Kill all processes
- streamProcessLogs(id, options) - Stream logs from running processes
- getProcessLogs(id) - Get accumulated process output

#### Git integration

Clone Git repositories directly into the sandbox.

```ts
await sandbox.gitCheckout("https://github.com/user/repo", {
	branch: "main",
	targetDir: "my-project",
});
```

Sandboxes are still experimental. We're using them to explore how isolated, container-like workloads might scale on Cloudflare — and to help define the developer experience around them.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-05-sandbox-sdk-major-update/#page","headline":"Cloudflare Sandbox SDK adds streaming, code interpreter, Git support, process control and more","description":"The latest release transforms the Sandbox SDK into a full edge-native code execution platform, enabling secure, containerized runtimes with real-time streaming, language interpreters, Git integration, process lifecycle management, and port forwarding.","url":"https://developers.cloudflare.com/changelog/post/2025-08-05-sandbox-sdk-major-update/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-05-sandbox-sdk-major-update/og.png?v=ce46a23f15be31c5","dateModified":"2025-08-05","datePublished":"2025-08-05","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
