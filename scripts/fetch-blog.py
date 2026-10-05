#!/usr/bin/env python3
"""Mirror Cloudflare blog posts on Web3, crypto payments and agent payments into raw/blog/.

Posts come from the tag listings in TAGS (all pages) plus any URLs in raw/blog/extra-urls.txt.
blog.cloudflare.com serves Markdown for `Accept: text/markdown`, so no scraper is needed.
"""
import os
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
OUT = os.path.join(ROOT, "raw", "blog")
TAGS = ["web3", "ethereum", "x402", "payments", "ipfs", "cryptography", "randomness"]
POST = re.compile(r"\((https://blog\.cloudflare\.com/[a-z0-9-]+/)\)")
SKIP = re.compile(r"blog\.cloudflare\.com/(tag|author|page|search|rss|_)")


def get(url):
    req = urllib.request.Request(url, headers={"Accept": "text/markdown", "User-Agent": "kb-mirror"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.read().decode("utf-8", "replace")
    except Exception as e:
        print("fail", url, e, file=sys.stderr)
        return ""


def tag_posts(tag):
    posts, n = [], 1
    while True:
        url = f"https://blog.cloudflare.com/tag/{tag}/" + (f"page/{n}/" if n > 1 else "")
        body = get(url)
        found = [u for u in POST.findall(body) if not SKIP.search(u)]
        new = [u for u in dict.fromkeys(found) if u not in posts]
        if not new:
            return posts
        posts += new
        n += 1


def save(url):
    body = get(url)
    if body:
        with open(os.path.join(OUT, url.rstrip("/").rsplit("/", 1)[1] + ".md"), "w") as f:
            f.write(body)


def main():
    os.makedirs(OUT, exist_ok=True)
    index = {}
    for tag in TAGS:
        for u in tag_posts(tag):
            index.setdefault(u, []).append(tag)
    extra = os.path.join(OUT, "extra-urls.txt")
    if os.path.exists(extra):
        for u in open(extra).read().split():
            index.setdefault(u if u.endswith("/") else u + "/", []).append("extra")
    with ThreadPoolExecutor(8) as ex:
        list(ex.map(save, index))
    with open(os.path.join(OUT, "index.tsv"), "w") as f:
        f.write("url\ttags\n" + "".join(f"{u}\t{','.join(t)}\n" for u, t in sorted(index.items())))
    print(len(index), "posts")


if __name__ == "__main__":
    main()
