from calendar_agent.tools.calendar_event import create_calendar_event

def test_schema():
    assert create_calendar_event.name == "create_calendar_event"

    schema = create_calendar_event.params_json_schema
    assert {"title", "start_time", "end_time"} <= set(schema["properties"])