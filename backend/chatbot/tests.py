from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import os

# Path to your credentials.json file
CLIENT_SECRET_FILE = './credentials.json'  # Replace with your actual path
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def authenticate():
    creds = None
    # Check if token.json exists and is valid
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # If no valid credentials or the token is expired, use the OAuth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Start the OAuth flow
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)  # This will open a browser window for the user to log in

        # Save the credentials for future use
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    print(f"Access Token: {creds.token}")  # You can print or use the access token here
    return creds.token

if __name__ == "__main__":
    access_token = authenticate()
    print(f"Access Token: {access_token}")
