import os
import subprocess
import time
from datetime import datetime

def check_host_status(ip):
    command = ['ping', '-c', '1', ip]
    response = subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return response == 0

def main():
    ip = '8.8.8.8'  # Replace with the IP address you want to test

    while True:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        status = 'Network Active' if check_host_status(ip) else 'Network Down'
        print(f'{timestamp} {status} to {ip}')
        time.sleep(2)

if __name__ == '__main__':
    main()
