#!/usr/bin/env python3

import os
import ipaddress
from scapy.all import *

# User menu prompting choice between TCP Port Range Scanner mode and ICMP Ping Sweep mode
def menu():
    print("Network Security Tool")
    print("1. TCP Port Range Scanner")
    print("2. ICMP Ping Sweep")
    choice = int(input("Enter your choice (1 or 2): "))
    return choice

# TCP Port Range Scanner
def tcp_port_range_scanner():
    target = input("Enter the target host: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout in seconds
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: Open")
            open_ports.append(port)
        else:
            print(f"Port {port}: Closed")
        sock.close()

    print("Open ports:", open_ports)
    pass

# ICMP Ping Sweep 
def icmp_ping_sweep():
    network_input = input("Enter network address with CIDR block (e.g., 10.10.0.0/24): ")
    network = ipaddress.IPv4Network(network_input, strict=False)

 # List of all addresses in the network
    online_hosts = 0
    for ip in network.hosts():
        ip_str = str(ip)
        response = os.system(f"ping -c 1 {ip_str} > /dev/null 2>&1")


        if response == 0:
            # Host is up, send ICMP echo request using Scapy
            icmp_response = sr1(IP(dst=ip_str) / ICMP(), timeout=1, verbose=0)
            if icmp_response is None:
                print(f"{ip_str} is up, but not responding to ICMP.")
            elif icmp_response.type == 0:
                print(f"{ip_str} is up and responding to ICMP.")
                online_hosts += 1
            elif icmp_response.type == 3 and icmp_response.code in [1, 2, 3, 9, 10, 13]:
                print(f"{ip_str} is up but actively blocking ICMP traffic.")
            else:
                print(f"{ip_str} is up but with an unknown ICMP response.")
        else:
            print(f"{ip_str} is down or unresponsive.")

    print(f"Number of online hosts: {online_hosts}")

def main():
    choice = menu()

    if choice == 1:
        tcp_port_range_scanner()
    elif choice == 2:
        icmp_ping_sweep()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()