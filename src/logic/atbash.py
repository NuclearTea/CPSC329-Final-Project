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
