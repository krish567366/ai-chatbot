SHELL := /usr/bin/bash

.PHONY: dev stop rebuild test fmt typecheck

dev:
	docker compose up -d --build

stop:
	docker compose down

rebuild:
	docker compose build --no-cache

fmt:
	docker compose exec backend bash -lc "ruff check --fix . && black . && isort ." || true
	docker compose exec frontend bash -lc "pnpm prettier -w ." || true

backend-test:
	docker compose exec backend bash -lc "pytest -q"

frontend-test:
	docker compose exec frontend bash -lc "pnpm test -- --run"

test: backend-test frontend-test

typecheck:
	docker compose exec backend bash -lc "mypy app" || true
	docker compose exec frontend bash -lc "pnpm tsc -noEmit" || true