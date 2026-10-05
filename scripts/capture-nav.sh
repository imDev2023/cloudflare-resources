#!/usr/bin/env bash
# Capture the docs sidebar with every dropdown expanded into raw/nav/home-sidebar.json and .md.
# Uses agent-browser in its own named session and closes only that session.
set -euo pipefail
OUT="$(cd "$(dirname "$0")/.." && pwd)/raw/nav"
S=cf-kb-nav
mkdir -p "$OUT"
agent-browser --session $S open https://developers.cloudflare.com/ >/dev/null
agent-browser --session $S wait --load networkidle >/dev/null
for _ in 1 2 3; do
  agent-browser --session $S eval "(() => { const b=[...document.querySelectorAll('nav[aria-label=\"Documentation\"] [aria-expanded=false]')]; b.forEach(x=>x.click()); return b.length })()" >/dev/null
  sleep 1
done
cat <<'JS' | agent-browser --session $S eval --stdin > "$OUT/home-sidebar.raw"
(() => {
  const nav = document.querySelector('nav[aria-label="Documentation"] [data-nb-sidebar]');
  const walk = (ul) => [...ul.children].map(li => {
    const a = li.querySelector(':scope > a');
    if (a) return { label: a.textContent.trim(), url: new URL(a.getAttribute('href'), location.href).href };
    const btn = li.querySelector(':scope > div > button');
    const sub = li.querySelector(':scope > div [data-nb-sidebar-sublist], :scope > div ul');
    return { label: btn ? btn.textContent.trim() : '?', children: sub ? walk(sub) : [] };
  });
  return [...nav.children].map(g => ({
    group: (g.querySelector(':scope > p') || {}).textContent?.trim() || null,
    items: g.querySelector(':scope > ul') ? walk(g.querySelector(':scope > ul')) : []
  }));
})()
JS
agent-browser --session $S close >/dev/null
python3 - "$OUT" <<'PY'
import json, os, sys
out = sys.argv[1]
d = json.loads(open(os.path.join(out, "home-sidebar.raw")).read())
d = json.loads(d) if isinstance(d, str) else d
json.dump(d, open(os.path.join(out, "home-sidebar.json"), "w"), indent=1)
lines = []
def pr(items, ind=0):
    for it in items:
        lines.append("  " * ind + "- " + it["label"] + (" " + it["url"] if "url" in it else ""))
        pr(it.get("children", []), ind + 1)
for g in d:
    lines.append("## " + str(g["group"]))
    pr(g["items"])
open(os.path.join(out, "home-sidebar.md"), "w").write("\n".join(lines) + "\n")
os.remove(os.path.join(out, "home-sidebar.raw"))
PY
echo "sidebar captured"
