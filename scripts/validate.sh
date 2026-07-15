#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
BUNDLED_PYTHON="$HOME/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"
PYTHON_BIN="${PYTHON:-python3}"

if [[ -x "$BUNDLED_PYTHON" ]]; then
  PYTHON_BIN="$BUNDLED_PYTHON"
fi

cd "$REPO_DIR"

bash -n scripts/validate.sh
"$PYTHON_BIN" scripts/validate-public.py

VALIDATOR="$HOME/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py"
if [[ -f "$VALIDATOR" ]]; then
  if ! "$PYTHON_BIN" -c 'import yaml' >/dev/null 2>&1; then
    YAML_SHIM=""
    for candidate in /private/tmp/*yaml-shim; do
      if [[ -d "$candidate" ]] && PYTHONPATH="$candidate" "$PYTHON_BIN" -c 'import yaml' >/dev/null 2>&1; then
        YAML_SHIM="$candidate"
        break
      fi
    done
    if [[ -n "$YAML_SHIM" ]]; then
      PYTHONPATH="$YAML_SHIM" "$PYTHON_BIN" "$VALIDATOR" plugins/fabricator
    else
      "$PYTHON_BIN" "$VALIDATOR" plugins/fabricator
    fi
  else
    "$PYTHON_BIN" "$VALIDATOR" plugins/fabricator
  fi
fi
