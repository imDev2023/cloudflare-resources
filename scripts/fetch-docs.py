#!/usr/bin/env python3
"""Mirror every page of developers.cloudflare.com as Markdown into raw/docs/.

Page discovery is the union of:
  - every llms.txt index, followed recursively (products nest section-level indexes),
  - the sitemap (which also covers the changelog and pages missing from the indexes).
Each page is fetched from its official `<url>/index.md` Markdown endpoint and saved
at raw/docs/<url path>/index.md, with the site footer ("Was this helpful?" and the
schema.org JSON) stripped. Indexes are kept at raw/docs/<path>/llms.txt.

Usage: python3 scripts/fetch-docs.py [--workers 12]
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

BASE = "https://developers.cloudflare.com"
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
RAW = os.path.join(ROOT, "raw", "docs")
UA = "Mozilla/5.0 (knowledge-base mirror; markdown-for-agents)"
PAGES = set()
LINK = re.compile(r"\((https://developers\.cloudflare\.com/[^)\s]+)\)")


def get(url, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.status, r.geturl(), r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return 404, url, ""
            if i == tries - 1:
                return e.code, url, ""
        except Exception:
            if i == tries - 1:
                return 0, url, ""
        time.sleep(2 ** i)


def local(path, name):
    path = path.strip("/")
    d = os.path.join(RAW, path) if path else RAW
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, name)


def crawl_indexes():
    seen, pages, queue = set(), set(), [BASE + "/llms.txt"]
    while queue:
        batch, queue = queue, []
        with ThreadPoolExecutor(12) as ex:
            results = list(ex.map(get, batch))
        for url, (status, _, body) in zip(batch, results):
            seen.add(url)
            if status != 200:
                print("index failed", status, url, file=sys.stderr)
                continue
            with open(local(urlparse(url).path.rsplit("/", 1)[0], "llms.txt"), "w") as f:
                f.write(body)
            for link in LINK.findall(body):
                link = link.split("#")[0]
                if link.endswith("/llms.txt") and link not in seen and link not in queue:
                    queue.append(link)
                elif link.endswith("/index.md"):
                    pages.add(link[: -len("index.md")])
    return pages, len(seen)


def sitemap():
    _, _, idx = get(BASE + "/sitemap-index.xml")
    urls = set()
    for sm in re.findall(r"<loc>([^<]+)</loc>", idx):
        _, _, body = get(sm)
        urls.update(re.findall(r"<loc>([^<]+)</loc>", body))
    return {u if u.endswith("/") else u + "/" for u in urls}


def clean(md):
    cut = md.rfind("\nWas this helpful?")
    return (md[:cut] if cut != -1 else md).rstrip() + "\n"


def fetch_page(url):
    status, final, body = get(url + "index.md")
    if status != 200 or not body.strip():
        return url, status, None
    final_page = final[: -len("index.md")] if final.endswith("index.md") else final
    moved = final_page if final_page != url else None
    # A redirected URL whose target is mirrored anyway is recorded, not saved twice.
    if not (moved and moved in PAGES):
        with open(local(urlparse(url).path, "index.md"), "w") as f:
            f.write(clean(body))
    return url, status, moved


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=12)
    args = ap.parse_args()
    os.makedirs(RAW, exist_ok=True)
    from_index, n_index = crawl_indexes()
    from_sitemap = sitemap()
    pages = sorted(from_index | from_sitemap)
    PAGES.update(pages)
    print(f"{n_index} indexes, {len(from_index)} pages in indexes, {len(from_sitemap)} in sitemap, {len(pages)} union")
    failed, redirects = [], {}
    with ThreadPoolExecutor(args.workers) as ex:
        for i, (url, status, moved) in enumerate(ex.map(fetch_page, pages), 1):
            if status != 200:
                failed.append({"url": url, "status": status})
            elif moved:
                redirects[url] = moved
            if i % 500 == 0:
                print(f"  {i}/{len(pages)}", flush=True)
    manifest = {
        "fetched": time.strftime("%Y-%m-%d"),
        "pages": len(pages) - len(failed),
        "only_in_indexes": sorted(from_index - from_sitemap),
        "only_in_sitemap": sorted(from_sitemap - from_index),
        "redirects": redirects,
        "failed": failed,
    }
    with open(os.path.join(RAW, "_manifest.json"), "w") as f:
        json.dump(manifest, f, indent=1)
    print(f"saved {manifest['pages']} pages, {len(failed)} failed, {len(redirects)} redirected")


if __name__ == "__main__":
    main()
