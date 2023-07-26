#!/usr/bin/env python3


import sys
import ipaddress
from scapy.all import sr1, IP, TCP

def scan_port(target_ip, port):
    # Sending SYN packet to check if the port is open
    response = sr1(IP(dst=target_ip)/TCP(dport=port, flags='S'), timeout=1, verbose=0)

    if response is None:
        return f"Port {port} is filtered (silently dropped)."
    elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
        # If flag 0x12 received, send a RST packet to close the open connection
        sr1(IP(dst=target_ip)/TCP(dport=port, flags='R'), timeout=1, verbose=0)
        return f"Port {port} is open."
    elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
        return f"Port {port} is closed."
    else:
        return f"Port {port} is filtered (silently dropped)."


def main():
    # Prompt the user for the target IP address
    target_ip = input("Enter the IP address to scan: ")


    # ICMP Ping Sweep
    print("Performing ICMP Ping Sweep:")
    online_hosts = 0
    for host in ipaddress.IPv4Network(target_ip):
        ip_str = str(host)
        if ip_str == target_ip:
            continue  

        response = sr1(IP(dst=ip_str)/ICMP(), timeout=1, verbose=0)
        if response is not None and response.getlayer(ICMP).type == 0:
            print(f"{ip_str} is up and responding to ICMP.")
            online_hosts += 1
        else:
            print(f"{ip_str} is down or unresponsive.")

    print(f"Number of online hosts: {online_hosts}")

    # TCP Port Scan
    print("\nPerforming TCP Port Scan:")
    start_port = 1
    end_port = 1024
# Print the open ports to the screen
    open_ports = []
    for port in range(start_port, end_port + 1):
        result = scan_port(target_ip, port)
        print(result)
        if "open" in result:
            open_ports.append(port)

    print("\nOpen ports:", open_ports)

if __name__ == "__main__":
    main()
