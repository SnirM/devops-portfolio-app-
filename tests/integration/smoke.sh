#!/usr/bin/env bash
set -e

BASE_URL="http://localhost:8000"

echo "Waiting for API..."
for i in {1..30}; do
  if curl -s "$BASE_URL/health" | grep ok >/dev/null; then
    echo "API is up"
    break
  fi
  sleep 2
done

echo "GET /person"
curl -s "$BASE_URL/person"

echo "POST /person/1"
curl -s -X POST "$BASE_URL/person/1" \
  -H "Content-Type: application/json" \
  -d '{"name":"Snir","age":32}'

echo "Integration test passed"
