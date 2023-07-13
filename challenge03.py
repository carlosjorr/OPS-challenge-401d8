#!/usr/bin/env python3

#Script:                      ops 401
# Author:                       carlos rojas 
# Date of latest revision:      07/12/2023
# Purpose:                       Uptime Sensor Tool Part 2 of 2


import smtplib
from email.message import EmailMessage
from datetime import datetime
import time
import subprocess
from getpass import getpass 

def send_email(sender_email, sender_password, receiver_email, subject, body):
    # Configure SMTP server and port
    smtp_server = 'smtp.gmail.com'  # Change if using a different email provider
    smtp_port = 587  # Change if using a different email provider

    # Create email message
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content(body)

    try:
        # Connect to SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Login to email account
        server.login(sender_email, sender_password)

        # Send email
        server.send_message(msg)
        print("Email sent successfully")
    except Exception as e:
        print("Failed to send email:", str(e))
    finally:
        # Terminate SMTP connection
        server.quit()


def check_host_status(host):
    # Ping the host to check its availability
    command = ['ping', '-c', '1', host]  # Adjust based on the OS and ping command syntax
    result = subprocess.run(command, capture_output=True, text=True)

    # Print the output of the ping command
    print(result.stdout)

    # Check the return code to determine if the ping was successful
    if result.returncode == 0:
        return True  # Host is up
    else:
        return False  # Host is down


def main():
    # Get user input for email details
    sender_email = input("Enter your email address: ")
    sender_password = getpass("Enter your email password: ")
    receiver_email = input("Enter the recipient's email address: ")
    host = input("Enter the host to monitor: ")
    previous_status = check_host_status(host)

    while True:
        current_status = check_host_status(host)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if current_status != previous_status:
            # Determine status change details
            status_before = "up" if previous_status else "down"
            status_after = "up" if current_status else "down"

            # Prepare email subject and body
            subject = f"Host Status Change: {host} ({status_before} to {status_after})"
            body = f"Host: {host}\nStatus Before: {status_before}\nStatus After: {status_after}\nTimestamp: {timestamp}"

            # Send email notification
            send_email(sender_email, sender_password, receiver_email, subject, body)

        previous_status = current_status
        time.sleep(60)  # Check status every 60 seconds


if __name__ == '__main__':
    main()
