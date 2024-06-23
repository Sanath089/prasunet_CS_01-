from termcolor import colored

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    
    return result

def main():
    print(colored(" _____                              _____ _       _               ", 'red'))
    print(colored("/  __ \\                            /  __ (_)     | |              ", 'green'))
    print(colored("| /  \\/ __ _  ___  ___  __ _ _ __  | /  \\/_ _ __ | |__   ___ _ __ ", 'yellow'))
    print(colored("| |    / _` |/ _ \\/ __|/ _` | '__| | |   | | '_ \\| '_ \\ / _ \\ '__|", 'blue'))
    print(colored("| \\__/\\ (_| |  __/\\__ \\ (_| | |    | \\__/\\ | |_) | | | |  __/ |   ", 'magenta'))
    print(colored(" \\____/\\__,_|\\___||___/\\__,_|_|     \\____/_| .__/|_| |_|\\___|_|   ", 'cyan'))
    print(colored("                                           | |                    ", 'white'))
    print(colored("                                           |_|                    ", 'grey'), end='')
    print(colored(" sanath", 'yellow'))

    while True:
        mode = input("Do you want to encrypt or decrypt? (e/d): ").lower()
        if mode not in ('e', 'd'):
            print("Invalid mode. Please enter 'e' for encrypt or 'd' for decrypt.")
            continue
        
        text = input("Enter your message: ")
        shift = int(input("Enter shift value: "))

        if mode == 'e':
            encrypted_text = caesar_cipher(text, shift, mode='encrypt')
            print(f"Encrypted message: {encrypted_text}")
        else:
            decrypted_text = caesar_cipher(text, shift, mode='decrypt')
            print(f"Decrypted message: {decrypted_text}")
        
        repeat = input("Do you want to process another message? (y/n): ").lower()
        if repeat != 'y':
            break

if __name__ == "__main__":
    main()
