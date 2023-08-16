#!/usr/bin/env python3

import sys
import ipaddress
import logging
from logging.handlers import RotatingFileHandler
import time
from scapy.all import sr1, IP, TCP, ICMP

# Configure the logging settings
log_filename = 'scan_tool15.log'
log_max_size = 1 * 1024 * 1024  # 1 MB
log_backup_count = 3  # Number of backup log files

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a rotating file handler
rotating_handler = RotatingFileHandler(log_filename, maxBytes=log_max_size, backupCount=log_backup_count)
rotating_handler.setLevel(logging.DEBUG)

# Create a formatter and set it for the handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
rotating_handler.setFormatter(formatter)

# Add the rotating file handler to the logger
logger.addHandler(rotating_handler)

# Create a stream handler for terminal output
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.INFO)  # Adjust the level as needed

# Create a formatter for the stream handler
stream_formatter = logging.Formatter('%(levelname)s - %(message)s')
stream_handler.setFormatter(stream_formatter)

# Add the stream handler to the logger
logger.addHandler(stream_handler)

for i in range(6):
    logger.info("This is a test log statement!")
    time.sleep(2)

# Configure the logging settings
logging.basicConfig(
    filename='scan_too.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def scan_port(target_ip, port):
    try:
        response = sr1(IP(dst=target_ip)/TCP(dport=port, flags='S'), timeout=1, verbose=0)

        if response is None:
            return f"Port {port} is filtered (silently dropped)."
        elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
            sr1(IP(dst=target_ip)/TCP(dport=port, flags='R'), timeout=1, verbose=0)
            return f"Port {port} is open."
        elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
            return f"Port {port} is closed."
        else:
            return f"Port {port} is filtered (silently dropped)."
    except Exception as e:
        logging.error(f"An error occurred while scanning port {port}: {e}", exc_info=True)
        return f"An error occurred while scanning port {port}."

def main():
    try:
        target_ip = input("Enter the IP address to scan: ")
        
        logging.info(f"Starting scan for target IP: {target_ip}")

        # ICMP Ping Sweep
        logging.info("Performing ICMP Ping Sweep:")
        online_hosts = 0
        for host in ipaddress.IPv4Network(target_ip):
            ip_str = str(host)
            if ip_str == target_ip:
                continue
            
            try:
                response = sr1(IP(dst=ip_str)/ICMP(), timeout=1, verbose=0)
                if response is not None and response.getlayer(ICMP).type == 0:
                    logging.info(f"{ip_str} is up and responding to ICMP.")
                    online_hosts += 1
                else:
                    logging.info(f"{ip_str} is down or unresponsive.")
            except Exception as e:
                logging.error(f"An error occurred while performing ICMP ping on {ip_str}: {e}", exc_info=True)

        logging.info(f"Number of online hosts: {online_hosts}")

        # TCP Port Scan
        logging.info("\nPerforming TCP Port Scan:")
        start_port = 1
        end_port = 1024

        open_ports = []
        for port in range(start_port, end_port + 1):
            result = scan_port(target_ip, port)
            logging.info(result)
            if "open" in result:
                open_ports.append(port)
        
                # Corrected indentation for logging the open ports
                logging.info("\nOpen ports: %s", open_ports)
    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}", exc_info=True)

if __name__ == "__main__":
    main()
