ChatOps Platform
A production-grade microservices chat platform built as a hands-on DevOps learning project. Evolves from local Docker Compose to Kubernetes with full GitOps, monitoring, and security.
Architecture
Client → Gateway (:8765) → Auth Service (:8001)
                          → Chat Service (:8002)
PostgreSQL :5432
Redis      :6379
Tech Stack
LayerTechnologyServicesPython 3.12 / FastAPIContainersDocker + Docker ComposeOrchestrationKubernetes (minikube / EKS)Package ManagerHelmGitOpsArgoCDCI/CDGitHub ActionsIaCTerraformMonitoringPrometheus + GrafanaLoggingLoki + PromtailSecurityKyverno + NetworkPoliciesCloudAWS (VPC, EKS, S3)
Quick Start
bashgit clone git@github.com:dpetkow69/chatops-platform.git
cd chatops-platform
cp .env.example .env
docker compose up --build
API: http://localhost:8765
Docs: http://localhost:8765/docs
API Usage
bash# Register
curl -X POST http://localhost:8765/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username":"drago","email":"you@email.com","password":"secret123"}'

# Login and get token
TOKEN=$(curl -s -X POST http://localhost:8765/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"drago","password":"secret123"}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['access_token'])")

# Send message
curl -X POST http://localhost:8765/chat/messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"content":"Hello ChatOps!","room":"general"}'

# Get messages
curl http://localhost:8765/chat/messages \
  -H "Authorization: Bearer $TOKEN"
CI/CD Pipeline
git push → GitHub Actions
  ├── Test Gateway Service
  └── Build and Push to GHCR
        └── ghcr.io/dpetkow69/chatops-platform/gateway:SHA
GitOps Flow
git push → ArgoCD detects change → kubectl apply → cluster updated
Project Structure
chatops-platform/
├── services/
│   ├── gateway/
│   ├── auth-service/
│   └── chat-service/
├── infra/terraform/
├── k8s/base/
├── helm/chatops/
├── monitoring/
├── scripts/
├── docs/runbooks/
└── .github/workflows/
Milestones

 Stage 2: Docker Compose
 Stage 3: CI/CD pipeline
 Stage 4: Kubernetes
 Stage 5: Monitoring and logging
 Stage 6: Infrastructure as Code
 Stage 7: AWS deployment
 Stage 8: GitOps with ArgoCD
 Stage 9: Security hardening
 Stage 10: Production ready

Lessons Learned

Network policies break port-forward — always test after applying
Docker Desktop on WSL2 needs explicit docker group membership
ArgoCD requires resources to be in git before creating the Application
NAT Gateway charges by the hour — always terraform destroy after testing
Kyverno policies in Audit mode first, then Enforce after validation