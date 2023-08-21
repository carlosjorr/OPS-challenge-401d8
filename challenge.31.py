import os

def search_files(file_name, search_directory):
    hits = 0
    total_files = 0

    for root, dirs, files in os.walk(search_directory):
        for file in files:
            total_files += 1
            if file_name.lower() in file.lower():
                hits += 1
                print(f"Hit: {os.path.join(root, file)}")

    print(f"\nSearch completed.")
    print(f"Total files searched: {total_files}")
    print(f"Total hits found: {hits}")

def main():
    file_name = input("Enter the file name to search for: ")
    search_directory = input("Enter the directory to search in: ")

    if os.name == "posix":  # Linux
        if not search_directory.startswith('/'):
            search_directory = '/' + search_directory
    elif os.name == "nt":   # Windows
        if not search_directory.endswith('\\'):
            search_directory += '\\'
    
    if os.path.exists(search_directory):
        search_files(file_name, search_directory)
    else:
        print("Invalid directory.")

if __name__ == "__main__":
    main()
