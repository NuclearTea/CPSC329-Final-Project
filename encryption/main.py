from encryp import encrypt_AES, decrypt_AES

key = "1234567890123456"  # 16-character key
plaintext = "Hello, World!"
ciphertext = encrypt_AES(key, plaintext)
print("Your text has been Encrypted:", ciphertext)
print("Your text has been Decrypted:", decrypt_AES(key, ciphertext))


#hashing stuff
from password_hashing import hash_password, verify_password

password = "mypassword"
hashed = hash_password(password)
print("Hashed Password:", hashed)
print("Verification:", verify_password("mypassword", hashed))

#key generation stuff
from keygeneration import generate_key

key = generate_key()
print("Generated Key:", key)