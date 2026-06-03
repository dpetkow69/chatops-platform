#!/usr/bin/env bash
set -euo pipefail

readonly SERVICES=(
  "gateway:8765"
  "auth-service:8001"
  "chat-service:8002"
)

PASS=0
FAIL=0

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"; }

check_service() {
  local name="$1"
  local port="$2"
  if curl -sf --max-time 3 "http://localhost:${port}/health" > /dev/null 2>&1; then
    log "✓ ${name} healthy"
    ((PASS++))
  else
    log "✗ ${name} UNHEALTHY on port ${port}"
    ((FAIL++))
  fi
}

log "Starting ChatOps health check..."
for svc in "${SERVICES[@]}"; do
  check_service "${svc%%:*}" "${svc##*:}"
done

log "Results: ${PASS} healthy, ${FAIL} unhealthy"

if [[ $FAIL -gt 0 ]]; then
  log "HEALTH CHECK FAILED"
  exit 1
fi

log "All services healthy!"
exit 0
