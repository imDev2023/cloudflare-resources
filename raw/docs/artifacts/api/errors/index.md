---
description: Error codes returned by the Artifacts REST API and Workers binding.
title: Errors
image: https://developers.cloudflare.com/artifacts/api/errors/og.png?v=4c63d47c2ba7b48e
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/artifacts/llms.txt  
> Use this file to discover all available pages before exploring further.

# Errors

Last updated May 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/artifacts/api/errors/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This is a list of Artifacts errors.

## Error codes

| Name | Code | Description |
| --- | --- | --- |
| `ALREADY_EXISTS` | 10201 | The target repository already exists in the namespace. |
| `NOT_FOUND` | 10200 | The repository or remote resource does not exist. |
| `IMPORT_IN_PROGRESS` | 10302 | The repository is still being imported and is not yet available. |
| `FORK_IN_PROGRESS` | 10303 | The repository is still being forked and is not yet available. |
| `INVALID_INPUT` | 10100 | A request parameter is missing, malformed, or outside the accepted range. |
| `INVALID_REPO_NAME` | 10101 | The repository name does not meet naming requirements. |
| `INVALID_TTL` | 10103 | The token TTL is outside the allowed range (60–31,536,000 seconds). |
| `INVALID_URL` | 10104 | The source URL does not point to a valid git repository. |
| `REMOTE_AUTH_REQUIRED` | 10106 | The remote repository requires authentication. |
| `UPSTREAM_UNAVAILABLE` | 10401 | The remote git server could not be reached. |
| `MEMORY_LIMIT` | 10402 | The operation exceeds service memory limits. |
| `INTERNAL_ERROR` | 10400 | An unexpected internal error occurred. |
