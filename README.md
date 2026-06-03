# ChatOps Platform

A production-grade microservices chat platform built as a hands-on DevOps learning project.

## Architecture
Client → Gateway (:8765) → Auth Service (:8001)
→ Chat Service (:8002)
PostgreSQL :5432 | Redis :6379

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Services | Python 3.12 / FastAPI |
| Containers | Docker + Docker Compose |
| Orchestration | Kubernetes (minikube / EKS) |
| Package Manager | Helm |
| GitOps | ArgoCD |
| CI/CD | GitHub Actions |
| IaC | Terraform |
| Monitoring | Prometheus + Grafana |
| Logging | Loki + Promtail |
| Security | Kyverno + NetworkPolicies |
| Cloud | AWS (VPC, EKS, S3) |

## Quick Start

```bash
git clone git@github.com:dpetkow69/chatops-platform.git
cd chatops-platform
cp .env.example .env
docker compose up --build
```

API: http://localhost:8765
Docs: http://localhost:8765/docs

## API Usage

```bash
curl -X POST http://localhost:8765/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username":"drago","email":"you@email.com","password":"secret123"}'

TOKEN=$(curl -s -X POST http://localhost:8765/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"drago","password":"secret123"}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['access_token'])")

curl -X POST http://localhost:8765/chat/messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"content":"Hello ChatOps!","room":"general"}'
```

## Milestones

- [x] Stage 2: Docker Compose
- [x] Stage 3: CI/CD pipeline
- [x] Stage 4: Kubernetes
- [x] Stage 5: Monitoring and logging
- [x] Stage 6: Infrastructure as Code
- [x] Stage 7: AWS deployment
- [x] Stage 8: GitOps with ArgoCD
- [x] Stage 9: Security hardening
- [x] Stage 10: Production ready

## Lessons Learned

- Network policies break port-forward — always test after applying
- Docker Desktop on WSL2 needs explicit docker group membership
- ArgoCD requires resources to be in git before creating the Application
- NAT Gateway charges by the hour — always terraform destroy after testing
- Kyverno policies in Audit mode first, then Enforce after validation
