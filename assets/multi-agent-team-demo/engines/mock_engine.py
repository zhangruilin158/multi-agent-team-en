# engines/mock_engine.py
# Zero-dependency engine: runs without installing any LLM SDK. Used for preview,
# teaching demos, or placeholder runs when no API key is available.
from .base import BaseEngine


class MockEngine(BaseEngine):
    name = "mock"

    def plan(self, team, task_brief, topic):
        lines = [
            "=== Mock multi-agent team (%d roles, in relay order) ===" % len(team)
        ]
        for i, a in enumerate(team, 1):
            lines.append("  %d. %s  ->  %s" % (i, a["role"], a["goal"]))
        lines.append("\nTopic: %s" % topic)
        lines.append("\n[mock] Real engine not enabled; showing team plan only. No LLM call, zero cost.")
        return "\n".join(lines)

    def run(self, team, task_brief, topic):
        print(self.plan(team, task_brief, topic))
        print("\n=== Mock run: each role produces output in turn (placeholder) ===")
        for a in team:
            print("  - %s done: <sample output>" % a["role"])
        print(
            "\n[tip] This is a dependency-free demo run. To really run, set LLM_API_KEY in .env "
            "and switch to the lightweight engine (default)."
        )
        return "<mock result>"
