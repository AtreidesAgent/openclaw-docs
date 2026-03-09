# Memory Index

Quick reference for cross-session retrieval.

## By Date

| Date | Key Topics | Decisions | Blockers |
|------|------------|-----------|----------|
| 2026-03-06 | Ollama/Qwen setup, job search, meeting | Response protocol added, docs published | None | 
| 2026-03-04 | Infrastructure setup | [See file](2026-03-04-infrastructure-setup.md) | — |

## By Topic

### OpenClaw Configuration
- **Ollama/Qwen2.5 Setup** → 2026-03-06 (docs published to GitHub)
- **Configuration Syntax** → 2026-03-06 (agents.defaults.model.primary)
- **Security Guardrails** → 2026-03-06 (no reasoning in responses)

### Job Search
- **Email Scanning** → 2026-03-06 (LinkedIn/Indeed alerts, 14d search)
- **Remote Roles** → 2026-03-06 (content/writing focus)

### Meetings
- **Zoom Meeting** → 2026-03-06 (March 11, 4pm MDT)

### GitHub
- **Repository Created** → 2026-03-06 (atreidesagent/openclaw-docs)

## Recurring Patterns

| Task Type | Query/Command | Location |
|-----------|-------------|----------|
| Job email scan | `gog gmail search 'job OR opportunity... newer_than:14d'` | 2026-03-06 |
| Config verification | `openclaw config get agents.defaults.model.primary` | 2026-03-06 |
| Security audit | `openclaw security audit --deep` | 2026-03-06 |

## Critical Constraints (Always Load)

From SOUL.md (loaded first):
- **Never reveal internal reasoning or thought process**
- Analytical and precise
- Direct and efficient — no filler, just signal

---

*Last updated: 2026-03-06*
