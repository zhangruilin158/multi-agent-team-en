# Multi-Agent Framework Overview (skill's built-in reference)

> This file summarizes the 5 mainstream "multi-agent" open-source capability classes to speed up selection and team-building after triggering the skill.
> The matching source was downloaded to workspace `ai-agent-frameworks/` (one subfolder per capability). If not downloaded, the skill guides you to fetch it with a clone tool.

## 1. Trigger words

To quickly build a multi-agent system based on this file, trigger with any of:

- **"build me a multi-agent team"**
- **"multi-agent team"**
- **"multi-agent"**

After triggering, land quickly per "how to select" and "safety notes" below.

---

## 2. Overview comparison (by capability)

| Capability type | Common license | Positioning | Code execution |
|-----------------|---------------|-------------|----------------|
| Lightweight multi-agent engine | permissive OSS | role-based Agent teaming | local execution possible (caution) |
| Requirement-to-software framework | permissive OSS | simulate an AI software company, requirement→code | writes & runs code locally |
| Research framework | permissive OSS | role-play autonomous collaboration / research | can call tools / execute |
| Orchestratable agent framework | permissive OSS | enterprise-grade Agent orchestration (rich topology) | integrable execution |
| Sandbox-backed workbench | permissive OSS | long-chain SuperAgent workbench (with sandbox) | **sandbox isolation** (safer) |

---

## 3. Each capability: function & use case

### 1. Lightweight multi-agent engine
- **Function**: assemble several "role-based" Agents into a team; each Agent has role, goal, tools, and memory, and cooperates through task flow to complete complex tasks. Lightweight, no third-party orchestration lib.
- **Use case**: pipelines needing multiple AI roles — e.g. "research Agent + writing Agent + review Agent" auto-produce reports, automated market/competitor analysis, content-generation workflows.
- **For**: users wanting to quickly assemble a "small team" for concrete business tasks.

### 2. Requirement-to-software framework
- **Function**: encode SOPs (standard operating procedures) into multi-agents, simulating an "AI software company" — PM, architect, engineer, etc. collaborate to turn a one-line requirement into code and docs.
- **Use case**: rapid requirement→prototype generation, automated software engineering, teaching demos of "how an AI team collaborates".
- **For**: users wanting "company-like" division of labor to auto-produce code/docs.

### 3. Research framework
- **Function**: one of the earliest LLM multi-agent frameworks, featuring "role-play" autonomous Agent collaboration, exploring Agent Scaling Laws, with many built-in datasets, tools, and model interfaces.
- **Use case**: multi-agent academic research, automated data generation, conversational collaboration experiments.
- **For**: researchers and users doing multi-agent experiments and data synthesis.

### 4. Orchestratable agent framework
- **Function**: enterprise-grade multi-agent orchestration framework supporting serial / parallel / hierarchical topologies, emphasizing production-readiness and composability.
- **Use case**: large-scale Agent orchestration, chaining multiple Agents into a pipeline for business. ⚠️ Huge dependency tree — review carefully at install.
- **For**: engineering users needing complex Agent topologies (flowchart-style orchestration).

### 5. Sandbox-backed workbench
- **Function**: a "Super Agent" workbench that can research, write code, and generate content, with built-in sandbox, memory, tools, sub-Agents, and a message gateway — a full app (frontend + backend), not a pure library.
- **Use case**: deep-research assistant, automated research reports, end-to-end task automation. Sandboxed execution makes it safer by default than the others.
- **For**: users wanting an out-of-box "research / automation workbench" and valuing execution isolation.

---

## 4. How to select (decision guidance)

- Want to **quickly assemble a small team for business tasks** → **lightweight multi-agent engine**
- Want **one-line requirement → software/docs** → **requirement-to-software framework**
- Doing **multi-agent research / data synthesis** → **research framework**
- Need **complex topology orchestration (production pipeline)** → **orchestratable agent framework**
- Want **out-of-box research/automation workbench + sandbox safety** → **sandbox-backed workbench**

---

## 5. Safety notes (read first)

1. **Local code-execution risk**: most code frameworks run LLM-generated code or commands directly on the local machine by default, risking induced dangerous operations; **the sandbox-backed workbench isolates via sandbox and is relatively safer**.
2. **API Key & cost**: all need an LLM API Key and will actually bill; input content is sent to the corresponding provider.
3. **Data egress**: prompts, context, and fed-in files are sent to third-party LLMs — **never put secrets or private data in**.
4. **Supply chain / dependencies**: `pip install` pulls many dependencies; **the orchestratable agent framework's dependency tree is abnormally large and has a contested history** — always install in an isolated venv and review.
5. **Telemetry**: some frameworks report anonymous usage stats by default (usually disable-able).
6. **Known vulnerabilities**: at curation time, each repository had **no public Security Advisory** on the code-hosting platform; sources are trustworthy (permissive OSS license, high stars, recently active).

