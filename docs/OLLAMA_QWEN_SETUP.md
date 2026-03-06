# Ollama & Qwen2.5 Local Model Setup Guide

A troubleshooting reference for running OpenClaw with local Ollama models (Qwen2.5).

---

## Ollama Setup & Connectivity

Before configuring OpenClaw, ensure Ollama is properly set up and accessible:

### Verify Ollama is Running

```bash
# List available models
ollama list

# Check active running models
ollama ps
```

### Pull Required Models

```bash
# Pull Qwen2.5 variants (choose based on your hardware)
ollama pull qwen2.5:14b   # Larger model, better quality
ollama pull qwen2.5:7b    # Smaller model, faster inference
```

### Verify Network Accessibility

```bash
# Check Ollama is listening on default port (11434)
curl http://localhost:11434

# Expected response: "Ollama is running"
```

### Remote/Tailscale Setup

- If running Ollama on a remote machine or Tailscale network:
  - Confirm the Ollama host is reachable from OpenClaw's machine
  - Use the full Tailscale IP or hostname (e.g., `http://100.x.x.x:11434`)
  - Ensure Ollama is configured to listen on `0.0.0.0:11434` (not just localhost)

---

## OpenClaw Model Configuration

### Primary Model Setting

**Correct config path:** `agents.defaults.model.primary`

```bash
# ❌ WRONG:
models.primary
models.fallback

# ✅ CORRECT:
agents.defaults.model.primary
```

Set your primary local model:

```bash
openclaw config set agents.defaults.model.primary ollama/qwen2.5:14b
```

### Fallback Models

- Fallbacks live at `agents.defaults.model.fallbacks` as a JSON array
- Order matters — place your MOR-staked model first if prioritizing it

```bash
openclaw config set agents.defaults.model.fallbacks '["ollama/qwen2.5:7b", "anthropic/claude-4.1-sonnet"]'
```

### Model Allowlist

**Critical:** Every model you want to use must be registered in the allowlist, or requests will fail with HTTP 400.

```bash
# Check current allowlist
openclaw config get agents.defaults.models

# Add models to allowlist
openclaw config set agents.defaults.models '["ollama/qwen2.5:14b", "ollama/qwen2.5:7b", "anthropic/claude-4.1-sonnet"]'
```

### Post-Restart Verification

**⚠️ After any gateway restart, verify your settings:**

```bash
# Check primary model didn't revert to default (e.g., anthropic/claude)
openclaw config get agents.defaults.model.primary

# Verify allowlist is intact
openclaw config get agents.defaults.models
```

---

## Heartbeat & Cron Model Assignment

### Heartbeat Tasks

- Use your **lightest local model** (e.g., `ollama/qwen2.5:7b`) for heartbeat tasks
- This conserves tokens and resources
- Configure in `HEARTBEAT.md` or via agent memory

### Cron Jobs

Each cron job has its own `--model` flag — the global default doesn't automatically apply.

```bash
# Example cron with local model
openclaw cron create --name daily-check \
  --schedule "0 9 * * *" \
  --model ollama/qwen2.5:7b \
  -- "heartbeat"
```

### Timeout Configuration

**Always specify `--timeout-seconds` on cron jobs**.

- Default (60–180s) is too short for Ollama on modest hardware
- Recommended: `300` (5 minutes) or higher depending on your hardware

```bash
openclaw cron create --name slow-task \
  --schedule "0 */6 * * *" \
  --model ollama/qwen2.5:14b \
  --timeout-seconds 300 \
  -- "long-running-task"
```

### Verify Cron Status

Don't trust agent-reported completion — check directly:

```bash
# List all cron jobs
openclaw cron list

# Check specific run status
openclaw cron runs --id <cron-job-id>
```

---

## Fallback Chain Logic

### When Do Fallbacks Trigger?

Fallbacks **only** activate on:
- ⏱️ Timeout
- 🔐 Authentication failure

They **do not** trigger on:
- ❌ Quality issues
- ❌ Hallucinations
- ❌ Incorrect responses

### Fallback Security Warning

