#!/usr/bin/env python3
"""Write navigation.md: the docs sidebar (raw/nav/home-sidebar.json) with page counts from raw/docs/,
the synthesized file covering each entry, and every product in raw/docs/llms.txt that the sidebar omits."""
import json
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
DOCS = os.path.join(ROOT, "raw", "docs")
BASE = "https://developers.cloudflare.com/"
COVER = {
    "Get started": "platform-and-tooling.md", "Developer Tools": "platform-and-tooling.md",
    "Compute": "build/01-compute.md", "AI": "build/02-ai.md", "Storage & Database": "build/03-storage-database.md",
    "Media": "build/04-media.md", "Application Security": "protect-connect/01-application-security.md",
    "Cloudflare One": "protect-connect/02-cloudflare-one.md", "Domains & DNS": "protect-connect/03-domains-dns.md",
    "Networking": "protect-connect/04-networking.md", "Monetize": "protect-connect/05-monetize.md",
    "Delivery & Performance": "protect-connect/06-delivery-performance.md", "Observe": "manage-observe.md",
}


def pages(url):
    rel = url.replace(BASE, "").split("?")[0].strip("/")
    if not rel:
        return 1
    return sum("index.md" in fs for _, _, fs in os.walk(os.path.join(DOCS, rel)))


def main():
    nav = json.load(open(os.path.join(ROOT, "raw", "nav", "home-sidebar.json")))
    out = ["# Docs navigation map", "",
           "The sidebar of https://developers.cloudflare.com/ with every dropdown expanded, as captured on the date in `raw/docs/_manifest.json`.",
           "Page counts are the mirrored pages under each URL in `raw/docs/`; the last column is the synthesized file that covers the entry.",
           "Regenerate with `python3 scripts/build-nav.py`.", ""]
    seen = set()

    def walk(items, depth, cover):
        for it in items:
            c = COVER.get(it["label"], cover)
            if "url" in it:
                seen.add(it["url"].replace(BASE, "").split("/")[0])
                out.append(f"{'  ' * depth}- [{it['label']}]({it['url']}) - {pages(it['url'])} pages - `{c}`")
            else:
                out.append(f"{'  ' * depth}- **{it['label']}** - `{c}`")
            walk(it.get("children", []), depth + 1, c)

    for g in nav:
        out += [f"## {g['group']}", ""]
        walk(g["items"], 0, COVER.get(g["group"]))
        out.append("")
    llms = open(os.path.join(DOCS, "llms.txt")).read()
    out += ["## Products not in the sidebar", "",
            "These are listed in https://developers.cloudflare.com/llms.txt but have no sidebar entry; see `other-products.md` unless another file is named in the README.", ""]
    section = None
    for line in llms.splitlines():
        if line.startswith("## "):
            section = line[3:]
        m = re.match(r"- \[(.+?)\]\(https://developers\.cloudflare\.com/([^/]+)/llms\.txt\): (.*)", line)
        if m and m.group(2) not in seen:
            out.append(f"- [{m.group(1)}]({BASE}{m.group(2)}/) ({section}) - {pages(BASE + m.group(2) + '/')} pages - {m.group(3)}")
    total = sum("index.md" in fs for _, _, fs in os.walk(DOCS))
    out += ["", f"Total mirrored docs pages: {total}.", ""]
    open(os.path.join(ROOT, "navigation.md"), "w").write("\n".join(out))


if __name__ == "__main__":
    main()