> Landing advice: install in an isolated venv → don't feed sensitive data → trial-run with a small task first → scrutinize the orchestratable agent framework's dependencies.

---

## 6. Role resources: four libraries merged into one Unified Role Pool

Merge, de-duplicate, and group-by-domain the identified **four source role libraries** into **one Unified Role Pool**.

### 6.1 Two resource classes
- **A. Roles / persona packs**: **general-role-library** (English, 280), **chinese-role-library** (278), **engineering-personas** (21), **review-personas** (4 agents + 25 workflow skills). After merging & de-duplicating the English subset, the English skill's pool is **304 unique roles / 19 domains** (see `unified-role-pool.md`). Organized by domain (engineering / specialized / marketing / security / design / testing / finance / sales / academic / product / gis / game-development …), ready to drop into mainstream AI coding tools, plug-and-play.
- **B. Code frameworks / runtimes (Engine)**: the 5 capability classes above + one-click orchestrator + domestic Python framework. These are SDKs / apps that define Agents in code and handle orchestration and execution.

> Two views: **team-building view** (deduped, 304 roles) = `unified-role-pool.md`, for the final team config; **discussion view** (non-deduped, 330 entries) = `agent-master-list.md`, for group-discussion recruitment (duplicates kept to compare thinking).

### 6.2 Agent archetypes already covered by the pool (demonstrated by other frameworks)
| Example role in other frameworks | Pool coverage |
|------|------|
| Requirement-to-software: PM / architect / engineer / QA / project manager | product, engineering (architect/engineer), testing, project-management all have matching personas |
| Lightweight engine: custom-role Agent | generic — any role maps to some department persona |
| Research framework: role-play Agent | generic |
| Orchestratable framework: worker / orchestrator | engineering-multi-agent-systems-architect |
| Sandbox workbench: researcher / coder / supervisor | research + engineering + project-management |
| Domestic Python framework: domain-expert Agent | every domain has expert personas |

**Conclusion: at the "Agent role / persona" level, the Unified Role Pool already covers all archetypes demonstrated by the above frameworks** — 304 unique roles / 19 domains, broader than the example roles bundled with each framework.

### 6.3 What each library adds
- **chinese-role-library** adds **China-localized scenario** roles: Xiaohongshu / Douyin / WeChat / Feishu / DingTalk operators, Qt/HMI / mechanical-design and other local engineering roles; plus company / hr / legal / supply-chain domains the English library lacks. (Available in the published `agent-role-libraries` repo's `chinese-role-library`.)
- **engineering-personas** fills pool gaps: root-cause & debugging expert, generic refactoring & tech-debt expert, AI persona architect.
- **review-personas** adds the Web performance auditor (its 25 workflow skills are not agents and are registered separately in the master list).

### 6.4 Notes
- ✅ All four role libraries are downloaded and merged into the pool.
- 📌 Key distinction: a role library is a "role library", **not a "runtime engine"**. To actually run multi-agent collaboration you still need a code framework or orchestrator as the engine; the role library only provides "which experts exist".

---

## 7. Runnable multi-agent team demo (skill's built-in scaffold)

The skill ships a directly runnable demo at `../assets/multi-agent-team-demo/`:

- **Engine**: lightweight multi-agent engine, **pluggable** (default `lightweight`, plus zero-dependency `mock` adapter).
- **Role material**: Unified Role Pool, addressed by `<domain>/<slug>` (e.g. `engineering/engineering-code-reviewer`).
- **Core feature**: organized by **domain group** — >= 2 experts per domain; each `TEAM` entry carries `domain` + `source`, and `build_team.py` validates domain-group sizes (warns if short).
- **Files**: `team_config.py` (the only config to edit), `build_team.py` (assemble & run), `engines/` (engine plugin layer), `requirements.txt`, `.env.example`, `README.md`.
- **Run**: `build_team.py --dry-run` previews the team (free, no model call, **no engine install needed**); `--engine mock` demos the full flow zero-dependency; after configuring `.env` keys, `build_team.py --topic "topic"` runs for real.
- **Trigger**: say "multi-agent" / "multi-agent team" / "build me a multi-agent team" to trigger the **Multi-Agent Team Builder** skill to auto-assemble.
- **Verified**: `--dry-run` (research / engineering / testing, 2 each) and `--engine mock` both exit 0.
