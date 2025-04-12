from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64


def encrypt(text, key):
    data = text.encode("utf-8")

    iv = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(data, AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)

    encrypted = iv + encrypted_data
    return base64.b64encode(encrypted).decode("utf-8")


def decrypt(encrypted_text, key):
    try:
        encrypted_data = base64.b64decode(encrypted_text)

        iv = encrypted_data[:16]
        ciphertext = encrypted_data[16:]

        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_data = cipher.decrypt(ciphertext)
        decrypted_data = unpad(padded_data, AES.block_size)

        return decrypted_data.decode("utf-8")
    except Exception as e:
        return f"Decryption error: {str(e)}"
