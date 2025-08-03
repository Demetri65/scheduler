from __future__ import print_function
import os
import os.path
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ["https://www.googleapis.com/auth/calendar.events"]

def get_calendar_service():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return build("calendar", "v3", credentials=creds)

def create_event(title: str, start_time: str, end_time: str, description: str = "", timezone: str = "America/New_York", attendees: list[str] | None = None):
    service = get_calendar_service()
    event = {
        "summary": title,
        "description": description,
        "start": {"dateTime": start_time, "timeZone": timezone},
        "end": {"dateTime": end_time, "timeZone": timezone},
    }
    if attendees:
        event["attendees"] = [{"email": email} for email in attendees]
    created_event = service.events().insert(calendarId="primary", body=event).execute()
    return created_event.get("htmlLink")