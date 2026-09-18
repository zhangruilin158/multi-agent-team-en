# engines/__init__.py
# Multi-agent engine plugin layer: the main flow knows only the unified interface
# and is never bound to any concrete framework.
from .base import BaseEngine
from .factory import get_engine, available_engines

__all__ = ["BaseEngine", "get_engine", "available_engines"]
