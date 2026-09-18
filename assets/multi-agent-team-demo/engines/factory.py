# engines/factory.py
# Engine registry + factory: to add a new engine, register one adapter class here.
from .base import BaseEngine
from .lightweight_engine import LightweightEngine
from .mock_engine import MockEngine

# Registered engines; to plug in another multi-agent framework, write a new adapter
# class and add it to this dict.
_ENGINES = {
    "lightweight": LightweightEngine,
    "mock": MockEngine,
}


def get_engine(name):
    cls = _ENGINES.get(name)
    if cls is None:
        raise ValueError("Unknown engine: %s (available: %s)" % (name, ", ".join(_ENGINES)))
    return cls()


def available_engines():
    return list(_ENGINES.keys())
