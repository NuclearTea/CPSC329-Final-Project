import secrets

def generate_key(length=16):
    return secrets.token_hex(length // 2)
