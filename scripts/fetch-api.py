#!/usr/bin/env python3
"""Mirror the Cloudflare API reference (developers.cloudflare.com/api/) into raw/api/.

- raw/api/llms.txt and raw/api/overview.md: the API reference index and overview.
- raw/api/resources/<resource>/.../index.md: every resource and subresource page (HTTP flavour),
  listing each endpoint with its method and path plus the object models.
- raw/api/openapi.json: the full OpenAPI spec from github.com/cloudflare/api-schemas (gitignored, large).
- raw/api/endpoints.tsv: one line per operation (method, path, operationId, tags, summary), derived from the spec.

Per-method pages are not mirrored; the spec carries every parameter and schema they show.
"""
import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from importlib import import_module

fd = import_module("fetch-docs")

BASE = "https://developers.cloudflare.com"
OUT = os.path.join(fd.ROOT, "raw", "api")
SPEC = "https://raw.githubusercontent.com/cloudflare/api-schemas/main/openapi.json"


def save(rel, body):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(body)


def page(rel_index_md):
    status, _, body = fd.get(BASE + rel_index_md)
    if status == 200 and body.strip():
        save(rel_index_md[len("/api/"):], body)
        return None
    return rel_index_md, status


def main():
    os.makedirs(OUT, exist_ok=True)
    _, _, index = fd.get(BASE + "/api/llms.txt")
    save("llms.txt", index)
    links = sorted(set(re.findall(r"\]\((/api/[^)]+/index\.md)\)", index)))
    with ThreadPoolExecutor(12) as ex:
        failed = [r for r in ex.map(page, links) if r]
    print(f"api pages: {len(links) - len(failed)} saved, {len(failed)} failed {failed[:5]}")

    _, _, spec = fd.get(SPEC)
    save("openapi.json", spec)
    doc = json.loads(spec)
    rows = []
    for path, ops in doc.get("paths", {}).items():
        for method, op in ops.items():
            if method.lower() not in {"get", "post", "put", "patch", "delete", "head"}:
                continue
            rows.append("\t".join([
                method.upper(), path, op.get("operationId", ""),
                ",".join(op.get("tags", [])), (op.get("summary") or "").replace("\t", " ").replace("\n", " "),
                "deprecated" if op.get("deprecated") else "",
            ]))
    rows.sort(key=lambda r: (r.split("\t")[1], r.split("\t")[0]))
    save("endpoints.tsv", "method\tpath\toperationId\ttags\tsummary\tdeprecated\n" + "\n".join(rows) + "\n")
    print(f"openapi {doc.get('info', {}).get('version')}: {len(rows)} operations, {len(doc.get('paths', {}))} paths")


if __name__ == "__main__":
    main()
