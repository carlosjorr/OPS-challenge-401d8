from cryptography.fernet import Fernet
import os

def encrypt_file(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data)
    
    encrypted_file_path = file_path + '.encrypted'
    
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    
    print(f'File encrypted and saved as: {encrypted_file_path}')
    os.remove(file_path)

def decrypt_file(file_path):
    with open(file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    
    key = Fernet.generate_key()
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data)
    
    decrypted_file_path = file_path[:-10]  # Remove '.encrypted' from the file name
    
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
    
    print(f'File decrypted and saved as: {decrypted_file_path}')
    os.remove(file_path)

def encrypt_string(plaintext):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(plaintext.encode())
    
    print(f'Ciphertext: {encrypted_data.decode()}')

def decrypt_string(ciphertext):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(ciphertext.encode())
    
    print(f'Plaintext: {decrypted_data.decode()}')

def main():
    print('Select a mode:')
    print('1. Encrypt a file')
    print('2. Decrypt a file')
    print('3. Encrypt a message')
    print('4. Decrypt a message')
    mode = int(input('Enter the mode number: '))
    
    if mode == 1 or mode == 2:
        file_path = input('Enter the file path: ')
        if mode == 1:
            encrypt_file(file_path)
        else:
            decrypt_file(file_path)
    elif mode == 3 or mode == 4:
        text = input('Enter the text: ')
        if mode == 3:
            encrypt_string(text)
        else:
            decrypt_string(text)
    else:
        print('Invalid mode number. Please select a valid mode.')
    
if __name__ == '__main__':
    main()
