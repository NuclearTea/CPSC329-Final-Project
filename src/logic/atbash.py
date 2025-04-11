def atbash_cipher(text):
    result = ""

    for char in text:
        if char.isalpha():
            ascii_base = 65 if char.isupper() else 97
            reversed_char = chr(ascii_base + (25 - (ord(char) - ascii_base)))
            result += reversed_char
        else:
            result += char

    return result

def main():
    while True:
        choice = input("Would you like to (e)ncrypt or (d)ecrypt? (or 'q' to quit): ").lower()

        if choice == 'q':
            print("Goodbye!")
            break

        if choice not in ['e', 'd']:
            print("Please enter 'e' for encrypt, 'd' for decrypt, or 'q' to quit")
            continue

        text = input("Enter your text: ")
        result = atbash_cipher(text)

        action = "Encrypted" if choice == 'e' else "Decrypted"
        print(f"{action} text: {result}\n")

if __name__ == "__main__":
    main()