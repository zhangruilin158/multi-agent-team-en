# Multi-Agent Team Builder (multi-agent-team) · Upload blurb

> This file is for filling in the intro/description when uploading to a Skill platform; copy the relevant paragraphs directly.

## One-line intro (subtitle under the title)
Turn "I want to build a multi-agent system" directly into a runnable team: internal selection, domain-based assembly, group discussion picks the plan, team discussion decides implementation — no agonizing, no hand-waving.

## Three shapes (in plain words)

The multi-agent solutions this skill delivers boil down to three shapes — pick by what you're doing:

- **Shape 1 · Drop in ready-made experts (persona library, plug-and-play)**: you want to drop a bunch of "experts" (frontend wizard, community operator, QA, security specialist…) straight into an AI coding tool to do the work. The skill picks ready-made personas from the role library (English general library, organized by department; Chinese role library, filling China-market niches like Xiaohongshu/Douyin/WeChat/Feishu/DingTalk), plug-and-play, no rewrite. This is a "persona pack", not a standalone program; it works through the coding tool's execution permission.
- **Shape 2 · Assemble your own team in code (SDK / lightweight-engine scaffold)**: you want to define Agents in code within your own Python project and run multi-agent collaboration. The skill ships a lightweight multi-agent engine scaffold — change one `TEAM` list to add/remove roles, preview free with `--dry-run` first, then run for real once keys are configured. This is genuinely runnable code.
- **Shape 3 · Ready-to-run app / enterprise framework**: you want a ready-made web/desktop/Docker app, or an enterprise framework that integrates with your existing Java/Python stack. The skill guides you to a one-click orchestrator, a sandbox-backed research/automation workbench, or a domestic Python framework to run a production-grade pipeline.

In one line: Shape 1 is the "expert pool" (who's available), Shapes 2/3 are the "engine" (how to actually run the experts); the three combine — pool personas can be fed straight into a code engine or an app.

## Feature highlights

- **Use it the moment it's chosen**: after triggering, internally decide the need shape and pick the engine, then **build the runnable project directly** — never stop at a pure selection suggestion.
- **No hand-written team**: reuse ready-made expert personas from the **Unified Role Pool** (four libraries merged & deduped, **304 unique roles / 19 domains**); create only what's missing from the pool.
- **Domain groups + two-stage discussion**: every domain gets >= 2 experts as a group; **group discussion** compares each agent's thinking and outputs "which plan + why", **team discussion** decides "how to implement that plan" (implementation, integration with existing code, responsibility split, execution order), then executes or gives a concrete example.
- **Discussion members not de-duplicated**: provides the **full agent master list** (four libraries, **330 entries**, non-deduped, with duplicate sources marked) — group discussion deliberately keeps duplicate agents to fully compare different thinking; only the final team config uses the de-duplicated view.
- **Ultra-terse communication**: the discussion process gives only **conclusion + key reason**; no long explanations, restating, or pleasantries.
- **Fully configurable**: ships a pluggable-engine scaffold; edit just one `TEAM` list to add/remove roles; preview free with `--dry-run`, then run for real with keys.
- **Safety net**: every delivery prompts about local code-execution risk, API cost, data egress, and secret management; workbench-type capabilities support sandbox isolation.
- **Self-contained**: built-in framework overview/selection docs, role pool, master list, and runnable scaffold — migratable or shareable with no external files.

## Default engine notes

- The scaffold's **default engine is the "lightweight multi-agent engine"** (internally the retained crewai, re-labeled `lightweight` after white-labeling) — works out of the box, no manual selection needed.
- **Engine is pluggable**: besides the default `lightweight`, a built-in **zero-dependency `mock` engine** demonstrates the full team-assembly flow without any third-party library (`--engine mock`), or use `--dry-run` for a free preview (no mock needed either).
- **Swapping engines is easy**: change `ENGINE` in `team_config.py`, use the CLI `--engine`, or set the env var `TEAM_ENGINE` — any one of the three; adding a new engine only requires one adapter class in `engines/` registered to the factory, with zero changes to the main flow.

## Team collaboration rules (highlight)

| Stage | Who | Does | Output |
|-------|-----|------|--------|
| **Group discussion** | >= 2 experts per domain | compare each agent's thinking & candidate plans, debate to convergence | **which plan + why** (1 line per domain) |
| **Team discussion** | cross-domain whole team | implementation, integration with existing code, responsibility split, execution order | **how to implement that plan** |

If a domain has < 2 members (e.g. `research`, `integrations`), fill cross-domain from a close domain — a lone person has no in-group debate and cannot converge.

## Applicable scenarios

- Quickly assemble a "small team" for research / writing / competitive analysis and other business tasks
- Auto-produce code or docs with "company-like" division of labor
- Multi-agent research / data-synthesis experiments
- Production-grade pipelines needing complex topology orchestration
- Ready-to-run research / automation workbench (with execution isolation)

## Trigger words

- "multi-agent"
- "multi-agent team"
- "build me a multi-agent team"

## Install

Copy the whole `multi-agent-team/` folder into the skills directory:
- User-level: `~/.workbuddy-ai/skills/multi-agent-team/`
- Project-level: `<project>/.workbuddy-ai/skills/multi-agent-team/`

## Notes

- Real runs consume LLM tokens and incur cost; start with a cheap entry-level model.
- A persona pack runs in your coding tool with the same file/command permission — Review the persona before enabling, and beware of prompt injection.
- Secrets only in `.env`, never hard-coded or committed; inputs go to your configured LLM provider — don't feed secrets or private data.
- The role library content is large and not bundled into this skill; it's published separately at `github.com/zhangruilin158/agent-role-libraries` (original licenses retained), clone when needed.
