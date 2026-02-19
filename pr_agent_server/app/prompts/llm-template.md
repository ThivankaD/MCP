# 🤖 LLM / ML PR Template

## Summary
> What does this PR do? (1-2 sentences)

## Type of Change
- [ ] 🧠 New model / LLM integration
- [ ] 📝 Prompt update
- [ ] 🔁 RAG / retrieval change
- [ ] 📊 Training / fine-tuning update
- [ ] 🐛 Bug fix
- [ ] ⚡ Performance / cost optimization
- [ ] 🧪 Evaluation update

## Changed Files
<!-- List key files touched -->
- `ml/`
- `models/`
- `prompts/`

## Model / Prompt Changes
| Item             | Before | After |
|------------------|--------|-------|
| Model            |        |       |
| Temperature      |        |       |
| Max tokens       |        |       |
| System prompt    |        |       |

## Prompt Diff
**Old Prompt:**
```
(paste old prompt here)
```
**New Prompt:**
```
(paste new prompt here)
```

## Evaluation Results
| Metric         | Before | After | Δ |
|----------------|--------|-------|---|
| Accuracy       |        |       |   |
| Hallucination  |        |       |   |
| Latency (ms)   |        |       |   |
| Cost / 1K req  |        |       |   |

## LLM Checklist
- [ ] Prompt tested against edge cases
- [ ] Output validation / parsing robust
- [ ] Guardrails / content filtering in place
- [ ] Token usage measured & acceptable
- [ ] Retry logic with backoff in place
- [ ] Eval dataset updated
- [ ] No API keys committed to repo

## Testing
- [ ] Eval script run and results recorded
- [ ] Manual spot-checks done
- [ ] Regression tests passing

## Related Issues
Closes #

## Notes for Reviewer
> Anything specific to look at?