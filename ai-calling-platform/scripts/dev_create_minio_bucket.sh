#!/usr/bin/env bash
set -euo pipefail

MC_BIN=${MC_BIN:-mc}
$MC_BIN alias set local http://localhost:9000 minio minio123
$MC_BIN mb -p local/recordings || true
$MC_BIN ls local