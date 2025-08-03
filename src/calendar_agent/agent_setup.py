
from agents import Agent, Runner 
from calendar_agent.tools.calendar_event import create_calendar_event
from dotenv import load_dotenv
load_dotenv() 

import os
assert os.getenv("OPENAI_API_KEY"), "OPENAI_API_KEY not found"

def build_agent():
    return Agent(
        name="Calendar Scheduler",
        instructions=(
            "You schedule tasks in the user's Google Calendar. "
            "When asked to create a meeting or reminder, call the create_calendar_event tool. "
            "Always use ISO 8601 date/time strings in the America/Los_Angeles time zone."
        ),
        tools=[create_calendar_event],
        model="gpt-4o"
    )

if __name__ == "__main__":
    agent = build_agent()
    runner = Runner()
    result = runner.run_sync(agent, input="Schedule a coffee chat with Alex on August 10th at 2 pm.")
    print(result)