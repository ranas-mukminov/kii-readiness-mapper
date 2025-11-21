#!/bin/bash
set -e

echo "Running bandit..."
bandit -r src -c pyproject.toml

echo "Running pip-audit..."
# pip-audit # Uncomment if pip-audit is installed
echo "pip-audit skipped for now"
