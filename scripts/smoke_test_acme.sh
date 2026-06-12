#!/usr/bin/env bash
set -euo pipefail

PORT="${ACME_PORT:-8000}"
HOST="${ACME_HOST:-127.0.0.1}"
BASE_URL="http://${HOST}:${PORT}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

python3 target-site/acme/app/server.py > /tmp/acme-smoke.log 2>&1 &
pid=$!
trap 'kill "$pid" >/dev/null 2>&1 || true' EXIT

for _ in {1..20}; do
  if curl -fsS "${BASE_URL}/health" >/tmp/acme-health.json 2>/dev/null; then
    break
  fi
  sleep 0.2
done

curl -fsS "${BASE_URL}/" | grep -q "ACME keeps smart supply chains moving"
curl -fsS "${BASE_URL}/robots.txt" | grep -q "Disallow: /lab-notes"
curl -fsS "${BASE_URL}/vendor?q=contoso" | grep -q "Contoso Sensors"
curl -fsS "${BASE_URL}/vendor?q=telemetry" | grep -q "vendor-table"
curl -fsS "${BASE_URL}/vendor?mode=lab&q=%27%20OR%20%271%27%3D%271" | grep -q "Northwind Freight"
curl -fsS -c /tmp/acme-cookies.txt -d 'username=jane.doe&password=Spring2026!' "${BASE_URL}/login" >/dev/null
curl -fsS -b /tmp/acme-cookies.txt "${BASE_URL}/portal" | grep -q "Operations Bulletin"
python3 -m json.tool /tmp/acme-health.json >/dev/null

echo "ACME smoke test passed"
