# 🚀 DevOps / CI-CD PR Template

## Summary
> What does this PR do? (1-2 sentences)

## Type of Change
- [ ] 🔄 CI/CD pipeline update
- [ ] 🐳 Docker / container change
- [ ] ☸️  Kubernetes / orchestration change
- [ ] 🏗️  Infrastructure as Code (IaC)
- [ ] 🔒 Security / secrets update
- [ ] 📦 Dependency / image version bump
- [ ] 🐛 Bug fix

## Changed Files
<!-- List key files touched -->
- `.github/workflows/`
- `Dockerfile`
- `docker-compose.yml`
- `k8s/`
- `terraform/`

## Pipeline Changes
| Job / Stage | Before | After |
|-------------|--------|-------|
|             |        |       |

## Infrastructure Changes
- [ ] New resources created
- [ ] Existing resources modified
- [ ] Resources destroyed
- [ ] Cost impact estimated: **~$___/month**

## DevOps Checklist
- [ ] Pipeline tested end-to-end
- [ ] Secrets stored in vault / GitHub Secrets (not in code)
- [ ] Rollback strategy defined
- [ ] Staging environment tested before production
- [ ] Downtime estimated & communicated: **~___ min**
- [ ] Health checks / smoke tests in place
- [ ] Monitoring / alerts updated if needed
- [ ] Documentation updated (runbooks, README)

## Testing
- [ ] CI pipeline passes on this branch
- [ ] Deployed to staging and verified
- [ ] Load / stress test run (if infra change)

## Deployment Plan
1. Merge PR
2. Monitor deployment in staging
3. Approve production rollout
4. Verify health checks pass
5. Rollback step: `kubectl rollout undo ...` / re-run previous workflow

## Related Issues
Closes #

## Notes for Reviewer
> Anything specific to look at?