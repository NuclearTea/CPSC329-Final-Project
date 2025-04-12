def letter_to_number_encrypt(text):
    result = []
    for char in text.upper():
        if char.isalpha():
            number = ord(char) - 64
            result.append(str(number))
        else:
            result.append(char)
    return " ".join(result)


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
