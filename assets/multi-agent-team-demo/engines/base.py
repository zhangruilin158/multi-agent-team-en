# engines/base.py
# Unified engine interface: every "multi-agent engine" must implement these two methods.
# The main flow depends only on this interface and never on any concrete framework.
from abc import ABC, abstractmethod


class BaseEngine(ABC):
    #: Engine identifier, used to select it from config / CLI.
    name = "base"

    @abstractmethod
    def plan(self, team, task_brief, topic):
        """Print only the team plan; does NOT call any LLM (used for preview / dry-run)."""
        raise NotImplementedError

    @abstractmethod
    def run(self, team, task_brief, topic):
        """Actually assemble and run the multi-agent team; return the final output."""
        raise NotImplementedError
