#!/usr/bin/env python
# build_team.py
# ─────────────────────────────────────────────────────────────
# Multi-agent team demo — team composition is fully configurable (see team_config.py);
# the number of roles is never hard-coded.
# The engine is pluggable: which engine to use is decided by team_config.ENGINE /
# an env var / --engine. The main flow does not depend on any concrete framework
# (see the engines/ plugin layer).
#
# Usage:
#   python build_team.py --dry-run                 # print the team only, no LLM call (no engine needed)
#   python build_team.py --engine mock             # zero-dependency demo run (no LLM call)
#   python build_team.py --topic "your topic"      # real run (default lightweight engine, needs .env key)
# ─────────────────────────────────────────────────────────────
import argparse
import os
import sys

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

import team_config
from team_config import TEAM, TASK_BRIEF, ENGINE
from engines import get_engine, available_engines

# Minimum experts per domain group (team rule: every domain needs >= 2).
DOMAIN_MIN_SIZE = getattr(team_config, "DOMAIN_MIN_SIZE", 2)


def group_by_domain(team):
    """Group the team into domain groups by the 'domain' field."""
    groups = {}
    for m in team:
        groups.setdefault(m.get("domain", "unassigned"), []).append(m)
    return groups


def check_domain_groups(team):
    """Validate domain-group sizes (each domain >= DOMAIN_MIN_SIZE).
    Returns (groups, display_lines, problems)."""
    groups = group_by_domain(team)
    lines, problems = [], []
    for domain, members in groups.items():
        n = len(members)
        flag = "OK " if n >= DOMAIN_MIN_SIZE else "!! "
        lines.append("  %s%-14s %d  : %s" % (flag, domain, n,
                                            ", ".join(m["role"] for m in members)))
        if n < DOMAIN_MIN_SIZE:
            problems.append(
                "Domain \"%s\" has only %d member(s) (needs >= %d); a single person cannot "
                "converge within the group. Fill the gap from a close domain or add experts."
                % (domain, n, DOMAIN_MIN_SIZE))
    return groups, lines, problems


def main():
    parser = argparse.ArgumentParser(description="Configurable multi-agent team (pluggable engine)")
    parser.add_argument("--topic", default="How to improve team collaboration with multi-agent systems")
    parser.add_argument("--engine", default=None,
                        help="Engine to use: %s (overrides team_config ENGINE)" % "/".join(available_engines()))
    parser.add_argument("--dry-run", action="store_true",
                        help="Print the team composition only; do not call any LLM")
    args = parser.parse_args()

    engine_name = args.engine or ENGINE
    engine = get_engine(engine_name)

    # Domain-group validation (team rule: every domain needs >= 2 experts).
    _, group_lines, problems = check_domain_groups(TEAM)
    print("Domain groups (each needs >= %d experts):" % DOMAIN_MIN_SIZE)
    for line in group_lines:
        print(line)
    for p in problems:
        print("  [!] " + p)
    print()

    # Preview mode: only run the engine's plan(), no LLM, no framework dependency.
    if args.dry_run:
        print(engine.plan(TEAM, TASK_BRIEF, args.topic))
        return

    # Zero-dependency demo engine.
    if engine_name == "mock":
        engine.run(TEAM, TASK_BRIEF, args.topic)
        return

    # Real engine needs a key.
    if not os.getenv("LLM_API_KEY"):
        print("\n[!] No LLM_API_KEY detected. Copy .env.example to .env and fill in the key, "
              "or use --engine mock to preview the team.")
        sys.exit(2)

    engine.run(TEAM, TASK_BRIEF, args.topic)


if __name__ == "__main__":
    main()
