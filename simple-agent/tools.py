import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

class Tools:

    def __init__(self, credentials_path: str, temp_dir: str = ".temp"):
        self.SCOPES = ["https://www.googleapis.com/auth/calendar"]
        self.credentials_path = credentials_path
        self.token_path = os.path.join(temp_dir, "token.json")
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

    def get_calendar_services(self):
        creds = None
        # Si el token existe lo cargamos
        if os.path.exists(self.token_path):
            creds = Credentials.from_authorized_user_file(self.token_path, self.SCOPES)

        # Refrescar token o solicitar uno nuevo
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not os.path.exists(self.credentials_path):
                    raise FileNotFoundError("Archivo de credenciales no encontrado")
                
                flow = InstalledAppFlow.from_client_secrets_file(self.credentials_path, self.SCOPES)
                creds = flow.run_local_server(port=0)
                with open(self.token_path, "w") as token:
                    token.write(creds.to_json())

        # Generar servicio de Google Calendar
        return build("calendar", "v3", credentials=creds)

    def check_availability(self):
        pass


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    
    credentials_path = os.getenv("GOOGLE_CREDENTIALS_PATH")
    if not credentials_path:
        raise ValueError("La variable de entorno GOOGLE_CREDENTIALS_PATH no está configurada")
    tools = Tools(credentials_path=credentials_path)
    calendar_service = tools.get_calendar_services()
    print("Google Calendar API autenticada correctamente")