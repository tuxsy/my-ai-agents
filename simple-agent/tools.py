import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from datetime import datetime
from zoneinfo import ZoneInfo


class Tools:

    def __init__(self, credentials_path: str, temp_dir: str = ".temp"):
        self.credentials_path = credentials_path
        if not os.path.exists(self.credentials_path):
            raise FileNotFoundError(
                "Archivo de credenciales no encontrado")

        self.SCOPES = ["https://www.googleapis.com/auth/calendar"]
        self.token_path = os.path.join(temp_dir, "token.json")
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

    def get_current_datetime(self):
        return {
            "current_datetime": datetime.now().isoformat(),
        }

    def get_calendar_services(self):
        creds = None
        # Si el token existe lo cargamos
        if os.path.exists(self.token_path):
            creds = Credentials.from_authorized_user_file(
                self.token_path, self.SCOPES)

        # Refrescar token o solicitar uno nuevo
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_path, self.SCOPES)
                creds = flow.run_local_server(port=0)
                with open(self.token_path, "w") as token:
                    token.write(creds.to_json())

        # Generar servicio de Google Calendar
        return build("calendar", "v3", credentials=creds)

    def check_availability(self, time_start: str, time_end: str, calendar: str = "primary", timezone: str = "Europe/Madrid"):
        time_start = add_zoneinfo(time_start, timezone)
        time_end = add_zoneinfo(time_end, timezone)
        
        body = {
            "timeMin": time_start,
            "timeMax": time_end,
            "items": [{"id": calendar}]
        }
        service = self.get_calendar_services()
        events_result = service.freebusy().query(body=body).execute()
        busy_times = events_result.get("calendars", {}).get(
            calendar, {}).get("busy", [])
        return {
            "calendar_id": calendar,
            "time_start": time_start,
            "time_end": time_end,
            "busy_times": busy_times,
            "available": len(busy_times) == 0
        }



# Utility functions

def add_zoneinfo(dt_str: str, timezone: str):
    dt = datetime.fromisoformat(dt_str)
    dt = dt.replace(tzinfo=ZoneInfo(timezone))
    return dt.isoformat(timespec="seconds")

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()

    tools = Tools(credentials_path=os.getenv("GOOGLE_CREDENTIALS_PATH"))
    result = tools.check_availability(
        "2026-02-16T17:00:00+01:00", "2026-02-16T17:30:00+01:00")
    print(result)
