#!/usr/bin/env bash
# Refresh every raw source. Needs an authenticated `gh` for the GitHub catalog.
# The sidebar capture uses agent-browser (its own named session).
set -euo pipefail
cd "$(dirname "$0")"
python3 fetch-docs.py
python3 fetch-api.py
python3 fetch-blog.py
./fetch-repos.sh
./capture-nav.sh
python3 build-nav.py
