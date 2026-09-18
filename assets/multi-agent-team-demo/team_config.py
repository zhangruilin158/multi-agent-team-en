# team_config.py
# ─────────────────────────────────────────────────────────────
# Team composition: fully configurable. List only the Agents your project needs.
#
# [Domain-group rule] Agents sharing a "domain" form a "domain group";
# every domain needs at least 2 members (DOMAIN_MIN_SIZE) — a single-person
# domain cannot converge internally, so it is forbidden.
# Role sources come from the "Unified Role Pool"
# (references/unified-role-pool.md):
#   source = pool slug (e.g. engineering-code-reviewer) -> reuse its persona
#   source = new:<your-slug>                            -> only when absent from pool
# When a domain has < 2 available roles (e.g. research has only 1), fill the gap
# from a semantically close domain.
# ─────────────────────────────────────────────────────────────

import os

# Which "engine" actually runs the team (pluggable):
#   lightweight -- default; requires pip-installing engine deps + LLM_API_KEY
#   mock       -- zero-dependency; demo/preview only, never calls an LLM
# Override with env var TEAM_ENGINE or CLI flag --engine.
ENGINE = os.getenv("TEAM_ENGINE", "lightweight")

# Minimum experts per domain group (team rule: every domain needs >= 2).
DOMAIN_MIN_SIZE = 2

TEAM = [
    # ── Domain group A: research ── 2 members
    {
        "domain": "research",
        "source": "research-synthesist",
        "role": "Senior Researcher",
        "goal": "Conduct deep research on the topic and produce sourced key findings",
        "backstory": "You are a rigorous researcher skilled at retrieval, cross-validation, and synthesis.",
    },
    {
        "domain": "research",
        "source": "academic-statistician",   # cross-domain fill: research has only 1 role, taken from academic
        "role": "Research Statistician",
        "goal": "Validate the data support and statistical significance of research conclusions",
        "backstory": "You let the data speak; you trust evidence, not intuition.",
    },
    # ── Domain group B: engineering ── 2 members
    {
        "domain": "engineering",
        "source": "engineering-ai-engineer",
        "role": "Software Engineer",
        "goal": "Turn research conclusions into a runnable technical plan and code",
        "backstory": "You are a senior engineer who values correctness and maintainability.",
    },
    {
        "domain": "engineering",
        "source": "engineering-backend-architect",
        "role": "Backend Architect",
        "goal": "Design a scalable, maintainable system structure and interfaces",
        "backstory": "You think through the structure before writing the first line of code.",
    },
    # ── Domain group C: testing (QA / review) ── 2 members
    {
        "domain": "testing",
        "source": "testing-reality-checker",
        "role": "Quality Reviewer",
        "goal": "Audit prior outputs and flag gaps, risks, and improvements",
        "backstory": "You are a picky reviewer who accepts only evidence and quality.",
    },
    {
        "domain": "testing",
        "source": "testing-evidence-collector",
        "role": "Evidence Checker",
        "goal": "Collect verifiable evidence for every claim; reject unsupported assertions",
        "backstory": "Any conclusion without evidence is bounced back by you.",
    },
    # ↓↓↓ Need more domains? Copy a dict above and fill domain + source (>= 2 per domain) ↓↓↓
    # {
    #     "domain": "product",
    #     "source": "new:pricing-analyst",   # absent from pool -> new: prefix
    #     "role": "Product Manager",
    #     "goal": "Break vague requirements into clear tasks and acceptance criteria",
    #     "backstory": "You turn ideas into executable plans.",
    # },
]

# The team's overall task ({topic} is replaced at runtime).
# Two discussion types: group = which plan + why; team = how to implement that plan.
TASK_BRIEF = (
    "Collaborate on \"{topic}\" and converge strictly through the two-stage discussion:\n"
    "1) Group discussion (within each domain group): research / engineering / testing groups "
    "compare approaches until they converge;\n"
    "2) Each group outputs exactly ONE recommendation: which plan + key reason "
    "(do NOT escalate unresolved disagreements as-is);\n"
    "3) Team discussion (cross-domain): combine the groups' recommendations and decide how to "
    "implement — integration with existing code, responsibility split, execution order, and resolve cross-domain conflicts;\n"
    "4) Output one final plan and execute it (or give a concrete example if it cannot run).\n"
    "Keep the discussion extremely terse: conclusion + key reason only. No long explanations, "
    "no restating others, no pleasantries."
)
