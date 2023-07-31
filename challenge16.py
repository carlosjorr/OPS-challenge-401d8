#!/usr/bin/env python3

#import libraries
import time

# Mode 1: Offensive; Dictionary Iterator
def load_wordlist(file_path):
    """
    Loads the wordlist from the given file path and returns a list of words.
    """
    try:
        with open(file_path, 'r', encoding='latin-1') as file:
            wordlist = file.readlines()
        return [word.strip() for word in wordlist]
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return []

def offensive_mode(wordlist):
    """
    Performs the offensive mode (Dictionary Iterator).
    """
    if not wordlist:
        print("Wordlist is empty. Exiting.")
        return
    
    delay = float(input("Enter the delay between words (in seconds): "))
    print("Starting Offensive Mode (Dictionary Iterator)...")
    
    for word in wordlist:
        print(word)
        time.sleep(delay)

# Mode 2: Defensive; Password Recognized
def defensive_mode(wordlist, user_input):
    """
    Performs the defensive mode (Password Recognized).
    """
    if not wordlist:
        print("Wordlist is empty. Exiting.")
        return
    
    if user_input in wordlist:
        print("Password found in the wordlist.")
    else:
        print("Password not found in the wordlist.")

if __name__ == "__main__":
    print("Welcome to the Brute Force Wordlist Attack Tool!")
    mode = input("Select Mode (1: Offensive; 2: Defensive): ")

    if mode == "1":
        wordlist_file_path = input("Enter the word list file path: ")
        wordlist = load_wordlist(wordlist_file_path)
        offensive_mode(wordlist)

    elif mode == "2":
        user_input = input("Enter the password you want to search for: ")
        wordlist_file_path = input("Enter the word list file path: ")
        wordlist = load_wordlist(wordlist_file_path)
        defensive_mode(wordlist, user_input)

    else:
        print("Invalid mode selected. Please choose either '1' or '2'.")