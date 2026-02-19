# 🔧 Backend / API PR Template

## Summary
> What does this PR do? (1-2 sentences)

## Type of Change
- [ ] ✨ New endpoint / feature
- [ ] 🐛 Bug fix
- [ ] 🔒 Security fix
- [ ] ♻️  Refactor
- [ ] 🗃️  Database migration
- [ ] 🧪 Test update

## Changed Files
<!-- List key files touched -->
- `api/routes/`
- `api/controllers/`
- `api/models/`

## API Changes
| Method | Endpoint | Description | Breaking? |
|--------|----------|-------------|-----------|
|        |          |             | Yes / No  |

## Database Changes
- [ ] New migration added
- [ ] Migration is reversible
- [ ] Indexes updated if needed
- Migration file: `migrations/`

## Backend Checklist
- [ ] Input validation on all new endpoints
- [ ] Authentication / authorization enforced
- [ ] Error responses follow standard format
- [ ] No sensitive data exposed in responses
- [ ] Rate limiting considered
- [ ] Logging added for key actions

## Testing
- [ ] Unit tests added / updated
- [ ] Integration tests cover new routes
- [ ] Tested with Postman / curl
- [ ] Edge cases verified (empty input, large payload, etc.)

## Related Issues
Closes #

## Notes for Reviewer
> Anything specific to look at?