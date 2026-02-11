# AI Calling Platform (Monorepo)

Production-oriented, multi-tenant no-code SaaS to build automated AI calling agents (outbound + inbound).

## Quickstart

Prereqs: Docker, Docker Compose, Node 18+, Python 3.11+

```bash
make dev
# API: http://localhost:8000  (docs at /docs)
# Frontend: http://localhost:5173
```

## Make Targets

```bash
make dev         # start local stack (compose)
make stop        # stop containers
make rebuild     # rebuild all images
make test        # run unit tests (backend + frontend)
make fmt         # format code
make typecheck   # mypy + tsc
```

## Structure

- backend: FastAPI, Celery, SQLAlchemy, Alembic
- frontend: React + Vite + Tailwind + React Flow
- infra: Docker, Terraform, Helm, GitHub Actions
- tests: unit, contract (OpenAPI), e2e (Playwright), load (k6)

## Default Admin

- username: admin@example.com
- password: admin123 (dev only)

## Notes

- Uses Postgres, Redis, MinIO (S3), and local Twilio webhook URLs via configurable base.
- Replace dummy secrets in `.env` before running in any shared environment.