**⚠️ Security Risk:** Placing small local models in fallback position with web tools enabled creates a prompt injection risk (per OpenClaw's security audit).

**Recommended fallback order:**
1. MOR-staked cloud model (trusted, higher quality)
2. Larger local model (e.g., qwen2.5:14b)
3. Smallest local model (e.g., qwen2.5:7b) — avoid web tools here

---

## Agent Behavior & Trust

### Verify Agent Actions

**Always verify agent-reported file creation:**

```bash
# Check files actually exist
ls -la /path/to/workspace/

# Inspect file contents
cat /path/to/file.txt
```

> _Note: Agents (especially Hawat) may fabricate completion status in reports._

### Memory-Based Guardrails

Set hard rules in agent memory for autonomous actions they must **never** perform:

```markdown
## NEVER AUTONOMOUSLY:
- Change models (primary, fallback, allowlist)
- Modify sandbox settings
- Reorder fallback chains
- Delete files without confirmation
```

### Post-Config Verification

After **any** agent config change session:

```bash
# Confirm actual state matches intent
openclaw config get agents.defaults.model.primary
openclaw config get agents.defaults.model.fallbacks
openclaw config get agents.defaults.models
```

### Source of Truth

| Trust Level | Command |
|-------------|---------|
| ✅ Primary | `openclaw cron list` |
| ✅ Primary | `openclaw cron runs --id <id>` |
| ⚠️ Secondary | Agent summaries/reports |

---

## Security Checklist

Run after any significant configuration change:

```bash
# Deep security audit
openclaw security audit --deep
```

### Telegram Policy Lockdown

For agents with `exec`/`write` tools:

```bash
# Lock to allowlist/pairing (not open access)
openclaw config set agents.<agent>.telegram.policy allowlist
```

### Cautious Tool Pairing

- Be cautious enabling `web_search` alongside small fallback models
- Small models are more susceptible to prompt injection via search results

---

## RSS & Corpus Scraping (Bonus)

When scraping content for local corpus/RSS feeds:

### WordPress RSS

- **Use RSS feed, not HTML:** `/author/slug/feed/`
  - ❌ Don't: `curl` + `htmlq` on author page (JS-rendered)
  - ✅ Do: Use the RSS XML feed directly

- **Pagination:** Supports `?paged=N`
  - Default feed (no param): Most recent 200 items
  - `?paged=1`: Returns 0 items (common gotcha!)
  - `?paged=2`: Next 200 items, etc.

### YouTube RSS

- **Channel ID required, not handle**
  - ❌ `youtube.com/@Handle` doesn't work in RSS
  - ✅ Extract real `channel_id` from page source: `UC...`
  - Feed: `https://www.youtube.com/feeds/videos.xml?channel_id=UC...`

### Parsing Tools

| Format | Recommended Tool | Notes |
|--------|----------------|-------|
| RSS/XML | `xml.etree.ElementTree` (Python) | XPath 2.0 support |
| ❌ RSS/XML | `xmlstarlet` | XPath 1.0 limitations |
| ❌ XML | `jq` | XML isn't JSON, won't work reliably |

### Script Safety

**Heredoc delimiter clash:**

```python
# ❌ Truncates if content contains "EOF"
python3 << 'EOF'
print(f"Content with EOF")
EOF

# ✅ Use unique, non-conflicting delimiter
python3 << 'PYEOF'
print(f"Content with EOF")
PYEOF
```

---

## Quick Reference Commands

```bash
# Verify Ollama status
ollama list && ollama ps && curl http://localhost:11434

# Configure OpenClaw for local model
openclaw config set agents.defaults.model.primary ollama/qwen2.5:14b
openclaw config set agents.defaults.models '["ollama/qwen2.5:14b", "ollama/qwen2.5:7b"]'

# Post-restart verification
openclaw config get agents.defaults.model.primary
openclaw config get agents.defaults.models

# Security audit
openclaw security audit --deep

# Cron verification
openclaw cron list
openclaw cron runs --id <job-id>
```

---

*Last updated: March 2026 | OpenClaw v2.x | Ollama v0.x*
