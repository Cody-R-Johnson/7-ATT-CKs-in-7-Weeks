#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DATA_DIR="$ROOT_DIR/target-site/acme/data"
HOST="${ACME_HOST:-127.0.0.1}"
PORT="${ACME_PORT:-8000}"

if curl -fsS --max-time 1 "http://${HOST}:${PORT}/health" >/dev/null 2>&1; then
  echo "ACME is still running at http://${HOST}:${PORT}."
  echo "Stop it with Ctrl+C, then run this reset command again."
  exit 1
fi

generated_files=(
  "$DATA_DIR/access.log"
  "$DATA_DIR/support_tickets.jsonl"
  "$DATA_DIR/acme.sqlite"
  "$DATA_DIR/acme.sqlite-journal"
  "$DATA_DIR/acme.sqlite-shm"
  "$DATA_DIR/acme.sqlite-wal"
)

removed=0
for file in "${generated_files[@]}"; do
  if [[ -e "$file" ]]; then
    rm -f -- "$file"
    echo "Removed ${file#"$ROOT_DIR/"}"
    removed=1
  fi
done

if [[ "$removed" -eq 0 ]]; then
  echo "ACME lab data is already clean."
else
  echo "ACME lab data reset complete."
fi

echo "Run ./scripts/run_acme.sh to create a fresh starter database."
