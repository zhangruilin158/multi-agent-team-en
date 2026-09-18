# Functional & Process Overview

> This file summarizes all the skill's functions and flows as flowcharts.
> Written in Mermaid, they **render directly as diagrams** on GitHub / any Mermaid-capable Markdown reader.

## ① End-to-end main flow

```mermaid
flowchart TD
  A["Trigger: multi-agent team"] --> B["Decide need shape (internal)"]
  B --> C["Form domain groups<br/>>= 2 per domain · recruit from master list"]
  C --> D["Converge via two discussions<br/>group picks plan → team decides impl"]
  D --> E["Execute / give a concrete example"]
  E --> F["Delivery notes + safety tips"]
```

## ② Need-shape decision → capability types

```mermaid
flowchart LR
  A["Need shape (four choices)"] --> A1["Shape A · ready-made expert personas<br/>persona library, plug-and-play"]
  A --> A2["Shape B · build in code with SDK<br/>write your own team"]
  A --> A3["Shape C · ready-to-run app<br/>orchestrator / workbench"]
  A --> A4["Shape D · enterprise framework<br/>domestic Python, joins existing stack"]

  A2 --> B["Shape B internal: pick one of five"]
  B --> B1["Lightweight multi-agent engine<br/>quick small team for business"]
  B --> B2["Requirement-to-software framework<br/>one-line need → code/docs"]
  B --> B3["Research framework<br/>multi-role research, data synthesis"]
  B --> B4["Orchestratable agent framework<br/>complex topology, prod pipeline"]
  B --> B5["Sandbox-backed workbench<br/>out-of-box research + isolation"]
```

## ③ Assembly iron rule: pool first, create only if missing

```mermaid
flowchart TD
  S["Check Unified Role Pool<br/>304 unique roles / 19 domains"] --> Q{"Pool has a match?"}
  Q -- yes --> R["Reuse its persona<br/>don't rewrite role / goal / backstory"]
  Q -- no --> N["Only then create<br/>source uses new: prefix"]
  R --> W["Write to TEAM<br/>carry domain + source"]
  N --> W
  W --> V["Validate: >= 2 per domain"]
  V --> D["dry-run validates team → real run"]
```

## ④ Two discussions & convergence (core rule)

```mermaid
flowchart TD
  G["Domain group<br/>>= 2 per domain"] --> G1["Group discussion · focus on the plan<br/>fully compare each agent's thinking"]
  G1 --> G2["Each domain outputs 1 recommendation<br/>which plan + key reason"]
  G2 --> T1["Team discussion · focus on fitting the task<br/>integration · responsibility · order"]
  T1 --> T2["Output: how to implement<br/>resolve cross-domain conflicts, one plan"]
  T2 --> F["Execute / give a concrete example"]
```

**Division of labor between the two discussions**:

| | Group discussion (inside domain group) | Team discussion (cross-domain, whole team) |
|---|---|---|
| Focus | the plan itself | how the plan fits the current task |
| Output | which plan + why | how to implement that plan |

**Communication constraint**: ultra-terse throughout — conclusion + key reason only (constrains the discussion process only, not the final deliverables).

## ⑤ Execution: pluggable engine

```mermaid
flowchart TD
  E["Choose engine<br/>--engine / TEAM_ENGINE / default config"] --> P1["--dry-run<br/>no engine, no model, zero cost"]
  E --> P2["--engine mock<br/>zero-dep full-flow demo, placeholder output"]
  E --> P3["Real run (default lightweight)<br/>needs API Key or local model"]
```

## ⑥ Role resources: two views

```mermaid
flowchart LR
  R["agent-role-libraries<br/>English + Chinese roles"] --> V1["Unified Role Pool<br/>deduped 304 → team-building"]
  R --> V2["Agent & Skill Master List<br/>non-deduped 330 → discussion"]
```

> Why discuss with the non-deduped list? The value of group discussion is **comparing different agents' thinking** — same name & duty but from different libraries can yield different plans, so duplicates stay in.

## ⑦ Safety notes (prompt on every delivery)

```mermaid
flowchart TD
  A["Every delivery"] --> S1["Local code-execution risk<br/>prefer sandbox"]
  A --> S2["Persona-pack permission<br/>same file/cmd permission, Review first"]
  A --> S3["Secret management<br/>only in .env, never hard-coded"]
  A --> S4["Data egress<br/>don't feed secrets or PII"]
  A --> S5["Cost<br/>billed per token, start cheap"]
```
