#!/bin/bash
# Double-click this to preview the site locally with live sheet data working.
# Opening index.html directly (double-click / file://) blocks the fetches
# to Google Sheets (CORS), so language/region switching silently falls back
# to English. Serving it over http:// (what this does) fixes that.

cd "$(dirname "$0")"
PORT=8934

# If something's already serving on this port (e.g. a previous run left
# running), just reuse it instead of failing to bind.
if ! lsof -i ":$PORT" >/dev/null 2>&1; then
  python3 -m http.server "$PORT" >/dev/null 2>&1 &
  sleep 1
fi

open "http://localhost:$PORT/index.html"

echo "Serving at http://localhost:$PORT/ — leave this window open while previewing."
echo "Close this window (or press Ctrl+C) to stop the server."
wait
