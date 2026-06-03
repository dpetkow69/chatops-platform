# ChatOps Platform

A microservices chat platform built as a hands-on DevOps learning project.
Evolves from local Docker Compose to production AWS EKS with GitOps.

## Current Stage
✅ Stage 2: Containerized with Docker Compose
⏳ Stage 3: CI/CD with GitHub Actions (coming next)

## Architecture
## Quick Start
```bash
git clone git@github.com:dpetkow69/chatops-platform.git
cd chatops-platform
cp .env.example .env
docker compose up --build
```

## Test the API
```bash
# Register
curl -X POST http://localhost:8765/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username":"drago","email":"you@email.com","password":"secret123"}'

# Login
curl -X POST http://localhost:8765/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"drago","password":"secret123"}'
```

## Tech Stack
- Services: Python 3.12 / FastAPI
- Runtime: Docker + Docker Compose
- Database: PostgreSQL 16
- Cache: Redis 7
- Metrics: Prometheus (via /metrics endpoint)
