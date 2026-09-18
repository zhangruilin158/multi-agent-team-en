# engines/lightweight_engine.py
# Default engine adapter: wraps the "lightweight multi-agent engine" (open-source,
# role-based teaming). Note: this is the ONLY file that references a concrete
# framework implementation; the main flow and config do not depend on it.
from .base import BaseEngine


class LightweightEngine(BaseEngine):
    name = "lightweight"

    def plan(self, team, task_brief, topic):
        lines = [
            "=== Configured multi-agent team (%d roles, in relay order) ===" % len(team)
        ]
        for i, a in enumerate(team, 1):
            lines.append("  %d. %s  ->  %s" % (i, a["role"], a["goal"]))
        lines.append("\nTopic: %s" % topic)
        lines.append("\n[plan] No LLM was called. Configure .env and run a real execution.")
        return "\n".join(lines)

    def run(self, team, task_brief, topic):
        # Lazily import only when actually running, so a missing dependency
        # never breaks the preview / dry-run path.
        from crewai import Agent, Task, Crew, Process, LLM
        import os

        llm_kwargs = {
            "model": os.getenv("LLM_MODEL"),
            "api_key": os.getenv("LLM_API_KEY"),
        }
        base_url = os.getenv("LLM_BASE_URL")
        if base_url:
            llm_kwargs["base_url"] = base_url
        llm = LLM(**llm_kwargs)

        agents = [
            Agent(
                role=a["role"],
                goal=a["goal"],
                backstory=a["backstory"],
                verbose=True,
                allow_delegation=False,
                llm=llm,
            )
            for a in team
        ]
        tasks = [
            Task(
                description=(
                    "Overall task: %s\nYou are \"%s\"; your goal is: %s. "
                    "Complete your part and hand off a clear result to the next role."
                    % (task_brief.format(topic=topic), a["role"], a["goal"])
                ),
                expected_output="Structured output for your role (findings / plan / review, etc.).",
                agent=agent_obj,
            )
            for a, agent_obj in zip(team, agents)
        ]
        crew = Crew(agents=agents, tasks=tasks, process=Process.sequential, verbose=True)

        print("=== Assembled multi-agent team (%d roles) ===" % len(crew.agents))
        for i, a in enumerate(crew.agents, 1):
            print("  %d. %s  ->  %s" % (i, a.role, a.goal))
        print("\nTopic: %s\n" % topic)

        print("=== Team is working ===")
        result = crew.kickoff(inputs={"topic": topic})
        print("\n=== Team output ===")
        print(result)
        return result
