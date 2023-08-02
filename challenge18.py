

import zipfile
from tqdm import tqdm

protected_file = input("Zip file: ")
wordlist = input("Choose wordlist: ")

try:
    zip_file = zipfile.ZipFile(protected_file)
    n_pass = len(list(open(wordlist, "rb")))
except:
    print("\a")
    print("File not zip, exiting...")
    exit(0)

print("Number of passwords that will be checked:", n_pass)
print('\n')

with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_pass, unit='word'):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("\a")
            print("[+] Password Found:", word.decode().strip())
            print("\a")
            print('Exiting...')
            exit(0)

print("\a")
print("[X] Password not found in the wordlist, try another one")
