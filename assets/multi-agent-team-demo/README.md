# Multi-Agent Team Demo (Unified Role Pool + Pluggable Engine)

A runnable multi-agent team example built on the **Unified Role Pool** (four libraries
merged & deduped) + a **lightweight multi-agent engine**.
Key features: **organized by domain groups, team composition fully configurable** —
every domain needs at least 2 experts; list only the Agents your project needs.

## Contents
- `team_config.py` —— **the only file you edit**: add/remove Agents in `TEAM`
  (`domain` / `source` / `role` / `goal` / `backstory`); `ENGINE` selects the engine.
  Every entry needs `domain` (domain) + `source` (pool slug), and **>= 2 per domain**.
- `build_team.py` —— reads config, assembles the team with the chosen engine and runs it
  (engine is pluggable).
- `engines/` —— **engine plugin layer**: unified interface `BaseEngine` + two adapters
  `lightweight` (default) and `mock` (zero-dependency), freely extensible.
- `requirements.txt` —— default engine deps (the lightweight engine libs + python-dotenv);
  not needed if you only use the mock engine.
- `.env.example` —— secret template (copy to `.env` and fill in values).

## Quick start
```bash
# 1) Install dependencies (skip if already in a .venv)
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt

# 2) Configure secrets
copy .env.example .env      # then edit .env to add your API key

# 3) Preview the team first (free, no model call, no engine dependency)
.venv\Scripts\python build_team.py --dry-run

# 4) Real run
.venv\Scripts\python build_team.py --topic "your specific topic"
```

## Pluggable engine (optional)
Which engine "actually runs the team" is swappable; the main flow hard-codes no framework:
- `ENGINE` in `team_config.py` (or env var `TEAM_ENGINE`, or CLI `--engine`) decides.
- Two adapters built in: `lightweight` (default; needs deps + key) and `mock`
  (zero-dependency; demonstrates without calling a model).
- To plug in another multi-agent framework: write a new adapter following `BaseEngine`
  in `engines/`, then register it in `engines/factory.py`'s dict — no business code changes.

```bash
# Zero-dependency demo, no install needed
.venv\Scripts\python build_team.py --engine mock --topic "your topic"
```

## How to extend the team (key point)
`TEAM` in `team_config.py` is a list; **each dict = one Agent**, and must carry
`domain` + `source`:
- To add a "Product Manager": copy a dict, set `domain` (e.g. `product`), `source`
  (a pool slug, or `new:<your-slug>` if outside the pool), and `role/goal/backstory`.
- **At least 2 per domain** to form a domain group; when < 2, fill from a close domain
  (e.g. `academic` / `specialized`).
- Personas come from the **Unified Role Pool**: `references/unified-role-pool.md`,
  addressed by `<domain>/<slug>` (e.g. `engineering/engineering-code-reviewer`).
- For the discussion stage (group / team discussion), recruit from the **non-deduped**
  master list: `references/agent-master-list.md`.

At runtime it prints the **domain groups** and validates headcounts (warns if short),
then lets each Agent take its turn in list order.

## Safety notes
- **Secrets live only in `.env`** — never hard-code them or commit them to the repo.
- By default this demo lets the LLM *generate content* (no code execution) on the
  local machine, which is relatively safe; if you later wire in Agents that run code,
  use a sandbox.
- Inputs are sent to your configured LLM provider — **do not feed in secrets or PII**.
- Cost: every real run consumes tokens; start with a cheap entry-level model.

## Relationship to the Multi-Agent Team Builder skill
This demo is the **standard scaffold** the "Multi-Agent Team Builder" skill uses when
delivering. After triggering "multi-agent" / "multi-agent team" / "build me a multi-agent
team", the skill uses this template combined with your real project: it picks/combines
roles from the Unified Role Pool (forming >= 2-person groups per domain), runs `--dry-run`
to validate, then runs for real.
