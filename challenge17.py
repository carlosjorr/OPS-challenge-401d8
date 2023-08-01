
#!/usr/bin/env python3



#import libraries

import paramiko
import getpass

host = input("Please provide the IP of the SSH server: ")
username = input("Please provide the SSH username: ")
password = getpass.getpass("Please provide the SSH password: ")

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(host, username=username, password=password)
    print("Connected to the remote server.")
    
    # Execute commands on the remote server
    while True:
        command = input("Enter a command to execute on the remote server (or 'exit' to quit): ")
        if command.lower() == 'exit':
            break

        stdin, stdout, stderr = ssh.exec_command(command)
        print(stdout.read().decode())
        print(stderr.read().decode())
    
    ssh.close()
    print("SSH connection closed.")
    
except paramiko.AuthenticationException:
    print("Authentication failed. Please check your credentials.")
except paramiko.SSHException as ssh_ex:
    print(f"Error while connecting: {ssh_ex}")
except Exception as ex:
    print(f"An error occurred: {ex}")
