def letter_to_number_encrypt(text):
    result = []
    for char in text.upper():
        if char.isalpha():
            number = ord(char) - 64
            result.append(str(number))
        else:
            result.append(char)
    return ' '.join(result)


def letter_to_number_decrypt(text):
    result = ""
    parts = text.split()

    for part in parts:
        if part.isdigit():
            num = int(part)
            if 1 <= num <= 26:
                result += chr(num + 64)
            else:
                result += part
        else:
            result += part
    return result


def main():
    print("Letter-to-Number Cipher Program")
    print("Converts letters to their alphabet positions (A=1, B=2, ..., Z=26)")

    while True:
        choice = input("\nWould you like to (e)ncrypt or (d)ecrypt? (or 'q' to quit): ").lower()

        if choice == 'q':
            print("Goodbye!")
            break

        if choice not in ['e', 'd']:
            print("Please enter 'e' for encrypt, 'd' for decrypt, or 'q' to quit")
            continue

        text = input("Enter your text: ")

        if choice == 'e':
            result = letter_to_number_encrypt(text)
            print(f"Encrypted text: {result}")
        else:
            result = letter_to_number_decrypt(text)
            print(f"Decrypted text: {result}")

        print()


if __name__ == "__main__":
    main()