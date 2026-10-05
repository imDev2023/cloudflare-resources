#!/usr/bin/env bash
# Catalog every public repo in the cloudflare GitHub org, and save the README of the
# 80 most-starred active (non-archived, non-fork) repos. Needs an authenticated `gh`.
set -euo pipefail
OUT="$(cd "$(dirname "$0")/.." && pwd)/raw/github"
mkdir -p "$OUT/readmes"
gh api --paginate "orgs/cloudflare/repos?per_page=100&type=public" \
  --jq '.[] | [.name, (.description // "" | gsub("[\t\n]"; " ")), (.language // ""), .stargazers_count, .pushed_at[:10], .archived, .fork, ((.topics // []) | join(","))] | @tsv' \
  | sort -t$'\t' -k4,4nr > "$OUT/repos.tsv.tmp"
{ printf 'name\tdescription\tlanguage\tstars\tpushed\tarchived\tfork\ttopics\n'; cat "$OUT/repos.tsv.tmp"; } > "$OUT/repos.tsv"
rm "$OUT/repos.tsv.tmp"
awk -F'\t' 'NR>1 && $6=="false" && $7=="false" {print $1}' "$OUT/repos.tsv" | head -80 | while read -r repo; do
  gh api "repos/cloudflare/$repo/readme" -H "Accept: application/vnd.github.raw" > "$OUT/readmes/$repo.md" 2>/dev/null || rm -f "$OUT/readmes/$repo.md"
done
echo "$(($(wc -l < "$OUT/repos.tsv") - 1)) repos, $(ls "$OUT/readmes" | wc -l | tr -d ' ') readmes"
