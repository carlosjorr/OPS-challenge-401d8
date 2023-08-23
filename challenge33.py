import os
import hashlib
import datetime

def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def check_virustotal(md5_hash):
    api_key = os.getenv('VT_API_KEY')  # Set your VirusTotal API key as an environment variable
    query = f'python3 virustotal-search.py -k {api_key} -m {md5_hash}'
    os.system(query)

def scan_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                md5_hash = calculate_md5(file_path)
                file_size = os.path.getsize(file_path)
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                print(f"Timestamp: {timestamp}")
                print(f"File Name: {file_name}")
                print(f"File Size: {file_size} bytes")
                print(f"File Path: {file_path}")
                print(f"MD5 Hash: {md5_hash}\n")
                
                check_virustotal(md5_hash)
            except Exception as e:
                print(f"Error scanning {file_path}: {e}")

def main():
    directory_path = input("Enter the directory path to scan: ")
    if os.path.exists(directory_path):
        scan_directory(directory_path)
    else:
        print("Invalid directory path.")

if __name__ == "__main__":
    main()
