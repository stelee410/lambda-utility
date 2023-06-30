from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os
import socket
import socks
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

def send_email(to, subject, body, image_path=None, proxy_url=None):
    # Authenticate with the Gmail API using the client secret file
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/gmail.compose'])
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', ['https://www.googleapis.com/auth/gmail.compose'])
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Create a SOCKS5 proxy connection
    if proxy_url:
        socks.set_default_proxy(socks.SOCKS5, proxy_url['hostname'], proxy_url['port'])
        socket.socket = socks.socksocket

    # Create the Gmail API client
    service = build('gmail', 'v1', credentials=creds)

    # Create the message
    message = MIMEMultipart()
    message['to'] = to
    message['subject'] = subject
    text = MIMEText(body)
    message.attach(text)
    if image_path:
        with open(image_path, 'rb') as f:
            img_data = f.read()
        image = MIMEImage(img_data, name=os.path.basename(image_path))
        message.attach(image)

    # Send the message
    try:
        create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
        send_message = (service.users().messages().send(userId="me", body=create_message).execute())
        print(F'sent message to {to} Message Id: {send_message["id"]}')
    except HttpError as error:
        print(F'An error occurred: {error}')
        send_message = None
    return send_message