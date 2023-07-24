#!/usr/bin/env python3

import sys
from scapy.all import sr1, IP, TCP

def scan_port(target_ip, port):
    # Sending SYN packet to check if the port is open
    response = sr1(IP(dst=target_ip)/TCP(dport=port, flags='S'), timeout=1, verbose=0)
    
    if response is None:
        print(f"Port {port} is filtered (silently dropped).")
    elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
        # If flag 0x12 received, send a RST packet to close the open connection
        sr(IP(dst=target_ip)/TCP(dport=port, flags='R'), timeout=1, verbose=0)
        print(f"Port {port} is open.")
    elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
        print(f"Port {port} is closed.")
    else:
        print(f"Port {port} is filtered (silently dropped).")

def main():
    if len(sys.argv) < 4:
        print("Usage: python port_scanner.py <target_ip> <start_port> <end_port>")
        sys.exit(1)

    target_ip = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])

    for port in range(start_port, end_port + 1):
        scan_port(target_ip, port)

if __name__ == "__main__":
    main()
