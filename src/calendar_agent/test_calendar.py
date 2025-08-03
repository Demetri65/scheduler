from datetime import datetime, timedelta
from calendar_agent.tools.calendar_event.google_calendar import create_event

# Prepare test data: event starting now + 1 hour, ending +2 hours
now = datetime.now()
start_time = (now + timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%S")
end_time = (now + timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%S")

title = "Test Meeting"
description = "Testing manual calendar event creation"
timezone = "America/Los_Angeles"
attendees = ["dsl418@nyu.edu"]  # optional

link = create_event(title, start_time, end_time, description, timezone, attendees)
print("Event created! Link:", link)