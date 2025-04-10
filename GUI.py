import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Encryption & Decryption")

from tkinter import *
from tkinter import messagebox
from Cryptodome.Cipher import AES
import secrets
import hashlib
PROGRAM_FONT = "Segoe UI"

# AES Functions
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

# Key Generation
def generate_key(length=16):
    return secrets.token_hex(length // 2)

# Password Hashing
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def verify_password(password, hashed):
    return hash_password(password) == hashed

# Tkinter Functions
def perform_encryption():
    try:
        key = key_entry.get()
        plaintext = input_text.get("1.0", END).strip()
        result = encrypt_AES(key, plaintext)
        output_text.delete("1.0", END)
        output_text.insert("1.0", result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def perform_decryption():
    try:
        key = key_entry.get()
        ciphertext = input_text.get("1.0", END).strip()
        result = decrypt_AES(key, ciphertext)
        output_text.delete("1.0", END)
        output_text.insert("1.0", result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def generate_new_key():
    try:
        length = int(key_length_entry.get())
        if length not in [16, 24, 32]:
            raise ValueError("Key length must be 16, 24, or 32 bytes")
        new_key = generate_key(length)
        messagebox.showinfo("Generated Key", f"New Key: {new_key}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def hash_password_action():
    password = password_entry.get()
    hashed = hash_password(password)
    password_result_entry.delete(0, END)
    password_result_entry.insert(0, hashed)

def verify_password_action():
    password = password_entry.get()
    hashed = password_result_entry.get()
    if verify_password(password, hashed):
        messagebox.showinfo("Verification", "Password is valid!")
    else:
        messagebox.showerror("Verification", "Password is invalid!")

# Tkinter GUI
root = Tk()
root.title("Encryption/Decryption & Hashing GUI")
root.geometry("600x400")

# AES Key & Text Input
Label(root, text="Key (16/24/32 bytes):").pack()
key_entry = Entry(root, width=50)
key_entry.pack()

Label(root, text="Input (Plaintext or Ciphertext):").pack()
input_text = Text(root, height=5, width=50)
input_text.pack()

# Encryption/Decryption Buttons
Button(root, text="Encrypt", command=perform_encryption).pack(pady=5)
Button(root, text="Decrypt", command=perform_decryption).pack(pady=5)

# Output Text
Label(root, text="Output:").pack()
output_text = Text(root, height=5, width=50)
output_text.pack()

# Key Generation Section
Label(root, text="Key Generation (16/24/32 bytes):").pack(pady=10)
key_length_entry = Entry(root, width=10)
key_length_entry.pack()

Button(root, text="Generate Key", command=generate_new_key).pack(pady=5)

# Password Hashing Section
Label(root, text="Password:").pack(pady=10)
password_entry = Entry(root, show="*", width=50)
password_entry.pack()

Button(root, text="Hash Password", command=hash_password_action).pack(pady=5)

Label(root, text="Hashed Password:").pack()
password_result_entry = Entry(root, width=50)
password_result_entry.pack()

Button(root, text="Verify Password", command=verify_password_action).pack(pady=5)

root.mainloop()
