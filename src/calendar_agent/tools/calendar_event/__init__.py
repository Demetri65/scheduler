"""
Calendar-event tool: create_calendar_event()

This __init__ file re-exports the @function_tool for use by agent_factory.
"""
from .impl import create_calendar_event  # type: ignore[F401] (export)
__all__ = ["create_calendar_event"]