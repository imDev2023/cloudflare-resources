---
description: Clone repositories, manage branches, and automate Git operations with the Sandbox SDK 0.x.
title: Work with Git
image: https://developers.cloudflare.com/sandbox/sdk/guides/git-workflows/og.png?v=048dfbf4df6a0a20
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/sandbox/llms.txt  
> Use this file to discover all available pages before exploring further.

# Work with Git

Last updated Sep 30, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/sandbox/sdk/guides/git-workflows/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

This page documents Sandbox SDK 0.x for existing applications. For new applications, refer to [Run tests from a Git repository](https://developers.cloudflare.com/sandbox/commands/run-tests-from-a-git-repository/). To move an existing application to `@cloudflare/sandbox` 1.0, refer to [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/).

This guide shows you how to clone repositories, manage branches, and automate Git operations in the sandbox.

## Clone repositories

```js
import { getSandbox } from "@cloudflare/sandbox";

const sandbox = getSandbox(env.Sandbox, "my-sandbox");

// Basic clone
await sandbox.gitCheckout("https://github.com/user/repo");

// Clone specific branch
await sandbox.gitCheckout("https://github.com/user/repo", {
	branch: "develop",
});

// Shallow clone (faster for large repos)
await sandbox.gitCheckout("https://github.com/user/large-repo", {
	depth: 1,
});

// Clone to specific directory
await sandbox.gitCheckout("https://github.com/user/my-app", {
	targetDir: "/workspace/project",
});
```

```plaintext
import { getSandbox } from '@cloudflare/sandbox';

const sandbox = getSandbox(env.Sandbox, 'my-sandbox');

// Basic clone
await sandbox.gitCheckout('https://github.com/user/repo');

// Clone specific branch
await sandbox.gitCheckout('https://github.com/user/repo', {
  branch: 'develop'
});

// Shallow clone (faster for large repos)
await sandbox.gitCheckout('https://github.com/user/large-repo', {
  depth: 1
});

// Clone to specific directory
await sandbox.gitCheckout('https://github.com/user/my-app', {
  targetDir: '/workspace/project'
});
```

## Clone private repositories

Use a personal access token in the URL:

```js
const token = env.GITHUB_TOKEN;
const repoUrl = `https://${token}@github.com/user/private-repo.git`;

await sandbox.gitCheckout(repoUrl);
```

```plaintext
const token = env.GITHUB_TOKEN;
const repoUrl = `https://${token}@github.com/user/private-repo.git`;

await sandbox.gitCheckout(repoUrl);
```

More secure alternative

Embedding a token in the URL passes the credential directly into the sandbox. For better access control, use an outbound handler that injects the real token at request time — the sandbox never holds the credential. Refer to [Handle outbound traffic](https://developers.cloudflare.com/sandbox/sdk/guides/outbound-traffic/).

## Clone and build

Clone a repository and run build steps:

```js
await sandbox.gitCheckout("https://github.com/user/my-app");

const repoName = "my-app";

// Install and build
await sandbox.exec(`cd ${repoName} && npm install`);
await sandbox.exec(`cd ${repoName} && npm run build`);

console.log("Build complete");
```

```plaintext
await sandbox.gitCheckout('https://github.com/user/my-app');

const repoName = 'my-app';

// Install and build
await sandbox.exec(`cd ${repoName} && npm install`);
await sandbox.exec(`cd ${repoName} && npm run build`);

console.log('Build complete');
```

## Work with branches

```js
await sandbox.gitCheckout("https://github.com/user/repo");

// Switch branches
await sandbox.exec("cd repo && git checkout feature-branch");

// Create new branch
await sandbox.exec("cd repo && git checkout -b new-feature");
```

```plaintext
await sandbox.gitCheckout('https://github.com/user/repo');

// Switch branches
await sandbox.exec('cd repo && git checkout feature-branch');

// Create new branch
await sandbox.exec('cd repo && git checkout -b new-feature');
```

## Make changes and commit

```js
await sandbox.gitCheckout("https://github.com/user/repo");

// Modify a file
const readme = await sandbox.readFile("/workspace/repo/README.md");
await sandbox.writeFile(
	"/workspace/repo/README.md",
	readme.content + "\n\n## New Section",
);

// Commit changes
await sandbox.exec('cd repo && git config user.name "Sandbox Bot"');
await sandbox.exec('cd repo && git config user.email "bot@example.com"');
await sandbox.exec("cd repo && git add README.md");
await sandbox.exec('cd repo && git commit -m "Update README"');
```

```plaintext
await sandbox.gitCheckout('https://github.com/user/repo');

// Modify a file
const readme = await sandbox.readFile('/workspace/repo/README.md');
await sandbox.writeFile('/workspace/repo/README.md', readme.content + '\n\n## New Section');

// Commit changes
await sandbox.exec('cd repo && git config user.name "Sandbox Bot"');
await sandbox.exec('cd repo && git config user.email "bot@example.com"');
await sandbox.exec('cd repo && git add README.md');
await sandbox.exec('cd repo && git commit -m "Update README"');
```

## Best practices

- **Use shallow clones** - Faster for large repos with `depth: 1`
- **Store credentials securely** - Use environment variables for tokens
- **Clean up** - Delete unused repositories to save space

## Troubleshooting

### Authentication fails

Verify your token is set:

```js
if (!env.GITHUB_TOKEN) {
	throw new Error("GITHUB_TOKEN not configured");
}

const repoUrl = `https://${env.GITHUB_TOKEN}@github.com/user/private-repo.git`;
await sandbox.gitCheckout(repoUrl);
```

```plaintext
if (!env.GITHUB_TOKEN) {
  throw new Error('GITHUB_TOKEN not configured');
}

const repoUrl = `https://${env.GITHUB_TOKEN}@github.com/user/private-repo.git`;
await sandbox.gitCheckout(repoUrl);
```

### Large repository timeout

Use shallow clone:

```js
await sandbox.gitCheckout("https://github.com/user/large-repo", {
	depth: 1,
});
```

```plaintext
await sandbox.gitCheckout('https://github.com/user/large-repo', {
  depth: 1
});
```

## Related resources

- [Files API reference](https://developers.cloudflare.com/sandbox/sdk/api/files/) - File operations after cloning
- [Execute commands guide](https://developers.cloudflare.com/sandbox/sdk/guides/execute-commands/) - Run git commands
- [Manage files guide](https://developers.cloudflare.com/sandbox/sdk/guides/manage-files/) - Work with cloned files
