---
description: Definitions of key terms used throughout the D1 documentation.
title: Glossary
image: https://developers.cloudflare.com/d1/reference/glossary/og.png?v=10757529d6ffbf71
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/d1/llms.txt  
> Use this file to discover all available pages before exploring further.

# Glossary

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/d1/reference/glossary/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Review the definitions for terms used across Cloudflare's D1 documentation.

| Term | Definition |
| --- | --- |
| bookmark | A bookmark represents the state of a database at a specific point in time.<ul><li>Bookmarks are lexicographically sortable. Sorting orders a list of bookmarks from oldest-to-newest.</li></ul> |
| primary database instance | The primary database instance is the original instance of a database. This database instance only exists in one location in the world. |
| query planner | A component in a database management system which takes a user query and generates the most efficient plan of executing that query (the query plan). For example, the query planner decides which indices to use, or which table to access first. |
| read replica | A read replica is an eventually-replicated copy of the primary database instance which only serve read requests. There may be multiple read replicas for a single primary database instance. |
| replica lag | The time it takes for the primary database instance to replicate its changes to a specific read replica. |
| session | A session encapsulates all the queries from one logical session for your application. For example, a session may correspond to all queries coming from a particular web browser session. |
