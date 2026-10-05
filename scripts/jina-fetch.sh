#!/usr/bin/env bash
# Fetch one non-Cloudflare-docs URL as Markdown into raw/external/ through the Jina reader.
# Usage: JINA_API_KEY=... xargs -P 6 -I{} scripts/jina-fetch.sh {} < raw/external/urls.txt
set -euo pipefail
url="$1"
out="$(cd "$(dirname "$0")/.." && pwd)/raw/external/$(echo "$url" | sed -E 's#^https?://##; s#[/?=&]+#_#g; s#_$##').md"
curl -sSf "https://r.jina.ai/$url" -H "Authorization: Bearer ${JINA_API_KEY:?}" -H "X-Return-Format: markdown" -o "$out" \
  && echo "ok $url" || { rm -f "$out"; echo "FAIL $url"; }
