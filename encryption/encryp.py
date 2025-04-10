from crypto.cipher import AES
import os

def pad(text):
    return text +(16-len(text) % 16) * chr(16 - len(text) % 16)

def unpad(text):
    return text[:-ord(text[-1])]

def encrypt_AES(key, plaintext):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    return cipher.encrypt(pad(plaintext).encode('utf-8')).hex()

def decrypt_AES(key, ciphertext):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    return unpad(cipher.decrypt(bytes.fromhex(ciphertext)).decode('utf-8'))

