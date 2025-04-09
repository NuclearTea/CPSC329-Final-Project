from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

def encrypt(text, key):
    data = text.encode('utf-8')

    iv = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(data, AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)

    encrypted = iv + encrypted_data
    return base64.b64encode(encrypted).decode('utf-8')

def decrypt(encrypted_text, key):
    try:
        encrypted_data = base64.b64decode(encrypted_text)

        iv = encrypted_data[:16]
        ciphertext = encrypted_data[16:]

        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_data = cipher.decrypt(ciphertext)
        decrypted_data = unpad(padded_data, AES.block_size)

        return decrypted_data.decode('utf-8')
    except Exception as e:
        return f"Decryption error: {str(e)}"


def main():
    key = get_random_bytes(32)
    print(f"Generated key (base64): {base64.b64encode(key).decode('utf-8')}")
    print()

    while True:
        choice = input("Would you like to (e)ncrypt or (d)ecrypt? (or 'q' to quit): ").lower()

        if choice == 'q':
            print()
            print("Goodbye!")
            break

        if choice not in ['e', 'd']:
            print("Please enter 'e' for encrypt, 'd' for decrypt, or 'q' to quit")
            continue

        if choice == 'e':
            text = input("Enter text to encrypt: ")
            encrypted = encrypt(text, key)
            print(f"Encrypted text: {encrypted}")
        else:
            encrypted_text = input("Enter encrypted text: ")
            decrypted = decrypt(encrypted_text, key)
            print(f"Decrypted text: {decrypted}")

        print()


if __name__ == "__main__":
    try:
        main()
    except ImportError:
        print("Please install pycryptodome first:")
        print("pip install pycryptodome")