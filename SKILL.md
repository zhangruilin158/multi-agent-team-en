---
name: multi-agent-team
description: >-
  Multi-Agent Team Builder: turns the intent "I want to build a multi-agent system" into a runnable project.
  Internally decides the need shape and picks an engine; reuses expert personas from the Unified Role Pool
  (304 unique roles / 19 domains) and recruits domain groups from the non-deduped master list (330 entries).
  Every domain gets >= 2 experts: group discussion converges on "which plan + why", then team discussion
  decides "how to implement", and finally it executes or gives a concrete example.
  Discussion is ultra-terse (conclusion + key reason only).
  Trigger words: "multi-agent", "multi-agent team", "build me a multi-agent team".
  Use when the user wants to scaffold or build a multi-agent system, or mentions "multi-agent" / "multi-agent team" / "build me a multi-agent team".
agent_created: true
---

# Multi-Agent Team Builder (multi-agent-team)

## Purpose
Turn the intent "I want to build a multi-agent system" into an **actually runnable project**: decide the shape → pick an engine (internally; **don't externally agonize over "which one to use"**) → form domain groups → converge through two kinds of discussion → execute or give a concrete example. **Once chosen, act immediately — never stop at a selection suggestion.**

## When to trigger
- The user says "multi-agent", "multi-agent team", "build me a multi-agent team"
- The user wants to compare / choose a multi-agent framework or persona pack
- The user wants automated research, writing, code generation, or expert-collaboration flows

## Step 1: Decide the "need shape" (the decisive step for selection)
Before acting, decide which category the user wants, then pick the route:

- **Shape A — ready-made expert roles/personas that just work**: drop a bunch of "experts" into a mainstream AI coding tool, plug-and-play.
  → Choose the **role-library family**: the English general library (organized by department) or the Chinese role library (fills China-market niches like Xiaohongshu/Douyin/WeChat/Feishu/DingTalk). This is a **persona/role pack**, not a standalone runtime; it relies on the coding tool's execution permission to actually do work.
  → **Key judgment**: the role libraries already cover **every role archetype** demonstrated by the various code frameworks (PM, architect, engineer, QA, researcher, etc.). A code framework is the "**engine**", not the role source — to actually run collaboration you still need an engine; the role library only tells you "which experts exist".
- **Shape B — use an SDK in your own Python code to build a multi-agent app**: go to "Pick one of five capability types" below.
- **Shape C — a ready-to-run web/desktop/Docker app**: a one-click orchestrator (assemble a "one-person company" from a sentence) or a sandbox-backed workbench (research/automation workbench).
- **Shape D — enterprise-grade / domestic Python framework, integrate with existing Java/Python stack**: domestic Python frameworks (enterprise-grade, pure Python).

## Step 2: Pick one of five capability types (Shape B only)
| Capability type | Best for |
|----------------|----------|
| Lightweight multi-agent engine | Quickly assemble a "small team" for concrete business tasks (lightweight, no third-party orchestration lib) |
| Requirement-to-software framework | Turn a one-line requirement into software/docs (simulates an AI software company) |
| Research framework | Multi-agent research / data-synthesis experiments (role-play autonomous collaboration) |
| Orchestratable agent framework | Complex topology orchestration (production-grade pipeline) |
| Sandbox-backed workbench | Out-of-box research/automation workbench + sandbox isolation (safer) |

## Execution flow (must actually deliver)
> **Core rule: act once chosen, never output pure advice.** Deciding the "need shape" and picking the framework are **internal judgments** of the skill; externally report only "what I used, what I ran". Unless the user explicitly says "advice only" or "compare only", always build the runnable project directly. This is especially true when triggering "build me a multi-agent team" — form the team and run `--dry-run` directly.

1. **Clarify needs** (at most 3 key questions; infer rather than ask if possible): task goal? need code execution/isolation? which LLM?
2. **Internal selection**: first decide the need shape, then fix the concrete framework within that shape — **complete it only in your head**; don't list comparisons to the user or ask "which do you want".
3. **Form domain groups**: per "Team Rule 1", recruit members from the master list, >= 2 per domain.
4. **Converge through two discussions**: per "Rule 2 / Rule 3", first the group discussion outputs "which plan", then the team discussion decides "how to implement".
5. **Build it (act, don't advise)**:
   - Code framework: check whether `ai-agent-frameworks/` already has source to reference; otherwise create an independent project dir + `python -m venv .venv`, `pip install` the chosen framework inside the venv, and write a minimal runnable example (define Agent/role, Task, wire into a team, run the demo).
   - Persona pack: directly import/generate the role definitions into the user's coding tool, and remind about execution permission and review points.
   - App class (orchestrator / sandbox workbench): follow the official README to launch via Docker / locally, and run one example task.
   - Safety defaults: secrets in `.env` + env vars, **never hard-coded**; prefer sandbox; don't feed sensitive data.
6. **Delivery notes**: how to run, how to swap in the user's real task, cost & risk warnings.

## Agent assembly iron rule: take from the pool first, create only if missing (mandatory when triggering "build me a multi-agent team")

The assembly order **must** be this; never start by inventing new Agents from scratch:

1. **Check the Unified Role Pool first**: consult **only** `references/unified-role-pool.md` (the merged & de-duplicated result of four source libraries: **304 unique roles / 19 domains**). Reference format `unified-role-pool/<domain>/<slug>`, e.g. `unified-role-pool/engineering/engineering-code-reviewer`. **Do not** scan each source library directory separately.
2. **Reuse**: on a hit, directly reference its `.md` as that Agent's `role / goal / backstory`, no rewrite; every role must carry `domain` (domain) and `source` (in-pool slug) fields.
3. **Create only if the pool lacks it**: create a new role only when the pool truly has no matching business role; set `source` to `new:<your-slug>`, keep the same persona structure, and make the **name/duty/capability unique within its domain**.
4. **Framework archetypes as capability templates**: each code framework's Agent/Task, Role, role-play, and orchestratable Agent can also serve as "capability templates" to reuse alongside the pool personas.
5. **Landing**: the final team is carried by `assets/multi-agent-team-demo/` (or workspace `agent-team-demo/`) `team_config.py`; every `TEAM` entry must carry `domain` + `source`; first run `--dry-run` to validate (including domain-group size checks) before real execution.

> In one line: the pool is the Agent pool — pick and assemble from it first; only the roles missing from the pool get created. Never default to "create"; default to "reuse".

## Team collaboration rules (mandatory when triggering "build me a multi-agent team")

### Rule 1: every domain must have 2+ experts, forming a domain group
- Group by the `domain` field of `TEAM` entries; **every domain needs at least 2 members**; that group is the "domain group", the basic unit of discussion and convergence.
- When a domain has < 2 available roles (currently `research` and `integrations` each have only 1 role), fill the gap from a semantically close domain (`academic` / `specialized` / `engineering`) **cross-domain** up to 2.
- "Single-expert domains" are forbidden — a lone expert has no in-group debate and cannot converge.
- **Member source**: recruit from `references/agent-master-list.md` (all four libraries, **330 entries, non-deduped**).
  - Group discussion needs **different perspectives**, so **cross-library duplicates / same-library repeats are kept** to compare approach differences;
  - only the final landed team config uses the de-duplicated view (`references/unified-role-pool.md`, 304 unique roles).
- **Relationship of the two views**: the master list = the **discussion** view (non-deduped); the role pool = the **team-building** view (de-duplicated). Discuss with the list, build with the pool.

### Rule 2: the two discussion types have different jobs (different purpose, different output)

| | **Group discussion** (inside a domain group) | **Team discussion** (cross-domain, whole team) |
|---|---|---|
| **Focus** | **the plan itself** | **how the plan fits the current task** |
| **Do** | fully compare each agent's thinking and candidate plans, debate until convergence | discuss implementation, integration with existing code, responsibility split, execution order |
| **Output** | **which plan + why** (one line) | **how to implement that plan** (final plan + execution path) |

> The two are not interchangeable: the group answers "do the right thing", the team answers "do the thing right".

### Rule 3: converge in order (no skipping levels)
1. **Group discussion** — the domain's 2+ experts each propose a plan, **fully compare their thinking**, debate until convergence.
2. **Output one best group recommendation** — each domain group outputs **only 1 line**: **which plan + key reason**; **forbidden** to escalate unresolved disagreements as-is.
3. **Team discussion** — the one recommendation per group is aggregated; discuss **how to implement**: integration with existing code, cross-domain responsibility split, execution order; cross-domain conflicts are resolved here.
4. **Output the implementation plan and execute** — converge to one final plan, **execute directly**; when real execution is impossible, give a **concrete example** (runnable config / code / steps); **forbidden** to stop at "advice".

> In one line: the group answers "**which plan + why**", the team answers "**how to implement that plan**". No skipping levels, no escalating disagreements as-is.

## Communication style constraint: ultra-terse (mandatory for the discussion process)

- The discussion process is **ultra-terse**: give only **conclusion + key reason**; cut every dispensable word, deliver the message with the shortest phrasing (caveman-style compression).
- **Forbidden**: long explanations, background padding, restating what others already said, "first/second/finally" filler, polite small talk.
- **Allowed**: one-line conclusions, bullet-style short phrases, necessary numbers/facts/trade-offs.
- Convergence records follow the four-stage format "domain group → one recommendation → team discussion → implementation plan", each stage kept to a few sentences.
- **Boundary**: terseness constrains only the **discussion process**; the final deliverables (config, code, docs) must be complete and runnable — never stripped for brevity.

## Built-in: configurable multi-agent team scaffold (demo)
The skill ships a directly runnable multi-agent team template: `assets/multi-agent-team-demo/` (workspace copy at `agent-team-demo/`). **The team composition is fully configurable; the role count is never hard-coded.**

- **Engine**: a lightweight multi-agent engine. The engine is **pluggable**: default engine `lightweight`, plus a built-in zero-dependency `mock` adapter; adding a new engine only requires writing one adapter class in `engines/` and registering it.
- **Config**: only edit the `TEAM` list in `team_config.py`. Default is organized by **domain group** (research / engineering / testing, 2 each); you can freely add/remove domains and roles, but **every domain needs >= 2**.
- **Role material**: taken from the **Unified Role Pool** by `<domain>/<slug>` (e.g. `engineering/engineering-code-reviewer`); every entry must carry `domain` + `source`.
- **Run**: `python build_team.py --dry-run` previews the team (free, no model call, **no engine install needed**); `python build_team.py --engine mock` demonstrates the full flow zero-dependency; copy `.env.example` to `.env` and fill the API Key, then `python build_team.py --topic "topic"` for a real run.
- **Action after trigger**: per "Agent assembly iron rule" check the pool and reuse → adjust `TEAM` by domain group (>= 2 per domain) → run `--dry-run` (with domain-group validation) → converge through two discussions → deliver.

## Safety notes (must prompt on every delivery)
- Local code execution risk: most code frameworks run LLM-generated code directly on the local machine by default; a sandbox-backed workbench is safer with sandboxing.
- **Persona-pack risk**: a persona pack runs inside your coding tool with the **same file/command permission** as that tool. Always Review the persona definition before enabling; beware of malicious instructions injected via web pages/docs (prompt injection).
- API Key & cost: all need an LLM API Key and will actually bill; input content is sent to the corresponding provider.
- Data egress: prompts and fed-in files are sent to third-party LLMs — never put secrets or private data in.
- Supply chain: an orchestratable agent framework has a huge dependency tree and a contested history — always install in an isolated venv and review.
- Known vulnerabilities: at curation time, the above repositories had no public Security Advisory on the code-hosting platform; sources are trustworthy (MIT/Apache-2.0, high stars, recently active).

## References & bundling notes
- **Unified Role Pool** (team-building view, deduped): `references/unified-role-pool.md` — 304 unique roles / 19 domains.
- **Agent & Skill Master List** (discussion view, non-deduped): `references/agent-master-list.md` — 330 entries (305 agents + 25 workflow skills), with duplicates (2 names appear twice) and per-row library/path/duty/dup-source.
- **Framework overview / selection**: `references/framework-overview-and-selection.md`; **flowchart**: `references/team-building-flow.svg`.
- **Runnable scaffold**: `assets/multi-agent-team-demo/`.
- **Role library (published, clone directly)**: the four source role libraries' role content is organized into a standalone repo
  **`https://github.com/zhangruilin158/agent-role-libraries`** (English + Chinese roles, organized by domain; original MIT/Apache licenses & copyright notices retained in `LICENSES/`).
  This skill's role pool / master list is based on it; if missing locally, clone that repo (when the connection to the code-hosting platform is unstable, first run `git config --global http.sslBackend openssl` + `core.longpaths true`, then clone).
  Note: the role pool in this English skill is the **English subset**; China-market localized roles (Xiaohongshu/Douyin/WeChat/Feishu/DingTalk operators, Qt/hardware engineering, company/hr/legal/supply-chain, etc.) live in that repo's `chinese-role-library` and can be added when needed.
- **Code-framework source**: the 5 classes of code frameworks were downloaded to workspace `ai-agent-frameworks/` for reference only; not distributed with the skill.
- This skill already carries `agent_created: true` and can be packaged directly (`SKILL.md` + `assets/` + `references/`) and migrated or shared to other machines.
