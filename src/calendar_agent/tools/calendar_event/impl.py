"""
Implementation + tool wrapper for Google-Calendar event creation.
"""
from typing import Optional, List

from agents import function_tool
from .google_calendar import create_event  # relative import

@function_tool
def create_calendar_event(
    title: str,
    start_time: str,
    end_time: str,
    description: str = "",
    timezone="America/New_York",
    attendees: Optional[List[str]] = None,
) -> dict:
    """
    Create a Google Calendar event and return its HTML link.

    Times must be ISO-8601, America/New_York.
    """
    link = create_event(title, start_time, end_time, description, timezone ,attendees)
    return {"event_link": link}