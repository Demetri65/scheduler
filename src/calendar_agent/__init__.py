"""
Top-level package for the Calendar Scheduler microservice.

Exposes:
    - build_agent(): factory that returns the configured Agent
"""
from .agent_setup import build_agent  # re-export convenience
__all__ = ["build_agent"]