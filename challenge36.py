import os

def banner_grabbing_netcat(target, port):
    command = f'nc -v {target} {port}'
    os.system(command)

def banner_grabbing_telnet(target, port):
    command = f'telnet {target} {port}'
    os.system(command)

def banner_grabbing_nmap(target):
    command = f'nmap -sV {target}'
    os.system(command)

def main():
    target = input("Enter the target URL or IP address: ")
    port = input("Enter the port number: ")

    banner_grabbing_netcat(target, port)
    banner_grabbing_telnet(target, port)
    banner_grabbing_nmap(target)

if __name__ == "__main__":
    main()

