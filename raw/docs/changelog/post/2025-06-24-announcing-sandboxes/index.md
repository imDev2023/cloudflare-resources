---
description: You can start creating sandboxes today by installing our new Sandbox package.
title: Run AI-generated code on-demand with Code Sandboxes (new)
image: https://developers.cloudflare.com/changelog/post/2025-06-24-announcing-sandboxes/og.png?v=e90f8d9cc4263982
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 25, 2025

## Run AI-generated code on-demand with Code Sandboxes (new)

[Agents](https://developers.cloudflare.com/agents/) [Workers](https://developers.cloudflare.com/workers/) [Workflows](https://developers.cloudflare.com/workflows/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-24-announcing-sandboxes/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

AI is supercharging app development for everyone, but we need a safe way to run untrusted, LLM-written code. We’re introducing [Sandboxes ↗︎](https://www.npmjs.com/package/@cloudflare/sandbox), which let your Worker run actual processes in a secure, container-based environment.

```ts
import { getSandbox } from "@cloudflare/sandbox";
export { Sandbox } from "@cloudflare/sandbox";

export default {
	async fetch(request: Request, env: Env) {
		const sandbox = getSandbox(env.Sandbox, "my-sandbox");
		return sandbox.exec("ls", ["-la"]);
	},
};
```

#### Methods

- `exec(command: string, args: string[], options?: { stream?: boolean })`:Execute a command in the sandbox.
- `gitCheckout(repoUrl: string, options: { branch?: string; targetDir?: string; stream?: boolean })`: Checkout a git repository in the sandbox.
- `mkdir(path: string, options: { recursive?: boolean; stream?: boolean })`: Create a directory in the sandbox.
- `writeFile(path: string, content: string, options: { encoding?: string; stream?: boolean })`: Write content to a file in the sandbox.
- `readFile(path: string, options: { encoding?: string; stream?: boolean })`: Read content from a file in the sandbox.
- `deleteFile(path: string, options?: { stream?: boolean })`: Delete a file from the sandbox.
- `renameFile(oldPath: string, newPath: string, options?: { stream?: boolean })`: Rename a file in the sandbox.
- `moveFile(sourcePath: string, destinationPath: string, options?: { stream?: boolean })`: Move a file from one location to another in the sandbox.
- `ping()`: Ping the sandbox.

Sandboxes are still experimental. We're using them to explore how isolated, container-like workloads might scale on Cloudflare — and to help define the developer experience around them.

You can try it today from your Worker, with just a few lines of code. Let us know what you build.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-24-announcing-sandboxes/#page","headline":"Run AI-generated code on-demand with Code Sandboxes (new)","description":"You can start creating sandboxes today by installing our new Sandbox package.","url":"https://developers.cloudflare.com/changelog/post/2025-06-24-announcing-sandboxes/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-06-24-announcing-sandboxes/og.png?v=e90f8d9cc4263982","dateModified":"2025-06-25","datePublished":"2025-06-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
