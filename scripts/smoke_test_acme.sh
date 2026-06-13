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
curl -fsS "${BASE_URL}/shipments?q=contoso" | grep -q "ACM-1001"
curl -fsS "${BASE_URL}/internal/config" | grep -q "FAKE_ACME_DEMO_KEY_DO_NOT_USE"
curl -fsS -c /tmp/acme-cookies.txt -d 'username=jane.doe&password=Spring2026!' "${BASE_URL}/login" >/dev/null
curl -fsS -b /tmp/acme-cookies.txt "${BASE_URL}/portal" | grep -q "Operations Bulletin"
curl -fsS -b /tmp/acme-cookies.txt "${BASE_URL}/portal/shipment?id=1" | grep -q "ACM-1001"
curl -sS -b /tmp/acme-cookies.txt "${BASE_URL}/portal/shipment?id=4" | grep -q "Access denied"
curl -fsS -b /tmp/acme-cookies.txt "${BASE_URL}/portal/shipment?id=4&mode=lab" | grep -q "IDOR Training Lab"
curl -fsS -c /tmp/acme-admin-cookies.txt -d 'username=sam.admin&password=ChangeMe123!' "${BASE_URL}/login" >/dev/null
curl -fsS -b /tmp/acme-admin-cookies.txt "${BASE_URL}/admin/tickets" | grep -q "Stored XSS Lab"
curl -fsS -b /tmp/acme-admin-cookies.txt "${BASE_URL}/admin/activity" | grep -q "Audit events"
curl -fsS -b /tmp/acme-admin-cookies.txt "${BASE_URL}/portal/shipment?id=4" | grep -q "ACM-1004"
python3 -m json.tool /tmp/acme-health.json >/dev/null

echo "ACME smoke test passed"
