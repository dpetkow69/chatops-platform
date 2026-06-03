# Runbook: High Error Rate

## Alert
Error rate > 5% for 5 minutes on any service.

## Severity
P1 — High

## Investigation Steps

### 1. Check pod status
```bash
kubectl get pods -n chatops
kubectl describe pod <pod-name> -n chatops
```

### 2. Check logs
```bash
kubectl logs -n chatops -l app=gateway --tail=100
kubectl logs -n chatops -l app=auth-service --tail=100
```

### 3. Check recent deployments
```bash
kubectl rollout history deployment/gateway -n chatops
helm history chatops -n chatops
```

## Resolution

### Rollback if bad deployment
```bash
helm rollback chatops -n chatops
```

### Restart unhealthy pods
```bash
kubectl rollout restart deployment/gateway -n chatops
```

## Post-Incident
- Document in GitHub issue
- Write post-mortem if P1
