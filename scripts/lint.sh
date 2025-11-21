#!/bin/bash
set -e

echo "Running ruff..."
ruff check src tests

echo "Running mypy..."
mypy src tests

echo "Running yamllint..."
# yamllint .  # Uncomment when yamllint is configured/installed
echo "yamllint skipped for now (install and configure if needed)"
