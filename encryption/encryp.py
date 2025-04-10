import os
from Cryptodome.Cipher import AES

# Padding to ensure plaintext is multiple of 16 bytes
def pad(text):
    pad_len = 16 - (len(text) % 16)
    return text + chr(pad_len) * pad_len

def unpad(text):
    pad_len = ord(text[-1])
    return text[:-pad_len]

def encrypt_AES(key, plaintext):
    if len(key) not in [16, 24, 32]:
        raise ValueError("Key must be 16, 24, or 32 bytes long")
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    padded = pad(plaintext).encode('utf-8')
    encrypted = cipher.encrypt(padded)
    return encrypted.hex()

def decrypt_AES(key, ciphertext):
    if len(key) not in [16, 24, 32]:
        raise ValueError("Key must be 16, 24, or 32 bytes long")
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    decrypted = cipher.decrypt(bytes.fromhex(ciphertext)).decode('utf-8')
    return unpad(decrypted)

