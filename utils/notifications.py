#!/usr/bin/env python3

"""
Sends a notification on pipeline health and general updates
"""

import os
import smtplib
from secret import point_of_contact, token
from email.mime.text import MIMEText

# Load credentials from environment variables
#POINT_OF_CONTACT = os.getenv('POINT_OF_CONTACT')
#TOKEN = os.getenv('EMAIL_TOKEN')

def send_notification():
    if not point_of_contact or not token:
        print("Error: Missing POINT_OF_CONTACT or EMAIL_TOKEN in environment variables.")
        return

    # Customize the message
    subject = "Pipeline Health Alert"
    body = "The Python script has failed multiple times. Please check the logs for details."

    # Create the email message
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = point_of_contact
    msg['To'] = point_of_contact

    try:
        # Connect to the Gmail SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(point_of_contact, token)
            server.send_message(msg)
        print("Notification sent successfully.")
    except Exception as e:
        print(f"Failed to send notification: {e}")

if __name__ == "__main__":
    print("Starting notification process...")
    try:
        send_notification()
    except Exception as e:
        print(f"Unexpected error: {e}")
